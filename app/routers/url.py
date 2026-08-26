from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.utils import gen_code
from app.database.connection import get_db
from app.database.models import URLItem
from app.schemas.schemas import URLCreate, URLResponse, URLStats

router = APIRouter(prefix="/urls", tags=["URLs"])

@router.post("/", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def creat_short_url(payload: URLCreate, db: Session = Depends(get_db)):
    while True:
        code = gen_code()
        exists = db.query(URLItem).filter(URLItem.short_code == code).first()
        if not exists:
            break

    db_item = URLItem(
        original_url = str(payload.url),
        short_code = code
    )

    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


    return URLResponse(
        original_url=db_item.original_url,
        short_url=f"http://localhost:8000/{db_item.short_code}",
        short_code=db_item.short_code,
        created_at=db_item.created_at,
    )


@router.get("/{short_code}/stats", response_model=URLStats)
def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    db_item = db.query(URLItem).filter(URLItem.short_code == short_code).first()
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "URL not found."
        )

    return db_item

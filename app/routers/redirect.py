from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import URLItem, AccessLog

router = APIRouter(tags=['Redirect'])

@router.get("/{short_code}")
def redirect(short_code: str, request: Request, db: Session = Depends(get_db)):
    db_item = db.query(URLItem).filter(URLItem.short_code == short_code).first()
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL encurtada não encontrada.",
        )
   
    db_item.clicks += 1
    ip = request.client.host if request.client else None
    agent = request.headers.get("user-agent")
    
    log = AccessLog(
        url_id = db_item.id,
        ip_adress = ip,
        user_agent = agent,
    )        
    
    try:
        db.add(log)
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao registrar acesso.",
        )
    
    return RedirectResponse(
        url=db_item.original_url,
        status_code=status.HTTP_302_FOUND
        )

from datetime import datetime
from pydantic import BaseModel, ConfigDict, HttpUrl

class URLCreate(BaseModel):
    url: HttpUrl

    model_config = ConfigDict(str_strip_whitespace=True)


class URLResponse(BaseModel):
    original_url: str
    short_code: str
    short_url: str
    created_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True
        )


class URLStats(BaseModel):
    original_url: str
    clicks: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class URLItem(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=True)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    
    logs = relationship("AccessLog", back_populates="url", cascade="all, delete-orphan")


class AccessLog(Base):
    __tablename__ = "acess_logs"

    id = Column(Integer, primary_key=True, index=True)
    url_id = Column(Integer, ForeignKey("urls.id", ondelete="CASCADE"), nullable=False)
    acessed_at = Column(DateTime, default=datetime.now)
    user_agent = Column(String, nullable=True)
    ip_adress = Column(String, nullable=True)

    url = relationship("URLItem", back_populates="logs")

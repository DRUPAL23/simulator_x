"""Synthetic virtual SIM profile model."""
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, String
from simulator_x.database.db import Base
class SIMProfile(Base):
    __tablename__ = "sim_profiles"
    id = Column(String(36), primary_key=True, index=True)
    profile_name = Column(String(100), nullable=False)
    test_imsi = Column(String(32), unique=True, nullable=False, index=True)
    test_iccid = Column(String(40), unique=True, nullable=False, index=True)
    operator_name = Column(String(100), nullable=False)
    country_code = Column(String(2), nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

"""Pydantic profile schemas."""
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
class ProfileCreate(BaseModel):
    profile_name: str = Field(min_length=2, max_length=100)
    operator_name: str = Field(min_length=2, max_length=100)
    country_code: str = Field(default="ZZ", pattern=r"^[A-Z]{2}$")
class ProfileUpdate(BaseModel):
    profile_name: str | None = Field(default=None, min_length=2, max_length=100)
    operator_name: str | None = Field(default=None, min_length=2, max_length=100)
    country_code: str | None = Field(default=None, pattern=r"^[A-Z]{2}$")
class ProfileStatusUpdate(BaseModel):
    active: bool
class ProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    profile_name: str
    test_imsi: str
    test_iccid: str
    operator_name: str
    country_code: str
    active: bool
    created_at: datetime
    updated_at: datetime

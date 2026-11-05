"""CRUD services for synthetic, isolated test profiles."""
import secrets, uuid
from sqlalchemy import select
from sqlalchemy.orm import Session
from simulator_x.profiles.models import SIMProfile
from simulator_x.profiles.schemas import ProfileCreate, ProfileUpdate
def _digits(n): return "".join(str(secrets.randbelow(10)) for _ in range(n))
def generate_test_identity():
    return {"id": str(uuid.uuid4()), "test_imsi": "TEST-IMSI-" + _digits(10), "test_iccid": "TEST-ICCID-" + _digits(13)}
def create_profile(db: Session, data: ProfileCreate):
    row = SIMProfile(**generate_test_identity(), profile_name=data.profile_name.strip(), operator_name=data.operator_name.strip(), country_code=data.country_code, active=False)
    db.add(row); db.commit(); db.refresh(row); return row
def list_profiles(db: Session): return list(db.scalars(select(SIMProfile).order_by(SIMProfile.created_at.desc())).all())
def get_profile(db: Session, profile_id: str): return db.get(SIMProfile, profile_id)
def update_profile(db: Session, row: SIMProfile, data: ProfileUpdate):
    for key, value in data.model_dump(exclude_unset=True).items():
        if value is not None: setattr(row, key, value.strip() if isinstance(value, str) else value)
    db.commit(); db.refresh(row); return row
def set_profile_status(db: Session, row: SIMProfile, active: bool):
    row.active = active; db.commit(); db.refresh(row); return row
def delete_profile(db: Session, row: SIMProfile): db.delete(row); db.commit()

"""Versioned API endpoints for synthetic test profiles."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simulator_x.database.db import get_db
from simulator_x.profiles import manager
from simulator_x.profiles.schemas import ProfileCreate, ProfileResponse, ProfileStatusUpdate, ProfileUpdate
router = APIRouter(prefix="/api/v1", tags=["profiles"])
@router.post("/profiles", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(payload: ProfileCreate, db: Session = Depends(get_db)): return manager.create_profile(db, payload)
@router.get("/profiles", response_model=list[ProfileResponse])
def list_profiles(db: Session = Depends(get_db)): return manager.list_profiles(db)
def _require_profile(db, profile_id):
    row = manager.get_profile(db, profile_id)
    if row is None: raise HTTPException(status_code=404, detail="Virtual test profile not found")
    return row
@router.get("/profiles/{profile_id}", response_model=ProfileResponse)
def get_profile(profile_id: str, db: Session = Depends(get_db)): return _require_profile(db, profile_id)
@router.put("/profiles/{profile_id}", response_model=ProfileResponse)
def update_profile(profile_id: str, payload: ProfileUpdate, db: Session = Depends(get_db)): return manager.update_profile(db, _require_profile(db, profile_id), payload)
@router.patch("/profiles/{profile_id}/status", response_model=ProfileResponse)
def set_status(profile_id: str, payload: ProfileStatusUpdate, db: Session = Depends(get_db)): return manager.set_profile_status(db, _require_profile(db, profile_id), payload.active)
@router.delete("/profiles/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(profile_id: str, db: Session = Depends(get_db)):
    manager.delete_profile(db, _require_profile(db, profile_id)); return None

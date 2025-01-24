from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.note import create_new_note, retrieve_notes, retrieve_note_by_id, update_existing_note, remove_note_by_id
from app.schemas.note import NoteCreate, NoteUpdate, NoteInDB
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=NoteInDB)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_new_note(db=db, note=note)

@router.get("/", response_model=list[NoteInDB])
def get_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return retrieve_notes(db=db, skip=skip, limit=limit)

@router.get("/{note_id}", response_model=NoteInDB)
def get_note(note_id: int, db: Session = Depends(get_db)):
    db_note = retrieve_note_by_id(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.put("/{note_id}", response_model=NoteInDB)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = update_existing_note(db=db, note_id=note_id, note=note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}", response_model=NoteInDB)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = remove_note_by_id(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

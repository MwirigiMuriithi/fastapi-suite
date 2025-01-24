from sqlalchemy.orm import Session
from app.db.note_crud import create_note, get_notes, get_note_by_id, update_note, delete_note
from app.schemas.note import NoteCreate, NoteUpdate

def create_new_note(db: Session, note: NoteCreate):
    return create_note(db=db, note=note)

def retrieve_notes(db: Session, skip: int = 0, limit: int = 10):
    return get_notes(db=db, skip=skip, limit=limit)

def retrieve_note_by_id(db: Session, note_id: int):
    return get_note_by_id(db=db, note_id=note_id)

def update_existing_note(db: Session, note_id: int, note: NoteUpdate):
    return update_note(db=db, note_id=note_id, note=note)

def remove_note_by_id(db: Session, note_id: int):
    return delete_note(db=db, note_id=note_id)

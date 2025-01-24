from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate

def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Note).offset(skip).limit(limit).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def update_note(db: Session, note_id: int, note: NoteUpdate):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.title = note.title
        db_note.content = note.content
        db.commit()
        db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note

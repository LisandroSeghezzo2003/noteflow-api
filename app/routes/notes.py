from fastapi import APIRouter, HTTPException
from app.schemas.note import NoteCreate, NoteResponse
from datetime import datetime

# Crear router
router = APIRouter()


# Crear UNA nota
@router.post("/")
def create_note():
    pass

# Mostrar notas
@router.get("/")
def get_note():
    pass

#Mostrar UNA nota
@router.get("/{note_id}")
def get_notes():
    pass

#Actualizar UNA nota
@router.put("/{note_id}")
def update_note(note_id: str):
    pass

#Eliminar UNA nota
@router.delete("/{note_id}")
def delete_note(note_id: str):
    pass
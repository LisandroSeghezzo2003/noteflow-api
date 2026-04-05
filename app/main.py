from fastapi import FastAPI
from app.routes import auth, notes


app = FastAPI()
app.include_router(notes.router, prefix="/notes")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Servidor: uvicorn app.main:app --reload


@app.get("/")
def root():
    return {"message": "Bienvenido a NoteFlow!!"}

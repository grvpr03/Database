import models
import auth
from schemas import Book, BookCreate, BookUpdate

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session 

from database import Base, engine, get_db
import models
from schemas import Book, BookCreate, BookUpdate

Base.metadata.create_all(engine)

app = FastAPI(title="Library API")
app.include_router(auth.router)

def find_book(db: Session, book_id: int):
    book = db.get(models.Book, book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@app.get("/books", response_model=list[Book])
def list_books(author: str | None = None, db: Session = Depends(get_db)):
    query = select(models.Book)
    if author is not None:
        query = query.where(models.Book.author.ilike(author))
    return db.scalars(query).all()

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return find_book(db, book_id)

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_create: BookCreate, db: Session = Depends(get_db)):
    book = models.Book(**book_create.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    book = find_book(db, book_id)
    for key, value in book_update.model_dump(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = find_book(db, book_id)
    db.delete(book)
    db.commit()
from fastapi import APIRouter, HTTPException, status, Query
from database import SessionDep
from schemas.book import SBookAdd, SBookEdit, SBookUpdate
from repository import BookRepository

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=SBookEdit, status_code=status.HTTP_201_CREATED)
async def add_book(book: SBookAdd, session: SessionDep):
    """
    Create a new book in the collection.
    """
    new_book = await BookRepository.add_new_book(book, session)
    return new_book


@router.get("/", response_model=list[SBookEdit])
async def get_books(session: SessionDep):
    books = await BookRepository.get_all_books(session)
    return books


@router.delete("/{book_id}", response_model=SBookEdit)
async def delete_book(book_id: int, session: SessionDep):
    """
    Delete a book from the collection.
    """
    book = await BookRepository.get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    await BookRepository.delete_book(session, book_id)
    return book


@router.put("/{book_id}", response_model=SBookEdit)
async def update_book(book_id: int, book_data: SBookUpdate, session: SessionDep):
    """
    Update a book in the collection.
    """
    updated_book = await BookRepository.update_book(book_data, session, book_id)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book


@router.get("/search/", response_model=list[SBookEdit])
async def search_books(
    session: SessionDep,
    query: str = Query(
        ..., min_length=1, description="Search by " "title, " "author, " "or year"
    ),
):
    """
    Search books by keyword.
    """
    books = await BookRepository.search_books(session, query)
    return books

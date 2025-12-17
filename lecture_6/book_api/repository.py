from typing import Sequence
from sqlalchemy import select, delete, update, or_
from sqlalchemy.ext.asyncio import AsyncSession
from models.books import Book
from schemas.book import SBookAdd, SBookUpdate


class BookRepository:
    """
    Repository for handling database operations related to Books.
    """

    @classmethod
    async def add_new_book(cls, book: SBookAdd, session: AsyncSession) -> Book:
        """
        Create a new book and add it to the database.
        """

        book_dict = book.model_dump()

        new_book = Book(**book_dict)

        session.add(new_book)

        await session.commit()
        await session.refresh(new_book)

        return new_book

    @classmethod
    async def get_all_books(cls, session: AsyncSession) -> Sequence[Book]:
        """
        Retrieves all books from the database.
        """
        query = select(Book).order_by(Book.id)

        result = await session.execute(query)

        return result.scalars().all()

    @classmethod
    async def get_book_by_id(cls, session: AsyncSession, book_id: int) -> Book:
        """
        Retrieves a book from the database.
        """
        result = await session.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    @classmethod
    async def delete_book(cls, session: AsyncSession, book_id: int) -> None:
        """
        Delete a book from the database.
        """
        query = delete(Book).where(Book.id == book_id)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def update_book(
        cls, book: SBookUpdate, session: AsyncSession, book_id: int
    ) -> Book | None:
        """
        Update a book from the database.
        """
        values_to_update = book.model_dump(exclude_unset=True)
        query = (
            (update(Book).where(Book.id == book_id))
            .values(**values_to_update)
            .returning(Book)
        )
        result = await session.execute(query)
        updated_book = result.scalar_one_or_none()
        await session.commit()
        return updated_book

    @classmethod
    async def search_books(
        cls, session: AsyncSession, search_text: str
    ) -> Sequence[Book]:
        """
        Search books from the database.
        """
        text = search_text.strip()
        conditions = [
            Book.title.ilike(f"%{text}%"),
            Book.author.ilike(f"%{text}%"),
        ]

        if text.isdigit():
            conditions.append(Book.year == int(search_text))

        query = select(Book).where(or_(*conditions))
        result = await session.execute(query)
        return result.scalars().all()

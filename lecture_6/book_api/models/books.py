from sqlalchemy.orm import Mapped, mapped_column
from database import Model


class Book(Model):
    """
    Database model representing a book in the collection.
    """

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int | None] = mapped_column(default=None)

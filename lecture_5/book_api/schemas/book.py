from pydantic import BaseModel, ConfigDict


class SBookBase(BaseModel):
    """
    Base schema containing common attributes for a book.
    Used as a parent class to avoid code duplication.
    """

    title: str
    author: str
    year: int | None = None


class SBookAdd(SBookBase):
    """
    Schema for creating a new book (request body).
    """

    pass


class SBookUpdate(BaseModel):
    """
    Schema for updating a book.
    """

    title: str | None = None
    author: str | None = None
    year: int | None = None


class SBookEdit(SBookBase):
    """
    Schema for editing a book (request body).
    """

    id: int
    model_config = ConfigDict(from_attributes=True)

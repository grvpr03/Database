from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    copies: int = Field(ge=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str | None = Field(default=None, min_length=1, max_length=100)
    author: str | None = Field(default=None, min_length=1, max_length=100)
    copies: int | None = Field(default=None, ge=0)

class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


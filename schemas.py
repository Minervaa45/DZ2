from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    email: str = Field(..., min_length=3, max_length=320)


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    email: str | None = Field(default=None, min_length=3, max_length=320)


class UserOut(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

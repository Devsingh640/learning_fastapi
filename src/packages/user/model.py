from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from datetime import datetime, timezone


# Since we have 3 unique values in the data set by which we can applied CRUD operation. Which are user_id, user_name, email

class UserData(BaseModel):
    user_id: str
    user_name: str
    password: str
    email: str
    created_at: datetime
    updated_at: datetime
    status: bool
    description: str


class User(SQLModel, table=True):
    model_config = {"protected_namespace":()}

    __tablename__ = "user_master"

    id: int | None = Field(default=None, primary_key=True)
    user_id : str = Field(default=None, unique=True, index=True)
    user_name:  str = Field(default=None, unique=True, index=True)
    password : str = Field(default=None)
    email: str = Field(default=None, unique=True, index=True)

    created_at : datetime = Field(default_factory=lambda :datetime.now(timezone.utc))
    updated_at : datetime = Field(default_factory=lambda :datetime.now(timezone.utc), sa_column_kwargs={"onupdate": lambda :datetime.now(timezone.utc)})
    status: Optional[bool] = None
    description: Optional[str] = None
    # description: str | None


class AddUserData(SQLModel):
    model_config = {"protected_namespace":()}

    user_id: str | None = None
    user_name: str | None = None
    password: str | None = None
    email: str | None = None

    created_at: datetime
    updated_at: datetime
    status: Optional[bool] = None
    description: Optional[str] = None

    class config:
        from_attributes = True


class ReadUserData(SQLModel):
    model_config = {"protected_namespace": ()}

    user_id: str | None = None
    user_name: str | None = None
    #password: str | None = None
    email: str | None = None

    created_at: datetime
    updated_at: datetime
    status: Optional[bool] = None
    description: Optional[str] = None

    class config:
        from_attributes = True


class UpdateUserData(SQLModel):
    model_config = {"protected_namespace": ()}

    #user_id: str | None = None
    #user_name: str | None = None
    password: str | None = None
    #email: str | None = None

    created_at: datetime
    updated_at: datetime
    status: Optional[bool] = None
    description: Optional[str] = None

    class config:
        from_attributes = True




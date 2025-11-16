from typing import Optional

from sqlmodel import SQLModel, Field

from datetime import datetime, timezone


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
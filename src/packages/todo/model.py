from typing import Optional

from sqlmodel import SQLModel, Field

from datetime import datetime, timezone


class Todo(SQLModel, table=True):
    model_config = {"protected_namespace":()}

    __tablename__ = "todo_master"

    id: int | None = Field(default=None, primary_key=True)
    todo_id: str  = Field(default=None, unique=True, index=True)
    user_id : str = Field(default=None, index=True)
    todo_task : str = Field(default=None)

    created_at : datetime = Field(default_factory=lambda :datetime.now(timezone.utc))
    updated_at : datetime = Field(default_factory=lambda :datetime.now(timezone.utc), sa_column_kwargs={"onupdate": lambda :datetime.now(timezone.utc)})
    status: Optional[bool] = None
    description: Optional[str] = None
    # description: str | None
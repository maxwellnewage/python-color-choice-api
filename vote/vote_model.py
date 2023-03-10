from sqlmodel import SQLModel, Field
from typing import Optional


class Vote(SQLModel, table=True):
    user_id: str = Field(default=None, primary_key=True)
    color_id_selected: Optional[int] = Field(default=None, foreign_key="color.color_id")
    color_voted: bool = Field(default=False)

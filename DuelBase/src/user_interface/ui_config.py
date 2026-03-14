from pydantic import BaseModel


class UIConfig(BaseModel):
    width: int = 800
    height: int = 600

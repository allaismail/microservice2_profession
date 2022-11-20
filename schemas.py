import datetime as _dt
import pydantic as _pydantic


class _BaseContact(_pydantic.BaseModel):
    profession : str


class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


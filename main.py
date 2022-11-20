from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
app = _fastapi.FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

@app.post("/api/users/", response_model=_schemas.Contact)
async def create_contact(
    contact: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_contact(contact=contact, db=db)



@app.get("/api/users/{contact_id}/", response_model=_schemas.Contact)
async def get_contact(
    contact_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")
    return contact

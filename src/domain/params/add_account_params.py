from typing import TypedDict


class AddAccountParams(TypedDict):
    id: str
    name: str
    email: str
    password: str

AddAccountResult = bool

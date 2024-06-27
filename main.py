from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Song(BaseModel):
    title: str
    author: str
    disk: str
    publisher: Optional[str]


@app.get("/")
def index():
    return {
        "Message": "Welcome.",
    }


@app.get("/song/{id}")
def give_back_song(id: int):
    return {"Perro Amor Explota": id}


@app.post("/books")
def put_song(song: Song):
    return {"msg": f"Song: {song.title} has been entered"}


@app.get("/songs")
def get_song(song: Song):
    return {f"{song.title}": f"{song.author}, {song.disk}, {song.publisher}"}

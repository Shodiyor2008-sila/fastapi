from fastapi import FastAPI
from . import models
from .database import engine
from .routes import user,post,auth,votes
from .config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# print(settings.database_username)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Список доменов, которым разрешен доступ
    allow_credentials=True,
    allow_methods=["*"],  # Разрешенные методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешенные заголовки
)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {'message':'Hello Wolrd'}





import logging
from fastapi import FastAPI
from game.endpoints import router as game_router
from users.endpoints import router as user_router
from questions.endpoints import questions_router


app = FastAPI()
app.include_router(user_router)
app.include_router(questions_router)
app.include_router(game_router)

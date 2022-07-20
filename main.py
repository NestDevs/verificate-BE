from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import questions_route, users_route

app = FastAPI(title="FastAPI", description="Verificate", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Verify your skills!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include urls from user.py
app.include_router(
    questions_route.router,
    tags=["questions"],
    prefix="/questions",
)

app.include_router(
    users_route.router,
    tags=["users"],
    prefix="/users",
)
from fastapi import APIRouter
from src.schema.questions_model import Question
# from src.controller.question_controls import get_questions, get_question, create_question, update_question, delete_question

router = APIRouter()

#create questions
@router.post("/questions")
async def create_question(question: Question):
    return question

#get questions/ random by category
@router.get("/questions/{category}")
async def get_questions(category: str):
    return category

#update questions
@router.put("/questions/{question_id}")
async def update_question(question_id: int, question: Question):
    return question

#delete questions
@router.delete("/questions/{question_id}")
async def delete_question(question_id: int):
    return question_id
from fastapi import APIRouter
from src.schema.questions_model import Question,Category
from src.controller.question_controls import get_questions, create_question, update_question, delete_question

router = APIRouter()

#create questions
@router.post("/questions")
async def _create_question(question: Question):
    return await create_question(question)

#get questions/ random by category
@router.get("/questions/{category}?number_of_questions={number_of_questions}")
async def _get_questions(category: Category = "GENERAL", number_of_questions: int = 5):
    return await get_questions(category, number_of_questions)

#update questions
@router.patch("/questions/{question_id}")
async def _update_question(question_id: int, question: Question):
    return await update_question(question_id, question)

#delete questions
@router.delete("/questions/{question_id}")
async def _delete_question(question_id: int):
    return await delete_question(question_id)
from fastapi import APIRouter
from src.schema.questions_model import Question,UpdateQuestion
from src.controller.question_controls import get_questions, create_question, update_question, delete_question

router = APIRouter()
#create questions
@router.post("/")
async def _create_question(question: Question):
    return await create_question(question)

#get questions/ random by category ?number_of_questions={number_of_questions}
@router.get("/{category}")
async def _get_questions(category, number_of_questions: int = 5):
    category = category.upper()
    return await get_questions(category, number_of_questions)

#update questions
@router.patch("/{question_id}")
async def _update_question(question_id, question: UpdateQuestion):
    return await update_question(question_id, question)

#delete questions
@router.delete("/{question_id}")
async def _delete_question(question_id):
    return await delete_question(question_id) 
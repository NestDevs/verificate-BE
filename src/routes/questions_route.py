from fastapi import APIRouter,Depends
from src.schema.questions_model import Question,UpdateQuestion
from src.utils.auth import verify_user
from src.schema.users_model import User
from src.controller.question_controls import (
     get_questions,
     create_question,
     update_question,
     delete_question,
     process_quiz_question
)
router = APIRouter()
#create questions
@router.post("/")
async def _create_question(question: Question,current_user:User=Depends(verify_user)):
    return await create_question(question,current_user)

#get questions/ random by category ?number_of_questions={number_of_questions}
@router.get("/{category}")
async def _get_questions(category, number_of_questions: int = 5,current_user:User=Depends(verify_user)):
    category = category.upper()
    return await get_questions(category, number_of_questions)

#update questions
@router.patch("/{question_id}")
async def _update_question(question_id, question: UpdateQuestion,current_user:User=Depends(verify_user)):
    return await update_question(question_id, question,current_user)

#delete questions
@router.delete("/{question_id}")
async def _delete_question(question_id,current_user:User=Depends(verify_user)):
    return await delete_question(question_id,current_user) 

# get results
@router.post("/")
async def _process_results(submission_: dict,current_user:User=Depends(verify_user)):
    return await process_quiz_question(submission_,current_user)
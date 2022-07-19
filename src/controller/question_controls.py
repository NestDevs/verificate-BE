# for the questions controller
from src.schema.questions_model import Question,Category,UpdateQuestion
from src.utils.functions import Model
import json
import random

# create questions
async def create_question(question: Question):
    """
        Create a question
        :param question: Question object
        :return: created Question object
    """
    try:
        # validate that caller is authorized to create a question
        # ---- TODO ---- auth user check
        # create question
        question = question.dict()
        question_exist = await Model.findone({"question": question["question"]}, "questions_collection")
        if question_exist is None:
            await Model.create(question, "questions_collection")
            return {
                "question":question,
                "success":True,
                "message":"Question created successfully",
                "status":201
                }
        return {
            "question":question,
            "success":False,
            "message":"Question already exists",
            "status":409
            }
    except Exception as error:
        return {
            "error": f'{error}',
            "success":False,
            "status":500,
            "message":"An error occurred while creating the question"
            }

# get questions/ random by category default is general and default number of question is 5 questions
async def get_questions(category: Category = "GENERAL", number_of_questions: int = 5):
    """
        Get questions by category
        :param category: category of questions
        :param min: minimum number of questions to return
        :return: list of questions
    """
    try:
        # validate that caller is authorized to take the test
        # ---- TODO ---- auth user check
        # get questions
        questions = await Model.findall({"category": category}, "questions_collection")
        
        # get random questions if questions are greater than default
        if len(questions) > number_of_questions:
            questions = random.sample(questions, number_of_questions)
            return {
                "questions":questions,
                "success":True,
                "message":"Questions retrieved successfully",
                "status":200
                }
        return {
            "questions": random.sample(questions, 1) if len(questions)>1  else questions,
            "success":True,
            "message":"Questions retrieved successfully",
            "status":200
            }
    except Exception as error:
        return {
            "error": f'{error}',
            "success":False,
            "status":500,
            "message":"An error occurred while retrieving the questions"
            }

# update questions
async def update_question(question_id, question: UpdateQuestion):
    """
        Update a question
        :param question_id: id of question to update
        :param question: Question object
        :return: updated Question object
    """
    try:
        # validate that caller is authorized to update a question
        # ---- TODO ---- auth user check
        # update question
        
        question_exist = await Model.findone({"_id": question_id}, "questions_collection")
        if question_exist is not None:
            questions ={}
            for k,v in question.dict().items():
                if v is not None:
                    questions[k] = v
                else:
                    questions[k] = question_exist[k]
        
            await Model.update(question_id, questions, "questions_collection")
            return {
                "question":questions,
                "success":True,
                "message":"Question updated successfully",
                "status":200
                }
        return {
            "question":question.dict(),
            "success":False,
            "message":"Question does not exist",
            "status":404
            }
    except Exception as error:
        return {
            "error": f'{error}',
            "success":False,
            "status":500,
            "message":"An error occurred while updating the question"
            }
  
# delete questions
async def delete_question(question_id):
    """
        Delete a question
        :param question_id: id of question to delete
        :return: deleted Question object
    """
    try:
        # validate that caller is authorized to delete a question
        # ---- TODO ---- auth user check
        # delete question
        question_exist = await Model.findone({"_id": question_id}, "questions_collection")
        if question_exist is not None:
            await Model.delete(question_id, "questions_collection")
            return {
                "question_id":question_id,
                "success":True,
                "message":"Question deleted successfully",
                "status":200
                }
        return {
            "question_id":question_id,
            "success":False,
            "message":"Question does not exist",
            "status":404
            }
    except Exception as error:
        return {
            "error": f'{error}',
            "success":False,
            "status":500,
            "message":"An error occurred while deleting the question"
            }
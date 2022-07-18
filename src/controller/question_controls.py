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
            return json.dumps({
                "question":question,
                "success":True,
                "message":"Question created successfully",
                "status":201
                })
        return json.dumps({
            "question":question,
            "success":False,
            "message":"Question already exists",
            "status":409
            })
    except Exception as error:
        return json.dumps({
            "error": f'{error}',
            "success":False
            })

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
            return json.dumps({
                "questions":questions,
                "success":True,
                "message":"Questions retrieved successfully",
                "status":200
                })
        return json.dumps({
            "questions":questions,
            "success":True,
            "message":"Questions retrieved successfully",
            "status":200
            })
    except Exception as error:
        return json.dumps({
            "error": f'{error}',
            "success":False
            })

# update questions
async def update_question(question_id: int, question: UpdateQuestion):
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
        question = question.dict()
        question_exist = await Model.findone({"_id": question_id}, "questions_collection")
        if question_exist is not None:
            await Model.update(question_id, question, "questions_collection")
            return json.dumps({
                "question":question,
                "success":True,
                "message":"Question updated successfully",
                "status":200
                })
        return json.dumps({
            "question":question,
            "success":False,
            "message":"Question does not exist",
            "status":404
            })
    except Exception as error:
        return json.dumps({
            "error": f'{error}',
            "success":False
            })
  
# delete questions
async def delete_question(question_id: int):
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
            return json.dumps({
                "question_id":question_id,
                "success":True,
                "message":"Question deleted successfully",
                "status":200
                })
        return json.dumps({
            "question_id":question_id,
            "success":False,
            "message":"Question does not exist",
            "status":404
            })
    except Exception as error:
        return json.dumps({
            "error": f'{error}',
            "success":False
            })
# for the questions controller
from src.schema.questions_model import Question,Category,UpdateQuestion
from src.utils.functions import Model
import random

# create questions
async def create_question(question: Question,current_user):
    """
        Create a question
        :param question: Question object
        :return: created Question object
    """
    try:
        # validate that caller is authorized to create a question
        is_verifier = current_user["is_verifier"]

        if not is_verifier:
            return {
                "success":False,
                "message":"Unauthorize access",
                "status":403
            }
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
async def update_question(question_id, question: UpdateQuestion,current_user):
    """
        Update a question
        :param question_id: id of question to update
        :param question: Question object
        :return: updated Question object
    """
    try:
        # validate that caller is authorized to update a question
        is_verifier = current_user["is_verifier"]
        if not is_verifier:
            return {
                "success":False,
                "message":"Unauthorize access",
                "status":403
            }
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
async def delete_question(question_id,current_user):
    """
        Delete a question
        :param question_id: id of question to delete
        :return: deleted Question object
    """
    try:
        # validate that caller is authorized to delete a question
        is_verifier = current_user["is_verifier"]
        
        if not is_verifier:
            return {
                "success":False,
                "message":"Unauthorize access",
                "status":403
            }
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

# process/mark quiz questions
async def process_quiz_question(submission_,current_user):
    """
        Process submitted   quiz question and answers
        :param submission: list of quiz questions and user answers
        :return: 
            {
                "success":True,
                "message":"Results Ready",
                "score": 19,
                "test_status":"FAILED",
                "status":200
            }

            submission_object={
                "skill":"REACT",
                "level":"BEGINNER",
                "quiz": [
                    {"question_id":"iw83084308","user_answer":"a"},
                    {"question_id":"iw8308430822","user_answer":"a"},
                    ]
            }
    """
    def quiz_question(questions,submission):
        submitted_ids = [i["question_id"] for i in submission["quiz"]]
        filtered = []
        for question in questions:
            if question["_id"] in submitted_ids:
                filtered.append(question)
        return filtered

    def validate_answers(question,submission):
        scores = []
        if len(questions) == len(submission):
            return {
                "success":False,
                "message":"Invalid test",
                "status":422
            }
        for quiz in range(len(questions)):
            if question[quiz]["answer"] == submission[quiz]["user_answer"]:
                scores.append(question[quiz]["mark"])
        total_mark = sum(scores)
        return total_mark
    try:
        submission =submission_.keys()
        # check if there is a submission object
        if "skill" not in submission.keys():
            return {
                "success": False,
                "message": "Invalid test for a Skill",
                "status":422
            }
        # get all questions for a category
        questions = await Model.findall({"category": submission["skill"].upper()}, "questions_collection")
        if len(questions) == 0:
            return {
                "success": False,
                "message": "Invalid test for a Skill",
                "status":422
                }
        filter_questions= quiz_question(questions,submission)
        total_mark = validate_answers(filter_questions,submission)
        
      
        # update user test result
        user = await Model.findone({"_id":current_user["_id"]},"users_collection")
        test_query_object = {
            "user_id": str(user["_id"]),
            "category":submission["skill"].upper(),
            "level": submission["level"].upper()
        }
        test_object={
            "user_id": str(user["_id"]),
            "category":submission["skill"].upper(),
            "level": submission["level"],
            "test_result": "FAILED" if total_mark < 65 else "PASSED",
            "score": total_mark
        }

        test_result = Model.findall(test_query_object,"user_results_collection")
        if test_result is None:
            new_test = await Model.create(test_object,"user_results_collection")
            return {
                "success":True,
                "message":"Results Successfully generated",
                "status":201,
                "payload":new_test
            }
        # update test results
        updated_result = await Model.update(test_object,"user_results_collection")
        return {
                "success":True,
                "message":"Results Successfully generated",
                "status":201,
                "payload":updated_result
            }

    except Exception as error:
        return {
            "error": f'{error}',
            "success":False,
            "status":500,
            "message":"An error occurred while computting results"
            }
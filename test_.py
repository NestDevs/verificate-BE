def quiz_question(questions,submission):
        submitted_ids = [i["question_id"] for i in submission["quiz"]]
    
        filtered = []
        for question in questions:
            if question["_id"] in submitted_ids:
                filtered.append(question)
        return filtered

submission_object={
                "skill":"REACT",
                "level":"BEGINNER",
                "quiz": [
                    {"question_id":"iw83084308","user_answer":"a"},
                    {"question_id":"iw8308430822","user_answer":"a"},
                    ]
            }
question = {
    "_id":"iw83084308",
    "test_name": "vereeif",
    "skill_level": "BEGINNER",
    "question":"secret of the world",
    "options": {
        "a":"money",
        "b":"money",
        "c":"money",
        "d":"money",
    },
    "answer": "a",
    "duration": 1.0,
    "category":"REACT",
    "set_by": "LOARD"
}
question1 = {
    "_id":"iw83084308e",
    "test_name": "vereeif",
    "skill_level": "BEGINNER",
    "question":"secret of the world",
    "options": {
        "a":"money",
        "b":"money",
        "c":"money",
        "d":"money",
    },
    "answer": "a",
    "duration": 1.0,
    "category":"JAVASCRIPT",
    "set_by": "LOARD"
}
question2 = {
    "_id":"iw8308430822",
    "test_name": "vereeif",
    "skill_level": "BEGINNER",
    "question":"secret of the world REACT WORLD",
    "options": {
        "a":"STUDF",
        "b":"money",
        "c":"money",
        "d":"money",
    },
    "answer": "d",
    "duration": 1.0,
    "category":"REACT",
    "set_by": "LUIS"
}

questions = [question,question1,question2]

filtered = quiz_question(questions=questions,submission=submission_object)
print(filtered)

user = {
           "first_name":"John",
            "last_name":"Doe",
            "email":"johndoe@gmail.com",
            "password":"123456789",
            "linked_in":"https://www.linkedin.com/in/johndoe",
            "results":{
                "java":[
                    {
                        "level":"BEGINNER",
                        "test_result":"FAILED",
                        "score":10
                    },
                    {
                        "level":"INTERMEDIATE",
                        "test_result":"PASSED",
                        "score":70
                    },
                    {
                        "level":"ADVANCED",
                        "test_result":"FAILED",
                        "score":40
                    }

                ]
            }
            
        }
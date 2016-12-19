#Imports
from db import Database

#Database file
filen = ""


def getQuestions(surveyID):
    #Connect to databse
    db = Database(filename = filen)
    questions = []
    
    #grab questions for survey
    for q in db.retrieve("questions","Survey",surveyID):
        question = {"id" :q['ID'] , "question" : q['Question'] , "type" : q['Answer_type'] , "answers" : q['Answer_text'].split(",")}
        questions.append(question)

    #close db and return questions
    db.close()
    return questions
          
def submit(answers):
    #Connect to databse
    db = Database(filename = filen)
    
    #Add answers to database
    try:
        for ans in answers:
            db.insert("answers",{"Question" : ans['QuestionID'], "Person" : ans['PersonID'], "Result" : ans['result']})
    except:
        #close db and return failure
        db.close()
        return False

    #close db and return success
    db.close()
    return True
    


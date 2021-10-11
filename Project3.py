import sqlite3

conn = sqlite3.connect('QuizQuestions.db')

cursor = conn.cursor()


def main():
    cursor.execute('select Category from QuestionsAndAnswers')

    result = cursor.fetchall()
    categorys = []
    for row in result:
        if row not in categorys:
            categorys.append(row)   
    print('Welcome which of the categories here would you like to be quizzed on?', categorys)
    cursor.execute('select QuestionText from QuestionsAndAnswers')

    result = cursor.fetchall()
    numbercorrect = 0
    for row in result:
        print(row)
        answers = createCorrectanswers()
        incorrect1 = Wronganswer1()
        incorrect2 = Wronganswer2()
        incorrect3 = Wronganswer3()
        print(answers)
        print(incorrect1)
        print(incorrect2)
        print(incorrect3)
        InputAnswer = input("")
        print('\n')
        if(InputAnswer == "A."):
            numbercorrect += 1
    username = input("What is your name?: ")
    print('congrats' + username + ' You got ' + numbercorrect)
    StoreResults(numbercorrect)
            

    

def StoreResults(numbercorrect):
    
    conn.execute('INSERT INTO QuizResults Score(numbercorrect)')
    conn.execute('INSERT INTO QuizResults Name(name)')
    conn.commit()



def createCorrectanswers():
    cursor.execute('select CorrectAnswer from QuestionsAndAnswers')
    result = cursor.fetchall()
    for row in result:
        print('A. ', row)
def Wronganswer1():
    cursor.execute('select WrongAnswer1 from QuestionsAndAnswers')
    result = cursor.fetchall()
    for row in result:
        print('B. ', row)
def Wronganswer2():
    cursor.execute('select WrongAnswer2 from QuestionsAndAnswers')
    result = cursor.fetchall()
    for row in result:
        print('C. ', row)
def Wronganswer3():
    cursor.execute('select WrongAnswer3 from QuestionsAndAnswers')
    result = cursor.fetchall()
    for row in result:
        print('D. ', row)


main()
import sys
sys.path.append("")

from util.helper import clear
from quiz_brain import QuizBrain

clear()
print('''
                                           
   _|_|      _|    _|  _|_|_|  _|_|_|_|_|  
 _|    _|    _|    _|    _|          _|    
 _|  _|_|    _|    _|    _|        _|      
 _|    _|    _|    _|    _|      _|        
   _|_|  _|    _|_|    _|_|_|  _|_|_|_|_|  
                                                                             
''')

from data import question_data, trivia_db_question_bank
from question_model import Question

question_bank = []

# for question in question_data:
#     new_question = Question(question['text'], question['answer'])
#     question_bank.append(new_question)

for question in trivia_db_question_bank:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print(f"\nFinal score: {quiz.score}/{len(quiz.question_list)}\n")

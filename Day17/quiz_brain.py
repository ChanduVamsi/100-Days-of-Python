class QuizBrain:
    def __init__(self, questions) -> None:
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def nextQuestion(self):
        ''''''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.checkAnswer(current_question.answer, input(f"\nQ{self.question_number}: {current_question.text} (True/False): ").capitalize())
        print(f"Current score: {self.score}/{self.question_number}")
    
    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self, solution, answer): 
        if solution == answer: 
            print("You got it right.")
            self.score += 1
        else: print("That's wrong.")
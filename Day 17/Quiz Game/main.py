from question_model import QuestionBank
from quiz_brain import QuizBrain


question_bank = QuestionBank(10, 'easy')
quiz = QuizBrain(question_bank.get_questions())

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

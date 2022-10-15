import requests
from html import unescape

class Question:
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer

    def __str__(self):
        return f'Question: {self.question}\nAnswer: {self.answer}'


def get_question_data(amount=10):
    params = {
        'amount': amount,
        'type': 'boolean'
    }
    response = requests.get('https://opentdb.com/api.php', params=params)
    data = response.json()['results']
    questions = [Question(unescape(question['question']), question['correct_answer']) for question in data]
    return questions


class Quiz:
    def __init__(self):
        self.questions = get_question_data()
        self.score = 0
        self.current_question = 0

    # func to return current question
    def get_question(self):
        q_text = self.questions[self.current_question].question
        q_number = self.current_question + 1
        return f'Q{q_number}: {q_text}'

    # func to return next question
    def next_question(self):
        question = self.get_question()
        self.current_question += 1
        return question

    # func to check the answer of the current question
    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question-1].answer
        return user_answer == correct_answer

    # func that returns true when there are questions remaining
    def has_questions(self):
        return self.current_question < len(self.questions)

    def increase_score(self):
        self.score += 1

import requests
import json
from html import unescape


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionBank:
    def __init__(self, question_count, difficulty):
        self.req = requests.get(
            f'https://opentdb.com/api.php?amount={question_count}&category=9&difficulty={difficulty}&type=boolean')
        self.data = json.loads(self.req.text)
        self.question_data = self.data['results']
        for item in self.question_data:
            item['question'] = unescape(item['question'])

    def get_questions(self):
        questions = [Question(item['question'], item['correct_answer']) for item in self.question_data]
        return questions

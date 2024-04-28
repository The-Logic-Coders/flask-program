from app.models import Questions
import random

class QuizHandler:
    def __init__(self):
        
        self.question_ids = [q.id for q in Questions.query.with_entities(Questions.id).all()]
        random.shuffle(self.question_ids)
        self.score = 0
        self.completed = False
        self.curr_index = 0
        
    def get_current_question(self):
        if self.curr_index < len(self.question_ids):
            question_id = self.question_ids[self.curr_index]
            return Questions.query.get(question_id)
        return None
        
    def submit_answer(self, selected_option):
        if not selected_option:
            return False 
        question = self.get_current_question()
        if question and question.correct_answer.lower() == selected_option.lower():
            self.score += 1
            return True
        return False
    
    def next_question(self):
        if self.curr_index < len(self.question_ids) - 1:
            self.curr_index += 1
        else:
            self.completed = True

    def get_quiz_length(self):
        return len(self.question_ids)
    
    def get_quiz_score(self):
        return self.score

    def serialize(self):
        return {
            "question_ids": self.question_ids,
            "current_index": self.curr_index,
            "score": self.score,
            "completed": self.completed
        }

    @staticmethod
    def deserialize(data):
        quiz = QuizHandler()
        quiz.question_ids = data.get("question_ids", [])
        quiz.curr_index = data.get("current_index", 0)
        quiz.score = data.get("score", 0)
        quiz.completed = data.get("completed", False)
        return quiz


        
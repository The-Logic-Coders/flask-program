from flask import Blueprint, render_template, session


main = Blueprint('main', __name__)

@main.route('/')
def index():
    session_keys = ['quiz_completed', 'score', 'current_index', 'question_ids', 'quiz_length', 'final_score']
    for key in session_keys:
        session.pop(key, None)
    
    return render_template('/home.html')

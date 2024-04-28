from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.models import Questions
import random
from app.utils.quiz_handler import QuizHandler

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quiz')
def start():
    quiz_handler = QuizHandler()
    session['quiz'] = quiz_handler.serialize()
    return redirect(url_for('quiz.questions', index=0))
    

@quiz_bp.route('/quiz/question/<int:index>')
def questions(index):
    if 'quiz' not in session:
        flash('Please start the quiz first.', 'warning')
        return redirect(url_for('quiz.start'))

    quiz_handler = QuizHandler.deserialize(session['quiz'])
    
    if quiz_handler.completed or index != quiz_handler.curr_index:
        return redirect(url_for('quiz.results'))
    
    question = quiz_handler.get_current_question()
    
    if question:
        return render_template('quiz.html', question=question, index=index)
    else:
        quiz_handler.curr_index += 1 
        session['quiz'] = quiz_handler.serialize() 
        return redirect(url_for('quiz.questions', index=quiz_handler.curr_index))

    
@quiz_bp.route('/submit_answer/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    selected_option = request.form.get('q_answer')
    
    quiz_data = session.get('quiz')
    if not quiz_data:
        flash("Quiz not started.", "warning")
        return redirect(url_for('quiz.start'))

    quiz_handler = QuizHandler.deserialize(quiz_data)

    # Check if an answer was submitted
    if not selected_option:
        flash('Please select an option.', 'warning')
        # Do not advance to the next question, just reload current question
        return redirect(url_for('quiz.questions', index=quiz_handler.curr_index))
    else:
        if quiz_handler.submit_answer(selected_option):
            flash('Correct!', 'success')
        else:
            flash('Incorrect answer.', 'info')
        # Only advance to the next question if an option was submitted
        quiz_handler.next_question()

    session['quiz'] = quiz_handler.serialize()
    
    if quiz_handler.completed:
        return redirect(url_for('quiz.results'))
    else:
        return redirect(url_for('quiz.questions', index=quiz_handler.curr_index))

@quiz_bp.route('/results')
def results():
    if 'quiz' not in session:
        flash('Quiz not started or session expired.', 'warning')
        return redirect(url_for('quiz.start'))
    
    quiz_handler = QuizHandler.deserialize(session['quiz'])
    
    if not quiz_handler.completed:
        flash('Quiz is not yet completed.', 'info')
        return redirect(url_for('quiz.questions', index=quiz_handler.curr_index))

    session.clear() 
    return render_template('results.html', final_score=quiz_handler.score, quiz_length=quiz_handler.get_quiz_length())


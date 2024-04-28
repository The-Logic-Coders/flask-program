from flask import Blueprint, request, flash, redirect, url_for, session
from app import db
from app.models import Questions
from app.utils.handler import Handler 

utils = Blueprint('utils', __name__)


@utils.route('/upload', methods=['POST'])
def upload_file():
    
    if 'question_ids' in session and 'quiz_completed' not in session:
        flash('You cannot upload questions during an ongoing quiz.', 'error')
        return redirect(url_for('main.index'))
    
    if 'file' not in request.files:
        flash('Missing File Data', 'error')
        return redirect(url_for('/'))
    file = request.files['file']
    if file:
        if Questions.query.first():
            flash('The database already has questions. Starting the quiz with existing questions.', 'info')
            return redirect(url_for('quiz.start'))
        try:
            processed_q, erroneous_q = Handler.process_file(file)
            db.create_all()
            for question in processed_q:
                question = Questions(**question)
                db.session.add(question)
            db.session.commit()
            
            flash('Questions uploaded successfully', 'success')
            return redirect(url_for('quiz.start'))
        
        except Exception as e:
            db.session.rollback()
            flash(str(e), 'error')
            return redirect(url_for('main.index'))
        
    
    


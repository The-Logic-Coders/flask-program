from app import db

class Questions(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(350), unique = True, nullable = False)
    option_a  = db.Column(db.String(100), nullable = False)
    option_b = db.Column(db.String(100), nullable = False)
    option_c = db.Column(db.String(100), nullable = False)
    option_d = db.Column(db.String(100), nullable = False)
    difficulty = db.Column(db.Enum('easy','medium','challenging'),name = 'difficulty', nullable = False)
    correct_answer = db.Column(db.String(100), nullable=False)
    
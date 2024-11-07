from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__, template_folder='../templates')
app.secret_key = 'quiz_app_secret'  # session manage

# sample q/a
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "J.K. Rowling"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O"
    }
]

# route for quiz to start
@app.route('/')
def home():
    # random q/a
    random.shuffle(questions)
    for i in questions:
        random.shuffle(i["options"])
    
    # storing each random q/a in session: no chage after session begans
    session['questions'] = questions
    session['current_question'] = 0  # Start at the first question
    session['score'] = 0  # Reset score at the start

    return redirect(url_for('question', question_number=0))

# to handle q/a
@app.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question(question_number):
    questions = session.get('questions', [])
    current_question = questions[question_number]

    if request.method == 'POST':
        # user answer from form
        selected_answer = request.form.get('answer')
        
        # answer check krna padega to update score
        if selected_answer == current_question['answer']:
            session['score'] += 1

       
        question_number += 1

        # result after 5th
        if question_number >= len(questions):
            return redirect(url_for('result'))

        #otherwise ++
        return redirect(url_for('question', question_number=question_number))

    return render_template('main.html', question=current_question, question_number=question_number, total=len(questions))

# final score implement
@app.route('/result')
def result():
    score = session.get('score', 0)
    total_questions = len(session.get('questions', []))

    print(f'Final Score: {score} / {total_questions}')



    return render_template('result.html', score=score, total=total_questions)

if __name__ == '__main__':
    app.run(port=8000, debug=True)

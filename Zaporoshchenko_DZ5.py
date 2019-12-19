from flask import Flask, render_template, request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3


db = sqlite3.connect('test.db')
cur = db.cursor()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Respondents(db.Model):
    __tablename__ = 'respondents'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Text)
    age = db.Column(db.Integer)


class Responses(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    q1_1 = db.Column(db.Text)
    q1_2 = db.Column(db.Text)
    q1_3 = db.Column(db.Text)
    q1 = db.Column(db.Text)
    q2_1 = db.Column(db.Text)
    q2_2 = db.Column(db.Text)
    q2_3 = db.Column(db.Text)
    q2 = db.Column(db.Text)
    q3_1 = db.Column(db.Text)
    q3_2 = db.Column(db.Text)
    q3_3 = db.Column(db.Text)
    q3 = db.Column(db.Text)
    q4_1 = db.Column(db.Text)
    q4_2 = db.Column(db.Text)
    q4_3 = db.Column(db.Text)
    q4 = db.Column(db.Text)
    q5_1 = db.Column(db.Text)
    q5_2 = db.Column(db.Text)
    q5_3 = db.Column(db.Text)
    q5 = db.Column(db.Text)


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)


@app.route('/')
def questionnaire():
    return render_template('questionnaire.html')


@app.route('/statistics')
def statistics():
    db = sqlite3.connect('test_full.db')
    cur = db.cursor()
    cur.execute('SELECT COUNT(*) FROM `respondents`')
    r = cur.fetchone()
    r = r[0]
    db = sqlite3.connect('test.db')
    cur = db.cursor()
    cur.execute('SELECT q1, q2, q3, q4, q5 from responses')
    p = cur.fetchall()
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    for i in p:
        num = 0
        for t in i:
            num = num + 1
            if t != "":
                if num == 1:
                    q1.append(t)
                if num == 2:
                    q2.append(t)
                if num == 3:
                    q3.append(t)
                if num == 4:
                    q4.append(t)
                if num == 5:
                    q5.append(t)
    q1 = " ,".join(q1)
    q2 = " ,".join(q2)
    q3 = " ,".join(q3)
    q4 = " ,".join(q4)
    q5 = " ,".join(q5)
    return render_template('statistics.html', r=r, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)


@app.route('/results', methods=['get'])
def results():
    if not request.args:
        return redirect(url_for('questionnaire'))
    gender = request.args.get('gender')
    age = request.args.get('age')
    respondents = Respondents(
        gender=gender,
        age=age
    )
    db.session.add(respondents)
    db.session.commit()
    q1_1 = request.args.get('q1_1')
    q1_2 = request.args.get('q1_2')
    q1_3 = request.args.get('q1_3')
    q1 = request.args.get('q1')
    q2_1 = request.args.get('q2_1')
    q2_2 = request.args.get('q2_2')
    q2_3 = request.args.get('q2_3')
    q2 = request.args.get('q2')
    q3_1 = request.args.get('q3_1')
    q3_2 = request.args.get('q3_2')
    q3_3 = request.args.get('q3_3')
    q3 = request.args.get('q3')
    q4_1 = request.args.get('q4_1')
    q4_2 = request.args.get('q4_2')
    q4_3 = request.args.get('q4_3')
    q4 = request.args.get('q4')
    q5_1 = request.args.get('q5_1')
    q5_2 = request.args.get('q5_2')
    q5_3 = request.args.get('q5_3')
    q5 = request.args.get('q5')
    responses = Responses(
        q1_1=q1_1,
        q1_2=q1_2,
        q1_3=q1_3,
        q1=q1,
        q2_1=q2_1,
        q2_2=q2_2,
        q2_3=q2_3,
        q2=q2,
        q3_1=q3_1,
        q3_2=q3_2,
        q3_3=q3_3,
        q3=q3,
        q4_1=q4_1,
        q4_2=q4_2,
        q4_3=q4_3,
        q4=q4,
        q5_1=q5_1,
        q5_2=q5_2,
        q5_3=q5_3,
        q5=q5
    )
    db.session.add(responses)
    db.session.commit()
    return render_template('results.html')


if __name__ == '__main__':
    app.run()
#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice
import requests

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id

def scrape():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [elem.string for elem in soup.select("h3")]
    headline = choice(headlines)
    return headline



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())


@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cilia")
def cilia():
    return render_template("cilia.html")

@app.route("/sophie")
def sophie():
    return render_template("sophie.html")

@app.route("/trixie")
def trixie():
    return render_template("trixie.html")

@app.route("/webscraping")
def webscraping():
    headline =scrape()
    return render_template("webscraping.html",headline=headline)


if __name__ == "__main__":
    app.run()


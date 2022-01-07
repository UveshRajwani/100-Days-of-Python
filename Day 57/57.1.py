from flask import Flask, render_template
import requests
app = Flask(__name__)



@app.route('/guess/<name>')
def hello_world(name):
    agify = requests.get(f"https://api.agify.io?name={name}")
    genderize = requests.get(f"https://api.genderize.io?name={name}")
    age = agify.json()["age"]
    gender = genderize.json()["gender"]
    print(gender)
    message = f"Hey {name},\nI think you are {gender},\nAnd maybe {age} year old."
    return message


if __name__ == "__main__":
    app.run(debug=True)
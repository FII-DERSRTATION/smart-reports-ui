import json

from flask import Flask, render_template, request


from docs_generator.docs_generator import generate_dummy_docx_file


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', title='test', userName='kentei')

@app.route('/generate')
def generate():
    firstName = request.args['firstName']
    lastName = request.args['lastName']
    SID = request.args['SID']
    anamnesis = request.args['anamnesis']

    anamnesisGen = requests.get("http://127.0.0.1:5001/anamnesis", params={'key1': anamnesis}).content
    berteilung = requests.get("http://127.0.0.1:5001/berteilung", params={'key1': anamnesisGen}).content

    generate_dummy_docx_file(firstName, lastName, SID, anamnesisGen, berteilung)

    return ''


if __name__ == '__main__':
    app.run()

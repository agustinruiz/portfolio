import csv
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_homepage(page_name = 'index.html'):
    return render_template(page_name)

def write_to_csv(data):
    with open('venv/database.csv', mode='a', newline='') as database:
        print(data)
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Submited Ok'
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<name>')
def page_identity(name=None):
    return render_template(name)

def write_to_file(data):
    with open('database.txt','a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n Email: {email}\n Subject: {subject}\n Message: {message} \n ')

def write_to_csv(data):
    with open('database.csv','a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('submit.html')
        except:
            return'something went wrong try again'
    else:
        return redirect('error.html')
    
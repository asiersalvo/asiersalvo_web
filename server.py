from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

#este @ es un decorador, acordarse:
#https://www.geeksforgeeks.org/decorators-in-python/
#En este caso, lo que va a pasar aquí es que cada vez que usemos una ruta con / se va a ejecutar un hello_world
# @app.route('/')
# def hello_world():
#     return 'Hello, Asier!'
# @app.route('/blog')
# def blog():
#     return 'This is my personal blog!'
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/<username>/<int:post_id>')
# def user_name_page(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
# @app.route('/index.html')
# def index_file():
#     return render_template('index.html')
# @app.route('/about.html')
# def about_file():
#     return render_template('about.html')
# @app.route('/contact.html')
# def contact_file():
#     return render_template('contact.html')
# @app.route('/components.html')
# def components_file():
#     return render_template('components.html')
# @app.route('/work.html')
# def work_file():
#     return render_template('work.html')
# @app.route('/works.html')
# def works_file():
#     return render_template('works.html')
#En vez de usar todo lo anterior de manera manual, vamos a generar algo más automatizado:
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#Con esta función lo que hacemos es escribir una BBDD en txt
def write_to_txt(data):
    with open('database.txt',mode='a') as database_txt:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database_txt.write(f'\n{email},{subject},{message}')

#Con esta función lo que hacemos es escribir una BBDD en CSV
def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv,delimiter= ',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
       data = request.form.to_dict()
       write_to_csv(data)
       return redirect('./thanks.html')
   else:
       return 'Something went wrong!'



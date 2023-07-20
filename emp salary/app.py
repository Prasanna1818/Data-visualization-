from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(_name_)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('home.html', num_emp=4)

@app.route('/process', methods=['POST'])
def process():
    employees = request.form.getlist('employee')
    salaries = request.form.getlist('salary')
    salaries = [int(salary) for salary in salaries]
    #bargraph
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.bar(employees, salaries)
    plt.xlabel('Employee')
    plt.ylabel('Salary')
    plt.title('Employee salary')
    plt.xticks(rotation=45)
    plt.title('employee salary Distribution')
    plt.savefig('static/visualization.png')
    plt.close()
    return render_template('visualization.html')
if _name_ == '_main_':
    app.run(debug=True)
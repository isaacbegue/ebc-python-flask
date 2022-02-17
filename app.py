from flask import Flask, request, render_template, url_for, redirect
from database import tasks
app = Flask(__name__)

#el método http de route por default es GET, ejecuta la funcion definida enseguida
@app.route("/")
def index():
    return render_template('index.html', todoList = tasks)

@app.route("/", methods=['POST'])
def add_new_tasK():
    if request.method == 'POST':
        newTask = {"id": len(tasks) + 1, "name": request.form['task_name']}
        tasks.append(newTask)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
from flask import Flask, request, render_template
app = Flask(__name__)

#el método http de route por default es GET, ejecuta la funcion definida enseguida
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def add_new_tasK():
    if request.method == 'POST':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
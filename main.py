from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html', name="Aaliyah")


if __name__ == '__main__':
    app.run(debug=True)


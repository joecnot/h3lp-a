from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    message = request.form['message']
    posts.append({'name': name, 'message': message})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

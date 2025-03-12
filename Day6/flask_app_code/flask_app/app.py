from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from forms import LoginForm
from models import db, User
from flask_restful import Api
from routes import UserListResource, UserResource, CreateUserResource, UpdateUserResource, DeleteUserResource

app = Flask(__name__) # Initialize the flask app
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize the database with the app
api = Api(app)

# Registering API routes
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(CreateUserResource, '/users/add')
api.add_resource(UpdateUserResource, '/user/update/<int:user_id>')
api.add_resource(DeleteUserResource, '/user/delete/<int:user_id>')

@app.route('/add_user')
def add_user():
    new_user = User(username="JohnDoe", email="johndoe@example.com")
    db.session.add(new_user)
    db.session.commit()
    return "User added successfully!"

@app.route('/') # Define a route for the home page
def home_page():
    return render_template('home.html', username='Siva Sai Narayana')

@app.route('/about') # Define a route for the home page
def about():
    return render_template('about.html')

@app.route('/user/<name>')
def greet_user(name):
    return f'Hello {name}. Welcome to the Flask app...'

@app.route('/post/<int:post_id>')
def display_post(post_id):
    return f'Displaying post ID: {post_id}'

# Returning strings
@app.route('/hello')
def hello():
    return "Hello, Flask!"

# Returning HTML
@app.route('/html')
def show_html():
    return "<h1>Welcome to My Flask App</h1>"

# Returning JSON
@app.route('/api')
def api():
    return jsonify({"message": "Hello, Flask!", "status": "success"})

# Dummy user data for testing
users = {
    "testuser": "password123",  # Replace with a database in real apps
}

@app.route('/index')
def index():
    return render_template('index.html', error=None)  # Pass 'error' as None initially

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return render_template('index.html', error="All fields are required!")

    if len(password) < 6:
        return render_template('index.html', error="Password must be at least 6 characters long!")

    if username in users and users[username] == password:
        return redirect(url_for('dashboard', username=username))  
    else:
        return render_template('index.html', error="Invalid username or password!")

@app.route('/dashboard/<username>')
def dashboard(username):
    return f"<h1>Welcome, {username}!</h1><p>You have successfully logged in.</p>"

@app.route('/form', methods=['GET', 'POST'])
def Register_form():
    form = LoginForm()
    if form.validate_on_submit():
        return f"Welcome, {form.username.data}!"
    return render_template('form.html', form=form)

@app.route('/users')
def get_users():
    users = User.query.all()  # Fetch all users
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

@app.route('/users_html')
def users_html():
    users = User.query.all()  # Fetch users
    return render_template('users.html', users=users)  # Pass to template


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

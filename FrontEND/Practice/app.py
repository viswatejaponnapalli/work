from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup the database (SQLite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database will be stored in this file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Route to display the form and save user data
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']

        # Basic form validation
        if not username or not password:
            flash('Please fill in both fields', 'error')
            return redirect(url_for('index'))

        # Check if the username already exists in the database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already taken, please choose another one', 'error')
            return redirect(url_for('index'))

        # Create a new user instance
        new_user = User(username=username, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('User created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)

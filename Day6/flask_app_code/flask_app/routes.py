from flask import request, jsonify
from flask_restful import Resource
from models import db, User  # Import the models

# Get all users
class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

# Get a single user
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify({"id": user.id, "username": user.username, "email": user.email})
        return {"error": "User not found"}, 404

# Create a new user
class CreateUserResource(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User added successfully"}, 201

# Update an existing user
class UpdateUserResource(Resource):
    def put(self, user_id):
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            db.session.commit()
            return {"message": "User updated successfully"}
        return {"error": "User not found"}, 404

# Delete a user
class DeleteUserResource(Resource):
    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}
        return {"error": "User not found"}, 404

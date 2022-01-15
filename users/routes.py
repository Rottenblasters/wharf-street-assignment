from flask import Blueprint
from flask import jsonify
from flask import request
from flask_expects_json import expects_json
import json
import uuid

from .schema import create_user_schema, edit_user_schema

users = Blueprint('users', __name__)

# Route for creating a new user
@users.route("/", methods=['POST'])
@expects_json(create_user_schema)
def create():
    try:
        # get request body
        data = request.get_json()
        json_object = {}

        # print(data)
        with open('data.json', 'r') as jsonFile:
            # Reading from json file
            json_object = json.load(jsonFile)
        
        Users = json_object["Users"]
        
        isValid = True
        # Checking if email already exists 
        for user in Users:
            if(user['email'] == data['email']):
                isValid = False
                break
        
        if(isValid):
            # Adding new user
            data["id"] = str(uuid.uuid4())
            Users.append(data)
            json_object = {"Users": Users}

            with open("data.json", "w") as jsonFile:
                # Writing in json file
                json.dump(json_object, jsonFile)
            
            return jsonify({'statusCode' : 200, 'user': data})
        else:
            return jsonify({'statusCode' : 401, 'message' : f'Email Already Exists'})
    except:
        return jsonify({'statusCode' : 500, 'message' : f'Server Error'})

# Route for handling getting, updating and deleting a user
@users.route("/<id>", methods=['GET', 'PUT', 'DELETE'])
@expects_json(edit_user_schema, ignore_for=['GET', 'DELETE'])
def read(id):
    if request.method == 'GET':
        try:
            json_object = {}

            with open('data.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)

            Users = json_object["Users"]

            # Searching for user 
            for user in Users:
                if(user['id'] == id):
                    return jsonify({'statusCode' : 200, 'user': user})

            return jsonify({'statusCode' : 401, 'message' : f'User Not Found'})
        except:
            return jsonify({'statusCode' : 500, 'message' : f'Server Error'})

    if request.method == 'PUT':
        try:
            # get request body
            data = request.get_json()
            json_object = {}

            with open('data.json', 'r') as jsonFile:
                # Reading from json file
                json_object = json.load(jsonFile)

            Users = json_object["Users"]
            isValid = False
            # Searching for user 
            for user in Users:
                if(user['id'] == id):
                    # Update value of user
                    if 'name' in data:
                        user['name'] = data['name']
                    if 'mobile' in data:
                        user['mobile'] = data['mobile']
                    if 'password' in data:
                        user['password'] = data['password']
                    isValid = True
                    break
            
            if(isValid):
                json_object = {"Users": Users}

                with open("data.json", "w") as jsonFile:
                    # Writing in json file
                    json.dump(json_object, jsonFile)
                
                return jsonify({'statusCode' : 200, 'user': user})
            else:
                return jsonify({'statusCode' : 401, 'message' : f'User Not Found'})
        except:
            return jsonify({'statusCode' : 500, 'message' : f'Server Error'})

    if request.method == 'DELETE':
        try:
            json_object = {}

            with open('data.json', 'r') as jsonFile:
                # Reading from json file
                json_object = json.load(jsonFile)

            Users = json_object["Users"]
            userIndex = -1
            # Searching for user 
            for index in range(len(Users)):
                if(Users[index]["id"] == id):
                    userIndex = index
                    break
            
            if(userIndex != -1):
                # Delete User
                Users.pop(userIndex)
                json_object = {"Users": Users}

                with open("data.json", "w") as jsonFile:
                    # Writing in json file
                    json.dump(json_object, jsonFile)
                
                return jsonify({'statusCode' : 200, 'message': 'User Deleted'})
            else:
                return jsonify({'statusCode' : 401, 'message' : f'User Not Found'})
        except:
            return jsonify({'statusCode' : 500, 'message' : f'Server Error'})


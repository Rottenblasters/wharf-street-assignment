from flask import Flask
from flask import jsonify

from users.routes import users

app = Flask(__name__)

app.register_blueprint(users, url_prefix = '/users' )

@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

if __name__ == "__main__":
    app.run(debug=True)
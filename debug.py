from flask import Flask, request

from app.repo.user_repo import UserRepository

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/user', methods=['POST'])
def post_user():
    user = request.get_json()
    user_repo = UserRepository()
    repo = user_repo.create(user)
    return repo

@app.get('/user')
def get_user():
    params = request.args
    print(params["id"])
    user_repo = UserRepository()
    repo = user_repo.get_by_id(params["id"])
    return repo
    
    


app.run(debug=True)
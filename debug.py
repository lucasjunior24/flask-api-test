from flask import Flask, request
import time
from app.repo.user_repo import UserRepository

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    # pause = 0
    # startTime = time.time()
    # print(startTime)
    # for i in range(0,5):
    #     print(i)
    #     # making delay for 1 second
    #     time.sleep(1)
    # endTime = time.time()
    # print(endTime)
    # elapsedTime = endTime - startTime
    # print("Elapsed Time = %s" % elapsedTime)

    # while True:
    #     pause += 1
    #     print(str(pause))
    #     time.sleep(2)
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
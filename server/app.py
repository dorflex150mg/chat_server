#!/usr/bin/python
from convBook import ConvBook 
from flask import Flask, request
from sets import Set
from users import Users


app = Flask(__name__)

user_ip = {}
conversations = set()
users = Users()
convBook = ConvBook()

@app.route('/login', methods=['GET'])
def login():
    ip = request.remote_addr
    source_id = request.args["register"]
    if users.check_registered_users(source_id):
        user_ip[source_id] = ip
        app.logger.warning("User found!")
        return "200"
    app.logger.warning("users: %s | register: %s" % (str(users.users), str(source_id)))
    return "401"
    

@app.route('/read', methods=['GET'])
def read_request():
    print("DEBUG - received read_request")
    dest_id = request.args["dest_id"]
    source_id = request.args["register"]
    pair = tuple(Set([dest_id, source_id]))
    if pair in conversations:
        if convBook.checked(pair):
            return "200"
        else:
            return str(convBook.getConv(pair))
    return "404"


@app.route('/send', methods=['POST'])
def send_request():
    dest_id = request.form["dest_id"]
    source_id = request.form["source_id"]
    msg = request.form["msg"]
    pair = tuple(Set([dest_id, source_id]))
    if pair not in conversations:
        conversations.add(pair)
        convBook.add(pair)
    convBook.append(pair, msg)
    return "200"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

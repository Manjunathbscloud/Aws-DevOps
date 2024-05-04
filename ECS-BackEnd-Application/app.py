from flask import Flask, request
from werkzeug.urls import url_quote_plus

app = Flask(__name__)

@app.route('/path1', methods=['GET'])
def path1():
    print(request)
    return "This is response from path1, This response genereated by  Docker container which running in AWS ECS service "

@app.route('/path2', methods=['GET'])
def path2():
    print(request)
    return "This is response from path2, This response genereated by  Docker container which running in AWS ECS service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

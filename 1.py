from flask import Flask

app = Flask(__name__)

@app.route('/')
def home1():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
# 测试git pull
# vscode 本地修改

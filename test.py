### 全てのオブジェクトはクラスのインスタンスである。
### クラスから作られるオブジェクトをインスタンスと呼ぶ。
### 本書の文脈では、オブジェクトと言った時はインスタンスのことを指す。

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)

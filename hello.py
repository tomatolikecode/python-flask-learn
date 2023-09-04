
from flask import Flask

print(__name__)

app = Flask(__name__)


# 修饰器 路由定义
@app.route('/')
def home():
    return 'It is Home'


@app.route('/hello')
def hello():
    return 'hello u'


def say():
    return "say hello"


# 函数添加路由
app.add_url_rule(rule='/say',  view_func=say)


if __name__ == '__main__':
    app.run()

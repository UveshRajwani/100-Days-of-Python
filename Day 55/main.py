# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# #
# # def make_bold(func):
# #     text = func
# #     text = f"<strong>text</strong>"
# #     return text
# #
# #
# # @app.route('/<name>')
# # def hello_world(name):
# #     return f'Hello, World ok! {name}'
# #
# #
# # @app.route('/bye')
# # @make_bold
# # def bye():
# #     return 'Hello, World ok!'
# #
# # if __name__ == "__main__":
# #     app.run(debug=True)
# def logging_decorator(func):
#     def loger(*args):
#         print(f"You called {func.__name__}{args}")
#         result = func(args[0], args[1], args[2])
#         print(f"It returned: {result}")
#
#     return loger
#
#
# @logging_decorator
# def mul(n1, n2, n3):
#     return n1 * n2 * n3
#
#
# mul(2, 2, 2)

from flask import Flask
from random import randint
app = Flask(__name__)

num = randint(0,9)
@app.route('/<int:number>')
def hello_world(number):
    if number > num:
        return '<p><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="480" height="453" alt="" /></p>'
    if number < num:
        return '<p><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="" width="480" height="600" /><img'
    if number == num:
        return  '<p><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="347" height="364" alt="" /><img'

if __name__ == "__main__":
    app.run(debug=True)
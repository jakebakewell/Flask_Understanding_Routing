from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/Dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<word>')
def hello(word):
    print(word)
    return f"Hello {word}"

@app.route('/repeat/<int:number>/<word>')
def repeat_word(number, word):
    print(word)
    print(number)
    return f"{word }" * number

@app.route('/<thing>')
def only_defined_routes(thing):
    return "Sorry! No response. Try again."
if __name__ == "__main__":
    app.run(debug = True)
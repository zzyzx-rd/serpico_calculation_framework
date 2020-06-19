from flask import Flask

app = Flask(__name__)

# Tell what URL should trigger the function
@app.route('/')
def main():
    return 'hello world'

@app.route('/test')
@app.route('/test2')
def test():
    return 'test'


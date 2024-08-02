from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def eval_code():
    code = request.args.get('code')
    return str(eval(code))

if __name__ == '__main__':
    app.run()


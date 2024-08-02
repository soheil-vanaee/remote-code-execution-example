from flask import Flask, request

app = Flask(__name__)

@app.route('/exec')
def exec_code():
    code = request.args.get('code')
    exec(code)
    return "Code executed."

if __name__ == '__main__':
    app.run()


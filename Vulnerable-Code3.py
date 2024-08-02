from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/subprocess')
def run_subprocess():
    cmd = request.args.get('cmd')
    subprocess.call(cmd, shell=True)
    return "Command executed."

if __name__ == '__main__':
    app.run()


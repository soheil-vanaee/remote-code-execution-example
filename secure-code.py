from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/secure_subprocess')
def secure_subprocess():
    cmd = request.args.get('cmd')
    if cmd in ['ls', 'pwd']:  # Whitelist valid commands
        result = subprocess.run([cmd], capture_output=True, text=True)
        return result.stdout
    else:
        return "Command not allowed."

if __name__ == '__main__':
    app.run()


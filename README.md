### Example 1: Basic RCE via `eval()`

**Vulnerable Code:**
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def eval_code():
    code = request.args.get('code')
    return str(eval(code))

if __name__ == '__main__':
    app.run()
```

**Exploitation:**
An attacker could pass malicious code through the `code` parameter:
```
http://example.com/eval?code=__import__('os').system('ls')
```
This would execute the `ls` command on the server, listing directory contents.

### Example 2: Using `exec()` Function

**Vulnerable Code:**
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/exec')
def exec_code():
    code = request.args.get('code')
    exec(code)
    return "Code executed."

if __name__ == '__main__':
    app.run()
```

**Exploitation:**
An attacker could pass code to delete files or perform other malicious actions:
```
http://example.com/exec?code=__import__('os').system('rm -rf /')
```
This would delete all files on the server.

### Example 3: Using `subprocess` Module

**Vulnerable Code:**
```python
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
```

**Exploitation:**
An attacker could execute arbitrary shell commands:
```
http://example.com/subprocess?cmd=ls
```
This would list the directory contents.

### How to Prevent RCE

1. **Avoid `eval()` and `exec()` for Untrusted Input:**
   ```python
   # Do not use eval() or exec() with user input
   ```

2. **Use Safe Methods for Executing Shell Commands:**
   Use the `subprocess` module without `shell=True` and pass arguments as a list.
   ```python
   from flask import Flask, request
   import subprocess

   app = Flask(__name__)

   @app.route('/safe_subprocess')
   def run_safe_subprocess():
       cmd = request.args.get('cmd')
       # Use a whitelist of allowed commands
       if cmd in ['ls', 'pwd']:
           result = subprocess.run([cmd], capture_output=True, text=True)
           return result.stdout
       else:
           return "Command not allowed."

   if __name__ == '__main__':
       app.run()
   ```

3. **Sanitize User Input:**
   Ensure that any user input is properly sanitized and validated before use.

4. **Use Parameterized Functions:**
   Use functions that accept parameters and avoid constructing shell commands by concatenating strings.

### Secure Example:

**Secure Code Using Parameterized Subprocess:**
```python
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
```

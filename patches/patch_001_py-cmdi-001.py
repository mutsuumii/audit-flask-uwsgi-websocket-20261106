# Command injection via shell=True
# CWE-78 | Severity: CRITICAL
# File: flask_uwsgi_websocket/_uwsgi.py line 51

**Risk:** User input passed to a shell command. Attacker can execute arbitrary OS commands.

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.

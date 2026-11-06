# Security audit: zeekay/flask-uwsgi-websocket

Date: 2026-11-06 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 1 issue(s): 1 critical.

## Findings

### 1. [CRITICAL] Command injection via shell=True

**CWE-78** | `flask_uwsgi_websocket/_uwsgi.py` line 51

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
sys.exit(os.system(cmd))
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

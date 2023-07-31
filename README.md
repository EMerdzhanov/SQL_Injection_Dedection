# SQL Injection Detection Script
This script automates sending malicious payloads to test web applications for SQL injection vulnerabilities.

### Description
The script sends a list of SQL payloads in web requests and checks the application's responses for error messages indicating potential injection flaws. This allows efficiently scanning sites for security weaknesses related to improper input sanitization.

Payloads are inserted into a login POST request to exercise common insecure code patterns. Error messages are fingerprinted by searching response content.

This demonstrates automated web security testing methods using Python.

### Usage
The script can be run with:

```python
sql_injection_scanner.py
```

By default it will target the example.com URL defined in the code.

To specify a different target, edit the url variable at the top of the file:

```
url = 'http://your-target.com/login'
```

Add or modify the list of sql_payloads to test different inputs.

### Requirements
* Python 3
* requests module

### Disclaimer
This tool is for educational purposes only. Do not use against sites you do not have permission to test.

### Author
Emil T Merdzhanov
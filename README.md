# XSS-Checker
XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities.

![image](https://user-images.githubusercontent.com/57470560/175960150-5da9a5da-9ccb-40cc-8b78-a3643a6a6a7c.png)

```
usage: XSS-Checker.py [-h] --url URL [--ext-url EXTRA_URL] [--threads THREADS] [--timeout TIMEOUT]
                      [--browser {Chrome,Chromium,Brave,Firefox,Edge}] [--proxy PROXY] [--sig SIG] [--silent]

XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities.

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Target URL to validate / check for XSS vulnerability
  --ext-url EXTRA_URL   Append EXTRA_URL to URL (URL = URL + EXTRA_URL)
  --threads THREADS     Number of concurrent threads (default: 5)
  --timeout TIMEOUT     Time to wait for the page to finish loading in seconds (default: 15)
  --browser {Chrome,Chromium,Brave,Firefox,Edge}
                        Browser used to validate / check for XSS vulnerability (default: Chrome)
  --proxy PROXY         Proxy URL (eg http://127.0.0.1:8080)
  --sig SIG             The message content of the pop-up box is used (default: XSS-Checker)
  --silent              Display only "Vulnerable" results in the output
  ```
  


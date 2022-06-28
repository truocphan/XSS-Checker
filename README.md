# XSS-Checker
XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities

![image](https://user-images.githubusercontent.com/57470560/176279707-7cdb56ae-0316-42d3-8693-e2b9ffbb0b1f.png)


```
usage: XSS-Checker [-h] --url URL [--ext-url EXTRA_URL] [--threads THREADS] [--timeout TIMEOUT]
                   [--browser {Chrome,Chromium,Brave,Firefox,Edge}] [--driver DRIVER] [--proxy PROXY] [--sig SIG]
                   [--silent]

XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Target URL to validate / check for XSS vulnerability
  --ext-url EXTRA_URL   Append EXTRA_URL to URL (URL = URL + EXTRA_URL)
  --threads THREADS     Number of concurrent threads (default: 5)
  --timeout TIMEOUT     Time to wait for the page to finish loading in seconds (default: 15)
  --browser {Chrome,Chromium,Brave,Firefox,Edge}
                        Browser used to validate / check for XSS vulnerability (default: Chrome)
  --driver DRIVER       Location of Browser Driver (chromedriver, geckodriver, msedgedriver) path
  --proxy PROXY         Proxy URL (eg 127.0.0.1:8080)
  --sig SIG             The message content of the pop-up box is used (default: XSS-Checker)
  --silent              Display only "Vulnerable" results in the output
```

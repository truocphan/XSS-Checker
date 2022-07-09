XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities

![image](https://user-images.githubusercontent.com/57470560/176995033-5d635a52-2c41-4b72-a26d-7d51c3dd6028.png)

## Installation
```console
pip install XSS-Checker
```

## Usage
```console
XSS-Checker -h
```

```
usage: XSS-Checker [-h] --url URL [--endpoint ENDPOINT] [--ext-url EXTRA_URL] [--cookies COOKIES]
                   [--sig SIG] [--threads THREADS] [--timeout TIMEOUT]
                   [--browser {Chrome,Chromium,Brave,Firefox,Edge}] [--driver DRIVER] [--proxy PROXY]
                   [--writefile WRITEFILE] [--silent] [--update] [--version]

XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Target URL to validate / check for XSS vulnerability
  --endpoint ENDPOINT   Overwrite URL's endpoint to ENDPOINT (URL = {{RootURL}} + ENDPOINT)
  --ext-url EXTRA_URL   Append EXTRA_URL to URL (URL = URL + EXTRA_URL)
  --cookies COOKIES     Cookies data "CookieName1=CookieValue1; CookieName2=CookieValue2" (TO-DO)
  --sig SIG             The message content of the pop-up box is used (default: XSS-Checker)
  --threads THREADS     Number of concurrent threads (default: 5)
  --timeout TIMEOUT     Time to wait for the page to finish loading in seconds (default: 10)
  --browser {Chrome,Chromium,Brave,Firefox,Edge}
                        Browser used to validate / check for XSS vulnerability (default: Chrome)
  --driver DRIVER       Location of Browser Driver (chromedriver, geckodriver, msedgedriver) path
  --proxy PROXY         Proxy URL (eg 127.0.0.1:8080)
  --writefile WRITEFILE
                        Write scan results to specified file
  --silent              Display only "Vulnerable" results in the output
  --update              Update XSS-Checker to the latest version
  --version             Show version of XSS-Checker
```

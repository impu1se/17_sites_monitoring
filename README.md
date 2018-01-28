# Sites Monitoring Utility
This program check health your web site. Web site is healthy if he response on request status code [200](https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP#200) and his domain paid for 1 month in advance.
The program must have a file with a URL.
The file must include the name of the web addresses starting with **https://** or without it.
# Running program
First you clone project on your computer, after you should run script as `python check_sites_health.py` *file_with_urls* ( when *file_with_urls* is file with web address, example :     
- http://devman.org 
- https://www.youtube.com
- www.yandex.com
- etc...)    
For help run script with key **-h** or **--help**
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

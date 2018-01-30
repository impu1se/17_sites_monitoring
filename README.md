# Sites Monitoring Utility
This program check health your web site. Web site is healthy if he response on request status code [200](https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP#200) and his domain paid for 1 month in advance.
The program must have a file with a URL.
The file must include the name of the web addresses starting with **https://** and with **http**, or without. It depence on the protocol the web sites.
# Running program
It is program multiplatform and running all operation system when have python 3.4 or above.    
First you clone project on your computer, after you should run script as `python check_sites_health.py` *file_with_urls* ( when *file_with_urls* is file with web address, example :     
- http://devman.org 
- https://www.youtube.com
- http://www.yandex.com
- etc...)    

You will have kind of `Web site: http://youtube.ru, is answer 200: True, paid status: True`    
For help run script with key **-h** or **--help**
# Warning
If you don't input file with URL you will have message about it.

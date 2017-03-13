"""python2
import urllib2
print urllib2.urlopen("http://www.example.com").read()

# python -c "import urllib2; print urllib2.urlopen('http://www.example.com').read()"
"""

# python3
from urllib.request import urlopen
print(urlopen("http://www.example.com").read().decode('utf-8'))

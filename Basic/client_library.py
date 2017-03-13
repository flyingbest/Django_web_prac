
""" python2
from urlparse import urlparse
result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
print(result)
"""

"""# python3
from urllib.parse import urlparse
result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
print(result)
"""

""" python2 - GET 
from urllib2 import urlopen
f = urlopen("http://www.example.com")
print f.read(50)
"""

"""# python2 - POST (data parameter automatically request POST method)
from urllib2 import urlopen
data = "query=python"
f = urlopen("http://www.example.com", data)
print f.read(300)
"""

"""# python2
import urllib2
req = urllib2.Request("http://www.example.com")
req.add_header("Content-Type", "text/plain")
req.add_data("query=python")	# POST method
f = urllib2.urlopen(req)
print f.read(300)
"""

"""# python3
import urllib.request
f = urllib.request.urlopen("http://www.example.com")
print(f.read(300).decode('utf-8'))
"""



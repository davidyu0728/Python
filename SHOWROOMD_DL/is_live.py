import datetime
import time
import urllib
from urllib import request
import re
import os
url = "https://www.showroom-live.com/akb48_official"
with request.urlopen(url) as f:
    data = f.read()
    f.close

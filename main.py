import math
import os
import sys

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.google.com/")

print(r.status_code)
print(sys.executable)

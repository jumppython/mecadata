from scrapy.cmdline import execute
import sys, os

# reset the obj dir into env-var activity
# os.path.abspath(__file__) -- obtain the path of main.py
# os.path.dirname(os.path.abspath(__file__)) -- obtain the upper dir of dir where main.py exists
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','remercari'])


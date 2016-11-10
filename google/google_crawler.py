import json
import html5lib
from html5lib import treebuilders
from bs4 import BeautifulSoup
import requests
import urllib2
import time
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
from common.jobs import Job
from common.fetcher import Fetcher


class GoogleJobParser:

    @staticmethod
    def parse_job(url):
        f = Fetcher.fetch_page(url)
        soup = BeautifulSoup(f.content, 'html5lib')
        job = Job()
        job.title = GoogleJobParser.get_title(soup)
        job.category = GoogleJobParser.get_category(soup)
        job.description= GoogleJobParser.get_description(soup)
        job.requirements = GoogleJobParser.get_requirements(soup)
        job.responsibilities = GoogleJobParser.get_responsibilities(soup)
        job.preferred_requirements = GoogleJobParser.get_preferred_requirements(soup)
        job.company = GoogleJobParser.get_company(soup)
        job.posting_link = url
        print job
        return job

    @staticmethod
    def get_title(soup):
        return ''

    @staticmethod
    def get_company(soup):
        return "Google, Inc."

    @staticmethod
    def get_location(soup):
        return ''

    @staticmethod
    def get_category(soup):
        return ''

    @staticmethod
    def get_description(soup):
        return ''

    @staticmethod
    def get_requirements(soup):
        return ''

    @staticmethod
    def get_responsibilities(soup):
        return ''

    @staticmethod
    def get_preferred_requirements(soup):
        return ''

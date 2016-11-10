import json
import html5lib
from html5lib import treebuilders
from bs4 import BeautifulSoup
import requests
import urllib2
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
from common.jobs import Job

base_url = 'https://www.facebook.com/careers/university'
eng_jobs_url = 'https://www.facebook.com/careers/university/grads/engineering'
sample_job_url = 'https://www.facebook.com/careers/jobs/a0I1200000JZKUFEA5'

class FacebookCrawler:

    def __init__(self):
        self.jobs = {}

    def fetch_jobs(self):
        while True:
            f = requests.get(eng_jobs_url)
            if f.status_code < 500:
                break

        soup = BeautifulSoup(f, 'html5lib')


class FacebookJobParser:

    def __init__(self):
        print "FacebookJobParser::__init__"

    @staticmethod
    def parse_job(url):
        while True:
            f = requests.get(url)
            if f.status_code < 500:
                break

        soup = BeautifulSoup(f.content, 'html5lib')
        job = Job()

        title = soup.find("h2")
        job.title = title.string

        location = title.nextSibling
        job.location = location.string

        description = location.nextSibling
        job.description = description.string
        description = description.nextSibling
        job.description += "\n" + str(description.string)

        responsibilities = description.find_next('ul').find_all('li')
        for responsibility in responsibilities:
            job.responsibilities.append(str(responsibility.string))

        requirements = description.find_next('ul').find_next('ul').find_all('li')
        for requirement in requirements:
            job.requirements.append(str(requirement.string))
        job.company = "Facebook, Inc."

        print job



FacebookJobParser.parse_job(sample_job_url.encode('utf-8'))

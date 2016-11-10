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

base_url = 'https://www.facebook.com'
eng_jobs_url = 'https://www.facebook.com/careers/university/grads/engineering'
eng_internships_url = 'https://www.facebook.com/careers/university/internships/engineering'
sample_job_url = 'https://www.facebook.com/careers/jobs/a0I1200000JZKUFEA5'


class FacebookCrawler:

    def __init__(self):
        self.jobs = {}

    @staticmethod
    def fetch_jobs(url):
        while True:
            f = requests.get(url)
            if f.status_code < 500:
                break

        soup = BeautifulSoup(f.content, 'html5lib')
        job_urls = soup.find_all('a', href=re.compile("^/careers/jobs/"))
        for job_url in job_urls:
            url = base_url + job_url['href']
            print url
            FacebookJobParser.parse_job(url)


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

        category = soup.find('h3')
        job.category = category.string

        location = title.nextSibling
        job.location = location.stringf

        description = location.nextSibling
        job.description.append(description.string)
        description = description.nextSibling
        job.description.append(str(description.string))

        if soup.find('h4', text='Responsibilities'):
            responsibilities = soup.find('h4', text="Responsibilities").nextSibling.find_all('li')
            for responsibility in responsibilities:
                job.responsibilities.append(str(responsibility.string))

        if soup.find('h4', text="Minimum Qualification"):
            requirements = soup.find('h4', text="Minimum Qualification").nextSibling.find_all('li')
            for requirement in requirements:
                job.requirements.append(str(requirement.string))

        if soup.find('h4', text="Preferred Qualifications"):
            preferred_requirements = soup.find('h4', text="Preferred Qualifications").nextSibling.find_all('li')
            for prq in preferred_requirements:
                job.preferred_requirements.append(str(prq.string))

        job.company = "Facebook, Inc."

        print job

FacebookCrawler.fetch_jobs(eng_internships_url)
# FacebookJobParser.parse_job(sample_job_url)
# FacebookJobParser.parse_job('https://www.facebook.com/careers/jobs/a0I1200000JXbY9EAL/')

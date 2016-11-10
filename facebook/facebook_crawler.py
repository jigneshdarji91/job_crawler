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


base_url = 'https://www.facebook.com'
sample_job_url = 'https://www.facebook.com/careers/jobs/a0I1200000JZKUFEA5'
curr_dir = os.path.abspath(os.path.join(__file__, os.pardir))
url_file = str(curr_dir) + '/urls.txt'


class FacebookCrawler:

    @staticmethod
    def fetch_jobs_all():
        f = open(url_file, 'r')
        urls = f.readlines()
        jobs = []
        for line in urls:
            fetched_jobs = FacebookCrawler.fetch_jobs_from_page(str(line.rstrip('\n')))
            for j in fetched_jobs:
                jobs.append(j)

        for job in jobs:
            print job

    @staticmethod
    def fetch_jobs_from_page(url):
        print "fetch jobs from ", url
        f = Fetcher.fetch_page(url)
        print "web page loaded successfully"
        soup = BeautifulSoup(f.content, 'html5lib')
        job_urls = soup.find_all('a', href=re.compile("^/careers/jobs/"))
        jobs = []
        for job_url in job_urls:
            url = base_url + job_url['href']
            jobs.append(FacebookJobParser.parse_job(url))

        return jobs


class FacebookJobParser:

    @staticmethod
    def parse_job(url):
        f = Fetcher.fetch_page(url)
        soup = BeautifulSoup(f.content, 'html5lib')

        job = Job()
        job.title                   = FacebookJobParser.get_title(soup)
        job.category                = FacebookJobParser.get_category(soup)
        job.description             = FacebookJobParser.get_description(soup)
        job.requirements            = FacebookJobParser.get_requirements(soup)
        job.responsibilities        = FacebookJobParser.get_responsibilities(soup)
        job.preferred_requirements  = FacebookJobParser.get_preferred_requirements(soup)
        job.company                 = FacebookJobParser.get_company(soup)
        job.posting_link            = url

        print job
        return job

    @staticmethod
    def get_title(soup):
        return soup.find("h2").string

    @staticmethod
    def get_company(soup):
        return "Facebook, Inc."

    @staticmethod
    def get_location(soup):
        title = soup.find('h2')
        return title.nextSibling.string

    @staticmethod
    def get_category(soup):
        return soup.find('h3')

    @staticmethod
    def get_description(soup):
        desc = []
        title = soup.find('h2')
        location = title.nextSibling
        description = location.nextSibling
        if description:
            desc.append(description.string)
            description = description.nextSibling
            if description:
                desc.append(description.string)
        return desc

    @staticmethod
    def get_requirements(soup):
        rq = []
        if soup.find('h4', text="Minimum Qualification"):
            requirements = soup.find('h4', text="Minimum Qualification")\
                .nextSibling.find_all('li')
            for requirement in requirements:
                rq.append(requirement.string)

        return rq

    @staticmethod
    def get_responsibilities(soup):
        r = []
        if soup.find('h4', text='Responsibilities'):
            responsibilities = soup.find('h4', text="Responsibilities")\
                .nextSibling.find_all('li')
            for responsibility in responsibilities:
                r.append(responsibility.string)

        return r

    @staticmethod
    def get_preferred_requirements(soup):
        prq = []
        if soup.find('h4', text="Preferred Qualifications"):
            pref_requirements = soup.find('h4', text="Preferred Qualifications")\
                .nextSibling.find_all('li')
            for prq in pref_requirements:
                prq.append(prq.string)

        return prq



FacebookCrawler.fetch_jobs_all()

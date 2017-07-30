import requests
import urllib
from bs4 import BeautifulSoup

from constants import *
import json


class Course(object):

    @staticmethod
    def getChapterList(courseNo):
        list = []
        try:
            page = urllib.urlopen(COURSE_PAGE_URL + str(courseNo + "/"))
            soup = BeautifulSoup(page, "html.parser")
            soup = BeautifulSoup(str(soup.find("div", id="div_lm")), "html.parser")
            list = soup.findAll('a', {"onclick": True})
            list = [a.getText() for a in list]
        except Exception, e:
            print e
        return list

    @staticmethod
    def searchCourse(searchTxt):
        list = []
        try:
            response = requests.post(SEARCH_COURSE_URL, data={"searchterm": str(searchTxt)})
            jsonResp = json.loads(response.content)
            list = [course["subjectName"] for course in jsonResp["subject"]]
        except Exception, e:
            print e
        return list

    @staticmethod
    def getCourseDetails(searchTxt):
        list = []
        try:
            response = requests.post(COURSE_DETAILS_URL, data={"name": str(searchTxt)})
            jsonResp = json.loads(response.content)
            list = [course["subjectName"] for course in jsonResp["subject"]]
        except Exception, e:
            print e
        return list


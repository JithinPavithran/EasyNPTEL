import json
import requests
import urllib
from bs4 import BeautifulSoup

from constants import *


class Course(object):
    def __init__(self):
        self.courseNo = -1
        self.courseName = ""
        self.chapterList = []

    def getChapterList(self, course_no):
        self.courseNo = course_no
        try:
            print "Sending request..."
            page = urllib.urlopen(COURSE_PAGE_URL + "/" + str(course_no))
            print "Got response"
            soup = BeautifulSoup(page, "html.parser")
            print "parsing HTML page for chapters and course name"
            self.chapterList = BeautifulSoup(
                str(soup.find("div", id="div_lm")), "html.parser"
            ).findAll('a', {"onclick": True})

            self.courseName = BeautifulSoup(
                str(soup.find("ul", id="breadcrumbs-course")),
                "html.parser").findAll('li')[2].text

        except Exception, e:
            print e

        return [a.getText() for a in self.chapterList]

    def getMp4UrlMirror1(self, index):
        lec_url = NPTEL_URL + self.chapterList[index]["onclick"][15:-1]
        lec_page = urllib.urlopen(lec_url)
        lec = BeautifulSoup(lec_page, "html.parser")
        lec = BeautifulSoup(str(lec.find("div", id="download")),
                            "html.parser")
        mirror = lec.find('a', {"onclick": True})
        return mirror['href']

    def getFileName(self, index, extension):
        return (str(index).zfill(2) + "-"
            + str(self.getChapterName(index)) + "." + extension)

    def getChapterName(self, index):
        return self.chapterList[index].getText() \
            if len(self.chapterList[index].getText()) < FILE_NAME_LENGTH \
            else self.chapterList[index].getText()[:FILE_NAME_LENGTH]

    def getCourseName(self):
        return self.courseName \
            if len(self.courseName) < COURSE_NAME_LENGTH \
            else self.courseName[:COURSE_NAME_LENGTH] + "..."

    @staticmethod
    def searchCourse(search_term):
        """Search for all courses with search_term in its Name."""
        course_list = []
        try:
            response = requests.post(
                SEARCH_COURSE_URL, data={"searchterm": str(search_term)})
            json_resp = json.loads(response.content)
            course_list = [course["subjectName"] for course in json_resp["subject"]]
        except Exception, e:
            print e
        return course_list

    @staticmethod
    def getCourseDetails(course_name):
        """Get details of all courses with course_name in its name."""
        course_list = []
        try:
            response = requests.post(COURSE_DETAILS_URL, data={"name": str(course_name)})
            json_resp = json.loads(response.content)
            course_list = [course["subjectName"] for course in json_resp["subject"]]
        except Exception, e:
            print e
        return course_list

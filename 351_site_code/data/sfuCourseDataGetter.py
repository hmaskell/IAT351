import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

r = requests.get('http://www.sfu.ca/bin/wcm/course-outlines?2019/spring/iat/')
data = r.json()

r2 = requests.get('http://www.sfu.ca/bin/wcm/course-outlines?2019/spring/iat/{0}/{1}'.format('438','e100'))
otherSectionInfo = r2.json()

#literally just for 438 because they don't have a d100 section >:(

number = otherSectionInfo['info']['number']
title = otherSectionInfo['info']['title']
courseDetails = otherSectionInfo['info']['description']
prerequisites = otherSectionInfo['info']['prerequisites']
units = otherSectionInfo['info']['units']
name = otherSectionInfo['instructor'][0]['name']
email = otherSectionInfo['instructor'][0]['email']
startTime = otherSectionInfo['courseSchedule'][0]['startTime']
days = otherSectionInfo['courseSchedule'][0]['days']
endTime = otherSectionInfo['courseSchedule'][0]['endTime']
campus = otherSectionInfo['courseSchedule'][0]['campus']
grades = otherSectionInfo['grades']

courseData = {
    number:{
        'title':title,
        'courseDetails':courseDetails,
        'prerequisites':prerequisites,
        'units':units,
        'name':name,
        'email':email,
        'startTime':startTime,
        'days':days,
        'endTime':endTime,
        'campus':campus,
        'grades':grades
    }
}


for course in data:
   # pp.pprint(course['text'])
    #pp.pprint(course['text'])
    r = requests.get('http://www.sfu.ca/bin/wcm/course-outlines?2019/spring/iat/{0}/{1}'.format(course['text'],'d100'))
    #pp.pprint(r.json())
    sectionInfo = r.json()
    #pp.pprint(sectionInfo)
    #pp.pprint(sectionInfo.keys())

    if "info" in sectionInfo:
        courseDetails = sectionInfo['info']['description']
        title = sectionInfo['info']['title']
        prerequisites = sectionInfo['info']['prerequisites']
        number = sectionInfo['info']['number']
        units = sectionInfo['info']['units'] 

    if "instructor" in sectionInfo:
        name = sectionInfo['instructor'][0]['name']
        email = sectionInfo['instructor'][0]['email']

    if "startTime" in sectionInfo:
        startTime = sectionInfo['courseSchedule'][0]['startTime']
        days = sectionInfo['courseSchedule'][0]['days']
        endTime = sectionInfo['courseSchedule'][0]['endTime']
        campus = sectionInfo['courseSchedule'][0]['campus']

    if "grades" in sectionInfo:
        grades = sectionInfo['grades']
        for element in grades:
            gradeWeight = element['weight']
            gradeDescription = element['description']

    courseData[number] = {
        'title':title,
        'courseDetails':courseDetails,
        'prerequisites':prerequisites,
        'units':units,
        'name':name,
        'email':email,
        'startTime':startTime,
        'days':days,
        'endTime':endTime,
        'campus':campus,
        'grades':grades
    }

pp.pprint(courseData)
'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
    
    #6a. title(self,phrase) -- filters courses containing the phrase in their title 
    #Completed by James Kong on 2/13/2022
    def title(self,phrase):
        return Schedule([c for c in self.courses if phrase in c['name']])

    #6b. description(self,phrase) - filters courses containing the phrase in the description 
    #Completed by James Kong on 2/13/2022
    def description(self,phrase):
        return Schedule([c for c in self.courses if phrase in c['description']])

    #6c. Create your own filter method (e.g. by class day or time?)
    #Completed by James Kong on 2/13/2022
    def courseNum(self,num):
        return Schedule([c for c in self.courses if num == c['coursenum']])

    #6c. Create your own filter method (e.g. by class day or time?)
    #Completed by Jeremy Bernstein on 2/17/2022
    def courseTimes(self,times):
        return Schedule([c for c in self.courses if times == c['coursetimes']])

    #Extra method used for 7e
    #Completed by James Kong on 2/17/2022
    def sectionNum(self, num):
        return Schedule([c for c in self.courses if num == c['section']])
        
    #6c. Create your own filter method (e.g. by class day or time?)
    #Completed by Hiro Chen on 2/17/2022/11:22PM
    def statusText(self,status):
        return Schedule([c for c in self.courses if c['status_text'] in status])

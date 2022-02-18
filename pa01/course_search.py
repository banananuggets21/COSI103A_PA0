'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
code (filter by a course number/code)
section (filter by a section number)
time (filter by time)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        #7a. course  -- filter by subject/coursenumber
        #Completed by James Kong on 2/13/2022
        elif command in ['c', 'course']:
            courseNum = input("enter a course number:")
            schedule = schedule.courseNum(courseNum)
        #7b. instructor -- filter by instructor email or lastname
        #Completed by Jeremy Bernstein on 2/16/2022
        elif command in ['i', 'instructor']:
            instructor = input("enter a instructor email/lastname:")
            schedule = schedule.courseNum(instructor) 
        #7c. title -- filter by phrase in the title
        #Completed by James Kong on 2/13/2022
        elif command in ['t', 'title']:
            title = input("enter a course title:")
            schedule = schedule.title(title)
        #7d. description -- filter by phrase in the description
        #Completed by Jeremy Bernstein on 2/17/2022
        elif command in ['d', 'description']:
            description = input("enter a course description:")
            schedule = schedule.title(description)
        #7e. Create your own filter (each team member creates their own)
        #Completed by Jeremy Bernstein on 2/16/2022
        elif command in ['c', 'code']:
            code = input("enter a course code:")
            schedule = schedule.courseNum(code)
        #7e. Create your own filter (each team member creates their own)
        #Completed by James Kong 2/17/2022
        elif command in ['sn', 'section']:
            sectionNum = input("Enter a section number")
            schedule = schedule.sectionNum(sectionNum)
        #7e. Create your own filter (each team member creates their own)
        #Completed by Hiro Chen on 2/17/2022
        elif command in ['t', 'time']:
            time = input("enter a course time")
            schedule = schedule.courseNum(time)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()


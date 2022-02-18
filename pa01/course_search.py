'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
from schedule import Schedule

SCHEDULE = Schedule()
SCHEDULE.load_courses()
SCHEDULE = SCHEDULE.enrolled(range(5, 1000)) # eliminate courses with no students

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
status (filter by status)
'''

TERMS = {c['term'] for c in SCHEDULE.courses}

def topmenu():
    ''' topmenu is the top level loop of the course search app '''
    global SCHEDULE
    while True:         
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r', 'reset']:
            SCHEDULE.load_courses()
            SCHEDULE = SCHEDULE.enrolled(range(5, 1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(TERMS)+":")
            SCHEDULE = SCHEDULE.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            SCHEDULE = SCHEDULE.subject([subject])
        #7a. course  -- filter by subject/coursenumber
        #Completed by James Kong on 2/13/2022
        elif command in ['c', 'course']:
            course_num = input("enter a course number:")
            SCHEDULE = SCHEDULE.course_num(course_num)
        #7b. instructor -- filter by instructor email or lastname
        #Completed by Jeremy Bernstein on 2/16/2022
        elif command in ['i', 'instructor']:
            instructor = input("enter a instructor email/lastname:")
            SCHEDULE = SCHEDULE.course_num(instructor) #note for Jeremy, incorrect method
        #7c. title -- filter by phrase in the title
        #Completed by James Kong on 2/13/2022
        elif command in ['t', 'title']:
            title = input("enter a course title:")
            SCHEDULE = SCHEDULE.title(title)
        #7d. description -- filter by phrase in the description
        #Completed by Jeremy Bernstein on 2/17/2022
        elif command in ['d', 'description']:
            description = input("enter a course description:")
            SCHEDULE = SCHEDULE.title(description)
        #7e. Create your own filter (each team member creates their own)
        #Completed by Jeremy Bernstein on 2/16/2022
        elif command in ['c', 'code']:
            code = input("enter a course code:")
            SCHEDULE = SCHEDULE.course_num(code)
        #7e. Create your own filter (each team member creates their own)
        #Completed by James Kong 2/17/2022
        elif command in ['sn', 'section']:
            section_num = input("Enter a section number:")
            SCHEDULE = SCHEDULE.section_num(section_num)
        #7e. Create your own filter (each team member creates their own)
        #Completed by Hiro Chen on 2/17/2022
        elif command in ['st', 'status_text']:
            status = input("enter a course status")
            schedule = schedule.statusText(status)
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(SCHEDULE.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in SCHEDULE.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    ''' print_course prints a brief description of the course '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])

if __name__ == '__main__':
    topmenu()

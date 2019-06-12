# its better to add some courses as admin first ,choose admin first then run the code again and choose type as teacher or student   please...
teacher_classes = []
teacher_resume = []
# LOGIN
def login():
    class User():
        def __init__(self, first_name, last_name, type, age):
            self.first_name = first_name.title()
            self.last_name = last_name.title()
            self.type = type.title()
            self.age = age

        def describe_user(self):
            print("-----")
            print("First Name" + " : " + self.first_name)
            print("Last Name" + " : " + self.last_name)
            print("Enter Type between admin , student or teacher:" + " : " + self.type)
            print("Age" + " : " + self.age)
            print('you are registered or log inned successfully')

    def ask_user(message=''):
        user_input = ''
        while not user_input:
            user_input = input(message)
        return user_input

    def form_complete(values, placement, length):
        placement = []
        while len(placement) < length:
            first_name = ask_user("Enter First Name: ")
            last_name =  ask_user("Enter Last Name: ")
            type = ask_user("Enter Type between admin , student or teacher: ")
            age = ask_user("Enter Age: ")
            values = User(first_name, last_name, type, age)
            placement.append(values)
        return placement

    if __name__ == '__main__':

        users = form_complete('user', 'users', 1)
        for a in range(len(users)):
            users[a].describe_user()    
# def executeReplacement2():
#         print('List of your classes is empty as a teacher:(')
#         option = str(input('You want add some class in the list of your classes as a teacher (yes/no)? : '))
#         if option == 'yes':
#             print('look at the courses please')
#             fi = open('Courses.txt' , 'r')
#             print (fi.read())

#             num = int(input('How many classes do you want to add as a teacher: '))
#             for i in range(1, num+1):
#                 print('Enter the', i, 'course name: ')
#                 n = str(input())
#                 teacher_classes.append(n)

#                 fo = open('Teacher.txt' , 'w')
#                 fo.write(str(teacher_classes))
#                 fo.close() 
            
#         else:
#             print('Thank you for using this school managment services !!')
#         print('\n', teacher_classes)

#admin and using singletone
def admin() :
    fo = open('Courses.txt' , 'w')
    coursename = []
    print('List of courses is empty :(')
    option = str(input('You want add the course in the list of courses (yes/no)? : '))
    if option == 'yes':
        num = int(input('How many courses do you want to add (enter number): '))
        for i in range(1, num+1):
            print('Enter the', i, 'course name: ')
            n = str(input())
            coursename.append(n)
    else:
        print('Thank you for using this school managment services !!')
    print('\n', coursename)




    class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

    class CreateCourse(metaclass=Singleton):
        fo.write(str(coursename))
        fo.close() 
        pass


    def Done(coursename):
        m1 =  CreateCourse(coursename)
        m2 =  CreateCourse(coursename)
        assert m1 is m2


        Done(coursename) 

#  STUDENT and using strategy
def student():
    class StrategyExample:
        def __init__(self, func=None):
            if func:
                self.execute = func

            def execute(self):
                print("Original execution")
    student_classes = []
    def executeReplacement1():
            print('List of your classes is empty :(')
            option = str(input('You want add some class in the list of your classes (yes/no)? : '))
            if option == 'yes':
                print('look at the courses please')
                fi = open('Courses.txt' , 'r')
                print (fi.read())

                num = int(input('How many classes do you want to add (enter int number): '))
                for i in range(1, num+1):
                    print('Enter the', i, 'course name: ')
                    n = str(input())
                    student_classes.append(n)

                    fo = open('Student.txt' , 'w')
                    fo.write(str(student_classes))
                    fo.close() 
                
            else:
                print('Thank you for using this school managment services !!')
            print('\n', student_classes)



    # first Strategy
    favorite_classes = []
    def executeReplacement2():
            print('List of your favorite classes is empty  :(')
            option = str(input(' could you please add some favorite courses name   (yes/no)? : '))
            if option == 'yes':
                print('look at the courses that you choosed before please')
                fi = open('Student.txt' , 'r')
                print (fi.read())

                num = int(input('How many favorite classes do you want to add (enter int number): '))
                for i in range(1, num+1):
                    print('Enter the', i, 'course name: ')
                    n = str(input())
                    favorite_classes.append(n)

                    fo = open('favorite_Classes.txt' , 'w')
                    fo.write(str(favorite_classes))
                    fo.close() 
                
            else:
                print('Thank you for using this school managment services !!')
            print('\n', favorite_classes)



    # secondStrotegy
    if __name__ == "__main__":
        strat0 = StrategyExample()
        strat1 = StrategyExample(executeReplacement1)
        strat2 = StrategyExample(executeReplacement2)

        strat0.execute()
        strat1.execute()
        strat2.execute()     
# teacher and observer

teacher_classes = []
teacher_resume = []
def teacher() :
    class Choose_Class:

        def prepare(self): pass
        def ask(self): pass
        def done(self): pass

        def go(self):
            self.prepare()
            self.ask()
            self.done()

    class Teacher_Courses(Choose_Class):
    

        def prepare(self):
            print('List of your classes is empty as a teacher:(')
        print('look at the courses please')
        fi = open('Courses.txt' , 'r')
        print (fi.read())
    
        def ask(self):
            num = int(input('How many classes do you want to add as a teacher(enter int number): '))
            for i in range(1, num+1):
                print('Enter the', i, 'course name: ')
                n = str(input())
                teacher_classes.append(n)
        def done(self):
                    fo = open('Teacher.txt' , 'w')
                    fo.write(str(teacher_classes))
                    fo.close() 
                    print ('Keep going :)')
    


        
    class Teacher_resume(Choose_Class):
        def prepare(self):
            print('Please enter your resume')
            n = str(input())

        
        def ask(self):
            num = int(input('How many resume do you want to add as a teacher (enter int number): '))
            for i in range(1, num+1):
                print('Enter the', i, 'resume: ')
                n = str(input())
                teacher_resume.append(n)
    
        def done(self):
            fo = open('Teacher_resume.txt' , 'w')
            fo.write(str(teacher_resume))
            fo.close() 
            print ('Thank you :)')
    

    Teacher_Courses = Teacher_Courses()
    Teacher_Courses.go()
    print ('Thank you :)')

    Teacher_resume = Teacher_resume()
    Teacher_resume.go()

# SWITCH
login()
def switch_func(value, x):
    return {
        'admin': lambda x: admin(),
        'student': lambda x: student(),
        'teacher': lambda x: teacher()
    }.get(value)(x)

# take user input
print('its better to add some courses as admin first ,choose admin first then run the code again and choose type as teacher or student   please...')
inp = input('input your type (write : admin/student/teacher) : ')

print('finished', switch_func(inp, 2))

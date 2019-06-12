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
            num = int(input('How many classes do you want to add as a teacher: '))
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
        def comment(self):
            print('Please enter your resume')
            n = str(input())

        
        def ask(self):
            num = int(input('How many resume do you want to add as a teacher: '))
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

teacher()
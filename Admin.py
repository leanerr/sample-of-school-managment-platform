def admin() :
    fo = open('Courses.txt' , 'w')
    coursename = []
    print('List of courses is empty :(')
    option = str(input('You want add the course in the list of courses (yes/no)? : '))
    if option == 'yes':
        num = int(input('How many courses do you want to add: '))
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







    


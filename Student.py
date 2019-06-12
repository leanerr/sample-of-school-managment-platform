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

                num = int(input('How many classes do you want to add: '))
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

                num = int(input('How many favorite classes do you want to add: '))
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
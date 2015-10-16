class Grades(object):
    ''' A mapping from students to a list of grades '''
    def __init__(self):
        ''' Create empty grade book '''
        self.students = [] #list of Stend objects
        self.grades = {} #maps idNum -> list of grades
        self.isSorted = True #true if self.students is sorted.
        
    def addStudent(self, student):
        '''
        Assumes: student is of type Student
        Add student to the grade book
        '''
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(Student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        ''' 
        Assumes: grade is a float
        Add grade to the list of grades for student
        '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise KeyError('Student not in grade book')
    
    def getGrades(self, student):
        ''' Return a list of grades for student '''
        try: #return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise KeyError('Student not in grade book')
            
    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        #return copy of list of students

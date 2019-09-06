class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.roster = {}

    def add_student(self, student_name, student_grade):
        #self.student_name = student_name
        #self.student_grade = student_grade
        #class_dict = self.roster
        
        if student_grade in self.roster.keys():
            self.roster[student_grade].append(student_name)
        else:
            self.roster.update({student_grade:[student_name]})
            
    def grade(self, num):
        if num in self.roster:
            return self.roster[num]
        else:
            return None
    
    def sort_roster(self):
        for grade in self.roster:
            self.roster[grade] = sorted(self.roster[grade])
        return self.roster
                
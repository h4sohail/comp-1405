class Student():
    def __init__(self):
        self.id = None
        self.fname = None
        self.lname = None
        self.age = None
        self.classes = {1405:'F',1001:'A+'}

    def set_id(self):
        self.id = int(input('What is the ID: '))
    def get_id(self):
        return self.id
    
    def set_fname(self):
        self.fname = (input('What is the fname: '))
    def get_fname(self):
        return self.fname
    
    def set_lname(self):
        self.lname = (input('What is the lname: '))
    def get_lname(self):
        return self.lname
    
    def set_age(self):
        self.age = (input('What is the age: '))
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.fname, self.lname

musa = Student()
musa.set_id()
musa.set_fname()
musa.set_lname()
musa.set_age()
print(musa.get_name())
print(musa.get_id())
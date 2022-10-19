

class Person:
    def __init__(self,id,surname,middlesurname,name,i_middlename,sex,age,hours,minutes,seconds):
        self.id = id
        self.surname = surname
        self.middlesurname = middlesurname
        self.name = name
        self.i_middlename = i_middlename
        self.sex = sex
        self.age = age
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Getters
    def get_id(self):
        return self.id

    def get_surname(self):
        return self.surname
        
    def get_middlesurname(self):
        return self.middlesurname

    def get_name(self):
        return f'{self.name} {self.surname}'

    def get_i_middlename(self):
        return self.i_middlename

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def return_list(self):
        return [self.id,self.surname,self.middlesurname,self.name,self.i_middlename,self.sex,self.age,self.hours,self.minutes,self.seconds]

    def get_time(self):
        return self.hours*3600 + self.minutes*60 + self.seconds








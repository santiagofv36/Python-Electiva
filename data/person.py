

class Person:
    def __init__(self,id,surname,middlesurname,name,i_middlename,sex,age,time):
        self.id = id
        self.surname = surname
        self.middlesurname = middlesurname
        self.name = name
        self.i_middlename = i_middlename
        self.sex = sex
        self.age = age
        self.time = time

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
        return [self.id,self.surname,self.middlesurname,self.name,self.i_middlename,self.sex,self.age,'{:02d}:{:02d}:{:02d}'.format(self.time.hour,self.time.minute,self.time.second)]

    def get_time(self):
        return self.time
        # return self.time.hour*3600 + self.time.minute*60 + self.time.second








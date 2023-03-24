#Create regular class taking 8 params on init :
# name, last_name, phone_number, address, email, birthday, age, sex
# Override a printable string representation of Profile class and return:
# list of the params mentioned above
class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
    def out(self):
        data = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]
        return data
    #def __str__(self):
        #return f"[{self.name}, {self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}, {self.sex}]"

profile1 = Profile("Anna", "Bytsenko", "+380 63 623 18 44", "c. Sumy, **** Str.", "anna.nvvs125@gmail.com", "2005-06-24", 17, "Female")


print(profile1.out())

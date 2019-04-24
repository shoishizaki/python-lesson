class Employee(object):
    def __init__(self, name, phone_number, home_number, adress):
        self.name = name
        self.phone_number = phone_number
        self.home_number = home_number
        self.adress = adress

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_home_number(self):
        return self.home_number

    def set_home_number(self, home_number):
        self.home_number = home_number

    def get_adress(self):
        return self.adress

    def set_adress(self, adress):
        self.adress = adress

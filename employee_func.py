import employee

emp_list = None
if emp_list is None:
    emp_list = []

class Employee_func(object):
    def __init__(self):
        pass

    def show_emp(self):
        if emp_list == []:
            print('None')
        else:
            print('----------------------------')
            print('name:', emp_list[0])
            print('phone-number:', emp_list[1])
            print('home-number:',emp_list[2])
            print('adress:', emp_list[3])
            print('----------------------------')

    def add_emp(self):
        name = input('name: ')
        phone_number = input('phone-number: ')
        home_number = input('home-number: ')
        adress = input('adress: ')
        emp_list.append(name)
        emp_list.append(phone_number)
        emp_list.append(home_number)
        emp_list.append(adress)

    def del_emp(self):
        global emp_list
        del emp_list
        emp_list = []

    def update_emp(self):
        while True:
            if emp_list == []:
                print('No data')
                break
            print('***************')
            print('update-command')
            print('1.name')
            print('2.phone-number')
            print('3.home-number')
            print('4.adress')
            print('5.finish')
            print('***************')
            update_element = input('choose-number: ')
            if update_element == '1':
                update_name = input('name: ')
                emp_list[0] = update_name
            elif update_element == '2':
                update_phone_number = input('phone-number: ')
                emp_list[1] = update_phone_number
            elif update_element == '3':
                update_home_number = input('home-number: ')
                emp_list[2] = update_home_number
            elif update_element == '4':
                update_adress = input('adress: ')
                emp_list[3] = update_adress
            elif update_element == '5':
                print('Thank you.')
                break
            else:
                print('This number is not define ')




import random
from time import sleep

"""
Program to manage a parking garage with limited spacing and variable prices depending on 
day and length of stay. Offers handicapped parking spaces.
"""


class Garage():
    def __init__(self):
        self.dis_total = random.randrange(5,31)
        self.gen_total = random.randrange(self.dis_total,101)
        self.dis_taken = random.randrange(self.dis_total)
        self.gen_taken = random.randrange(self.gen_total)
        self.dis_available = self.dis_total - self.dis_taken
        self.gen_available = self.gen_total - self.gen_taken
        
        
        

    def dispense_ticket(self):
        weekend = ['sat', 'sun']
        valid_time = ["f", "h"]
        valid_day = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
        valid_yn = ["y", "n"]


        print("Thank you for choosing Coding Temple Garage.")
        while True:
            day = input('Please enter today\'s day. Enter (mon/tues/wed/thurs/fri/sat/sun): ').strip().lower()
            time = input('Will you need a half day or full day? Please enter (h/f): ').strip().lower()

            if time in valid_time and day in valid_day:
                break
            else: 
                print("Please enter valid answers.")
        
        if day in weekend and time == 'f':
            price = '$20'             
        elif day in weekend and time == 'h':
            price = '$10'              
        elif day not in weekend and time == 'f':
            price = '$10'         
        else:
            price = '$5'
                    

        while True:
            dis = input('Do you require disabled parking? Please enter (y/n): ').strip().lower()
            if dis in valid_yn:
                break
            else: 
                print("Please enter a valid answer.")

        if dis == 'y':
            self.dis_space()
            self.id_number = self.dis_ticket_id()
        else:
            self.general_space()
            self.id_number = self.gen_ticket_id()

        print(f'The price for today will be {price} and your ticket number is {self.id_number}.')

        if dis == 'y':
            print(f"{self.dis_available} spaces remain.")
        else:
            print(f"{self.gen_available} spaces remain.")

        print("Please park in your assigned space!")
        print('Make sure you leave on time or else we\'ll tow you!')
        
    def dis_ticket_id(self):
        self.id_number = random.randrange((self.dis_total))
        return self.id_number

    def gen_ticket_id(self):
        self.id_number = random.randrange((self.gen_total))
        return self.id_number
    

    def checkout(self):
        check_id = 0
        while check_id != self.id_number:
            check_id = int(input("Thank you for visiting Coding Temple Garage, please input your ticket number. "))
            print("Please wait while we validate your ticket")
            sleep(1)
            print("...")
            sleep(1)
            if check_id == self.id_number:

                print("You have been checked out. Have a lovely timezone!")
                break
            else: 
                print("Please enter a valid id.")   

    def dis_space(self):
        if self.dis_available > 0:
            print(f'Great, we have {self.dis_available} spaces left.')
            self.dis_available -= 1
        else:
            print('Unfortunately, we don\'t have any more handicap spaces available.')  

    def general_space(self):
        if self.gen_available > 0:
            print(f'Great, we have {self.gen_available} spaces left.')
            self.gen_available -= 1
        else:
            print('Unfortunately, we don\'t have any more spaces available.')


class Main:

    def show_desc():
        print("""
            Welcome to Coding Temple Garage! We offer parking 24 hours a day, 7 days a week for either half or full day, whatever best meets your needs. Handicapped parking available. Prices may vary based on date and availability. 
        """)
    
    def run():

        Main.show_desc()
        my_ticket = Garage()

        while True:
            answer = input("Happy timezone, would you like to park your car here today? Please enter (y/n): ").strip().lower()

            if answer == "y":
                my_ticket.dispense_ticket()
                sleep(1)
                print("...")
                sleep(1)
                my_ticket.checkout()
                break
            if answer == "n":
                print("Have a lovely timezone!")
                break
            else:
                print("Please enter a valid answer.")


Main.run()


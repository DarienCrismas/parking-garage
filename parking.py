class Garage():
    def __init__(self):
        self.gen_total = None
        self.dis_total = None
        self.gen_taken = None
        self.dis_taken = None
        

    def dispense_ticket(self):
        weekend = ['sat', 'sun']
        day = input('Enter today\'s day(Ex: for Monday enter Mon): ').strip().lower()
        time = input('Will you need a half day or full day? (h/f)').strip().lower()
        if day in weekend and time == 'f':
            price = '$20'
        elif day in weekend and time == 'h':
            price = '$10'
        elif day not in weekend and time == 'f':
            price = '$10'
        else:
            price = '$5'
        dis = input('Do you require disabled parking? (y/n): ').strip().lower()
        if dis == 'y':
            self.dis_space()
        else:
            self.general_space()
        print(f'The price for today will be: {price}.')
        print('Make sure you leave on time or else we\'ll tow you!')


    def general_space(self):
        gen_available = self.gen_total - self.gen_taken
        if gen_available > 0:
            print(f'Great, we have {gen_available} spaces left.')
        else:
            print('Unfortunately, we don\'t have anymore spaces available.')
        
        

    def dis_space(self):
        dis_available = self.dis_total - self.dis_taken
        if dis_available > 0:
            print(f'Great, we have {dis_available} spaces left.')
        else:
            print('Unfortunately, we don\'t have anymore handicap spaces available.')
        


class Main():

    my_ticket = Garage()

class Battery:
    def charge(self):
        print("Battery charging")

class Phone:
    def __init__(self, battery):
        self.battery = Battery()

    def charge_phone(self):
        self.battery.charge()

battery1 = Battery()
phone1 = Phone(battery1)
phone1.charge_phone()
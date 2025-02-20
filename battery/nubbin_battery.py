from abc import ABC

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def battery_should_be_serviced(self):
        date_which_battery_should_be_serviced_by =  super().__init__(self.last_service_date, 4)
        return date_which_battery_should_be_serviced_by < self.current_date 

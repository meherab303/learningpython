class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def vehicle_info(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}")    
class Car(Vehicle):
    def __init__(self,brand,model,year, fuel_type, doors):
        super().__init__(brand, model, year)
        self.fuel_type=fuel_type
        self.doors=doors        
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Fuel_type:{self.fuel_type}\nDoors:{self.doors}")
    def start_engine(self):
        print("Engine Startring..")    

    def stop_engine(self):
        print("Engine Stoppped....") 


my_car=Car("tesla","model_s",2022,"electric",4)
my_car.vehicle_info()
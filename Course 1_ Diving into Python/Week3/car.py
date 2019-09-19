import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            self.body_length = float(body_whl.split("x")[2])
            self.body_width = float(body_whl.split("x")[0])
            self.body_height = float(body_whl.split("x")[1])
        except (ValueError, IndexError):
            self.body_width, self.body_height, self.body_length = 0.0, 0.0, 0.0
        
    def get_body_volume(self):
            return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if (row != []) and (row[0] != "") and (row[1] != "") and (len(row) != 6):
                if(row[0] == 'car'):
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif(row[0] == 'truck'):
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif(row[0] == 'spec_machine'):
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
    return car_list

if __name__ == '__main__':
    car_list = get_car_list("coursera_week3_cars.csv")
    for car in car_list:
        print(car.__dict__)
        if car.car_type == 'truck':
            print(car.get_body_volume())
            #print(car.get_body_volume())

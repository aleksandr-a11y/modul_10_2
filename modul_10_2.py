from os import name
import threading
import time   
from datetime import datetime
from threading import Thread

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        print(f'{self.name} на нас напали!')
    def run(self):
        k = 1
        i = 100 - self.power
        while i > 0:
            print(f'{self.name} сражается {k} дней..., осталось {i} воинов.')
            time.sleep(1)
            i = i - self.power
            k += 1
        print(f'{self.name} одержал победу спустя {k} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
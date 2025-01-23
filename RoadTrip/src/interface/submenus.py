from src.logic.car_controls import *
from src.logic.miscellaneous import *
from src.util import draw_line, input_interger


def car_controls_main():
    draw_line(20)
    user_input = input_interger('Choose one option: ')

    if user_input == 1:
        accel()
    elif user_input == 2:
        brake()
    elif user_input == 3:
        turn_r()
        return car.crash
    elif user_input == 4:
        turn_l()
        return car.crash
    elif user_input == 5:
        get_speed()
    elif user_input == 6:
        get_direction()
    else:
        print('Returning...')
    sleep(1)


def miscellaneous_main():
    draw_line(18)
    user_input = input_interger('Choose one option: ')

    if user_input == 1:
        weather_now()
    elif user_input == 2:
        temperature()
    elif user_input == 3:
        time()
    else:
        print('Returning...')
    sleep(1 )

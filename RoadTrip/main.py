from src.interface import gui, submenus
from src import util
from src.logic.car_controls import car

while True:
    if car.crash:
        break
    gui.menu('  Road Trip   ', ['Car controls', 'Miscellaneous', 'Time Skip'])
    user_input = util.input_interger('Choose one option: ')

    if user_input == 1:
        gui.menu('  Car Controls  ', ['Accelerate', 'Brake', 'Turn right', 'Turn left', 'Get speed', 'Get direction',
                                      'Return'])
        submenus.car_controls_main()
    elif user_input == 2:
        gui.menu('   Miscellaneous   ', ['Get weather', 'Get temperature', 'Get time', 'Return'])
        submenus.miscellaneous_main()
    elif user_input == 3:
        print('You arrived your destination!')
        break
    else:
        print('Please input a valid option!')

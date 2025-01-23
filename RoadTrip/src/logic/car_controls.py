from src import util
from src.car import Car
from time import sleep

color = ['\033[32m', '\033[0m']
car = Car(50)


def accel():
    percentage = util.input_percentage('Input the acceleration percentage: ')
    car.accelerate(percentage)

    print(color[0])

    if percentage >= 80:
        print("With determination and a forcefull grip on the wheel you firmly press down the cars\n"
              "accelerator, unleashing all the power you were eager to experience.\nThe engine roared to life,"
              "its revving sound echoing\nthrough the air, as the tires screeches against the treacherous terrain.")
    elif 80 > percentage >= 40:
        print("With a steady grip on the steering wheel you gently press the accelerator with a regular force\n"
              "causing a smooth increase in the car's speed. The engine begins to purr steadily\nemitting a"
              "confident and consistent sound, providing a sense of calm and confident control.")
    else:
        print("With a gentle grip on the steering wheel, you delicately apply pressure to the accelerator,\n"
              "initiating a subtle acceleration of the car. The engine hums softly, emitting a subdued and \n"
              "harmonious tone. As you carefully adjusted the pedal, you move forward with a graceful motion")

    print(color[1])


def brake():
    percentage = util.input_percentage('Input the brake percentage: ')
    car.brake(percentage)

    print(color[0])
    if car.get_speed() >= 60 and percentage >= 75:
        print("A surge of urgency fills your senses as you forcefully press your foot down on the brake pedal. \n"
              "The screech of tires fills the air, echoing through the surroundings. The vehicle begins to\n"
              "decelerate rapidly, the powerful brakes exerting their force as the speedometer needle rapidly drops")
    elif car.get_speed() < 60 and 50 < percentage < 75:
        print("You press foot down on the brake pedal, instigating an intense but controlled deceleration of the\n"
              "car. The speedometer needle descends steadily.")
    else:
        print("With a composed grip on the steering wheel, you gently ease your foot onto the brake pedal\n"
              "gradually exerting pressure to slow down the car. The vehicle begins to decelerate smoothly\n"
              "gliding through the air with a controlled grace. The speedometer needle gradually descends")
    print(color[1])


def turn_r():
    if car.get_speed() != 200:
        print("\033[32mYou gently apply the brakes, navigate the curve to the right, and then smoothly press the\n"
              "accelerator pedal to regain your forward momentum.\033[0m")
        car.turn_right()
        sleep(2)
    else:
        car.accident('right')


def turn_l():
    if car.get_speed() != 200:
        print("\033[32mYou gently apply the brakes, navigate the curve to the left, and then smoothly press the\n"
              "accelerator pedal to regain your forward momentum.\033[0m")
        car.turn_left()
        sleep(2)
    else:
        car.accident('left')


def get_speed():
    print(color[0])
    if car.get_speed() == 200:

        print('You realize you are going too fast. You take a worried look at the speedometer, it points to its\n'
              f'maximum speed indicator {color[1]}{car.get_speed()}KM/h.{color[0]} You may need to slow down, '
              f'or something \nis going to happen...')
    elif car.get_speed() == 0:
        print(
            f"You know the car is stopped, but you glance the speedometer anyways. It marks {color[1]}{car.get_speed()}"
            f"KM/h{color[0]}")
    else:
        print(f'You take a quick glance at the speedometer, it marks {color[1]}{car.get_speed()}KM/h{color[0]}')

    print(color[1])


def get_direction():
    print(f'{color[0]}You quickly open the glove compartment and retrive a small compass that lies inside,'
          f'\nAfter you analize the compass, the pointer{color[1]} indicates {car.get_direction()}. {color[0]}After'
          f' examining it\nbriefy, you put it back into its original compartment.{color[1]}')

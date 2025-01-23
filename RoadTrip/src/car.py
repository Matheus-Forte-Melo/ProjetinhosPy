class Car:
    def __init__(self, speed):
        self.crash = False
        self.speed = speed
        self.directions = {0: "O", 1: "N", 2: "L", 3: "S"}
        self.current_direction = 1

    def get_speed(self):
        return self.speed

    def brake(self, percentage: int):
        percentage = percentage / 100
        self.speed = self.speed - (self.speed * percentage)
        self.speed = round(self.speed)

        if self.speed < 0:
            self.speed = 0
        return self.speed

    def accelerate(self, percentage: int):
        percentage = percentage / 100 + 1
        self.speed = self.speed * percentage
        self.speed = round(self.speed)
        # Impede que o carro não consiga acelerar novamente depois de parado.
        if self.speed == 0:
            self.speed = 50

        if self.speed > 200:
            self.speed = 200
        return self.speed

    def get_direction(self) -> str:
        return self.directions[self.current_direction]

    def turn_right(self) -> str:
        self.current_direction += 1
        if self.current_direction > 3:
            self.current_direction = 0
        return self.directions[self.current_direction]

    def turn_left(self) -> str:
        self.current_direction -= 1
        if self.current_direction < 0:
            self.current_direction = 3
        return self.directions[self.current_direction]


    def accident(self, direct):
        print(f'\033[32mYou pushed the speed limits, approaching a {direct} turn. Panic set in as you realized\nyou '
              'were going too fast to handle it. Heart pounding, hands gripping the wheel, you fought to slow down\nbut'
              ' it was futile. The car flipped violently, spinning out of control. Glass shattered, metal screeched\n'
              'Impact after impact. \033[0mYou are dead.')
        self.crash = True


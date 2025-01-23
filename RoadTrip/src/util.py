def draw_line(length):
    print('=' * length)


def input_percentage(txt) -> int:
    while True:
        try:
            percentage = int(input(txt))
            if percentage < 0:
                percentage = percentage * 1
            return percentage
        except (TypeError, ValueError):
            print('\033[32mPlease, input a interger value!\033[0m')


def input_interger(txt) -> int:
    while True:
        try:
            return int(input(txt))
        except (TypeError, ValueError):
            print('Input an interger!')



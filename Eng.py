import random
import os

CWD = os.getcwd()
CNT_WORD = 0
IS_STOP = 1
WORDS = ""
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#
# console helpers
#
def _set_console_color(color):
    print(color, end='')

def _reset_console_color():
    print(Colors.ENDC, end='')

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

def info(msg):
    _set_console_color(Colors.OKGREEN)
    print('{}'.format(msg))
    _reset_console_color()

def oneCycle():
    global IS_STOP, CNT_WORD, WORDS
    with open("data.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    random_line = random.choice(lines)
    info(random_line)
    user_input = input("Y,N: ").strip().lower()
    if user_input == 'y':
        parts = random_line.split(", ")
        word = parts[0]
        value = int(parts[1])
        value -= 1
        new_line = f"{word}, {value}"
        print(new_line)
        if value == 0:
            lines.remove(random_line)
            CNT_WORD += 1
        else:
            lines[lines.index(random_line)] = new_line
    elif user_input == 'n':
        parts = random_line.split(", ")
        word = parts[0]
        value = int(parts[1])
        value += 3
        new_line = f"{word}, {value}"
        WORDS += word + ", "
        lines[lines.index(random_line)] = new_line
    elif user_input == 'e':
        IS_STOP = 0
        info(f'You deleted {CNT_WORD}, Learn: {WORDS}')
    with open("data.txt", "w") as file:
        for v in lines:
            v = v + "\n"
            file.write(v)

clear_console()

while IS_STOP:
    oneCycle()


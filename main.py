from sys import path
from constants import UI_CODES

def main():
    path.append(UI_CODES)

    from ui_main import UI

    ui_instance = UI()
    ui_instance.start()


if __name__ == '__main__':
    main()
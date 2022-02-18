from common_utils import menu_utils
from info_collection import info_collection_menu
from vulnerability_analysis import vulnerability_analysis_menu
from attack import attack_menu
import signal


def main_keyboard_interrupt_handler(signal, frame):
    menu_utils.see_you_soon()


signal.signal(signal.SIGINT, main_keyboard_interrupt_handler)
menu_utils.banner()

while 1:

    """ CRACK MENU """

    option = menu_utils.nice_menu('Select category', ['combine information', 'consider loopholes', 'Attack It'])

    if (option < 1) | (option > 3):
        menu_utils.see_you_soon()

    if option == 1:
        info_collection_menu.menu()

    elif option == 2:
        vulnerability_analysis_menu.menu()

    elif option == 3:
        attack_menu.menu()

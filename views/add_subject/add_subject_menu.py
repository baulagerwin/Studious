from ..components import border, menu
from .add_subject_menu_list import add_subject_menu_list

def add_subject_menu():
    add_subjects = add_subject_menu_list()
    menu("--Add Subject Menu", "Choose one of the above: ", add_subjects, "--INVALID INPUT: Type how many you want to add")
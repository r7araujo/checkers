import pygame, pygame_gui, sys

def main_menu(ui_manager):
    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 270), (200, 50)),
        text = 'Play game',
        manager=ui_manager
    )
    return start_button

def win_menu(ui_manager, winner):
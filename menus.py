import pygame, pygame_gui, sys

def main_menu(ui_manager):
    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 270), (200, 50)),
        text = 'Play game',
        manager=ui_manager
    )
    return start_button

def win_menu(ui_manager, winner):
    button_rect = pygame.Rect((220, 380), (200, 50))
    if winner == 'W':
        display_text = 'White wins! Play again.'
    else:
        display_text = 'Black wins! Play again.'
    restart_button = pygame_gui.elements.UIButton(
        relative_rect=button_rect,
        text = display_text,
        manager = ui_manager
    )
    return restart_button
import pygame as pg
from variables import *

# Useful tools for calculation and display

# ----- Classes ------


class Button(pg.sprite.Sprite):
    """Class that creates button that takes custom command input"""
    def __init__(self, pos, color, text, action, font=font):
        super().__init__()
        self.color = color
        self.action = action
        self.text = text
        self.font = font
        self.image = pg.Surface((150, 40))
        self.rect = self.image.get_rect(bottomleft=pos)
        self.fill_surf(self.color)

    def fill_surf(self, color):
        self.image.fill(pg.Color(color))
        self.image.blit(self.font.render(self.text, True, pg.Color('White')), (10, 10))

    def update(self, events, dt):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # if the player clicked the button, the action is invoked
                    self.action()


# ----- Methods ------


def text_format(text, text_size, text_color, text_font=font):
    """Template for creating text in pygame"""
    new_font = pg.font.Font(text_font, text_size)
    new_text = new_font.render(text, 0, text_color)

    return new_text


def mouse_collison(objects, radius):
    """Gets the position of the mouse and checks if it collides with any objects in the game"""
    pos_x, pos_y = pg.mouse.get_pos()
    selected, selected_offset_x, selected_offset_y = None, 0, 0
    # Checks if the mouse collides with element
    for i, o in enumerate(objects):
        # Pythagoras a^2 + b^2 = c^2
        dx = o.centerx - pos_x
        dy = o.centery - pos_y
        distance_square = dx ** 2 + dy ** 2

        # Checks the distance between the cursor and the circle
        if distance_square <= radius[i] ** 2:
            selected = i
            selected_offset_x = o.x - pos_x
            selected_offset_y = o.y - pos_y

    return selected, selected_offset_x, selected_offset_y


def verlet_algorithm(position: int, velocity: int, acceleration: int, dt: int = 0.5):
    """This calculats the second order Taylor solution to the newton DGLs"""
    # Maybe use scipy.integrate to solve newton DGLs

    position = position - velocity * dt + (acceleration * (dt**2) * 0.5)
    velocity = velocity + acceleration * dt

    return position, velocity


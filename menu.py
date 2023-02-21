import pygame

class Button:
    def __init__(self, x, y, image):

        self.button_image = image
        self.button_rect = self.button_image.get_rect(topleft = (x, y))

        # 'debouncer' for click
        self.clicked_state = False

    def draw(self, surface):
        surface.blit(self.button_image, self.button_rect)

    def is_clicked(self):

        # bool to return for button click
        self.action = False

        # check for button mouseover and click
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            print('mouse over')
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_state:
                self.clicked_state = True
                print('clicked')

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return self.action
        
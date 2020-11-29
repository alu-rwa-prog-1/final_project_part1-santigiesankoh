import unittest

positions = []


def get_head_position():
    pass


class Snake(unittest.TestCase):
    def exit_game(self):
        self.assertEqual('exit'.upper( ), 'EXIT')

    def handle_keys(self):
        from pygame.examples.prevent_display_stretching import event
        import pygame
        self.assertIs(event.key, pygame.K_DOWN)

    def reset(self):
        snake_position = [0]
        self.assertIs(snake_position, 0)

    def move(self):
        self.assertIn(get_head_position( ), positions.pop( ))

    def draw(self):
        self.assertEqual([0, 1, 2, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main( )

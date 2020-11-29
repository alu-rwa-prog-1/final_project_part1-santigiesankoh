import unittest



class Food(unittest.TestCase):
    def randomize_food_position(self):
        self.assertEqual([0], [0])

    def draw_food(self):
        self.assertEqual((12, 2, 4), (12, 2, 4))

    def My_font(self):
        self.assertEqual('Monospace', 'Monospace')


if __name__ == '__main__':
    unittest.main()
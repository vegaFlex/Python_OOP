

import unittest
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.Task_3_UnitTests_EXam_Prep_30_06_24_Python_OOP_06_2024.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.player = TennisPlayer("Roger Federer", 38, 10000.0)

    def test_constructor(self):
        self.assertEqual(self.player.name, "Roger Federer")
        self.assertEqual(self.player.age, 38)
        self.assertEqual(self.player.points, 10000.0)
        self.assertEqual(self.player.wins, [])

    def test_name_property(self):
        with self.assertRaises(ValueError):
            self.player.name = "Ro"
        with self.assertRaises(ValueError):
            self.player.name = ""
        with self.assertRaises(ValueError):
            self.player.name = "A"
        self.player.name = "Rafael Nadal"
        self.assertEqual(self.player.name, "Rafael Nadal")

    def test_age_property(self):
        with self.assertRaises(ValueError):
            self.player.age = 17
        with self.assertRaises(ValueError):
            self.player.age = -5
        with self.assertRaises(ValueError):
            self.player.age = 0
        self.player.age = 25
        self.assertEqual(self.player.age, 25)

    def test_add_new_win(self):
        self.player.add_new_win("Wimbledon")
        self.assertIn("Wimbledon", self.player.wins)
        result = self.player.add_new_win("Wimbledon")
        self.assertEqual(result, "Wimbledon has been already added to the list of wins!")
        self.assertEqual(len(self.player.wins), 1)
        self.player.add_new_win("US Open")
        self.assertIn("US Open", self.player.wins)
        self.assertEqual(len(self.player.wins), 2)

    def test_lt_method(self):
        other_player = TennisPlayer("Novak Djokovic", 33, 11000.0)
        self.assertEqual(self.player < other_player,
                         "Novak Djokovic is a top seeded player and he/she is better than Roger Federer")
        other_player.points = 9000.0
        self.assertEqual(self.player < other_player,
                         "Roger Federer is a better player than Novak Djokovic")
        other_player.points = 10000.0
        self.assertEqual(self.player < other_player,
                         "Roger Federer is a better player than Novak Djokovic")

    def test_str_method(self):
        expected_str = "Tennis Player: Roger Federer\nAge: 38\nPoints: 10000.0\nTournaments won: "
        self.assertEqual(str(self.player), expected_str)
        self.player.add_new_win("US Open")
        expected_str = "Tennis Player: Roger Federer\nAge: 38\nPoints: 10000.0\nTournaments won: US Open"
        self.assertEqual(str(self.player), expected_str)
        self.player.add_new_win("Wimbledon")
        expected_str = "Tennis Player: Roger Federer\nAge: 38\nPoints: 10000.0\nTournaments won: US Open, Wimbledon"
        self.assertEqual(str(self.player), expected_str)


if __name__ == '__main__':
    unittest.main()
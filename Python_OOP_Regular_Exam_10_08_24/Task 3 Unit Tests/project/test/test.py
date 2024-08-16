import unittest
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(unittest.TestCase):

    def setUp(self):
        # This method runs before each test case
        self.player = SoccerPlayer("Lionel Messi", 35, 750, "Barcelona")

    def test_initialization(self):
        self.assertEqual(self.player.name, "Lionel Messi")
        self.assertEqual(self.player.age, 35)
        self.assertEqual(self.player.goals, 750)
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(self.player.achievements, {})

    def test_name_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = "Messi"
        self.assertEqual(str(context.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(ValueError) as context:
            self.player.name = ""  # Empty string case
        self.assertEqual(str(context.exception), "Name should be more than 5 symbols!")

    def test_age_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player.age = 15
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

        with self.assertRaises(ValueError) as context:
            self.player.age = -5  # Negative age case
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

    def test_goals_validation(self):
        self.player.goals = -1
        self.assertEqual(self.player.goals, 0)

        self.player.goals = 10
        self.assertEqual(self.player.goals, 10)

    def test_team_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player.team = "Chelsea"
        self.assertEqual(str(context.exception), "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")

        with self.assertRaises(ValueError) as context:
            self.player.team = ""  # Empty string case
        self.assertEqual(str(context.exception), "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")

    def test_change_team(self):
        result = self.player.change_team("Real Madrid")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "Real Madrid")

        result = self.player.change_team("Chelsea")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player.team, "Real Madrid")  # Ensure team didn't change

    def test_add_new_achievement(self):
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 1)

        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 2)

        # Test adding a different achievement
        result = self.player.add_new_achievement("Golden Boot")
        self.assertEqual(result, "Golden Boot has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Golden Boot"], 1)

    def test_lt_method(self):
        other_player = SoccerPlayer("Cristiano Ronaldo", 37, 800, "Juventus")
        result = self.player.__lt__(other_player)
        self.assertEqual(result, "Cristiano Ronaldo is a top goal scorer! S/he scored more than Lionel Messi.")

        # Test case where self has more goals than other
        another_player = SoccerPlayer("Neymar", 32, 500, "PSG")
        result = another_player.__lt__(self.player)
        self.assertEqual(result, "Lionel Messi is a top goal scorer! S/he scored more than Neymar.")

    def test_invalid_comparisons(self):
        # What happens if the other object is not a SoccerPlayer?
        with self.assertRaises(AttributeError):
            self.player.__lt__("Not a player")

if __name__ == "__main__":
    unittest.main()
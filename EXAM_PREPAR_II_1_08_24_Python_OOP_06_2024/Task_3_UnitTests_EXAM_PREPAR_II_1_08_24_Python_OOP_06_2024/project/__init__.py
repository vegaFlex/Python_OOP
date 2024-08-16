import unittest
from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.Task_3_UnitTests_EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.project.robot import Robot


class TestRobot(unittest.TestCase):

    def test_initialization(self):
        # Test proper initialization
        r = Robot("R001", "Military", 100, 1000.0)
        self.assertEqual(r.robot_id, "R001")
        self.assertEqual(r.category, "Military")
        self.assertEqual(r.available_capacity, 100)
        self.assertEqual(r.price, 1000.0)
        self.assertEqual(r.hardware_upgrades, [])
        self.assertEqual(r.software_updates, [])

        # Test invalid category
        with self.assertRaises(ValueError) as context:
            Robot("R002", "InvalidCategory", 100, 1000.0)
        self.assertTrue("Category should be one of" in str(context.exception))

        # Test invalid price
        with self.assertRaises(ValueError) as context:
            Robot("R003", "Education", 100, -1000.0)
        self.assertTrue("Price cannot be negative!" in str(context.exception))

    def test_category_setter(self):
        r = Robot("R004", "Education", 100, 500.0)
        with self.assertRaises(ValueError):
            r.category = "InvalidCategory"

    def test_price_setter(self):
        r = Robot("R005", "Humanoids", 100, 500.0)
        with self.assertRaises(ValueError):
            r.price = -100.0

    def test_upgrade(self):
        r = Robot("R006", "Entertainment", 100, 2000.0)
        result = r.upgrade("Laser", 300.0)
        self.assertEqual(result, "Robot R006 was upgraded with Laser.")
        self.assertIn("Laser", r.hardware_upgrades)
        self.assertEqual(r.price, 2000.0 + 300.0 * Robot.PRICE_INCREMENT)

        # Test upgrade with existing component
        result = r.upgrade("Laser", 300.0)
        self.assertEqual(result, "Robot R006 was not upgraded.")

    def test_update(self):
        r = Robot("R007", "Military", 100, 1500.0)
        result = r.update(1.0, 30)
        self.assertEqual(result, "Robot R007 was updated to version 1.0.")
        self.assertEqual(r.available_capacity, 70)
        self.assertIn(1.0, r.software_updates)

        # Test update with insufficient capacity
        result = r.update(2.0, 80)
        self.assertEqual(result, "Robot R007 was not updated.")
        self.assertNotIn(2.0, r.software_updates)
        self.assertEqual(r.available_capacity, 70)

        # Test update with an older version
        result = r.update(1.0, 20)
        self.assertEqual(result, "Robot R007 was not updated.")
        self.assertEqual(r.available_capacity, 70)

    def test_comparison(self):
        r1 = Robot("R008", "Education", 100, 1000.0)
        r2 = Robot("R009", "Humanoids", 100, 1500.0)
        r3 = Robot("R010", "Entertainment", 100, 1000.0)

        self.assertEqual(r1 > r2, "Robot with ID R008 is cheaper than Robot with ID R009.")
        self.assertEqual(r2 > r1, "Robot with ID R009 is more expensive than Robot with ID R008.")
        self.assertEqual(r1 > r3, "Robot with ID R008 costs equal to Robot with ID R010.")


if __name__ == "__main__":
    unittest.main()

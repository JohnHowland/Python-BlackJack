import unittest
import MainProgram


class MyTestCase(unittest.TestCase):
    def test_one(self):
        player = MainProgram.Player('Jose', 100)
        name = player.name
        bank = player.balance
        self.assertEqual(name, 'Jose')
        self.assertEqual(bank, 100)

    def test_two(self):
        player = MainProgram.Player('Jack', 100)
        name = player.name
        bank = player.balance
        self.assertEqual(name, 'Jack')
        self.assertEqual(bank, 100)


if __name__ == '__main__':
    unittest.main()

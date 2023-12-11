import unittest
import run


class TestNameValidation(unittest.TestCase):
    def test_name_nonalpha(self):
        self.assertEqual(run.validate_name('$%&$&£"'), False, 'Should be alpha')

    def test_name_empty(self):
        self.assertEqual(run.validate_name(''), False, 'Should not be empty')

    def test_name_with_space(self):
        self.assertEqual(run.validate_name('Gary Parsnip'), True, 'Names with spaces should be allowed')

if __name__ == '__main__':
    unittest.main()
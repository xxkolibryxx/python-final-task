import unittest
import pandas as pd
from src.one_hot_encoding import convert_to_one_hot

class TestOneHotEncoding(unittest.TestCase):
    def test_one_hot_encoding(self):
        data = pd.DataFrame({'whoAmI': ['robot', 'human', 'robot']})
        expected_output = pd.DataFrame({
            'robot': [1, 0, 1],
            'human': [0, 1, 0]
        })
        result = convert_to_one_hot(data)
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()

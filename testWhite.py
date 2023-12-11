import unittest
from tongyiqianwen import creation_of_poem, creation_of_story, analysis_of_classical_chinese, professional_planner, psychological_counselor
class TestTextGenerationFunctions(unittest.TestCase):

    def test_analysis_of_classical_chinese_1(self):
        title = "今天天气不好"
        result_title, result_output = analysis_of_classical_chinese(title)
        self.assertEqual(result_title, title)
        self.assertIsInstance(result_output, str)

    def test_analysis_of_classical_chinese_2(self):
        title = "今天天气很好"
        result_title, result_output = analysis_of_classical_chinese(title)
        self.assertEqual(result_title, title)
        self.assertIsInstance(result_output, str)

if __name__ == '__main__':
    unittest.main()
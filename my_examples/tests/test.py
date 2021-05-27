from unittest import TestCase
# from src.main import Calculator
from unittest import TestCase
from unittest.mock import patch, Mock


# class TestCalculator(TestCase):
#     def setUp(self):
#         self.calc = Calculator()
#
#     def test_sum(self):
#         answer = self.calc.sum(2, 4)
#         self.assertEqual(answer, 6)


class TestCalculator(TestCase):
    @patch('src.main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)


class TestBlog(TestCase):
    @patch('src.main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)


def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator1(TestCase):
    @patch('src.main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)
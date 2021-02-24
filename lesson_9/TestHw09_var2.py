import unittest

from hw09_var2 import TagFactory

class TestTagFactory(unittest.TestCase):

    factory = TagFactory()
    
    def test_create_tag(self):
        self.tag_name = 'image'
        # self.tag_name = 0
        # self.tag_name = None

        self.assertTrue(self.factory.create_tag(self.tag_name), True)
        self.assertIsInstance(self.tag_name, str)


if __name__ == "__main__":
    unittest.main()

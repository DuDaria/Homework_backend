import unittest

from hw09_var1 import Tag, TagFactory, get_html, _tag_a, _tag_image, _tag_input, _tag_p

class TestTagFactory(unittest.TestCase):

    tagfactory = TagFactory()
    
    def test_create_tag(self):
        self.format = 'image'
        # self.format = 0
        # self.format = None

        self.tag = Tag(self.format)

        self.assertTrue(self.format, True)
        self.assertIsInstance(self.format, str)
        self.assertEqual(self.tagfactory.create_tag(self.tag, self.format), ('<image></image>'))


class TestTags(unittest.TestCase):

    def test_get_html(self):
        self.format = 'image'
        # self.format = 0
        # self.format = None

        self.assertEqual(self.format, 'image')
        self.assertNotEqual(self.format, ' ')
        self.assertNotEqual(self.format, '')
        self.assertTrue(self.format, True)
        self.assertIsInstance(self.format, str)

    def test__tag_image(self):
        self.tag = 'image'
        # self.format = 0
        # self.format = None

        self.assertNotEqual(self.tag, ' ')
        self.assertNotEqual(self.tag, '')
        self.assertTrue(self.tag, True)
        self.assertIsInstance(self.tag, str)
        
    def test__tag_input(self):
        self.tag = 'input'
        # self.tag = 0
        # self.tag = None

        self.assertEqual(self.tag, 'input')
        self.assertNotEqual(self.tag, ' ')
        self.assertNotEqual(self.tag, '')
        self.assertTrue(self.tag, True)
        self.assertIsInstance(self.tag, str)

    def test__tag_p(self):
        self.tag = 'p'
        # self.tag = 0
        # self.tag = None

        self.assertEqual(self.tag, 'p')
        self.assertNotEqual(self.tag, ' ')
        self.assertNotEqual(self.tag, '')
        self.assertTrue(self.tag, True)
        self.assertIsInstance(self.tag, str)

    def test__tag_a(self):
        self.tag = 'a'
        # self.tag = 0
        # self.tag = None

        self.assertEqual(self.tag, 'a')
        self.assertNotEqual(self.tag, ' ')
        self.assertNotEqual(self.tag, '')
        self.assertTrue(self.tag, True)
        self.assertIsInstance(self.tag, str)

if __name__ == "__main__":
    unittest.main()



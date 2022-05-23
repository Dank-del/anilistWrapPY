import unittest
from anilistWrapPY import aniWrapPYClient

cl = aniWrapPYClient()

class TestWrapper(unittest.TestCase):
    def test_anime(self):
        self.assertIsNotNone(cl.Anime("Summertime Render"))
        
    def test_airing(self):
        self.assertIsNotNone(cl.Airing("Summertime Render"))
        
    def test_media(self):
        self.assertIsNotNone(cl.Media("Classroom of the elite"))
        
    def test_character(self):
        self.assertIsNotNone(cl.Character("Shin"))
        
    def test_manga(self):
        self.assertIsNotNone(cl.Manga("Summertime Render"))
        
    def test_user(self):
        self.assertIsNotNone(cl.User("TheDankDel"))
        
if __name__ == '__main__':
    unittest.main()
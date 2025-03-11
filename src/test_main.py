import unittest

from main import *

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        print("Main Test: test_extract_title")
        md = """# The Main Title
        
        ### Not the Main Title
        """
        title = extract_title(md)
        self.assertEqual("The Main Title", title)

if __name__ == "__main__":
    unittest.main()
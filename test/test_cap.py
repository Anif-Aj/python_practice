import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)  # function calling
        self.assertNotEqual(result, 'python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertNotEqual(result, 'monty python')
        
if __name__ == '__main__':
    unittest.main()
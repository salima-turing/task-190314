import unittest
import random
import string

def extract_names(text):
    # Dummy data extraction function for demonstration purposes
    names = []
    words = text.split()
    for word in words:
        if word.istitle():
            names.append(word)
    return names

class TestDataExtraction(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input data
        text = "Hello, my name is Alice. How are you?"
        expected_names = ["Alice"]
        self.assertEqual(extract_names(text), expected_names)

    def test_fuzz_testing(self):
        # Fuzz testing function to generate random strings
        def generate_random_string(length):
            return "".join(random.choice(string.ascii_letters) for _ in range(length))

        # Run fuzz testing with multiple random inputs
        for _ in range(100):  # You can adjust the number of iterations as needed
            random_text = generate_random_string(random.randint(1, 20))
            with self.subTest(random_text=random_text):
                # Expect the function to handle invalid inputs gracefully
                # and return an empty list
                self.assertEqual(extract_names(random_text), [])

if __name__ == "__main__":
    unittest.main()

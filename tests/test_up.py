import subprocess
import unittest

class TestAppUp(unittest.TestCase):
    def test_app_up(self):
        result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', 'http://localhost:5000'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), '200', "The application is not up on port 5000")

if __name__ == '__main__':
    unittest.main()
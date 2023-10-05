import unittest
from main import app

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_download_file(self):
        response = self.app.get('/download?user=rodrigo-kenji')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Disposition'], 'attachment; filename=user.txt')
        self.assertEqual(response.headers['Content-Type'], 'text/plain; charset=utf-8')

    def test_invalid_user(self):
        response = self.app.get('/download?user=rodrigo-kenji-invalid-user-for-test')
        self.assertEqual(response.status_code, 404)

    def test_missing_user(self):
        response = self.app.get('/download')
        self.assertEqual(response.status_code, 400)

if __name__ == '__name__':
    unittest.main()
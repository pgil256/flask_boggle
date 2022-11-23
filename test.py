from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        '''Stuff to do before every test.'''

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        '''Get session info and display HTML'''

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["M", "O", "M", "M", "M"], 
                                 ["M", "O", "M", "M", "M"],
                                 ["M", "O", "M", "M", "M"],
                                 ["M", "O", "M", "M", "M"],
                                 ["M", "O", "M", "M", "M"]]
        response = self.client.get('/check-word?word=mom')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        '''Tests if word is real'''

        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        '''Test if word exists on board'''

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=jkdfgkljdfknvjdvnkjn')
        self.assertEqual(response.json['result'], 'not-word')

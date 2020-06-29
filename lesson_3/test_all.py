import unittest
import json
import time
import server
from client import create_parcer, presence_message, read_message, defenition_answer



class TestClient(unittest.TestCase):
    def testserverCreateAnswer(self):
        code = server.create_answer(200)
        self.assertEqual(code, json.dumps({'response': 200, 'alert': 'OK'}))

    def testClientAnswer(self):
        message = {
            'action': 'presence',
            'time': time.ctime(),
            'type': 'status',
            'user': {
                'account_name': 'client',
                'status': 'OK',
            }
        }
        test = server.read_message(json.dumps(message))
        self.assertEqual(test, json.dumps({'response': 200, 'alert': 'OK'}))

    def testparceraddr(self):
        parcer = create_parcer()
        result = parcer.parse_args()
        self.assertEqual(result.addr, '127.0.0.1')

    def testparcerport(self):
        parcer = create_parcer()
        result = parcer.parse_args()
        self.assertEqual(result.port, 7777)


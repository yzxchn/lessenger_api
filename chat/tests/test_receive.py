from django.test import TestCase, RequestFactory
from django.http import JsonResponse

from chat import receive as rv
from chat import dialog as dg

class TestReceive(TestCase):
    def setUp(self):
        self.dm_text = dg.MessageReply("Test Reply")
        self.dm_cmd = dg.CommandReply("Test Command", {})
        self.rf = RequestFactory()
        join_params = {"action": "join", 
                       "user_id": 123456, 
                       "name": "Test"}
        msg_params = {"action": "message", 
                       "user_id": 123456, 
                       "text": "I love ice cream"}
        x_params = {"action": "foo"}
        self.join_request = self.rf.post('/chat/messages', join_params)
        self.msg_request = self.rf.post('/chat/messages', msg_params)
        self.x_request = self.rf.post('/chat/messages', x_params)

    def test_handle_dm__response(self):
        self.assertEqual("Test Reply", 
                         rv.handle_DM_response(self.dm_text))
        self.assertRaises(ValueError, rv.handle_DM_response, self.dm_cmd)

    def test_handle_request(self):
        res_join = rv.handle_request(self.join_request)
        res_msg = rv.handle_request(self.msg_request)
        self.assertIsInstance(res_join, JsonResponse)
        self.assertIsInstance(res_msg, JsonResponse)
        self.assertRaises(ValueError, rv.handle_request, self.x_request)

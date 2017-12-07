from django.test import TestCase
from .. import dialog

class TestDialog(TestCase):
    def setUp(self):
        self.msg1 = "what's the weather in San Francisco"
        self.msg2 = "weather in San Francisco"
        self.msg3 = "San Francisco weather"
        self.msgx = "Foo Bar"
        self.event_join = "join"
        self.join_params = {"name": "Test User"}
        self.wrong_params = {}
        self.eventx = "sleep_furiously"

    def test_handle_message(self):
        r1 = dialog.handle_message(self.msg1)
        r2 = dialog.handle_message(self.msg2)
        r3 = dialog.handle_message(self.msg3)
        rx = dialog.handle_message(self.msgx)
        self.assertEqual(r1.get_command_type(), "get-weather")
        self.assertEqual(r1.get_params()["location"], "san francisco")
        self.assertEqual(r2.get_command_type(), "get-weather")
        self.assertEqual(r2.get_params()["location"], "san francisco")
        self.assertEqual(r3.get_command_type(), "get-weather")
        self.assertEqual(r3.get_params()["location"], "san francisco")
        self.assertEqual(str(rx), "Sorry, I don't understand.")

    def test_handle_event(self):
        r1 = dialog.handle_event(self.event_join, self.join_params)
        r2 = dialog.handle_event(self.eventx, self.wrong_params)
        r3 = dialog.handle_event(self.event_join, self.wrong_params)
        self.assertEqual(str(r1), "Hello, Test User!")
        self.assertEqual(str(r2), "Sorry, I don't understand.")
        self.assertEqual(str(r3), "Hello, stranger!")

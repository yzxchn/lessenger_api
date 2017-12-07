import re

def handle_message(message):
    intent = classify_message(message)
    if intent == "ask-weather":
        return handle_ask_weather(message)
    else:
        return default_response()

def classify_message(message):
    """Classify a message, returns the intent of the message."""
    if "weather" in message.lower():
        return "ask-weather"
    else:
        return "unknown"

def handle_event(event, params):
    if event == "join":
        return event_join(params)
    else:
        return default_response()

def event_join(params):
    try:
        name = params["name"]
    except KeyError:
        name = "stranger"

    return MessageReply("Hello, {}!".format(name))


def handle_ask_weather(message):
    patterns = [r"what's the weather in ([\w ]+)", 
                r"weather in ([\w ]+)", 
                r"([\w ]+) weather"]
    for p in patterns:
        m = re.match(p, message.lower())
        if m:
            loc = m.group(1)
            return CommandReply("get-weather", 
                                {"location": loc})
    return default_response()

def default_response():
    return MessageReply("Sorry, I don't understand.")

class Reply:
    def __init__(self, type_):
        self.type = type_

    def get_type(self):
        return self.type

class MessageReply(Reply):
    def __init__(self, text):
        Reply.__init__(self, "text")
        self.text = text

    def get_text(self):
        return self.text

    def __str__(self):
        return self.text

class CommandReply(Reply):
    def __init__(self, command, params):
        Reply.__init__(self, "command")
        self.cmd_type = command
        self.params = params

    def get_command_type(self):
        return self.cmd_type

    def get_params(self):
        return self.params

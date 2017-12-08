import re
"""Dialog Manager Module

The dialog manager is used for managing the conversation with a user. 
It receives either a "message" or an "event". A message is just a text string. 
While an event can contain parameters. 
After receiving a message or event, the dialog processes the request. Then, 
depending on the request, either returns a text message to be sent to the user, 
or a "command" telling the bot that there is further actions to be performed. 
"""

def handle_message(message):
    """Handles a text message request.

    Classifies the message into an "intent", then responds accordingly.
    """
    intent = classify_message(message)
    if intent == "ask-weather":
        return handle_ask_weather(message)
    else:
        return default_response()

def classify_message(message):
    """Classifies a message, returns the intent of the message.

    An intent represents what the user wants with the message. For example, 
    when a user asks "what's the weather in San Francisco", the intent should be 
    "ask-weather"
    """
    if "weather" in message.lower():
        return "ask-weather"
    else:
        return "unknown"

def handle_event(event, params):
    """Handles an event request.
    An event is a non textual request. For example, a "join" event indicates 
    that the user has joined the conversation.
    """
    if event == "join":
        return event_join(params)
    # given some weather information, put it into a natural sounding text 
    # message.
    elif event == "report-weather": 
        return event_report_weather(params)
    # the bot fails to find the location provided by the user.
    elif event == "loc-not-found":
        return MessageReply("Sorry, I don't know about that location.")
    elif event == "weather-not-found":
        return MessageReply("Sorry, I can't find weather information"+\
                            " for that location.")
    else:
        return default_response()

def event_join(params):
    """Sends a greeting message when a "join" event is received.
    """
    try:
        name = params["name"]
    except KeyError:
        name = "stranger"

    return MessageReply("Hello, {}!".format(name))

def event_report_weather(params):
    """Composes a natural-sounding report of the weather information.
    """
    return MessageReply("Currently, it's {}F. {}"\
                                    .format(params["temperature"],
                                            params["summary"]))

def handle_ask_weather(message):
    """Parses and extracts the location from a message asking for weather.
    """
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

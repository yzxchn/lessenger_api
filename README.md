# Lessenger API Implementation

This is my solution to the [Hipmunk Lessenger problem](https://github.com/Hipmunk/hipproblems/tree/master/lessenger).

# How to use
First, clone the repository into a directory of your choice.

>`git clone git@github.com:yzxchn/lessenger_api.git`

Change into the project root, and put the separately provided `keys.config` file here.

Then, install the dependencies:

>`pip3 install -r requirements.txt`

Run the server with the following command:

>`python3 manage.py runserver 9000`

Open the chatbot UI [here](http://hipmunk.github.io/hipproblems/lessenger/)

# Description
There are several core components of the program:

* `receive.py` is used for handling and responding to requests sent by the UI.
* `dialog.py` is the "dialog manager", it processes the messages sent by the user, and is also responsible for generating responses to be sent to the user.
* `actions.py` contains code for actions the bot could perform. For now, it only contains the action of getting weather information for a location the user specifies.
* `weather.py` contains code for querying the Google Maps API and DarkSky API.

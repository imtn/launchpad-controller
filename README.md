This program reads in inputs from a nova launchpad mini mk3 and writes out keyboard events depending on the input passed in. This is useful to have a launchpad act as a keyboard, with custom combinations and states as you want.

This programs uses states to determine which buttons are available, which lights light up, and what keys they send.

Requires Python 3 and pip to install everything in requirements.txt

Set up this program by defining your states in launchpad/states. states/state.py defines a state, which is a combination of hotkeys. states/default.py defines the default state when this program is first loaded. Create other states in this folder and connect them to default.py to make them accessible.

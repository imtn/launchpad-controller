import keyboard
import mido
from mido import Message
from mido.backends.rtmidi import Input, Output
from states.ffxiv import FFXIV
from states.state import LPState, KeyNote


class Default(LPState):
	def __init__(self, inport: Input, outport: Output):
		super().__init__(inport, outport)
		self.name = "Default State"
		self.states = [FFXIV(inport, outport)] # Add new custom states here
		self.currState = None

		self.keynotes = [
			KeyNote('00 5e 4a'), # left arrow yellow, scroll options
			KeyNote('00 5d 4a'), # right arrow yellow, scroll options
			KeyNote('00 5b 4c'), # up arrow green, select
		]

	def default_callback(self, message: mido.Message):
		# if one of the above three notes, change currstate and redraw grid
		# otherwise ignore
		if message.is_cc(93) and message.dict()['value'] == 127: # left arrow
			if not self.currState:
				self.currState = 0
			else:
				self.currState = (self.currState - 1) % len(states)
		elif message.is_cc(94) and message.dict()['value'] == 127: # right arrow
			if not self.currState:
				self.currState = 0
			else:
				self.currState = (self.currState + 1) % len(states)
		elif message.is_cc(91) and message.dict()['value'] == 127: # up arrow
			# self.states[self.currState].load_state()
			# self.inport.callback = None
			return
		else:
			return

		# redraw grid
		if self.states[self.currState].icon:
			# draw icon
			self.states[self.currState].light_up_icon()
		else:
			# write name
			command = 'f0 00 20 29 02 0d 07 00 0c 00 75'
			for letter in self.states[self.currState].name:
				command += f" {int(hex(ord(letter))[2:])}"
			command += " f7"
			self.outport.send(Message.from_hex(command))


	def load_state(self):
		# set callbacks in outport
		# light up panel
		self.clear_launchpad_lights()
		self.inport.callback = self.default_callback
		self.light_up_launchpad()

import keyboard
import mido
from mido.backends.rtmidi import Input, Output
from states.state import LPState, KeyNote

class FFXIV(LPState):
	def __init__(self, inport: Input, outport: Output):
		super().__init__(inport, outport)
		self.name = "FFXIV"
		self.icon = [
			KeyNote('00 33 48'),
			KeyNote('00 29 48'),
			KeyNote('00 1f 48'),
			KeyNote('00 16 48'),
			KeyNote('00 0d 48'),
			KeyNote('00 0e 48'),
			KeyNote('00 0f 48'),
			KeyNote('00 1a 48'),
			KeyNote('00 25 48'),
			KeyNote('00 2f 48'),
			KeyNote('00 39 48'),
			KeyNote('00 42 48'),
			KeyNote('00 4b 48'),
			KeyNote('00 4a 48'),
			KeyNote('00 49 48'),
			KeyNote('00 3e 48'),
			KeyNote('00 3f 48'),
			KeyNote('00 40 48'),
			KeyNote('00 41 48'),
			KeyNote('00 34 48'),
			KeyNote('00 38 48'),
			KeyNote('00 2a 48'),
			KeyNote('00 2e 48'),
			KeyNote('00 20 48'),
			KeyNote('00 24 48'),
			KeyNote('00 17 48'),
			KeyNote('00 18 48'),
			KeyNote('00 19 48'),
			KeyNote('00 4c 7c'),
			KeyNote('00 57 7c'),
			KeyNote('00 58 7c'),
			KeyNote('00 43 7c'),
		]


	def load_state(self):
		super().load_state()
		# no class selected currently
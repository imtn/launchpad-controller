import keyboard
import mido
from mido import Message
from mido.backends.rtmidi import Input, Output
from typing import Callable

class LPState:
	# An LP State contains a list of KeyNotes, the input midi port, and the output midi port
	# An LP State has an init function to create itself. a setup function to create and register all the KeyNote hotkeys. a light up function to light up all launchpad buttons as defined by the keynotes.
	def __init__(self, inport: Input, outport: Output):
		self.inport = inport
		self.outport = outport
		self.keynotes = []
		self.name = ""
		self.icon = []


	def set_up_keynotes(self):
		for kn in keynotes:
			# create hotkey with callback if it exists
			pass


	def light_up_launchpad(self):
		command = 'f0 00 20 29 02 0d 03'
		for kn in self.keynotes:
			command += f" {kn.colorspec}"
		command += ' f7'
		self.outport.send(Message.from_hex(command))


	def light_up_icon(self):
		command = 'f0 00 20 29 02 0d 03'
		for kn in self.icon:
			command += f" {kn.colorspec}"
		command += ' f7'
		self.outport.send(Message.from_hex(command))


	def clear_launchpad_lights(self):
		command = 'f0 00 20 29 02 0d 03'
		for note in range(128):
			note = hex(note)[2:]
			if len(note) == 1:
				note = '0' + note
			command += f" 00 {note} 00"
		command += ' f7'
		self.outport.send(Message.from_hex(command))


class KeyNote:
	# A KeyNote has a keyboard key combination, a launchpad button/note, a color, and an optional callback that happens when the key is pressed.
	def __init__(self, colorspec: str, key: str=None, keypress_callback: Callable=None):
		self.key = key
		self.colorspec = colorspec
		self.keypress_callback = keypress_callback

		cs_split = colorspec.split(' ')
		if len(cs_split) != 3 or len(cs_split[0]) != 2 or len(cs_split[1]) != 2 or len(cs_split[2]) != 2:
			raise Exception("Colorspec must be a string of 3 hex values of length 2 without the 0x prefix, separated by a space.")

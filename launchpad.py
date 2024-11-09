import keyboard
import mido
from mido import Message
from states.default import Default as DS

# keyboard.add_hotkey("space", lambda: print("TNT pressed space", flush=True))
# keyboard.hook(lambda e: print(f"TNT pressed {e.name} scan code {e.scan_code} event type {e.event_type}", flush=True))
# keyboard.on_press_key("0", lambda e: keyboard.send("1"))

input_port_name = 'MIDIIN2 (LPMiniMK3 MIDI) 1'
output_port_name = 'MIDIOUT2 (LPMiniMK3 MIDI) 2'
sysex_header = 'f0 00 20 29 02 0d'
sysex_universal_device_inquiry = 'f0 7e 7f 06 01 f7'

def get_layout_message(layout: str):
	layouts = {
		'session': '00', # only selectable in DAW mode
		'custom1': '04', # default drum rack
		'custom2': '05', # default keys
		'custom3': '06', # default lighting mode in drum rack layout
		'daw_faders': '0d', # only selectable in DAW mode
		'programmer': '7f',
	}
	if layout not in layouts:
		raise Exception(f"Layout {layout} not in layouts.")
	return f'f0 00 20 29 02 0d 00 {layouts[layout]} f7'

def print_message_input(message):
	print(f"Input: {message.hex()}", flush=True)

def print_message_output(message):
	print(f"Output: {message.hex()}", flush=True)

def main():
	try:
		inport = mido.open_input(input_port_name, callback=print_message_input)
		outport = mido.open_output(output_port_name, callback=print_message_output)
	except Exception as err:
		if str(err).startswith('unknown port'):
			print("Unable to open port: " + str(err))
			print(f"Available input ports: {mido.get_input_names()}")
			print(f"Available output ports: {mido.get_output_names()}")
		else:
			print(str(err))
		return

	msg = Message.from_hex(get_layout_message('programmer'))
	outport.send(msg)
	# outport.send(Message.from_hex('f0 00 20 29 02 0d 07 00 0c 00 75 46 46 58 49 56 f7'))

	# def tntest():
	# 	print("TNT pressed space", flush=True)
	# 	keyboard.unhook_all_hotkeys()
	# 	keyboard.add_hotkey("a", lambda: print("TNT pressed A", flush=True))
	# keyboard.add_hotkey("space", tntest)



	print("keyboard waiting", flush=True)
	default_state = DS(inport, outport)
	default_state.load_state()
	keyboard.wait()


if __name__ == '__main__':
	main()

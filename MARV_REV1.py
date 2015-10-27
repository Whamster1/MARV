# MARV
# Marine Autonomous Research Vessel
import mraa, time, math, numpy 

def main():
	x_scaled = 0.0
	y_scaled = 0.0

	joystick = selectDevice()
	print("Joystick Initialized")
	for event in joystick.read_loop()
def selectDevice():
	"Select a device from a list of usb input devices"
	devices = [Input Device(i) for i in reversed(list_devices('/dev/input/'))]
	if(len(devices) > 2):
		return devices[2]
	else:
		print("No joysticks found!")
		exit()

class motor:
	MARVmotor = []

	def __init__(self):
		self.motor1 = mraa.Pwm(3)
		self.motor2 = mraa.Pwm(6)
		self.motor1.enable(True)
		self.motor2.enable(True)

	def power_motors(self):



from requests import get
import time
import gi


ip_starting = ""
recon_command = ""
rate = 60


def main():
	print("Example: nordvpn disconnect && nordvpn connect")
	recon_command = input("Enter the command used to reconnect to VPN: ")

	ip_starting = get('https://api.ipify.org').text
	print("Starting ip:", ip_starting)
	print("Connect to your VPN now!")

	import subprocess
	while True:
		time.sleep(rate)
		print("checking ip")
		if ip_starting == get('https://api.ipify.org').text:
			print("Snakeswitch activated")
			subprocess.run('notify-send Snakeswitch activated', shell=True)
			subprocess.run(recon_command)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			import sys
			sys.exit(0)
		except SystemExit:
			import os
			os._exit(0)

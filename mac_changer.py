import subprocess
import optparse

interface=input("Your interface >")
mac_adress=("Your mac adress >")

dm_init=optparse.ParseOption()

subprocess.call("ifconfig wlan0",shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:22:33:44:55:55",shell=True)
subprocess.call("ifconfig wlan0 up",shell=True)

dm_init.add_option("--i","--interface" ,help="Put your mac adress")
dm_init.parse_args()



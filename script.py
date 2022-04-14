import os

active = 'active'
inactive = 'inactive'

disabled = 'disabled'
enabled = 'enabled'

allow = 'allow'
deny = 'deny'
updated = 'updated'

print("Welcome to the UFW python script\n.1 Get firewall status\n.2 Open firewall ports\n.3 Close firewall ports\n.4 List firewall rules\n.5 Enable firewall\n.6 Disable firewall")
optioninput = input("\nPlease enter the number of the function you want to execute and press enter: ")
  
if optioninput.find('1') != -1:
	option1 = os.popen('sudo ufw status').read()
	if option1.find(inactive) != -1:
		os.system('clear')
		print("The firewall is:\n" + inactive)
		exit()
	else:
		os.system('clear')
		print("The firewall is:\n" + active)
		exit()

if optioninput.find('2') != -1:
	os.system('clear')
	portinput = input("Please enter the portnumber you want to allow: ")
	option2 = os.popen('sudo ufw allow ' + portinput).read()
	if option2.find(updated) != -1:
		os.system('clear')
		print("Allowing traffic for port:\n" + portinput)
		exit()

	else:
		os.system('clear')
		print("ERROR allowing port:\n" + portinput)
		exit()

if optioninput.find('3') != -1:
	os.system('clear')
	portinput = input("Please enter the portnumber you want to block: ")
	option2 = os.popen('sudo ufw deny ' + portinput).read()
	if option2.find(updated) != -1:
		os.system('clear')
		print("Denying traffic for port:\n" + portinput)
		exit()

	else:
		os.system('clear')
		print("ERROR denying port:\n" + portinput)
		exit()

if optioninput.find('4') != -1:
	os.system('clear')
	os.system('sudo ufw status')
	exit()

if optioninput.find('5') != -1:
	option5 = os.popen('sudo ufw enable').read()
	if option5.find(enabled) != -1:
		os.system('clear')
		print("The firewall is:\n" + enabled)
		exit()
	else:
		os.system('clear')
		print("The firewall is NOT " + enabled)
		exit()

if optioninput.find('6') != -1:
	option6 = os.popen('sudo ufw disable').read()
	if option6.find(disabled) != -1:
		os.system('clear')
		print("The firewall is:\n" + disabled)
		exit()
	else:
		os.system('clear')
		print("The firewall is NOT " + disabled)
		exit()

else:
	os.system('clear')
	print("Wrong input\nPlease input a number ONLY without any spaces and letters")
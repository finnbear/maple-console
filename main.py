import sys
import time
import random
from termcolor import colored

def clear():
	for i in range(12):
		time.sleep(0.01)
		print("")

def info(message):
	time.sleep(random.random() / 4)
	print(message)

def warn(message, ok):
	sys.stdout.write(message.ljust(31))
	sys.stdout.flush();

	if ok:
		time.sleep(random.random() / 2)
	else:
		time.sleep(random.random() * 2)

	sys.stdout.write(" [")

	if ok:
		sys.stdout.write(colored("  OK  ", "green"))
	else:
		sys.stdout.write(colored(" fail ", "red"))

	sys.stdout.write("]\n")
	sys.stdout.flush()

time.sleep(1);

info("BIOS(C)2020 Canada Systems, Inc. ")
info("BIOS Rev: 1.0.0")
info("CPU : OEM Installed")
info(" Speed : 5.00 GHz   Count: 4")

print("")

info("Checking system memory...")
warn("Found DIMM 1", True)
warn("Found DIMM 2", False)

print("")

info("Auto-detecting storage devices...")

warn("Scanning USB", True)
warn("Scanning CDROM", True)
warn("Scanning SATA", True)
warn("Found SATA device sda0", True)

print("")

print("+----------+")
print("| MAPLE OS |")
print("+----------+")
warn("Loading modules...", True)
warn("Loading startup script...", True)

clear()

#     [--------------------------------------]
print("#!/bin/robolang")
print(colored("# Made in Canada", "green"))
print("")
print("do")
print(colored("     find Child", "yellow"))
print("repeat")
print("")
print("")
print("")
print("")
print("______________________________________")

for j in range(1):
	for i in range(38):
		sys.stdout.write(".")
		time.sleep(0.1)
		sys.stdout.flush()
	sys.stdout.write("\r")
	for i in range(39):
		sys.stdout.write(" ")
	sys.stdout.write("\r")
	sys.stdout.flush()

print("#!/bin/robolang")
print(colored("# Made in .,.,..", "green"))
print(colored("          Canada", "green"))
print("do")
print(colored("     find Child", "yellow"))
print("repeat")
print("")
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write(".")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in  ,. .", "green"))
print(colored("          .,.,.,", "green"))
print("do" + colored("        Canada", "green"))
print(colored("     find Child", "yellow"))
print("repeat")
print("")
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write("..")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in   .", "green"))
print(colored("          . .. .", "green"))
print("do" + colored("        '..,.,", "green"))
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat    " + colored("Child", "yellow"))
print("")
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write("...")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print(colored("            .  .", "green"))
print("do" + colored("        ' .. .", "green"))
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("          " + colored("Child", "yellow"))
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write("....")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("          " + colored("Child", "yellow"))
print("")
print("")
print("______________________________________")
sys.stdout.write(".....")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("")
print("          " + colored("Child", "yellow"))
print("")
print("______________________________________")
sys.stdout.write("......")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("")
print("")
print("          " + colored("Child", "yellow"))
print("______________________________________")
sys.stdout.write(".......")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("")
print("")
print("")
print("__________" + colored("Child", "yellow") + "_______________________")
sys.stdout.write("........")
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write("......... " + colored("Child", "yellow"))
sys.stdout.flush()

time.sleep(0.1)

sys.stdout.write("\n")
print("#!/bin/robolang")
print(colored("# Made in", "green"))
print("")
print("do")
print(colored("     find ", "yellow") + colored("Canada", "green"))
print("repeat")
print("")
print("")
print("")
print("")
print("______________________________________")
sys.stdout.write("..........")
sys.stdout.flush()

for i in range(28):
	sys.stdout.write(".")
	time.sleep(0.1)
	sys.stdout.flush()
sys.stdout.write("\r")
for i in range(39):
	sys.stdout.write(" ")
sys.stdout.write("\r")
sys.stdout.flush()

while True:
	for i in range(38):
		sys.stdout.write(".")
		time.sleep(0.1)
		sys.stdout.flush()
	sys.stdout.write("\r")
	for i in range(39):
		sys.stdout.write(" ")
	sys.stdout.write("\r")
	sys.stdout.flush()

time.sleep(50)
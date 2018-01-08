import sys
import time
import random
from termcolor import colored

def info(message, ok):
	sys.stdout.write(message.ljust(31))
	sys.stdout.flush();

	if ok:
		time.sleep(random.random())
	else:
		time.sleep(random.random() + 1)

	sys.stdout.write(" [")

	if ok:
		sys.stdout.write(colored("  OK  ", "green"))
	else:
		sys.stdout.write(colored(" fail ", "red"))

	sys.stdout.write("]\n")
	sys.stdout.flush()

time.sleep(1);

info("Mounting /", True)
info("Accessing drive sda1", False)

time.sleep(1000);
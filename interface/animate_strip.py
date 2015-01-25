from bibliopixel.drivers.WS2801 import DriverWS2801
from bibliopixel.led import *
import strip_animations
import bibliopixel.colors as colors
import random
import sys
import getopt

def randcolor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def build_rainbow(led, opts, args):
	return strip_animatons.Rainbow(led)

def build_rainbow_cycle(led, opts, args):
	return strip_animations.RainbowCycle(led)

def get_anim(led, opts, args):

	anim_type = opts['--anim'].title()

	return {
		'Rainbow': build_rainbow(led, opts, args),
		'RainbowCycle': build_rainbow_cycle(led, opts, args)
	}[anim_type]


def main(argv):
	driver = DriverWS2801(num = 120)
	led = LEDStrip(driver)
	optlist, args = getopt.getopt(argv, "", [
		"anim=", "width=", "step=", "count=", "tail=", "cycles="])
	opts = dict(optlist)
	anim = get_anim(led, opts, args)
	anim.run()


if __name__ == "__main__":
    main(sys.argv[1:])
	

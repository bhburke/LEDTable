from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.WS2801 import DriverWS2801
from bibliopixel.led import *
from ast import literal_eval
import strip_animations
import bibliopixel.colors as colors
import random
import sys
import getopt

STRIP_LENGTH = 120

def randcolor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def build_rainbow(led, opts):
	return strip_animations.Rainbow(led)

def build_rainbow_cycle(led, opts):
	return strip_animations.RainbowCycle(led)

def build_color_pattern(led, opts):
	colors = literal_eval(opts.get('--colors')) if opts.get('--colors') else [randcolor() for i in range(random.randint(2,6))]
	width = int(opts.get('--width')) if opts.get('--width') else random.randint(3, int(STRIP_LENGTH/len(colors)))
	return strip_animations.ColorPattern(led, colors, width)

def build_color_fade(led, opts):
	colors = literal_eval(opts.get('--colors')) if opts.get('--colors') else [randcolor() for i in range(random.randint(2,6))]
	steps = int(opts.get('--steps')) if opts.get('--steps') else 5
	return strip_animations.ColorFade(led, colors, steps)

def build_color_wipe(led, opts):
	color = literal_eval(opts.get('--color')) if opts.get('--color') else randcolor()
	return strip_animations.ColorWipe(led, color)

def build_color_chase(led, opts):
	color = literal_eval(opts.get('--color')) if opts.get('--color') else randcolor()
	return strip_animations.ColorChase(led, color)

def build_party_mode(led, opts):
	colors = literal_eval(opts.get('--colors')) if opts.get('--colors') else [randcolor() for i in range(random.randint(2,6))]
	return strip_animations.PartyMode(led, colors)

def build_fireflies(led, opts):
	colors = literal_eval(opts.get('--colors')) if opts.get('--colors') else [randcolor() for i in range(random.randint(2,6))]
	width = int(opts.get('--width')) if opts.get('--width') else random.randint(1, 10)
	count = int(opts.get('--count')) if opts.get('--count') else random.randint(1, 10)
	return strip_animations.FireFlies(led, colors, width, count)

def build_larson_scanner(led, opts):
	color = literal_eval(opts.get('--color')) if opts.get('--color') else randcolor()
	tail = int(opts.get('--tail')) if opts.get('--tail') else random.randint(2, 30)
	return strip_animations.LarsonScanner(led, color, tail)

def build_larson_rainbow(led, opts):
	tail = int(opts.get('--tail')) if opts.get('--tail') else random.randint(2, 30)
	return strip_animations.LarsonRainbow(led, tail)

def build_wave(led, opts):
	color = literal_eval(opts.get('--color')) if opts.get('--color') else randcolor()
	cycles = int(opts.get('--cycles')) if opts.get('--cycles') else random.randint(2, 50)
	return strip_animations.Wave(led, color, cycles)

def build_wave_move(led, opts):
	color = literal_eval(opts.get('--color')) if opts.get('--color') else randcolor()
	cycles = int(opts.get('--cycles')) if opts.get('--cycles') else random.randint(2, 50)
	return strip_animations.WaveMove(led, color, cycles)


def get_anim(led, opts):
	anim_type = opts.get('--anim').lower()

	anim, args = {
		'rainbow': (build_rainbow, (led, opts,)),
		'rainbowcycle': (build_rainbow_cycle, (led, opts,)),
		'colorpattern': (build_color_pattern, (led, opts,)),
		'colorfade': (build_color_fade, (led, opts,)),
		'colorwipe': (build_color_wipe, (led, opts,)),
		'colorchase': (build_color_chase, (led, opts,)),
		'partymode': (build_party_mode, (led, opts,)),
		'fireflies': (build_fireflies, (led, opts,)),
		'larsonscanner': (build_larson_scanner, (led, opts,)),
		'larsonrainbow': (build_larson_rainbow, (led, opts,)),
		'wave': (build_wave, (led, opts,)),
		'wavemove': (build_wave_move, (led, opts,)),
	}.get(anim_type)

	return anim(*args)

def get_driver(opts):
	driver_type = opts.get('--driver').lower() if opts.get('--driver') else 'ws2801'
	driver, args = {
		'visualizer': (DriverVisualizer, (STRIP_LENGTH,)),
		'ws2801': (DriverWS2801, (STRIP_LENGTH,))
	}[driver_type]
	return driver(*args)

def main(argv):
	optlist, args = getopt.getopt(argv, "", [
		"anim=", "width=", "step=", "count=", "tail=", "cycles=","color=","colors=", "driver="])
	opts = dict(optlist)

	driver = get_driver(opts)
	led = LEDStrip(driver)

	anim = get_anim(led, opts)
	anim.run(max_steps=900)


if __name__ == "__main__":
    main(sys.argv[1:])
	

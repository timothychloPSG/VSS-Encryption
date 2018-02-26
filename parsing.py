import sys
import argparse
import numpy
from PIL import Image

parser = argparse.ArgumentParser(description = 'Runs VSS-encryption')
parser.add_argument('-e', help = 'encrypt', action = 'store_true', default = False)
parser.add_argument('-d', help = 'decrypt', action = 'store_true', default = False)
parser.add_argument('-i', help = 'input file', nargs = 1)
parser.add_argument('-o', help = 'output file (if not specified, stdout)', nargs = 1)
args = parser.parse_args()

def image_to_bits(image):
	print "Image info:"
	print "Number of bits:", image.bits, " Image size:", image.size, " Image format:", image.format
	image.show()

	return list(image.convert("1").getdata())
	

def print_bit_array(image, data):	
	count = 0
	for bit in data:
		count += 1

		if count % image.size[1] == 0:
			print bit/255

		else:
			print bit/255,
	

if __name__ == '__main__':

	if args.i:
		inp = Image.open(args.i[0])
		image_to_bits(inp)

	# if args.i and args.o:
	# 	inp = Image.open(args.i[0])
	# 	out = Image.open(args.o[0])

	# 	stackImages(inp, out)


		


	
import sys
import argparse
import numpy
import os 
import io 
import scipy.misc
from array import array
from PIL import Image

parser = argparse.ArgumentParser(description = 'Runs VSS-encryption')
#parser.add_argument('-e', help = 'encrypt', action = 'store_true', default = False)
#parser.add_argument('-d', help = 'decrypt', action = 'store_true', default = False)
parser.add_argument('-i', help = 'input file', nargs = 1)
parser.add_argument('-o', help = 'output file (if not specified, stdout)', nargs = 1)
parser.add_argument('-p', help = 'Print out the bit array', action = 'store_true', default = False)
args = parser.parse_args()


def image_to_bits(image):
	print 	"Image info:"
	print 	"""Number of bits: %d,  Image Size: %s,  Image format: %s""" %(image.bits, image.size, image.format)
	image.show()
	return 	list(image.convert("1").getdata())


def print_image(image):
	image.show()
	

def print_bit_array(image, data):	
	count = 0
	for bit in data:
		count += 1

		if count % image.size[1] == 0:
			print bit/255

		else:
			print bit/255,


def flip_bits(bits):
# Flips bits for KofK peoples (1 is black and 0 is white)
	for x in range(len(bits)):
		if bits[x] == 255:
			bits[x] = 0
		else:
			bits[x] = 255


def paste_images(background, foreground):
# Pastes foreground image on background
	return Image.alpha_composite(background, foreground).save("stacked-img.png")


if __name__ == '__main__':
	if args.i:
		inp = Image.open(args.i[0])										# Open image
		out = image_to_bits(inp)										# Convert to bits
		flip_bits(out)
		if args.p:														# Print the bit array
			print_bit_array(inp, out) 									
		data = numpy.array(out).reshape(inp.size[0], inp.size[1])		# Convert bits to image
		if args.o: 
			scipy.misc.imsave(args.o[0], data)							# Save the file
		else:
			scipy.misc.imsave("output.jpg", data)						# Print file to stdout
			inp = Image.open("output.jpg")
			print_image(inp)


	# if args.i and args.o:
	# 	inp = Image.open(args.i[0])
	# 	out = Image.open(args.o[0])

	# 	stackImages(inp, out)


		


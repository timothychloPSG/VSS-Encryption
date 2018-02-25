import argparse
import sys

parser = argparse.ArgumentParser(description = 'Runs RSA')
parser.add_argument('-e', help = 'encrypt', action = 'store_true', default = False)
parser.add_argument('-d', help = 'decrypt', action = 'store_true', default = False)
parser.add_argument('-i', help = 'input file', nargs = 1)
parser.add_argument('-o', help = 'output file (if not specified, stdout)', nargs = 1)
parser.add_argument('-g', help = 'generate a key of specific size; use with -o for base file name', nargs = 1)
parser.add_argument('-k', help = 'key file (required for encrypt, decrypt, sign, and verify)', nargs = 1)
parser.add_argument('-s', help = 'sign', action = 'store_true', default = False)
parser.add_argument('-v', help = 'verify', action = 'store_true', default = False)
args = parser.parse_args()

def main():
	print "hello minhanh"


if __name__ == '__main__':
	main()
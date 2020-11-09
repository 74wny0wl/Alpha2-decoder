import argparse


def create_args_parser():
    parser = argparse.ArgumentParser(description='Decoder for shellcodes generated with Alpha2-encoder')

    parser.add_argument('-u', action='store_true', help='unicode shellcode')

    parser.add_argument('-v', action='version', version='%(prog)s 1.0.0')

    return parser
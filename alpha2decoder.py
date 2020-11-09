#! /usr/bin/python3

import random
import fileinput

from utils import argparsers

def decode(payload, unicode):
    shellcode = []
    for i in range(0, len(payload)-1, 2) :
        X = ord(payload[i])
        Y = ord(payload[i+1])
        C = X & 0xF0
        D = X & 0x0F
        E = (Y & 0xF0) >> 4
        F = Y & 0x0F
        B = F
        
        if unicode:
            A = (((D+E) & 0x0F) << 4)    
        else:
            A = (((D^E) & 0x0F) << 4)
        character = A|B
        shellcode.append(character)
    shellcode = bytes(shellcode).hex()
    return shellcode

#valid_chars = "0123456789BCDEFGHIJKLMNOPQRSTUVWXYZ"
valid_chars = "0123456789BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def main():
    args_parser = argparsers.create_args_parser()
    script_args = args_parser.parse_args()
    payload = input()
    shellcode = decode(payload, script_args.u)
    print(shellcode)
if __name__ == "__main__":
    main()  
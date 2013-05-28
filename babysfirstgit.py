#!/usr/bin/env python3

from __future__ import print_function

import sys
def get_input(prompt):
    if sys.hexversion > 0x03000000:
        return input(prompt)
    else:
        return raw_input(prompt)

name = get_input("What's your name? ")

print(''.join(["Welcome to github, ", name, "!"]))



#!/usr/bin/env python3
"""
Terminal ASCII Art Portrait
A stylized portrait with ANSI colors rendered in the terminal.
"""

import sys
import time

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"

# Skin tones
SKIN    = "\033[38;5;173m"   # warm tan
SKIN_D  = "\033[38;5;130m"   # darker skin shadow
SKIN_L  = "\033[38;5;216m"   # highlight

# Hair
HAIR    = "\033[38;5;234m"   # very dark hair
HAIR_G  = "\033[38;5;102m"   # grey/silver strands
WHITE   = "\033[38;5;255m"

# Eyes / features
EYE     = "\033[38;5;232m"
BEARD   = "\033[38;5;240m"   # dark beard
BEARD_G = "\033[38;5;145m"   # grey beard patches

# Jacket / clothes
JACKET  = "\033[38;5;234m"   # near black
JACKET2 = "\033[38;5;236m"
SHIRT   = "\033[38;5;253m"   # off-white inner shirt
GLASS   = "\033[38;5;232m"   # sunglasses dark
GLASS_F = "\033[38;5;238m"   # frame

# Background
BG      = "\033[38;5;108m"   # muted green foliage BG

def c(color, text):
    return f"{color}{text}{RESET}"

portrait = [
    # Row 0 - top bg + hair starts
    f"  {c(BG,'~~~~~')}  {c(HAIR,BOLD+'▄▄███▄▄')}  {c(HAIR_G,'▄▄')}  {c(BG,'~~~~~')}  ",
    # Row 1 - hair sweep
    f" {c(BG,'~~~~')} {c(HAIR,BOLD+'▄████████▄▄')} {c(HAIR_G,'▄█▄')} {c(BG,'~~~')} ",
    # Row 2 - hair top full
    f"{c(BG,'~~~')} {c(HAIR,BOLD+'██████████████')} {c(HAIR_G,'██')} {c(BG,'~~')} ",
    # Row 3 - forehead begins
    f"{c(BG,'~~')} {c(HAIR,BOLD+'████')} {c(SKIN,'▄████████')} {c(HAIR,'████')} {c(BG,'~')} ",
    # Row 4 - upper face
    f"{c(BG,'~')} {c(HAIR,'███')} {c(SKIN_L,'▄')} {c(SKIN,'███████████')} {c(HAIR,'███')} {c(BG,'~')}",
    # Row 5 - eyes level
    f"{c(BG,'~')} {c(HAIR,'██')} {c(SKIN,'██')} {c(EYE,'◕')} {c(SKIN,'████')} {c(EYE,'◕')} {c(SKIN,'███')} {c(HAIR,'██')} ",
    # Row 6 - nose bridge
    f"  {c(HAIR,'██')} {c(SKIN,'███')} {c(SKIN_D,'▄')} {c(SKIN,'███████')} {c(HAIR,'██')}  ",
    # Row 7 - nose
    f"  {c(HAIR,'█')} {c(SKIN,'███')} {c(SKIN_D,'▄██▄')} {c(SKIN,'██████')} {c(HAIR,'█')}   ",
    # Row 8 - upper lip / moustache
    f"   {c(SKIN,'███')} {c(BEARD,'▄▄▄▄▄▄▄▄▄▄▄')} {c(SKIN,'██')}    ",
    # Row 9 - mouth
    f"   {c(SKIN,'██')} {c(BEARD,'█')} {c(SKIN,'▄▀▀▀▀▀▀▀▀▄')} {c(BEARD,'█')} {c(SKIN,'█')}    ",
    # Row 10 - smile
    f"   {c(SKIN,'██')} {c(BEARD,'█')} {c(SKIN,'█')} {c(WHITE,'◡◡◡◡◡◡')} {c(SKIN,'█')} {c(BEARD,'█')} {c(SKIN,'█')}    ",
    # Row 11 - chin beard
    f"   {c(SKIN,'█')} {c(BEARD,'██')} {c(BEARD_G,'▄▄')} {c(BEARD,'███')} {c(BEARD_G,'▄▄')} {c(BEARD,'██')} {c(SKIN,'█')}    ",
    # Row 12 - lower beard / jaw
    f"   {c(SKIN,'▀')} {c(BEARD,'████')} {c(BEARD_G,'▄▄▄▄')} {c(BEARD,'████')} {c(SKIN,'▀')}    ",
    # Row 13 - chin bottom
    f"     {c(BEARD,'▀███████████▀')}       ",
    # Row 14 - neck
    f"       {c(SKIN,'▄███▄')} {c(SKIN_D,'▄')} {c(SKIN,'███▄')}        ",
    # Row 15 - collar / sunglasses
    f"     {c(JACKET,'▄▄')} {c(SKIN,'██')} {c(SHIRT,'████')} {c(SKIN,'██')} {c(JACKET,'▄▄')}      ",
    # Row 16 - sunglasses on collar
    f"    {c(JACKET,'█▀')} {c(SHIRT,'████')} {c(GLASS_F,'╔')} {c(GLASS,'██')} {c(GLASS_F,'╗')} {c(SHIRT,'████')} {c(JACKET,'▀█')}     ",
    # Row 17 - jacket shoulder
    f"   {c(JACKET,'██')} {c(SHIRT,'█████')} {c(GLASS,'▐▌')} {c(SHIRT,'████')} {c(JACKET,'██')}     ",
    # Row 18 - jacket body
    f"  {c(JACKET,'████')} {c(SHIRT,'██████████████')} {c(JACKET,'████')}    ",
    # Row 19 - jacket lower
    f" {c(JACKET,'██████')} {c(SHIRT,'████████████')} {c(JACKET,'██████')}   ",
    # Row 20 - bottom
    f"{c(JACKET,'████████████████████████████████')}  ",
]

def print_portrait():
    print()
    # Title
    title = "  ✦  ASCII PORTRAIT  ✦  "
    print(f"\033[38;5;215m{BOLD}{title:^36}{RESET}")
    print(f"\033[38;5;238m{'─' * 36}{RESET}")
    print()
    for i, row in enumerate(portrait):
        sys.stdout.write(f"  {row}\n")
        sys.stdout.flush()
        time.sleep(0.04)   # animate drawing line by line
    print()
    print(f"\033[38;5;238m{'─' * 36}{RESET}")
    credit = "  rendered in Python  •  ANSI terminal art"
    print(f"\033[38;5;102m{credit}{RESET}")
    print()

if __name__ == "__main__":
    print_portrait()
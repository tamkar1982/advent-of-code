#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5fbf5531c6408939283a4fd41b8709f8362e0269f211c671ebdba2c915f3c4cdd68a515e5a1ec300e4634c26888bedfdb6fdb647f7536e3545'

useragent = 'https://github.com/tamkar1982/advent-of-code/blob/master/get_input.py'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A {useragent}'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')

with open(rf"C:/Users/tkarakay/Desktop/GitHub/advent-of-code/inputs/day{args.day}_input.txt", "w") as f:
	f.write(output)
	f.close()
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)

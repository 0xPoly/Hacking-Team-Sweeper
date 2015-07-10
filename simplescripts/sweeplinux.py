#!/usr/bin/python2.7

# sweeplinux v0.1: a simple script to look for signs of HackingTeam RCS Linux agent
# gsteenss@riseup.net
#
# based on: https://github.com/0xPoly/Hacking-Team-Sweeper/blob/master/signatures/linux.md


import glob
import sys
from platform import platform,architecture
from os.path import expanduser

whoopsie=expanduser('~/.whoopsie*')
crashreports='/var/crash/.reports-*-*'
tmpreports='/var/tmp/.reports-*-*'


#print(sys.version,platform(),architecture())
ok=True

if glob.glob(whoopsie)!=[]: 
  print('WARNING: Detected HT whoopsie file in home directory, Your computer may be infected with a version of HackingTeam RCS Agent!')
  ok=False
  
if glob.glob(crashreports)!=[]:
  print('WARNING: Detected HT crash reports, Your computer may be infected with a version of HackingTeam RCS Agent!')
  ok=False
  
if glob.glob(tmpreports)!=[]:
  print('WARNING: Detected HT tmp reports, Your computer may be infected with a version of HackingTeam RCS Agent!')
  ok=False


if ok: 
  print('OK: Nothing strange to report.')
else: 
  print('Please shutdown your network connection NOW!')



#!/usr/bin/python2.7

# sweepandroid v.01: a simple script to look for signs of HackingTeam RCS Agent on Android devices
# gsteenss@riseup.net
#
# also see: https://github.com/0xPoly/Hacking-Team-Sweeper/blob/master/signatures/android.md

#    android version: RCSAndroid removes a specific file as root when uninstalling: /system/app/StkDevice.apk
#        source: https://github.com/hackedteam/core-android/blob/master/RCSAndroid/src/com/android/dvci/action/UninstallAction.java#L109
#
#    android exploit writes 'shell' file to /system/bin/ntpsvd
#        source: https://github.com/hackedteam/core-android/blob/master/RCSAndroid/jni/exploit.c#L739



import glob
import sys
from platform import platform,architecture
import androidhelper


app='/system/app/StkDevice.apk'
shell='/system/bin/ntpsvd'


ok=True

#print(sys.version,platform(),architecture())

droid=androidhelper.Android()

if glob.glob(app)!=[]:
  droid.makeToast('WARNING: HT apk present: Your phone may be infected with a version of HackingTeam RCS Agent!')
  ok=False
  
if glob.glob(shell)!=[]:
  droid.makeToast('WARNING: HT shell present: Your phone may be infected with a version of HackingTeam RCS Agent!')
  ok=False

if ok: 
  droid.makeToast('OK: Nothing strange to report.')

  



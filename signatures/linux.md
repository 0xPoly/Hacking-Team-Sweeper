Linux Signatures
================

* Files matching the patterns "/var/crash/.reports-%u-%s" or "/var/tmp/.reports-%u-%s" 
  * original report: https://twitter.com/matalaz/status/618100209835503622
  * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L1268

* Run this command: find ~/.config/autostart -name '.whoopsie*'
  * source: https://github.com/hackedteam/core-linux/blob/master/dropper/src/dropper.c
  * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L1288
   
* Same scramble_name function for hiding logfile names as seen for Windows is used in offline installer for Max/Linux
   * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L2604
   * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L2716


Linux Signatures
================

* Files matching the patterns "/var/crash/.reports-%u-%s" or "/var/tmp/.reports-%u-%s" 
  * source: https://github.com/hackedteam/core-linux/blob/9252cba42283e71d7858292a400f6c94043ee8ff/dropper/src/dropper.c#L146
  * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L1268

* Run this command: find ~/.config/autostart -name '.whoopsie*'

  * source https://github.com/hackedteam/core-linux/blob/master/dropper/src/dropper.c
  * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L1288

* Same scramble_name function for hiding logfile names as seen for Windows is used in offline installer for Mac/Linux
   * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L2604
   * source: https://github.com/hackedteam/vector-offline2/blob/master/offline-linux/offline-install/offline_gui.py#L2716

* config file for linux version is '.cache' (located in the whoopsie directory)
  * source: https://github.com/hackedteam/core-linux/blob/master/core/src/core.c#L123

* params.h and params.c file contain keys for decrypting config file and watermark information:
  * source: https://github.com/hackedteam/core-linux/blob/master/core/src/params.h

* config file is encrypted with aes-128-cbc and confkey from params (iv=0)
  * source: https://github.com/hackedteam/core-linux/blob/master/core/src/config.c#L48

* core-linux agent creates encrypted 'evidence' files (ie: stolen data) with the following format:
     .tmp-AAAAAAAAAA-BBBBBB-CCCCCC where
      AAAAAAAAAA : number of seconds since unix epoch from gettimeofday()
      BBBBBB : microseconds from gettimeofday()
      CCCCCC : random letters/numbers from mkstemp() function
  comparing AAAAAAAAAA with the file's modification time from unix stat() function would give high reliability in identifying them

  source: https://github.com/hackedteam/core-linux/blob/master/core/src/evidencemanager.c#L60

Windows Signatures
=================

* Windows Soldier Updater writes file with distinct signature: "SOLDIEROSOLDIEROSOLDIEROSOLDIERO" 

  * source: https://github.com/hackedteam/soldier-win/blob/master/Updater/main.cpp line 43
  * Windows Soldier Features in Knowledgebase: http://ht.transparencytoolkit.org/KnowledgeBase/Windows%20-%20Soldier%20Feature%20Compatibility%209.6%20-%20%5DHT%5B%20%3a%3a%20KnowledgeBase%20Product.html

  
* core-win32: scrambles logfile names and config files with a simple substituion of chars from 2 alphabets, scanning for filenames which only include these chars maybe help in detecting an install.  
  * source: https://github.com/hackedteam/core-win32/blob/master/LOG.cpp#L559
  * and : https://github.com/hackedteam/core-win32/blob/master/LOG.cpp#L591
  


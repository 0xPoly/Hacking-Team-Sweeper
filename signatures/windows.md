Windows Signatures
=================

* Windows Soldier Updater writes file with distinct signature: "SOLDIEROSOLDIEROSOLDIEROSOLDIERO" 

  * source: https://github.com/hackedteam/soldier-win/blob/master/Updater/main.cpp line 43
  * Windows Soldier Features in Knowledgebase: http://ht.transparencytoolkit.org/KnowledgeBase/Windows%20-%20Soldier%20Feature%20Compatibility%209.6%20-%20%5DHT%5B%20%3a%3a%20KnowledgeBase%20Product.html


* core-win32 scambles log filenames and config files with a simple substitution of characters from two alphabets, scanning for filesname which only have these characters may help in detecting an install.
  * source: https://github.com/hackedteam/core-win32/blob/master/LOG.cpp#L559 
    and: https://github.com/hackedteam/core-win32/blob/master/LOG.cpp#L591 

* Soldier/scout file binpath.h has configuration for various keys: client_key,encr_key backdoor_id and watermark
    * source: https://github.com/hackedteam/soldier-win/blob/master/Soldier/binpatch.h
  The watermarker is later used to check for presence of existing install via sharedmemory resource
    * source: https://github.com/hackedteam/soldier-win/blob/master/Soldier/utils.cpp#L87

* core-win32 encryption keys/watermark/backdoor_id are defined in common.h 
    * source: https://github.com/hackedteam/core-win32/blob/master/common.h#L100
    

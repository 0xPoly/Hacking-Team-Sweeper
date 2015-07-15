Network Signatures
=================

* RCS downloader connects to http://[address1]/gh/3735928545/deadbee2  and http://[address2]/gh/3735928545/deadbee2over HTTP port 80. [address1] and [address2] are hardcoded.
* User Agent : Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11

  * source: https://github.com/hackedteam/vector-recover/blob/master/download_exec.cpp


* Windows Soldier & Scout version.h file define different user agents (and urls) for each RCS version:

  source: https://github.com/hackedteam/soldier-win/blob/master/Soldier/version.h#L22
  source: https://github.com/hackedteam/scout-win/blob/master/core-scout-win32/version.h#L33

* HT client wiki reveals several IP addresses of RCS anonymizers and control servers for a specific install which can be used for network detection 






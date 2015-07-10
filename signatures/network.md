Network Signatures: ways to detect network traffic?
==================================================
 

* HT client wiki has revealed several IP addresses of RCS anonymizers and control servers: these may be used to detect network traffic?

* RCS agent connects to http://[HOST]/index.html over HTTP port 80 and encrypts data. [HOST] is configured in its (encrypted) config file
  * source: https://github.com/hackedteam/core-linux/blob/master/core/src/am_synchronize.c#L262

* RCS anonymizer looks for a certain cookie in data received to forward requests, and send response with same cookie 
  * source: https://github.com/hackedteam/rcs-anonymizer/blob/master/src/bbproxy-proxy.c#L89
  * source: https://github.com/hackedteam/rcs-anonymizer/blob/master/src/bbproxy-proxy.c#L369




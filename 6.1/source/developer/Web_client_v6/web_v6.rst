.. _web_v6:

================
OpenERP Web v6.0
================

Introduction
============

**Web Client – A software application that is launched via a web browser.**

With the launch of OpenERP v6, a new web client has been designed and developed, 
which provides a more professional appearance than OpenERP v5.

We migrated the web client to CherryPy3 dropping TurboGears completely
and migrated kid templates to faster Mako templates, a major step towards making
the Web Client much faster and easier to deploy.
	
All the Kid templates were converted to faster Mako templates, i18n/l18n features
have been partially reimplemented using Python Babel, CherryPy2 (TG is built on 
top of CP2) was replaced with CherryPy3, the latest, much better version of 
CherryPy Server.

This greatly reduces the pain of getting started with and deploying of OpenERP Web client.

Now the number of third party dependencies are reduced to 3-4 pure Python libraries which 
you can install within the local lib dir with the help of `populate.sh` script, found under 
the same lib directory.
	
-	Just get the source from Launchpad, run the **populate.sh** and launch the web client...

The initial test results are very impressive.

We have seen 3-5 times speed improvement.

Against OpenERP Web 5.0
=======================

Here are the benchmark results of the latest stable 6.0 version against the stable 5.0 branch which is running over TurboGears.

The benchmark test used Apache Benchmark Tool against larger Customer Invoice Form view.


.. csv-table::
	:header: "Result of OpenERP Web 5.0 (TurboGears + Kid)","Result of OpenERP Web 6.0 (CherryPy3 + Mako)"
	:widths: 50,50
	
	"This is ApacheBench, Version 2.3 <$Revision: 655654 $>","This is ApacheBench, Version 2.3 <$Revision: 655654 $>"
	"Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/","Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/"
	"Licensed to The Apache Software Foundation, http://www.apache.org/","Licensed to The Apache Software Foundation, http://www.apache.org/"
	"Benchmarking localhost (be patient).....done","Benchmarking localhost (be patient).....done"
	"Server Software: CherryPy/2.3.0","Server Software: CherryPy/3.1.2"
	"Server Hostname: localhost","Server Hostname: localhost"
	"Server Port: 8081","Server Port: 8080"
	"Document Path: /form/edit?model=account.invoice&id=1","Document Path: /form/edit?model=account.invoice&id=1"
	"Document Length: 79965 bytes","Document Length: 90394 bytes"
	"Concurrency Level: 1","Concurrency Level: 1"
	"Time taken for tests: 166.323 seconds","Time taken for tests: 42.054 seconds"
	"Complete requests: 100","Complete requests: 100"
	"Failed requests: 0","Failed requests: 0"
	"Write errors: 0","Write errors: 0"
	"Total transferred: 8022000 bytes","Total transferred: 9063400 bytes"
	"HTML transferred: 7996500 bytes","HTML transferred: 9039400 bytes"
	"Requests per second: 0.60 [#/sec] (mean)","Requests per second: 2.38 [#/sec] (mean)"
	"Time per request: 1663.228 [ms] (mean, across all concurrent requests)","Time per request: 420.543 [ms] (mean, across all concurrent requests)"
	"Transfer rate: 47.10 [Kbytes/sec] received","Transfer rate: 210.47 [Kbytes/sec] received"
	"**Connection Times (ms)**","**Connection Times (ms)**"
	"min mean[+/-sd] median max","min mean[+/-sd] median max"
	"Connect: 0 0 0.0 0 0","Connect: 0 0 0.0 0 0"
	"Processing: 1556 1663 71.3 1663 1856","Processing: 1556 1663 71.3 1663 1856"
	"Waiting: 1555 1662 71.3 1662 1855","Waiting: 381 420 27.7 415 522"
	"Total: 1556 1663 71.3 1663 1856","Total: 382 420 27.7 416 523"
	"**Percentage of the requests served within a certain time (ms)**","**Percentage of the requests served within a certain time (ms)**"
	"50% 1663","50% 416"
	"66% 1681","66% 418"
	"75% 1695","75% 420"
	"80% 1715","80% 424"
	"90% 1775","90% 436"
	"95% 1801","95% 512"
	"98% 1829","98% 520"
	"99% 1856","99% 523"
	"100% 1856 (longest request)","100% 523 (longest request)"
	

Conclusion
==========
-	You can see significant performance boost in second test result. 
-	We observed 3-5 times speedup. 
-	There is still room to improve the performance further.
-	Like reducing RPC calls, catching results of some computationally heavy functions.


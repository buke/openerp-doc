.. i18n: .. _web_v6:
.. i18n: 
.. i18n: ================
.. i18n: OpenERP Web v6.0
.. i18n: ================
..

.. _web_v6:

================
OpenERP Web v6.0
================

.. i18n: Introduction
.. i18n: ============
..

介绍
============

.. i18n: **Web Client – A software application that is launched via a web browser.**
..

**Web Client – 一个软件应用程序通过一个web浏览器中启动.**

.. i18n: With the launch of OpenERP v6, a new web client has been designed and developed, 
.. i18n: which provides a more professional appearance than OpenERP v5.
..

推出OpenERP v6,一个新的web客户端进行设计和开发, 
它提供了一个更专业的形象 than OpenERP v5.

.. i18n: We migrated the web client to CherryPy3 dropping TurboGears completely
.. i18n: and migrated kid templates to faster Mako templates, a major step towards making
.. i18n: the Web Client much faster and easier to deploy.
.. i18n: 	
.. i18n: All the Kid templates were converted to faster Mako templates, i18n/l18n features
.. i18n: have been partially reimplemented using Python Babel, CherryPy2 (TG is built on 
.. i18n: top of CP2) was replaced with CherryPy3, the latest, much better version of 
.. i18n: CherryPy Server.
..

我们迁移web客户端来CherryPy3滴TurboGears完全和迁移的孩子模板来更快的尖吻鲭鲨模板,
一个重大步骤使web客户端更快和更容易部署。
	
All the Kid templates were converted to faster Mako templates, i18n/l18n features
have been partially reimplemented using Python Babel, CherryPy2 (TG is built on 
top of CP2) was replaced with CherryPy3, the latest, much better version of 
CherryPy Server.

.. i18n: This greatly reduces the pain of getting started with and deploying of OpenERP Web client.
..

这大大减少了使用和部署OpenERP Web client的难度.

.. i18n: Now the number of third party dependencies are reduced to 3-4 pure Python libraries which 
.. i18n: you can install within the local lib dir with the help of `populate.sh` script, found under 
.. i18n: the same lib directory.
.. i18n: 	
.. i18n: -	Just get the source from Launchpad, run the **populate.sh** and launch the web client...
..

Now the number of third party dependencies are reduced to 3-4 pure Python libraries which 
you can install within the local lib dir with the help of `populate.sh` script, found under 
the same lib directory.
	
-	仅需要从 Launchpad 获取源码后, 运行 **populate.sh** 就可以完成 web client 的启动...

.. i18n: The initial test results are very impressive.
..

	整个测试效果会让你惊叹!.

.. i18n: We have seen 3-5 times speed improvement.
..

一般3-5次后的提速效果就很明显了.

.. i18n: Against OpenERP Web 5.0
.. i18n: =======================
..

弥补 OpenERP Web 5.0 不足
===========================

.. i18n: Here are the benchmark results of the latest stable 6.0 version against the stable 5.0 branch which is running over TurboGears.
..

下面是 6.0 版与 5.0 版就web性能方面做的测试报告:

.. i18n: The benchmark test used Apache Benchmark Tool against larger Customer Invoice Form view.
..

使用 Apache ap.exe 工具对处理大量的 客户发票表单为例做性能测试.

.. i18n: .. csv-table::
.. i18n: 	:header: "Result of OpenERP Web 5.0 (TurboGears + Kid)","Result of OpenERP Web 6.0 (CherryPy3 + Mako)"
.. i18n: 	:widths: 50,50
.. i18n: 	
.. i18n: 	"This is ApacheBench, Version 2.3 <$Revision: 655654 $>","This is ApacheBench, Version 2.3 <$Revision: 655654 $>"
.. i18n: 	"Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/","Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/"
.. i18n: 	"Licensed to The Apache Software Foundation, http://www.apache.org/","Licensed to The Apache Software Foundation, http://www.apache.org/"
.. i18n: 	"Benchmarking localhost (be patient).....done","Benchmarking localhost (be patient).....done"
.. i18n: 	"Server Software: CherryPy/2.3.0","Server Software: CherryPy/3.1.2"
.. i18n: 	"Server Hostname: localhost","Server Hostname: localhost"
.. i18n: 	"Server Port: 8081","Server Port: 8080"
.. i18n: 	"Document Path: /form/edit?model=account.invoice&id=1","Document Path: /form/edit?model=account.invoice&id=1"
.. i18n: 	"Document Length: 79965 bytes","Document Length: 90394 bytes"
.. i18n: 	"Concurrency Level: 1","Concurrency Level: 1"
.. i18n: 	"Time taken for tests: 166.323 seconds","Time taken for tests: 42.054 seconds"
.. i18n: 	"Complete requests: 100","Complete requests: 100"
.. i18n: 	"Failed requests: 0","Failed requests: 0"
.. i18n: 	"Write errors: 0","Write errors: 0"
.. i18n: 	"Total transferred: 8022000 bytes","Total transferred: 9063400 bytes"
.. i18n: 	"HTML transferred: 7996500 bytes","HTML transferred: 9039400 bytes"
.. i18n: 	"Requests per second: 0.60 [#/sec] (mean)","Requests per second: 2.38 [#/sec] (mean)"
.. i18n: 	"Time per request: 1663.228 [ms] (mean, across all concurrent requests)","Time per request: 420.543 [ms] (mean, across all concurrent requests)"
.. i18n: 	"Transfer rate: 47.10 [Kbytes/sec] received","Transfer rate: 210.47 [Kbytes/sec] received"
.. i18n: 	"**Connection Times (ms)**","**Connection Times (ms)**"
.. i18n: 	"min mean[+/-sd] median max","min mean[+/-sd] median max"
.. i18n: 	"Connect: 0 0 0.0 0 0","Connect: 0 0 0.0 0 0"
.. i18n: 	"Processing: 1556 1663 71.3 1663 1856","Processing: 1556 1663 71.3 1663 1856"
.. i18n: 	"Waiting: 1555 1662 71.3 1662 1855","Waiting: 381 420 27.7 415 522"
.. i18n: 	"Total: 1556 1663 71.3 1663 1856","Total: 382 420 27.7 416 523"
.. i18n: 	"**Percentage of the requests served within a certain time (ms)**","**Percentage of the requests served within a certain time (ms)**"
.. i18n: 	"50% 1663","50% 416"
.. i18n: 	"66% 1681","66% 418"
.. i18n: 	"75% 1695","75% 420"
.. i18n: 	"80% 1715","80% 424"
.. i18n: 	"90% 1775","90% 436"
.. i18n: 	"95% 1801","95% 512"
.. i18n: 	"98% 1829","98% 520"
.. i18n: 	"99% 1856","99% 523"
.. i18n: 	"100% 1856 (longest request)","100% 523 (longest request)"
.. i18n: 	
..

.. csv-table::
	:header: "OpenERP Web 5.0 (TurboGears + Kid)","OpenERP Web 6.0 (CherryPy3 + Mako)"
	:widths: 50,50
	
	"ApacheBench工具, 版本 2.3 <内部版本: 655654>","ApacheBench工具, 版本 2.3 <内部版本: 655654>"
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
	

.. i18n: Conclusion
.. i18n: ==========
.. i18n: -	You can see significant performance boost in second test result. 
.. i18n: -	We observed 3-5 times speedup. 
.. i18n: -	There is still room to improve the performance further.
.. i18n: -	Like reducing RPC calls, catching results of some computationally heavy functions.
..

测试结果
==========
-	报告显示, 第二列的测试结果明显好于第一列. 
-	3-5次缓存加速明显. 
-	还有进一步提升性能的空间.
-	如还可以再减少一些RPC调用, 有一些获取结果后仍有一定量的冗余计算.

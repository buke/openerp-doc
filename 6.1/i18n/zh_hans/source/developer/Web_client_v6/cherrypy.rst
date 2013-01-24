.. i18n: .. _web_cherrypy:
.. i18n: 
.. i18n: ==================
.. i18n: What is Cherrypy ?
.. i18n: ==================
..

.. _web_cherrypy:

==================
Cherrypy 是嘛东西?
==================

.. i18n: CherryPy is a pythonic, object-oriented HTTP framework.
.. i18n:  
.. i18n: CherryPy allows developers to build web applications in much the same way they would build any other 
.. i18n: object-oriented Python program. This results in smaller source code developed in less time.
.. i18n: 	
.. i18n: ::
.. i18n: 
.. i18n: 	import cherrypy
.. i18n: 	class HelloWorld:
.. i18n: 	    def index(self):
.. i18n: 	        return "Hello World!"
.. i18n: 	    index.exposed = True
.. i18n: 	cherrypy.quickstart(HelloWorld())
..

CherryPy 是个典型的面向对象的 HTTP 开发框架.

CherryPy 可以让开发者可以象开发类似其他Python面向对象的程序那样简单并快速地去开发一个Web应用. 下面就是一个简单的例子:
	
::

	import cherrypy
	class HelloWorld:
	    def index(self):
	        return "Hello World!"
	    index.exposed = True
	cherrypy.quickstart(HelloWorld())

.. i18n: Start the application at the command prompt(after navigating to its folder):
.. i18n: 	**python hello.py**
.. i18n: 		
.. i18n: Direct your browser to http://localhost:8080
..

要运行这段代码, 只需要在命令行进入该代码文件夹, 运行下面的命令:
::

	python hello.py
		
然后 使用浏览器访问地址: http://localhost:8080

.. i18n: The rendering:
.. i18n: 	**Hello World!**
.. i18n: 		
.. i18n: ctrl+c in command window to terminate the application
..

浏览器上就显示出结果:
::

	Hello World!

这时, 在命令行窗口上按下 Ctrl+C 键便可以终止程序的运行.

.. i18n: Statement **import cherrypy** imports the main CherryPy module.
..


代码 **import cherrypy** 将引入 CherryPy 模块扩展.

.. i18n: An instance of class **HelloWorld** is the object that will be **published.**
..

**HelloWorld** 类的定义则会将完成类的方法的发布.

.. i18n: Method **index()** is called when the root URL for the site(e.g., http://localhost:8080) is requested, 
.. i18n: This method returns the **contents** of the Web page(the **'Hello World!'** string)
..

有一个必须定义的 **index()** 方法则默认为URL(如: http://localhost:8080)中的网站root, 该方法返回的字符串将做为网页中的 **内容** (如本例中的 **'Hello World!'**).

.. i18n: Statement **index.exposed = True** tells CherryPy that method **index()** will be exposed
..

代码 **index.exposed = True** 则表明 **index()** 方法是要开放出去的.

.. i18n: -	Only exposed methods can be called to answer a request
.. i18n: -	Lets the user to select which methods of an object are Web accessible
.. i18n: -	Can also place the decoration **@cherrypy.expose** immediately before the method:
..

-	只有开放出去的方法,才可以处理各种HTTP请求.
-	让开发人员自主控制对象的方法是否开放为Web请求更简单快捷.
-	在方法前使用代码 **@cherrypy.expose** 同样也能立即发布该方法:

.. i18n: ::
.. i18n: 
.. i18n: 	@cherrypy.expose
.. i18n: 	def index(self):
.. i18n: 	    return "Hello World!"
..

::

	@cherrypy.expose
	def index(self):
	    return "Hello World!"

.. i18n: Statement, **cherrypy.quickstart(HelloWorld())**
..

代码 **cherrypy.quickstart(HelloWorld())** 是将对象做为 CherryPy 的HTTP Handle 启动 CherryPy 的 Web 服务.

.. i18n: 	**publishes** an instance of the HelloWorld class
.. i18n: 	
.. i18n: 	-	And it starts the embedded webserver
.. i18n: 	-	Runs until explicitly interrupted(ctrl+c)
.. i18n: 	
.. i18n: When the application is executed, the CherryPy server is started with the default configuration
.. i18n: 	
.. i18n: -	Listening on **localhost**  at port **8080**
.. i18n: -	Defaults overriden by using a configuration file or dictionary
.. i18n: 	
.. i18n: 	-	**cherrypy.config.update({'server.socket_port':8010})**
.. i18n: 	-	Now it will run on port 8010.
.. i18n: 	
.. i18n: Webserver receives the request for URL http://localhost:8080 
..

	**发布** HelloWorld 类的实例
	
	-	启动内嵌 webserver 
	-	直到按(Ctrol+C)键结束运行
	
当应用运行时, CherryPy 是以默认配置运行的.
	
-	监听地址 **localhost**  监听端口 **8080**
-	这些默认值都可以使用配置文件进行覆盖修改
	
	-	**cherrypy.config.update({'server.socket_port':8010})**
	-	这样就将监听端口修改为8010了.
	
服务器的访问地址为: http://localhost:8080 

.. i18n: -	Searches for the best method to handle the request,starting from the **HelloWorld** instance
.. i18n: -	CherryPy calls **HelloWorld().index()**
.. i18n: -	Result of the call is sent back to the browser as the content of the index page for the website
..

-	从 **HelloWorld** 类中找最匹配的方法来处理Web请求.
-	调用 **HelloWorld().index()** 方法.
-	方法返回给请求用户的浏览器内显示.

.. i18n: Cherrypy Application Facts
.. i18n: ==========================
.. i18n: Your CherryPy powered web applications are in fact stand-alone Python applications embedding their 
.. i18n: own multi-threaded web server. You can deploy them anywhere you can run Python applications. 
.. i18n: Apache is not required, but it's possible to run a CherryPy application behind it (or lighttpd, or IIS). 
.. i18n: CherryPy applications run on Windows, Linux, Mac OS X and any other platform supporting Python. 
..

Cherrypy 应用实例
==========================
CherryPy 可以让你开发出内嵌Python标准应用多线程Web服务的强大的Web应用. 你可以在任何可以运行Python程序的环境下布曙它. 
并不需要Apache, 但你可以在Apache(或者 lightpd 甚至 IIS)中调用 CherryPy 应用. 
可以运行于 Windows, Linux, Max OS X 以及其他的支持 Python 语言的操作系统.

.. i18n: Beyond this functionality, CherryPy pretty much stays out of your way. You are free to use any kind of templating, 
.. i18n: data access etc. technology you want. CherryPy can also handle sessions, static files, cookies, file uploads and 
.. i18n: everything you would expect from a decent web framework. 
..

除此之外, CherryPy 还会原汁原味地保留你的应用. 你可以自由地使用各种各样的模板,数据存取等技术方案. 
CherryPy 也能处理诸如 Session, 静态文件, Cookie, 文件上传等几乎所有 Web 应用中涉及到的东西.

.. i18n: Features
.. i18n: ========
.. i18n: -	A **fast**, HTTP/1.1-compliant, WSGI thread-pooled webserver. Typically, CherryPy itself takes only 1-2ms per page!
.. i18n: -	Support for any other WSGI-enabled webserver or adapter, including Apache, IIS, lighttpd, mod_python, FastCGI, SCGI, and mod_wsgi 
.. i18n: -	Easy to run multiple HTTP servers (e.g. on multiple ports) at once
.. i18n: -	A powerful configuration system for developers and deployers alike
.. i18n: -	A flexible plugin system
.. i18n: -	Built-in tools for caching, encoding, sessions, authorization, static content, and many more
.. i18n: -	A native mod_python adapter 
.. i18n: -	A complete test suite 
.. i18n: -	Swappable and customisable... everything.
.. i18n: -	Built-in profiling, coverage, and testing support.
..

功能
========
-	**高效的**, 兼容HTTP/1.1, 支持 WSGI 线程池的webserver. 通常 CherryPy 处理页面本身耗时仅 1-2ms!
-	支持其他任何支持 WSGI 的webserver, 诸如 Apache, IIS, lighttpd, mod_python, FastCGI, SCGI, 和 mod_wsgi 等等.
-	多HTTP实例服务.
-	强大的开发与布曙配置系统.
-	灵活的扩展性能.
-	内建 缓存, 编码, SESSION, 身份认证, 静态化 等支持.
-	内置支持 mod_python .
-	完整的测试套件.
-	任意交互与定制.
-	Built-in profiling, coverage, and testing support.

.. i18n: Consider these examples (**root** is conceptual, referring to the root of the document tree),
.. i18n: 	**root = HelloWorld()**
.. i18n: 	
.. i18n: 	**root.onepage = OnePage()**
.. i18n: 	
.. i18n: 	**root.otherpage = OtherPage()**
..

Consider these examples (**root** is conceptual, referring to the root of the document tree),
	**root = HelloWorld()**
	
	**root.onepage = OnePage()**
	
	**root.otherpage = OtherPage()**

.. i18n: URL http://localhost:8080/onepage points at the 1st object,
..

URL http://localhost:8080/onepage points at the 1st object,

.. i18n: URL http://localhost:8080/otherpage points at the 2nd.
..

URL http://localhost:8080/otherpage points at the 2nd.

.. i18n: Consider,
.. i18n: 	**root.some = Page()**
.. i18n: 	
.. i18n: 	**root.some.page = Page()** 
..

Consider,
	**root.some = Page()**
	
	**root.some.page = Page()** 

.. i18n: URL http://localhost:8080/some/page  is mapped to the **root.some.page** object. 
.. i18n: If this object is exposed (or its **index** method is), it’s called for that URL
..

URL http://localhost:8080/some/page  is mapped to the **root.some.page** object. 
If this object is exposed (or its **index** method is), it’s called for that URL

.. i18n: In our HelloWorld example, adding the http://.../onepage to OnePage() mapping could be done as:
..

In our HelloWorld example, adding the http://.../onepage to OnePage() mapping could be done as:

.. i18n: ::
.. i18n: 
.. i18n: 	class OnePage():
.. i18n: 	    def index(self):
.. i18n: 	        return "one page!"
.. i18n: 	    index.exposed = True
.. i18n: 	class HelloWorld(object):
.. i18n: 	    onepage = OnePage()
.. i18n: 	    def index(self):
.. i18n: 	        return "hello world"
.. i18n: 	    index.exposed = True
.. i18n: 	cherrypy.quickstart(HelloWorld())
..

::

	class OnePage():
	    def index(self):
	        return "one page!"
	    index.exposed = True
	class HelloWorld(object):
	    onepage = OnePage()
	    def index(self):
	        return "hello world"
	    index.exposed = True
	cherrypy.quickstart(HelloWorld())

.. i18n: In the address bar of the browser, put http://localhost:8080/onepage 
..

In the address bar of the browser, put http://localhost:8080/onepage 

.. i18n: The Index Method
.. i18n: ================
.. i18n: -	Method **index()**, like the **index.html** file, is the default page for any internal node in the object tree
.. i18n: -	Can take additional keyword arguments, mapped to the form variables as sent via its GET or POST methods
.. i18n: -	It’s only called for a full match on the URL
..

The Index Method
================
-	Method **index()**, like the **index.html** file, is the default page for any internal node in the object tree
-	Can take additional keyword arguments, mapped to the form variables as sent via its GET or POST methods
-	It’s only called for a full match on the URL

.. i18n: Calling Other Methods
.. i18n: =====================
.. i18n: CherryPy can also directly call methods in the published objects if it receives a URL that is directly mapped to them—e.g.,
..

Calling Other Methods
=====================
CherryPy can also directly call methods in the published objects if it receives a URL that is directly mapped to them—e.g.,

.. i18n: ::
.. i18n: 
.. i18n: 	class HelloWorld():
.. i18n: 	    def index(self):
.. i18n: 	        return "Hello World!"
.. i18n: 	    index.exposed = True
.. i18n: 
.. i18n: 	    @cherrypy.expose
.. i18n: 	    def test(self):
.. i18n: 	        return "Test Controller"
.. i18n: 	cherrypy.quickstart(HelloWorld())
..

::

	class HelloWorld():
	    def index(self):
	        return "Hello World!"
	    index.exposed = True

	    @cherrypy.expose
	    def test(self):
	        return "Test Controller"
	cherrypy.quickstart(HelloWorld())

.. i18n: Then request http://localhost:8080/test 
..

Then request http://localhost:8080/test 

.. i18n: When CherryPy receives a request for the /**test** URL, it calls the test() function.
..

When CherryPy receives a request for the /**test** URL, it calls the test() function.

.. i18n: -	It can be a plain function, or a method of any object—any callable will do.
..

-	It can be a plain function, or a method of any object—any callable will do.

.. i18n: If CherryPy finds a full match and the last object in the match is a **callable**.
..

If CherryPy finds a full match and the last object in the match is a **callable**.

.. i18n: -	A method, function, or any other Python object that supports the **__call__** method and the callable doesn't contain a valid **index()** method.
..

-	A method, function, or any other Python object that supports the **__call__** method and the callable doesn't contain a valid **index()** method.

.. i18n: Then the object itself is called.
..

Then the object itself is called.

.. i18n: These rules are needed because classes in Python are callables (for producing instances).
..

These rules are needed because classes in Python are callables (for producing instances).

.. i18n: CherryPy supports both the GET and POST method for forms.
..

CherryPy supports both the GET and POST method for forms.

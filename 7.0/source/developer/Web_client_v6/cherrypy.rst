.. _web_cherrypy:

==================
What is Cherrypy ?
==================

CherryPy is a pythonic, object-oriented HTTP framework.
 
CherryPy allows developers to build web applications in much the same way they would build any other 
object-oriented Python program. This results in smaller source code developed in less time.
	
::

	import cherrypy
	class HelloWorld:
	    def index(self):
	        return "Hello World!"
	    index.exposed = True
	cherrypy.quickstart(HelloWorld())


Start the application at the command prompt(after navigating to its folder):
	**python hello.py**
		
Direct your browser to http://localhost:8080

The rendering:
	**Hello World!**
		
ctrl+c in command window to terminate the application

Statement **import cherrypy** imports the main CherryPy module.

An instance of class **HelloWorld** is the object that will be **published.**

Method **index()** is called when the root URL for the site(e.g., http://localhost:8080) is requested, 
This method returns the **contents** of the Web page(the **'Hello World!'** string)

Statement **index.exposed = True** tells CherryPy that method **index()** will be exposed

-	Only exposed methods can be called to answer a request
-	Lets the user to select which methods of an object are Web accessible
-	Can also place the decoration **@cherrypy.expose** immediately before the method:

::

	@cherrypy.expose
	def index(self):
	    return "Hello World!"


Statement, **cherrypy.quickstart(HelloWorld())**

	**publishes** an instance of the HelloWorld class
	
	-	And it starts the embedded webserver
	-	Runs until explicitly interrupted(ctrl+c)
	
When the application is executed, the CherryPy server is started with the default configuration
	
-	Listening on **localhost**  at port **8080**
-	Defaults overriden by using a configuration file or dictionary
	
	-	**cherrypy.config.update({'server.socket_port':8010})**
	-	Now it will run on port 8010.
	
Webserver receives the request for URL http://localhost:8080 

-	Searches for the best method to handle the request,starting from the **HelloWorld** instance
-	CherryPy calls **HelloWorld().index()**
-	Result of the call is sent back to the browser as the content of the index page for the website

Cherrypy Application Facts
==========================
Your CherryPy powered web applications are in fact stand-alone Python applications embedding their 
own multi-threaded web server. You can deploy them anywhere you can run Python applications. 
Apache is not required, but it's possible to run a CherryPy application behind it (or lighttpd, or IIS). 
CherryPy applications run on Windows, Linux, Mac OS X and any other platform supporting Python. 

Beyond this functionality, CherryPy pretty much stays out of your way. You are free to use any kind of templating, 
data access etc. technology you want. CherryPy can also handle sessions, static files, cookies, file uploads and 
everything you would expect from a decent web framework. 

Features
========
-	A **fast**, HTTP/1.1-compliant, WSGI thread-pooled webserver. Typically, CherryPy itself takes only 1-2ms per page!
-	Support for any other WSGI-enabled webserver or adapter, including Apache, IIS, lighttpd, mod_python, FastCGI, SCGI, and mod_wsgi 
-	Easy to run multiple HTTP servers (e.g. on multiple ports) at once
-	A powerful configuration system for developers and deployers alike
-	A flexible plugin system
-	Built-in tools for caching, encoding, sessions, authorization, static content, and many more
-	A native mod_python adapter 
-	A complete test suite 
-	Swappable and customisable... everything.
-	Built-in profiling, coverage, and testing support.

Consider these examples (**root** is conceptual, referring to the root of the document tree),
	**root = HelloWorld()**
	
	**root.onepage = OnePage()**
	
	**root.otherpage = OtherPage()**

URL http://localhost:8080/onepage points at the 1st object,

URL http://localhost:8080/otherpage points at the 2nd.

Consider,
	**root.some = Page()**
	
	**root.some.page = Page()** 

URL http://localhost:8080/some/page  is mapped to the **root.some.page** object. 
If this object is exposed (or its **index** method is), it’s called for that URL

In our HelloWorld example, adding the http://.../onepage to OnePage() mapping could be done as:

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


In the address bar of the browser, put http://localhost:8080/onepage 

The Index Method
================
-	Method **index()**, like the **index.html** file, is the default page for any internal node in the object tree
-	Can take additional keyword arguments, mapped to the form variables as sent via its GET or POST methods
-	It’s only called for a full match on the URL

Calling Other Methods
=====================
CherryPy can also directly call methods in the published objects if it receives a URL that is directly mapped to them—e.g.,

::

	class HelloWorld():
	    def index(self):
	        return "Hello World!"
	    index.exposed = True

	    @cherrypy.expose
	    def test(self):
	        return "Test Controller"
	cherrypy.quickstart(HelloWorld())

Then request http://localhost:8080/test 

When CherryPy receives a request for the /**test** URL, it calls the test() function.

-	It can be a plain function, or a method of any object—any callable will do.

If CherryPy finds a full match and the last object in the match is a **callable**.

-	A method, function, or any other Python object that supports the **__call__** method and the callable doesn't contain a valid **index()** method.

Then the object itself is called.

These rules are needed because classes in Python are callables (for producing instances).

CherryPy supports both the GET and POST method for forms.


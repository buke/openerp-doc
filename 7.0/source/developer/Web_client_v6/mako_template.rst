.. _mako_template:

=============
Mako Template
=============

Mako is a template library written in Python. 

It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance.

Mako's syntax and API borrows from the best ideas of many others, including Django templates, Cheetah, Myghty, and Genshi. 

Conceptually, Mako is an embedded Python (i.e. Python Server Page) language, which refines the familiar ideas of 
componentized layout and inheritance to produce one of the most straightforward and flexible models available, 
while also maintaining close ties to Python calling and scoping semantics.

::

	<%inherit file="base.html"/>
	<%
	    rows = [[v for v in range(0,10)] for row in range(0,10)]
	%>

	<table>
	    % for row in rows:
	        ${makerow(row)}
	    % endfor
	</table>

	<%def name="makerow(row)">
	    <tr>
	    % for name in row:
	        <td>${name}</td>
	    % endfor
	    </tr>
	</%def>

Features
========

Super-simple API. For basic usage, just one class, Template is needed:

::

	from mako.template import Template
	print Template("hello ${data}!").render(data="world")

For filesystem management and template caching, add the TemplateLookup class.

Insanely Fast. An included bench suite, adapted from a suite included with Genshi, has 
these results for a simple three-sectioned layout: 

::

	Mako: 1.10 ms                                             Kid: 14.54 ms

-	**Standard template features**
 
	-	control structures constructed from real Python code (i.e. loops, conditionals)
	-	straight Python blocks, inline or at the module-level

-	**Callable blocks**

	-	can access variables from their enclosing scope as well as the template's request context
	-	can be nested arbitrarily
	-	can specify regular Python argument signatures
	-	outer-level callable blocks can be called by other templates or controller code (i.e. "method call")
	-	calls to functions can define any number of sub-blocks of content which are accessible to the called 
		function (i.e. "component-call-with-content"). This is the basis for nestable custom tags.

-	**Inheritance**

	-	supports "multi-zoned" inheritance - define any number of areas in the base template to be overridden.
	-	supports "chaining" style inheritance - call next.body() to call the "inner" content.
	-	the full inheritance hierarchy is navigable in both directions (i.e. parent and child) from anywhere in the chain.
	-	inheritance is dynamic ! Specify a function instead of a filename to calculate inheritance on the fly for every request.

Examples
========

-	**Basic Usage**

::

	from mako.template import Template

	mytemplate = Template("hello world!")
	print mytemplate.render()

The text argument to **Template** is **compiled** into a Python module representation.

This module contains a function called render_body(),which produces the output of the template.

When mytemplate.render() is called, Mako sets up a runtime environment for the template and calls 
the render_body() function, capturing the output into a buffer and returning its string contents.

The code inside the render_body() function has access to a namespace of variables. You can specify 
these variables by sending them as additional keyword arguments to the **render()** method:

::

	from mako.template import Template

	mytemplate = Template("hello, ${name}!")
	print mytemplate.render(name="openerp")

-	**Using File-based Templates**

A **Tempalte** can also load its template source code from a file, using the filename keyword argument:

::

	from mako.template import Template

	mytemplate = Template(filename='/test.html')
	print mytemplate.render()

-	**Using TemplateLookup**

All of the examples thus far have dealt with the usage of a single **Template** object.

If the code within those templates tries to locate another template resource, 
it will need some way to find them, using simple URI strings.	

For this need, the resolution of other templates from within a template is accomplished by the **TemplateLookup** class. 

This class is constructed given a list of directories in which to search for templates, as well as keyword arguments 
that will be passed to the **Template** objects it creates:

::

	from mako.template import Template
	from mako.lookup import TemplateLookup

	mylookup = TemplateLookup(directories=[''])
	mytemplate = Tempalte('<% include file="header.txt"/> Hello!',lookup=mylookup)

Above, we created a textual template which includes the file "header.txt". 

In order for it to have somewhere to look for "header.txt", we passed a **TemplateLookup** object to it, 
which will search in the current directory  for the file "header.txt".

Syntax
======

-	**Expression Substitution**

The simplest expression is just a variable substitution.

The syntax for this is the ${} construct, which is inspired by Perl, Genshi, JSP EL, and others:

    **${x}**

    **${5%5}**

    **${7*2}**

    **${pow(x,2) + pow(y,2)}**

-	**Controller Structures**

	-	Conditionals(i.e if/else)

	-	loops(for and while)

	-	as well as try/except

control structures are written using the % marker followed by a regular Python control expression, 
and are “closed” by using another % marker with the tag “end<name>“, where “<name>” is the keyword of the expression:

::

	% if user_name == 'openerp':
	    valid user
	% endif

	% if a > 1:
	    a is positive number
	% elif a == 0:
	    a is 0
	% else:
	    a is negative number
	% endif

	<table>
	% for a in [1,2,3,4,5]:
	    <tr>
	        <td>
	            ${a}
	        </td>
	    </tr>
	% endfor
	</table>


-	**Python Blocks**

Any arbitrary block of python can be dropped in using the <% %> tags:

::

	<%
	    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
	    b = a.values()
	%>
	% for x in b:
	    ${x}
	% endfor


-	**Module-level Blocks**

A variant on <% %> is the module-level code block, denoted by <%! %>.

Code within these tags is executed at the module level of the template, and not within the rendering function of the template.

::

	<%!
	    import cherrypy
	    def get_user_from_session():
	        return cherrypy.session['current_user']
	%>

Therefore, this code does not have access to the template’s context and is only executed when the template is loaded into 
memory (which can be only once per application, or more, depending on the runtime environment).


-	**Mako Tags**

**<%page>**

This tag defines general characteristics of the template, including caching arguments, and optional lists of arguments which the template expects when invoked.

Also defines caching characteristics.

::

	<%page args="x, y, z='default'"/>
	<%page cached="True" cache_type="memory"/>


**<%include>**

just accepts a file argument and calls in the rendered result of that file:

Also accepts arguments which are available as <%page> arguments in the receiving template:

::

	<%include file="header.mako"/>
	    Welcome to OpenERP
	<%include file="footer.mako"/>

	<%include file="toolbar.html" args="current_section='members', username='ed'"/>


**<%inherit>**

Inherit allows templates to arrange themselves in inheritance chains.

When using the %inherit tag, control is passed to the topmost inherited template first, which 
then decides how to handle calling areas of content from its inheriting templates.

::

	<%inherit file="index.mako"/>


**<%def>**

The %def tag defines a Python function which contains a set of content, that can be called at some other point in the template.

The %def tag is a lot more powerful than a plain Python def, as the Mako compiler provides many extra services 
with %def that you wouldn’t normally have, such as the ability to export defs as template “methods”, 
automatic propagation of the current Context, buffering/filtering/caching flags, and def calls with content, 
which enable packages of defs to be sent as arguments to other def calls (not as hard as it sounds).

::

	<%def name="my_function(x)">
	    this is function ${x}
	<%def>


**<%namespace>**

%namespace is Mako’s equivalent of Python’s import statement.

It allows access to all the rendering functions and metadata of other template files, plain Python modules, 
as well as locally defined “packages” of functions.	

::

	<%namespace file="test.mako" import="*"/>


**<%doc>**

handles multiline comments:

::

	<%doc>
	    Multi line comments
	    Using doc tag
	</%doc>


For More Details visit the documentation: http://www.makotemplates.org/docs/index.html


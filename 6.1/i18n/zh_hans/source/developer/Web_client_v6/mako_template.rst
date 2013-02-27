.. i18n: .. _mako_template:
.. i18n: 
.. i18n: =============
.. i18n: Mako Template
.. i18n: =============
..

.. _mako_template:

=============
Mako 模板
=============

.. i18n: Mako is a template library written in Python. 
..

**Mako** 是Python语言的一个模板处理库.

.. i18n: It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance.
..

它能提供编译为常见的非XML语法的高性能的Python模块.

.. i18n: Mako's syntax and API borrows from the best ideas of many others, including Django templates, Cheetah, Myghty, and Genshi. 
..

Mako 的语法及API融合了很多模块系统的亮点, 如常用的 Django, Cheetah, Myghty, Genshi等等. 

.. i18n: Conceptually, Mako is an embedded Python (i.e. Python Server Page) language, which refines the familiar ideas of 
.. i18n: componentized layout and inheritance to produce one of the most straightforward and flexible models available, 
.. i18n: while also maintaining close ties to Python calling and scoping semantics.
..

从概念上讲, Mako 属于一种内嵌Python语言(如Python的服务端页面). 这样模板开发者精确的想法布局实现及简单而直接地继承.
模式灵活同时还保证了与应用与Python的调用及语义的紧密联系.

.. i18n: ::
.. i18n: 
.. i18n: 	<%inherit file="base.html"/>
.. i18n: 	<%
.. i18n: 	    rows = [[v for v in range(0,10)] for row in range(0,10)]
.. i18n: 	%>
.. i18n: 
.. i18n: 	<table>
.. i18n: 	    % for row in rows:
.. i18n: 	        ${makerow(row)}
.. i18n: 	    % endfor
.. i18n: 	</table>
.. i18n: 
.. i18n: 	<%def name="makerow(row)">
.. i18n: 	    <tr>
.. i18n: 	    % for name in row:
.. i18n: 	        <td>${name}</td>
.. i18n: 	    % endfor
.. i18n: 	    </tr>
.. i18n: 	</%def>
..

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

.. i18n: Features
.. i18n: ========
..

功能
========

.. i18n: Super-simple API. For basic usage, just one class, Template is needed:
..

API简洁, 最简单的例子, 只需要引用一个 Template class 即可.

.. i18n: ::
.. i18n: 
.. i18n: 	from mako.template import Template
.. i18n: 	print Template("hello ${data}!").render(data="world")
..

::

	from mako.template import Template
	print Template("hello ${data}!").render(data="world")

.. i18n: For filesystem management and template caching, add the TemplateLookup class.
..

另一个例子,使用文件模板以及模板缓存,模板文件优先查询的处理.

.. i18n: Insanely Fast. An included bench suite, adapted from a suite included with Genshi, has 
.. i18n: these results for a simple three-sectioned layout: 
..

Insanely Fast. An included bench suite, adapted from a suite included with Genshi, has 
these results for a simple three-sectioned layout: 

.. i18n: ::
.. i18n: 
.. i18n: 	Mako: 1.10 ms                                             Kid: 14.54 ms
..

::

	Mako: 1.10 ms                                             Kid: 14.54 ms

.. i18n: -	**Standard template features**
.. i18n:  
.. i18n: 	-	control structures constructed from real Python code (i.e. loops, conditionals)
.. i18n: 	-	straight Python blocks, inline or at the module-level
.. i18n: 
.. i18n: -	**Callable blocks**
.. i18n: 
.. i18n: 	-	can access variables from their enclosing scope as well as the template's request context
.. i18n: 	-	can be nested arbitrarily
.. i18n: 	-	can specify regular Python argument signatures
.. i18n: 	-	outer-level callable blocks can be called by other templates or controller code (i.e. "method call")
.. i18n: 	-	calls to functions can define any number of sub-blocks of content which are accessible to the called 
.. i18n: 		function (i.e. "component-call-with-content"). This is the basis for nestable custom tags.
.. i18n: 
.. i18n: -	**Inheritance**
.. i18n: 
.. i18n: 	-	supports "multi-zoned" inheritance - define any number of areas in the base template to be overridden.
.. i18n: 	-	supports "chaining" style inheritance - call next.body() to call the "inner" content.
.. i18n: 	-	the full inheritance hierarchy is navigable in both directions (i.e. parent and child) from anywhere in the chain.
.. i18n: 	-	inheritance is dynamic ! Specify a function instead of a filename to calculate inheritance on the fly for every request.
..

-	**标准模板功能**
 
	-	模板结构,逻辑控制使用标准Python语法(如 循环语句, 条件语句等)
	-	straight Python blocks, inline or at the module-level

-	**可重复使用模板块**

	-	can access variables from their enclosing scope as well as the template's request context
	-	模块任意嵌套
	-	can specify regular Python argument signatures
	-	outer-level callable blocks can be called by other templates or controller code (i.e. "method call")
	-	calls to functions can define any number of sub-blocks of content which are accessible to the called 
		function (i.e. "component-call-with-content"). This is the basis for nestable custom tags.

-	**模板继承**

	-	supports "multi-zoned" inheritance - define any number of areas in the base template to be overridden.
	-	supports "chaining" style inheritance - call next.body() to call the "inner" content.
	-	the full inheritance hierarchy is navigable in both directions (i.e. parent and child) from anywhere in the chain.
	-	inheritance is dynamic ! Specify a function instead of a filename to calculate inheritance on the fly for every request.

.. i18n: Examples
.. i18n: ========
..

例子
========

.. i18n: -	**Basic Usage**
..

-	**基本用法**

.. i18n: ::
.. i18n: 
.. i18n: 	from mako.template import Template
.. i18n: 
.. i18n: 	mytemplate = Template("hello world!")
.. i18n: 	print mytemplate.render()
..

::

	from mako.template import Template

	mytemplate = Template("hello world!")
	print mytemplate.render()

.. i18n: The text argument to **Template** is **compiled** into a Python module representation.
..

传给 **Template** 的模板文本被处理成一种类似 Python 模块的对象.

.. i18n: This module contains a function called render_body(),which produces the output of the template.
..

这个模块对象有一个 **render_body()** 方法, 用于将模板处理为最终的输出结果.

.. i18n: When mytemplate.render() is called, Mako sets up a runtime environment for the template and calls 
.. i18n: the render_body() function, capturing the output into a buffer and returning its string contents.
..

当 mytemplate.render() 时，Mako 会处理当前的运行环境并调用 render_body() 方法渲染模板后返回处理结果为一个
字符串.

.. i18n: The code inside the render_body() function has access to a namespace of variables. You can specify 
.. i18n: these variables by sending them as additional keyword arguments to the **render()** method:
..

The code inside the render_body() function has access to a namespace of variables. You can specify 
these variables by sending them as additional keyword arguments to the **render()** method:

.. i18n: ::
.. i18n: 
.. i18n: 	from mako.template import Template
.. i18n: 
.. i18n: 	mytemplate = Template("hello, ${name}!")
.. i18n: 	print mytemplate.render(name="openerp")
..

::

	from mako.template import Template

	mytemplate = Template("hello, ${name}!")
	print mytemplate.render(name="openerp")

.. i18n: -	**Using File-based Templates**
..

-	**基于文件的模板**

.. i18n: A **Tempalte** can also load its template source code from a file, using the filename keyword argument:
..

使用文件做为模板代码源, 只需要使用 **filename** 参数指定文件路径即可:

.. i18n: ::
.. i18n: 
.. i18n: 	from mako.template import Template
.. i18n: 
.. i18n: 	mytemplate = Template(filename='/test.html')
.. i18n: 	print mytemplate.render()
..

::

	from mako.template import Template

	mytemplate = Template(filename='/test.html')
	print mytemplate.render()

.. i18n: -	**Using TemplateLookup**
..

-	**使用 TemplateLookup 匹配最佳模板**

.. i18n: All of the examples thus far have dealt with the usage of a single **Template** object.
..

到目前, 所有的例子还都是只使用单一的 **Template** 模板.

.. i18n: If the code within those templates tries to locate another template resource, 
.. i18n: it will need some way to find them, using simple URI strings.	
..

如果模板代码中引用一个本地的另一个模板资源, Mako 则可以使用简单的 URI 串来指定查找位置.

.. i18n: For this need, the resolution of other templates from within a template is accomplished by the **TemplateLookup** class. 
..

因此, **TemplateLookup** 类就解决了在一个模板中引用其它模板的问题.

.. i18n: This class is constructed given a list of directories in which to search for templates, as well as keyword arguments 
.. i18n: that will be passed to the **Template** objects it creates:
..

该类将按给定的目录列表查找模板，
This class is constructed given a list of directories in which to search for templates, as well as keyword arguments 
that will be passed to the **Template** objects it creates:

.. i18n: ::
.. i18n: 
.. i18n: 	from mako.template import Template
.. i18n: 	from mako.lookup import TemplateLookup
.. i18n: 
.. i18n: 	mylookup = TemplateLookup(directories=[''])
.. i18n: 	mytemplate = Tempalte('<% include file="header.txt"/> Hello!',lookup=mylookup)
..

::

	from mako.template import Template
	from mako.lookup import TemplateLookup

	mylookup = TemplateLookup(directories=[''])
	mytemplate = Tempalte('<% include file="header.txt"/> Hello!',lookup=mylookup)

.. i18n: Above, we created a textual template which includes the file "header.txt". 
..

上面的代码, 则创建了一个引用了 "header.txt" 文件的模板.

.. i18n: In order for it to have somewhere to look for "header.txt", we passed a **TemplateLookup** object to it, 
.. i18n: which will search in the current directory  for the file "header.txt".
..

为了让系统能找到 "header.txt" 模板, 我们传了一个 **TemplateLookup** 对象过去,告诉系统从当前文件夹中查找 "header.txt".

.. i18n: Syntax
.. i18n: ======
..

语法
======

.. i18n: -	**Expression Substitution**
..

-	**表达式**

.. i18n: The simplest expression is just a variable substitution.
..

模板最简单的表达式就是模板变量的替换了.

.. i18n: The syntax for this is the ${} construct, which is inspired by Perl, Genshi, JSP EL, and others:
..

${} 的语法类似于 Perl, Genshi, JSP EL等模板系统的语法:

.. i18n:     **${x}**
..

    **${x}**

.. i18n:     **${5%5}**
..

    **${5%5}**

.. i18n:     **${7*2}**
..

    **${7*2}**

.. i18n:     **${pow(x,2) + pow(y,2)}**
..

    **${pow(x,2) + pow(y,2)}**

.. i18n: -	**Controller Structures**
.. i18n: 
.. i18n: 	-	Conditionals(i.e if/else)
.. i18n: 
.. i18n: 	-	loops(for and while)
.. i18n: 
.. i18n: 	-	as well as try/except
..

-	**流程控制**

	-	条件语句(如: if/else)

	-	循环语句(如: for 与 while)

	-	异常控制(如: try/except)

.. i18n: control structures are written using the % marker followed by a regular Python control expression, 
.. i18n: and are “closed” by using another % marker with the tag “end<name>“, where “<name>” is the keyword of the expression:
..

control structures are written using the % marker followed by a regular Python control expression, 
and are “closed” by using another % marker with the tag “end<name>“, where “<name>” is the keyword of the expression:

.. i18n: ::
.. i18n: 
.. i18n: 	% if user_name == 'openerp':
.. i18n: 	    valid user
.. i18n: 	% endif
.. i18n: 
.. i18n: 	% if a > 1:
.. i18n: 	    a is positive number
.. i18n: 	% elif a == 0:
.. i18n: 	    a is 0
.. i18n: 	% else:
.. i18n: 	    a is negative number
.. i18n: 	% endif
.. i18n: 
.. i18n: 	<table>
.. i18n: 	% for a in [1,2,3,4,5]:
.. i18n: 	    <tr>
.. i18n: 	        <td>
.. i18n: 	            ${a}
.. i18n: 	        </td>
.. i18n: 	    </tr>
.. i18n: 	% endfor
.. i18n: 	</table>
..

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

.. i18n: -	**Python Blocks**
..

-	**Python Blocks**

.. i18n: Any arbitrary block of python can be dropped in using the <% %> tags:
..

Any arbitrary block of python can be dropped in using the <% %> tags:

.. i18n: ::
.. i18n: 
.. i18n: 	<%
.. i18n: 	    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
.. i18n: 	    b = a.values()
.. i18n: 	%>
.. i18n: 	% for x in b:
.. i18n: 	    ${x}
.. i18n: 	% endfor
..

::

	<%
	    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
	    b = a.values()
	%>
	% for x in b:
	    ${x}
	% endfor

.. i18n: -	**Module-level Blocks**
..

-	**Module-level Blocks**

.. i18n: A variant on <% %> is the module-level code block, denoted by <%! %>.
..

A variant on <% %> is the module-level code block, denoted by <%! %>.

.. i18n: Code within these tags is executed at the module level of the template, and not within the rendering function of the template.
..

Code within these tags is executed at the module level of the template, and not within the rendering function of the template.

.. i18n: ::
.. i18n: 
.. i18n: 	<%!
.. i18n: 	    import cherrypy
.. i18n: 	    def get_user_from_session():
.. i18n: 	        return cherrypy.session['current_user']
.. i18n: 	%>
..

::

	<%!
	    import cherrypy
	    def get_user_from_session():
	        return cherrypy.session['current_user']
	%>

.. i18n: Therefore, this code does not have access to the template’s context and is only executed when the template is loaded into 
.. i18n: memory (which can be only once per application, or more, depending on the runtime environment).
..

Therefore, this code does not have access to the template’s context and is only executed when the template is loaded into 
memory (which can be only once per application, or more, depending on the runtime environment).

.. i18n: -	**Mako Tags**
..

-	**Mako Tags**

.. i18n: **<%page>**
..

**<%page>**

.. i18n: This tag defines general characteristics of the template, including caching arguments, and optional lists of arguments which the template expects when invoked.
..

This tag defines general characteristics of the template, including caching arguments, and optional lists of arguments which the template expects when invoked.

.. i18n: Also defines caching characteristics.
..

Also defines caching characteristics.

.. i18n: ::
.. i18n: 
.. i18n: 	<%page args="x, y, z='default'"/>
.. i18n: 	<%page cached="True" cache_type="memory"/>
..

::

	<%page args="x, y, z='default'"/>
	<%page cached="True" cache_type="memory"/>

.. i18n: **<%include>**
..

**<%include>**

.. i18n: just accepts a file argument and calls in the rendered result of that file:
..

just accepts a file argument and calls in the rendered result of that file:

.. i18n: Also accepts arguments which are available as <%page> arguments in the receiving template:
..

Also accepts arguments which are available as <%page> arguments in the receiving template:

.. i18n: ::
.. i18n: 
.. i18n: 	<%include file="header.mako"/>
.. i18n: 	    Welcome to OpenERP
.. i18n: 	<%include file="footer.mako"/>
.. i18n: 
.. i18n: 	<%include file="toolbar.html" args="current_section='members', username='ed'"/>
..

::

	<%include file="header.mako"/>
	    Welcome to OpenERP
	<%include file="footer.mako"/>

	<%include file="toolbar.html" args="current_section='members', username='ed'"/>

.. i18n: **<%inherit>**
..

**<%inherit>**

.. i18n: Inherit allows templates to arrange themselves in inheritance chains.
..

Inherit allows templates to arrange themselves in inheritance chains.

.. i18n: When using the %inherit tag, control is passed to the topmost inherited template first, which 
.. i18n: then decides how to handle calling areas of content from its inheriting templates.
..

When using the %inherit tag, control is passed to the topmost inherited template first, which 
then decides how to handle calling areas of content from its inheriting templates.

.. i18n: ::
.. i18n: 
.. i18n: 	<%inherit file="index.mako"/>
..

::

	<%inherit file="index.mako"/>

.. i18n: **<%def>**
..

**<%def>**

.. i18n: The %def tag defines a Python function which contains a set of content, that can be called at some other point in the template.
..

The %def tag defines a Python function which contains a set of content, that can be called at some other point in the template.

.. i18n: The %def tag is a lot more powerful than a plain Python def, as the Mako compiler provides many extra services 
.. i18n: with %def that you wouldn’t normally have, such as the ability to export defs as template “methods”, 
.. i18n: automatic propagation of the current Context, buffering/filtering/caching flags, and def calls with content, 
.. i18n: which enable packages of defs to be sent as arguments to other def calls (not as hard as it sounds).
..

The %def tag is a lot more powerful than a plain Python def, as the Mako compiler provides many extra services 
with %def that you wouldn’t normally have, such as the ability to export defs as template “methods”, 
automatic propagation of the current Context, buffering/filtering/caching flags, and def calls with content, 
which enable packages of defs to be sent as arguments to other def calls (not as hard as it sounds).

.. i18n: ::
.. i18n: 
.. i18n: 	<%def name="my_function(x)">
.. i18n: 	    this is function ${x}
.. i18n: 	<%def>
..

::

	<%def name="my_function(x)">
	    this is function ${x}
	<%def>

.. i18n: **<%namespace>**
..

**<%namespace>**

.. i18n: %namespace is Mako’s equivalent of Python’s import statement.
..

%namespace is Mako’s equivalent of Python’s import statement.

.. i18n: It allows access to all the rendering functions and metadata of other template files, plain Python modules, 
.. i18n: as well as locally defined “packages” of functions.	
..

这允许访问所有的渲染函数及其它模板文件的元数据, plain Python modules, 
甚至本地定义的函数包.	

.. i18n: ::
.. i18n: 
.. i18n: 	<%namespace file="test.mako" import="*"/>
..

::

	<%namespace file="test.mako" import="*"/>

.. i18n: **<%doc>**
..

**<%doc>**

.. i18n: handles multiline comments:
..

处理多行内容:

.. i18n: ::
.. i18n: 
.. i18n: 	<%doc>
.. i18n: 	    Multi line comments
.. i18n: 	    Using doc tag
.. i18n: 	</%doc>
..

::

	<%doc>
	    多行内容
	    使用文档标签
	</%doc>

.. i18n: For More Details visit the documentation: http://www.makotemplates.org/docs/index.html
..

更多的资料，请访问访官方文档: http://www.makotemplates.org/docs/index.html

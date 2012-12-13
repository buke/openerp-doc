.. i18n: =======
.. i18n: Reports
.. i18n: =======
..

=======
报表
=======

.. i18n: There are mainly three types of reports in OpenERP:
..

OpenERP 主要有三种类型的报表:

.. i18n:     * OpenOffice.org reports
.. i18n:     * RML reports
.. i18n:     * custom reports (based on PostgreSQL views and displayed within the interface) 
..

    * OpenOffice.org 报表
    * RML 报表
    * 自定义报表 (基于 PostgreSQL 视图和显示接口) 

.. i18n: This chapter mainly describes OpenOffice.org reports, and then XSL:RML reports. Custom reports are described in section Advanced Modeling - Reporting With PostgreSQL Views.
..

这一部分主要描述 OpenOffice.org 报表, 和 XSL:RML 报表. 自定义报表在高级模块部分描述 -  PostgreSQL 视图报表.

.. i18n: OpenOffice.org reports
.. i18n: ======================
..

OpenOffice.org 报表
======================

.. i18n: **The document flow**
..

**文件流**

.. i18n: OpenOffice.org reports are the most commonly used report formats. OpenOffice.org Writer is used (in combination with [[1]]) to generate a RML template, which in turn is used to generate a pdf printable report.
..

OpenOffice.org是通用的报表格式。OpenOffice.org Writer被用来生成RML模板，而RML模板用来生成pdf报表。

.. i18n: .. figure::  images/ooo_report_overview.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/ooo_report_overview.png
   :scale: 85
   :align: center

.. i18n: **The internal process**
..

**内部过程**

.. i18n: .. figure::  images/process_ooo.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/process_ooo.png
   :scale: 85
   :align: center

.. i18n: **The .SXW template file**
..

**.SXW 模板文件**

.. i18n:     * We use a .SXW file for the template, which is the OpenOffice 1.0 format. The template includes expressions in brackets or OpenOffice fields to point where the data from the OpenERP server will be filled in. This document is only used for developers, as a help-tool to easily generate the .RML file. OpenERP does not need this .SXW file to print reports. 
..

    * •	我们用OpenOffice1.0的.sxw文件作为模板。模板中包含用括号括起来的表达式或OpenOffice字段(field)，用来提供 给OpenERP server填充数据。但这只是作为一种较容易的方法，提供给开发者生成.RML文件。OpenERP并不需要SXW文件产生报表。 

.. i18n: **The .RML template**
..

**.RML 模板**

.. i18n:     * We generate a .RML file from the .SXW file using Open SXW2RML. A .RML file is a XML format that represent a .PDF document. It can be converted to a .PDF after. We use RML for more easy processing: XML syntax seems to be more common than PDF syntax. 
..

    * •	可以使用Open SXW2RML从SXW文件生成RML文件。RML文件是一种表现PDF文档的XML格式，可以转换为PDF文件。RML是一种更容易的方法，至少XML语法比PDF语法更加通俗易懂。 

.. i18n: **The report engine**
..

**报表引擎**

.. i18n:     * The Open Report Engine process the .RML file inserting data from the database at each expression. 
..

    * 报表引擎(report engine)从数据库中读出数据，插入在RML文件的表达式中。 

.. i18n: in the .RML file will be replaced by the name of the country of the partner of the printed invoice. This report engine produce the same .RML file where all expressions have been replaced by real data.
..

在.RML文件中，将以(打印)发票上parter的城市名称替换掉相应表达式。报表引擎以真实数据替换所有表达式之后，生成相同的.RML文件。

.. i18n: **The final document**
..

**生成最终文档**

.. i18n:     * Finally the .RML file is converted to PDF or HTML as needed, using OpenReport's scripts. 
..

    * 最后RML文件会根据OpenReport代码的需要，转换成PDF或者HTML文件。

.. i18n: Creating a SXW
.. i18n: --------------
..

生成 SXW 文件
--------------

.. i18n: You can design reports using *OpenOffice*. Here, as an example, is the file **server/bin/addons/sale/report/order.sxw**.
..

你可以使用 OpenOffice 设计报表。举个例子，如： **server/bin/addons/sale/report/order.sxw**.

.. i18n: .. figure::  images/writer_report.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/writer_report.png
   :scale: 85
   :align: center

.. i18n: .. _dynamic-report-content:
.. i18n: 
.. i18n: Dynamic content in OpenOffice reports 
.. i18n: -------------------------------------
..

.. _dynamic-report-content:

OpenOffice 报表中的动态内容
-------------------------------------

.. i18n: **Dynamic content**
..

**动态内容**

.. i18n: In the .SXW/.RML reports, you can put some Python code that accesses the OpenERP objects in brackets. The context of the code (the variable's values you can use) is the following:
..

SXW/RML报表中，你可以在括号中加入Python代码，以获得OpenERP中的对象(object)。代码(可以使用变量)如下:

.. i18n: **Available variables**
..

**可用的变量**

.. i18n: Here are Python objects/variables available:
..

可以用的 Python 对象/变量:

.. i18n:     * **objects** : the list of objects to be printed (invoices for example).
.. i18n:     * **data** : comes from the wizard
.. i18n:     * **time** : the Python time module (see Python documentation for more information).
.. i18n:     * **user** : the user object launching the report. 
..

    * **objects** : 将要打印的object列表(例如发票（invoice)对象）.
    * **data** : 向导(wizard)中获得的数据
    * **time** : Python的time模块(查看Python文档获取更多信息).
    * **user** : 创建这个报表的user. 

.. i18n:  **Available functions**
..

 **可用的函数**

.. i18n: Here are Python functions you can use:
..

可以用的 Python 函数:

.. i18n:     * **setLang('fr')** : change the language used in automated translation (fields...).
.. i18n:     * **repeatIn(list, varname[, tagname])** : repeat the current part of the template 
.. i18n:       (whole document, current section, current row in the table) for each 
.. i18n:       object in the list. Use varname in the template's tags. Since versions 
.. i18n:       4.1.X, you can use an optional third argument that is the name of the 
.. i18n:       .RML tag you want to loop on.
.. i18n:     * **setTag('para','xpre')** : replace the enclosing RML tag (usually 'para') with an other (xpre is a preformatted paragraph), in the (converted from sxw)rml document (?)
.. i18n:     * **removeParentNode('tr')** : removes the parent node of type 'tr', this parameter is usually used together with a conditional (see examples below)
..

    * **setLang('fr')** : 根据国际化自动切换语言 (字段...).
    * **repeatIn(list, varname[, tagname])** : 重复 模板(template)当前部分list中的对象 (整个文档, 当前段落, 表格中的当前行) 可以使用模板(template)的 varname标签 。 从 4.1.X版开始, 你可以使用第三个参数(可选的)选择你想在.RML标记(RML tag)中重复的内容.
    * **setTag('para','xpre')** : 在rml文档中(由sxw转换)，用其它标记(0tag) (xpre 是一个预处理格式的段落，preformatted paragraph),替换封闭的 RML 标签 (一般是 ‘para’)(?)
    * **removeParentNode('tr')** : 移除类型 ‘tr’的父结点, 这个参数经常在条件语句中使用 (如下例)

.. i18n: Example of useful tags:
..

有用的标签举例:

.. i18n:     * **[[ repeatIn(objects,'o') ]]** : 循环打印选中的object
.. i18n:     * **[[ repeatIn(o.invoice_line,'l') ]]** : Loop on every line
.. i18n:     * **[[ repeatIn(o.invoice_line,'l', 'td') ]]** : Loop on every line and make
.. i18n:       a new table cell for each line.
.. i18n:     * **[[ (o.prop=='draft')and 'YES' or 'NO' ]]** : Print YES or NO according the field 'prop'
.. i18n:     * **[[ round(o.quantity * o.price * 0.9, 2) ]]** : Operations are OK.
.. i18n:     * **[[ '%07d' % int(o.number) ]]** : Number formatting
.. i18n:     * **[[ reduce(lambda x, obj: x+obj.qty , list , 0 ) ]]** : Total qty of list (try "objects" as list)
.. i18n:     * **[[ user.name ]]** : user name
.. i18n:     * **[[ setLang(o.partner_id.lang) ]]** : Localized printings
.. i18n:     * **[[ time.strftime('%d/%m/%Y') ]]** : Show the time in format=dd/MM/YYYY, check python doc for more about "%d", ...
.. i18n:     * **[[ time.strftime(time.ctime()[0:10]) ]]** or **[[ time.strftime(time.ctime()[-4:]) ]]** : Prints only date.
.. i18n:     * **[[ time.ctime() ]]** : Prints the actual date & time
.. i18n:     * **[[ time.ctime().split()[3] ]]** : Prints only time
.. i18n:     * **[[ o.type in ['in_invoice', 'out_invoice'] and 'Invoice' or removeParentNode('tr') ]]** : If the type is 'in_invoice' or 'out_invoice' then the word 'Invoice' is printed, if it's neither the first node above it of type 'tr' will be removed.
..

    * **[[ repeatIn(objects,'o') ]]** : Loop on each objects selected for the print
    * **[[ repeatIn(o.invoice_line,'l') ]]** : Loop on every line
    * **[[ repeatIn(o.invoice_line,'l', 'td') ]]** : Loop on every line and make
      a new table cell for each line.
    * **[[ (o.prop=='draft')and 'YES' or 'NO' ]]** : Print YES or NO according the field 'prop'
    * **[[ round(o.quantity * o.price * 0.9, 2) ]]** : Operations are OK.
    * **[[ '%07d' % int(o.number) ]]** : Number formatting
    * **[[ reduce(lambda x, obj: x+obj.qty , list , 0 ) ]]** : Total qty of list (try "objects" as list)
    * **[[ user.name ]]** : user name
    * **[[ setLang(o.partner_id.lang) ]]** : Localized printings
    * **[[ time.strftime('%d/%m/%Y') ]]** : Show the time in format=dd/MM/YYYY, check python doc for more about "%d", ...
    * **[[ time.strftime(time.ctime()[0:10]) ]]** or **[[ time.strftime(time.ctime()[-4:]) ]]** : Prints only date.
    * **[[ time.ctime() ]]** : Prints the actual date & time
    * **[[ time.ctime().split()[3] ]]** : Prints only time
    * **[[ o.type in ['in_invoice', 'out_invoice'] and 'Invoice' or removeParentNode('tr') ]]** : If the type is 'in_invoice' or 'out_invoice' then the word 'Invoice' is printed, if it's neither the first node above it of type 'tr' will be removed.

.. i18n: One more interesting tag: if you want to print out the creator of an entry 
.. i18n: (create_uid) or the last one who wrote on an entry (write_uid) you have to add 
.. i18n: something like this to the class your report refers to:
..

One more interesting tag: if you want to print out the creator of an entry 
(create_uid) or the last one who wrote on an entry (write_uid) you have to add 
something like this to the class your report refers to:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     'create_uid': fields.many2one('res.users', 'User', readonly=1) 
..

.. code-block:: python

    'create_uid': fields.many2one('res.users', 'User', readonly=1) 

.. i18n: and then in your report it's like this to print out the corresponding name:
..

and then in your report it's like this to print out the corresponding name:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     o.create_uid.name 
..

.. code-block:: python

    o.create_uid.name 

.. i18n: Sometimes you might want to print out something only if a certain condition is 
.. i18n: met. You can construct it with the python logical operators "not", "and" and 
.. i18n: "or". Because every object in python has a logical value (TRUE or FALSE) you can 
.. i18n: construct something like this:
..

Sometimes you might want to print out something only if a certain condition is 
met. You can construct it with the python logical operators "not", "and" and 
"or". Because every object in python has a logical value (TRUE or FALSE) you can 
construct something like this:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     (o.prop=='draft') and 'YES' or 'NO' #prints YES or NO 
..

.. code-block:: python

    (o.prop=='draft') and 'YES' or 'NO' #prints YES or NO 

.. i18n: It works like this: `and` is higher priority than `or`, so that expression is
.. i18n: equivalent to this one:
..

It works like this: `and` is higher priority than `or`, so that expression is
equivalent to this one:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     ((o.prop=='draft') and 'YES') or 'NO' 
.. i18n:  
.. i18n: If `o.prop` is `'draft'`, then it evaluates like this:
.. i18n: 	#. `o.prop == 'draft'` is `True`.
.. i18n: 	#. `True and 'YES'` is `'YES'`. Because the left side is a "true" value, the
.. i18n: 	   `and` expression evaluates to the right side.
.. i18n: 	#. `'YES' or 'NO'` is `'YES'`. Because the left side is a "true" value, the
.. i18n: 	   `or` expression short cuts and ignores the right side. It evaluates to 
.. i18n: 	   the left side.
..

.. code-block:: python

    ((o.prop=='draft') and 'YES') or 'NO' 
 
If `o.prop` is `'draft'`, then it evaluates like this:
	#. `o.prop == 'draft'` is `True`.
	#. `True and 'YES'` is `'YES'`. Because the left side is a "true" value, the
	   `and` expression evaluates to the right side.
	#. `'YES' or 'NO'` is `'YES'`. Because the left side is a "true" value, the
	   `or` expression short cuts and ignores the right side. It evaluates to 
	   the left side.

.. i18n: If `o.prop` is something else like `'confirm'`, then it evaluates like this:
.. i18n: 	#. `o.prop == 'draft'` is `False`.
.. i18n: 	#. `False and 'YES'` is `False`. Because the left side is a "false" value, the
.. i18n: 	   `and` expression short cuts and ignores the right side. It evaluates to
.. i18n: 	   the left side.
.. i18n: 	#. `False or 'NO'` is `'NO'`. Because the left side is a "false" value, the
.. i18n: 	   `or` expression evaluates to the right side.
..

If `o.prop` is something else like `'confirm'`, then it evaluates like this:
	#. `o.prop == 'draft'` is `False`.
	#. `False and 'YES'` is `False`. Because the left side is a "false" value, the
	   `and` expression short cuts and ignores the right side. It evaluates to
	   the left side.
	#. `False or 'NO'` is `'NO'`. Because the left side is a "false" value, the
	   `or` expression evaluates to the right side.

.. i18n: One can use very complex structures. To learn more, see the python manuals
.. i18n: section on `Python's boolean operators`_.
..

One can use very complex structures. To learn more, see the python manuals
section on `Python's boolean operators`_.

.. i18n: python function "filter" can... filter: try something like:
..

python function "filter" can... filter: try something like:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     repeatIn(filter( lambda l: l.product_id.type=='service' ,o.invoice_line), 'line') 
..

.. code-block:: python

    repeatIn(filter( lambda l: l.product_id.type=='service' ,o.invoice_line), 'line') 

.. i18n: for printing only product with type='service' in a line's section.
..

for printing only product with type='service' in a line's section.

.. i18n: To display binary field image on report (to be checked)
..

To display binary field image on report (to be checked)

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     [[ setTag('para','image',{'width':'100.0','height':'80.0'}) ]] o.image or setTag('image','para') 
.. i18n:  
..

.. code-block:: python

    [[ setTag('para','image',{'width':'100.0','height':'80.0'}) ]] o.image or setTag('image','para') 
 

.. i18n: SXW2RML
.. i18n: -------
..

SXW2RML
-------

.. i18n: Open Report Manual
.. i18n: ++++++++++++++++++
..

Open Report Manual
++++++++++++++++++

.. i18n: About
.. i18n: """""
..

About
"""""

.. i18n: The OpenERP's report engine.
..

The OpenERP's report engine.

.. i18n: Open Report is a module that allows you to render high quality PDF document
.. i18n: from an OpenOffice template (.sxw) and any relational database. It can be used
.. i18n: as an OpenERP module or as a standalone program.
..

Open Report is a module that allows you to render high quality PDF document
from an OpenOffice template (.sxw) and any relational database. It can be used
as an OpenERP module or as a standalone program.

.. i18n: SXW to RML script setup - Windows users
.. i18n: """""""""""""""""""""""""""""""""""""""
..

SXW to RML script setup - Windows users
"""""""""""""""""""""""""""""""""""""""

.. i18n: In order to use the 'tiny_sxw2rml.py' Python script you need the following packages installed:
..

In order to use the 'tiny_sxw2rml.py' Python script you need the following packages installed:

.. i18n:     * Python (http://www.python.org)
.. i18n:     * ReportLab (http://www.reportlab.org)/(Installation)
.. i18n:     * Libxml for Python (http://users.skynet.be/sbi/libxml-python) 
..

    * Python (http://www.python.org)
    * ReportLab (http://www.reportlab.org)/(Installation)
    * Libxml for Python (http://users.skynet.be/sbi/libxml-python) 

.. i18n: SXW to RML script setup - Linux (Open source) users
.. i18n: """""""""""""""""""""""""""""""""""""""""""""""""""
..

SXW to RML script setup - Linux (Open source) users
"""""""""""""""""""""""""""""""""""""""""""""""""""

.. i18n: The **tiny_sxw2rml.py** can be found in the **base_report_designer** OpenERP module at this location::
.. i18n: 
.. i18n:   server/bin/addons/base_report_designer/wizard/tiny_sxw2rml/tiny_sxw2rml.py
..

The **tiny_sxw2rml.py** can be found in the **base_report_designer** OpenERP module at this location::

  server/bin/addons/base_report_designer/wizard/tiny_sxw2rml/tiny_sxw2rml.py

.. i18n: Ensure normalized_oo2rml.xsl is available to tiny_sxw2rml otherwise you will get an error like:
..

Ensure normalized_oo2rml.xsl is available to tiny_sxw2rml otherwise you will get an error like:

.. i18n:     * failed to load external entity normalized_oo2rml.xsl 
..

    * failed to load external entity normalized_oo2rml.xsl 

.. i18n: Running tiny_sxw2rml
.. i18n: """"""""""""""""""""
..

Running tiny_sxw2rml
""""""""""""""""""""

.. i18n: When you have all that installed just edit your report template and run the script with the following command:
.. i18n: ::
.. i18n: 
.. i18n:   tiny_sxw2rml.py template.sxw > template.rml
..

When you have all that installed just edit your report template and run the script with the following command:
::

  tiny_sxw2rml.py template.sxw > template.rml

.. i18n: Note: **tiny_sxw2rml.py** help suggests that you specify the output file with: "-o OUTPUT" but this does not seem to work as of V0.9.3 
..

Note: **tiny_sxw2rml.py** help suggests that you specify the output file with: "-o OUTPUT" but this does not seem to work as of V0.9.3 

.. i18n: OpenERP Server PDF Output 
.. i18n: --------------------------
..

OpenERP Server PDF Output 
--------------------------

.. i18n: Server PDF Output
.. i18n: +++++++++++++++++
..

Server PDF Output
+++++++++++++++++

.. i18n: About
.. i18n: """""
.. i18n: To generate the pdf from the rml file, OpenERP needs a rml parser.
..

About
"""""
To generate the pdf from the rml file, OpenERP needs a rml parser.

.. i18n: Parser
.. i18n: """"""
.. i18n: The parsers are generally put into the report folder of the module. Here is the code for the sale order report:
..

Parser
""""""
The parsers are generally put into the report folder of the module. Here is the code for the sale order report:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     import time
.. i18n:     from report import report_sxw
.. i18n: 
.. i18n:     class order(report_sxw.rml_parse):
.. i18n:         def __init__(self, cr, uid, name, context):
.. i18n:             super(order, self).__init__(cr, uid, name, context)
.. i18n:             self.localcontext.update({
.. i18n:                 'time': time,
.. i18n:             })
.. i18n: 
.. i18n:     report_sxw.report_sxw('report.sale.order', 'sale.order',
.. i18n:           'addons/sale/report/order.rml', parser=order, header=True)
..

.. code-block:: python

    import time
    from report import report_sxw

    class order(report_sxw.rml_parse):
        def __init__(self, cr, uid, name, context):
            super(order, self).__init__(cr, uid, name, context)
            self.localcontext.update({
                'time': time,
            })

    report_sxw.report_sxw('report.sale.order', 'sale.order',
          'addons/sale/report/order.rml', parser=order, header=True)

.. i18n: The parser inherit from the **report_sxw.rml_parse** object and it add to the localcontext, the function time so it will be possible to call it in the report.
..

The parser inherit from the **report_sxw.rml_parse** object and it add to the localcontext, the function time so it will be possible to call it in the report.

.. i18n: After an instance of **report_sxw.report_sxw** is created with the parameters:
..

After an instance of **report_sxw.report_sxw** is created with the parameters:

.. i18n:     * the name of the report
.. i18n:     * the object name on which the report is defined
.. i18n:     * the path to the rml file
.. i18n:     * the parser to use for the report (by default rml_parse)
.. i18n:     * the header to use from the company configuration
.. i18n:         * ``'external'`` (default)
.. i18n:         * ``'internal'``
.. i18n:         * ``'internal landscape'``
.. i18n:         * ``False`` - use the report's own header
..

    * the name of the report
    * the object name on which the report is defined
    * the path to the rml file
    * the parser to use for the report (by default rml_parse)
    * the header to use from the company configuration
        * ``'external'`` (default)
        * ``'internal'``
        * ``'internal landscape'``
        * ``False`` - use the report's own header

.. i18n: The xml definition
.. i18n: """"""""""""""""""
..

The xml definition
""""""""""""""""""

.. i18n: To be visible from the client, the report must be declared in an xml file (generally: "module_name"_report.xml) that must be put in the **__openerp__.py** file
..

To be visible from the client, the report must be declared in an xml file (generally: "module_name"_report.xml) that must be put in the **__openerp__.py** file

.. i18n: Here is an example for the sale order report:
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 	<openerp>
.. i18n: 		<data>
.. i18n: 			<report
.. i18n: 	   			id="report_sale_order"
.. i18n: 	   			string="Print Order"
.. i18n: 	   			model="sale.order"
.. i18n: 	   			name="sale.order"
.. i18n: 	   			rml="sale/report/order.rml"
.. i18n: 	   			auto="False"/>
.. i18n: 	   			header="False"/>
.. i18n: 	 	</data>
.. i18n: 	</openerp>
..

Here is an example for the sale order report:
::

	<?xml version="1.0"?>
	<openerp>
		<data>
			<report
	   			id="report_sale_order"
	   			string="Print Order"
	   			model="sale.order"
	   			name="sale.order"
	   			rml="sale/report/order.rml"
	   			auto="False"/>
	   			header="False"/>
	 	</data>
	</openerp>

.. i18n: The arguments are:
..

The arguments are:

.. i18n:     * **id**: the id of the report like any xml tag in OpenERP
.. i18n:     * **string**: the string that will be display on the Client button
.. i18n:     * **model**: the object on which the report will run
.. i18n:     * **name**: the name of the report without the first "report."
.. i18n:     * **rml**: the path to the rml file
.. i18n:     * **auto**: boolean to specify if the server must generate a default parser or not
.. i18n:     * **header**: allows to enable or disable the report header. To edit them for a specific company, go to: Administration -> Users -> Company's structure -> Companies. There, select and edit your company: the "Header/Footer" tab allows you to edit corporate header/footer.  
..

    * **id**: the id of the report like any xml tag in OpenERP
    * **string**: the string that will be display on the Client button
    * **model**: the object on which the report will run
    * **name**: the name of the report without the first "report."
    * **rml**: the path to the rml file
    * **auto**: boolean to specify if the server must generate a default parser or not
    * **header**: allows to enable or disable the report header. To edit them for a specific company, go to: Administration -> Users -> Company's structure -> Companies. There, select and edit your company: the "Header/Footer" tab allows you to edit corporate header/footer.  

.. i18n: .. _Python's boolean operators: http://docs.python.org/library/stdtypes.html#boolean-operations-and-or-not
..

.. _Python's boolean operators: http://docs.python.org/library/stdtypes.html#boolean-operations-and-or-not

.. i18n: XSL:RML reports
.. i18n: ===============
..

XSL:RML reports
===============

.. i18n: RML reports don't require programming but require two simple XML files to be written:
..

RML reports don't require programming but require two simple XML files to be written:

.. i18n:     * a file describing the data to export (\*.xml)
.. i18n:     * a file containing the presentation rules to apply to that data (\*.xsl)
..

    * a file describing the data to export (\*.xml)
    * a file containing the presentation rules to apply to that data (\*.xsl)

.. i18n: .. figure::  images/automatic-reports.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/automatic-reports.png
   :scale: 85
   :align: center

.. i18n: The role of the XML template is to describe which fields of the resource have to be exported (by the server). The XSL:RML style sheet deals with the layout of the exported data as well as the "static text" of reports. Static text is referring to the text which is common to all reports of the same type (for example, the title of table columns).
..

The role of the XML template is to describe which fields of the resource have to be exported (by the server). The XSL:RML style sheet deals with the layout of the exported data as well as the "static text" of reports. Static text is referring to the text which is common to all reports of the same type (for example, the title of table columns).

.. i18n: **Example**
..

**Example**

.. i18n: Here is, as an example, the different files for the simplest report in the ERP.
..

Here is, as an example, the different files for the simplest report in the ERP.

.. i18n: .. figure::  images/ids-report.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/ids-report.png
   :scale: 85
   :align: center

.. i18n: **XML Template**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 
.. i18n: 	    <ids> 
.. i18n: 	    <id type="fields" name="id">
.. i18n: 
.. i18n: 		<name type="field" name="name"/> 
.. i18n: 		<ref type="field" name="ref"/> 
.. i18n: 
.. i18n: 	    </id> 
.. i18n: 	    </ids> 
..

**XML Template**
::

	<?xml version="1.0"?>

	    <ids> 
	    <id type="fields" name="id">

		<name type="field" name="name"/> 
		<ref type="field" name="ref"/> 

	    </id> 
	    </ids> 

.. i18n: **XML data file (generated)**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 
.. i18n: 	    <ids> 
.. i18n: 	    <id>
.. i18n: 
.. i18n: 		<name>Tiny sprl</name> 
.. i18n: 		<ref>pnk00</ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>ASUS</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Agrolait</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Banque Plein-Aux-As</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>China Export</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Ditrib PC</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Ecole de Commerce de Liege</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Elec Import</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Maxtor</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Mediapole SPRL</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Opensides sprl</name> 
.. i18n: 		<ref>os</ref> 
.. i18n: 
.. i18n: 	    </id><id>
.. i18n: 
.. i18n: 		<name>Tecsas sarl</name> 
.. i18n: 		<ref></ref> 
.. i18n: 
.. i18n: 	    </id> 
.. i18n: 	    </ids> 
..

**XML data file (generated)**
::

	<?xml version="1.0"?>

	    <ids> 
	    <id>

		<name>Tiny sprl</name> 
		<ref>pnk00</ref> 

	    </id><id>

		<name>ASUS</name> 
		<ref></ref> 

	    </id><id>

		<name>Agrolait</name> 
		<ref></ref> 

	    </id><id>

		<name>Banque Plein-Aux-As</name> 
		<ref></ref> 

	    </id><id>

		<name>China Export</name> 
		<ref></ref> 

	    </id><id>

		<name>Ditrib PC</name> 
		<ref></ref> 

	    </id><id>

		<name>Ecole de Commerce de Liege</name> 
		<ref></ref> 

	    </id><id>

		<name>Elec Import</name> 
		<ref></ref> 

	    </id><id>

		<name>Maxtor</name> 
		<ref></ref> 

	    </id><id>

		<name>Mediapole SPRL</name> 
		<ref></ref> 

	    </id><id>

		<name>Opensides sprl</name> 
		<ref>os</ref> 

	    </id><id>

		<name>Tecsas sarl</name> 
		<ref></ref> 

	    </id> 
	    </ids> 

.. i18n: **XSL stylesheet**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0" encoding="utf-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
.. i18n: 
.. i18n: 	    <xsl:template match="/">
.. i18n: 
.. i18n: 		<xsl:apply-templates select="ids"/> 
.. i18n: 
.. i18n: 	    </xsl:template> 
.. i18n: 
.. i18n: 	    <xsl:template match="ids">
.. i18n: 
.. i18n: 		<document>
.. i18n: 
.. i18n: 		    <template pageSize="21cm,29.7cm">
.. i18n: 
.. i18n: 		        <pageTemplate>
.. i18n: 
.. i18n: 		            <frame id="col1" x1="2cm" y1="2.4cm" width="8cm" height="26cm"/> 
.. i18n: 		            <frame id="col2" x1="11cm" y1="2.4cm" width="8cm" height="26cm"/> 
.. i18n: 
.. i18n: 		        </pageTemplate> 
.. i18n: 
.. i18n: 		    </template> 
.. i18n: 
.. i18n: 		<stylesheet>
.. i18n: 
.. i18n: 		    <blockTableStyle id="ids"> 
.. i18n: 
.. i18n: 		        <blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/> 
.. i18n: 		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,0"/> 
.. i18n: 
.. i18n: 		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-1"/> 
.. i18n: 
.. i18n: 		    </blockTableStyle> 
.. i18n: 
.. i18n: 		</stylesheet> 
.. i18n: 
.. i18n: 		<story>
.. i18n: 
.. i18n: 		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">
.. i18n: 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td t="1">Ref.</td> 
.. i18n: 		            <td t="1">Name</td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <xsl:apply-templates select="id"/> 
.. i18n: 
.. i18n: 		    </blockTable> 
.. i18n: 
.. i18n: 		</story> 
.. i18n: 		</document> 
.. i18n: 
.. i18n: 	    </xsl:template> 
.. i18n: 
.. i18n: 	    <xsl:template match="id">
.. i18n: 
.. i18n: 		<tr>
.. i18n: 
.. i18n: 		    <td><xsl:value-of select="ref"/></td> 
.. i18n: 		    <td><para><xsl:value-of select="name"/></para></td> 
.. i18n: 
.. i18n: 		</tr> 
.. i18n: 
.. i18n: 	    </xsl:template> 
.. i18n: 	    </xsl:stylesheet> 
..

**XSL stylesheet**
::

	<?xml version="1.0" encoding="utf-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

	    <xsl:template match="/">

		<xsl:apply-templates select="ids"/> 

	    </xsl:template> 

	    <xsl:template match="ids">

		<document>

		    <template pageSize="21cm,29.7cm">

		        <pageTemplate>

		            <frame id="col1" x1="2cm" y1="2.4cm" width="8cm" height="26cm"/> 
		            <frame id="col2" x1="11cm" y1="2.4cm" width="8cm" height="26cm"/> 

		        </pageTemplate> 

		    </template> 

		<stylesheet>

		    <blockTableStyle id="ids"> 

		        <blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/> 
		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,0"/> 

		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-1"/> 

		    </blockTableStyle> 

		</stylesheet> 

		<story>

		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

		        <tr>

		            <td t="1">Ref.</td> 
		            <td t="1">Name</td> 

		        </tr> 
		        <xsl:apply-templates select="id"/> 

		    </blockTable> 

		</story> 
		</document> 

	    </xsl:template> 

	    <xsl:template match="id">

		<tr>

		    <td><xsl:value-of select="ref"/></td> 
		    <td><para><xsl:value-of select="name"/></para></td> 

		</tr> 

	    </xsl:template> 
	    </xsl:stylesheet> 

.. i18n: **Resulting RML file (generated)**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 
.. i18n: 	    <document> 
.. i18n: 	    ...
.. i18n: 
.. i18n: 		<story>
.. i18n: 
.. i18n: 		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">
.. i18n: 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td t="1">Ref.</td> 
.. i18n: 		            <td t="1">Name</td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td>pnk00</td> 
.. i18n: 		            <td><para>Tiny sprl</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>ASUS</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Agrolait</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Banque Plein-Aux-As</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>China Export</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Ditrib PC</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Ecole de Commerce de Liege</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Elec Import</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Maxtor</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Mediapole SPRL</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr>
.. i18n: 
.. i18n: 		            <td>os</td> 
.. i18n: 		            <td><para>Opensides sprl</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 		        <tr> 
.. i18n: 		        <td></td>
.. i18n: 
.. i18n: 		            <td><para>Tecsas sarl</para></td> 
.. i18n: 
.. i18n: 		        </tr> 
.. i18n: 
.. i18n: 		    </blockTable> 
.. i18n: 
.. i18n: 		</story> 
.. i18n: 
.. i18n: 	    </document> 
..

**Resulting RML file (generated)**
::

	<?xml version="1.0"?>

	    <document> 
	    ...

		<story>

		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

		        <tr>

		            <td t="1">Ref.</td> 
		            <td t="1">Name</td> 

		        </tr> 
		        <tr>

		            <td>pnk00</td> 
		            <td><para>Tiny sprl</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>ASUS</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Agrolait</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Banque Plein-Aux-As</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>China Export</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Ditrib PC</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Ecole de Commerce de Liege</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Elec Import</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Maxtor</para></td> 

		        </tr> 
		        <tr>

		            <td></td> 
		            <td><para>Mediapole SPRL</para></td> 

		        </tr> 
		        <tr>

		            <td>os</td> 
		            <td><para>Opensides sprl</para></td> 

		        </tr> 
		        <tr> 
		        <td></td>

		            <td><para>Tecsas sarl</para></td> 

		        </tr> 

		    </blockTable> 

		</story> 

	    </document> 

.. i18n: For more information on the formats used:
..

For more information on the formats used:

.. i18n:     * `RML user guide`_
.. i18n:     * `XSL specification`_ 
.. i18n:     * `XSL tutorial`_  
..

    * `RML user guide`_
    * `XSL specification`_ 
    * `XSL tutorial`_  

.. i18n: All these formats are extensions of the `XML specification`_.
..

All these formats are extensions of the `XML specification`_.

.. i18n: .. _RML user guide: http://www.reportlab.com/docs/rml2pdf-userguide.pdf  
.. i18n: .. _XSL specification: http://www.w3.org/TR/xslt
.. i18n: .. _XSL tutorial: http://www.zvon.org/xxl/XSLTutorial/Books/Output/contents.html
.. i18n: .. _XML specification: http://www.w3.org/XML/
..

.. _RML user guide: http://www.reportlab.com/docs/rml2pdf-userguide.pdf  
.. _XSL specification: http://www.w3.org/TR/xslt
.. _XSL tutorial: http://www.zvon.org/xxl/XSLTutorial/Books/Output/contents.html
.. _XML specification: http://www.w3.org/XML/

.. i18n: XML Template
.. i18n: ------------
..

XML Template
------------

.. i18n: XML templates are simple XML files describing which fields among all available object fields are necessary for the report.
..

XML templates are simple XML files describing which fields among all available object fields are necessary for the report.

.. i18n: File format
.. i18n: +++++++++++
..

File format
+++++++++++

.. i18n: Tag names can be chosen arbitrarily (it must be valid XML though). In the XSL file, you will have to use those names. Most of the time, the name of a tag will be the same as the name of the object field it refers to.
..

Tag names can be chosen arbitrarily (it must be valid XML though). In the XSL file, you will have to use those names. Most of the time, the name of a tag will be the same as the name of the object field it refers to.

.. i18n: Nodes without **type** attribute are transferred identically into the XML destination file (the data file). Nodes with a type attribute will be parsed by the server and their content will be replaced by data coming from objects. In addition to the type attribute, nodes have other possible attributes. These attributes depend on the type of the node (each node type supports or needs different attributes). Most node types have a name attribute, which refers to the  **name** of a field of the object on which we work.
..

Nodes without **type** attribute are transferred identically into the XML destination file (the data file). Nodes with a type attribute will be parsed by the server and their content will be replaced by data coming from objects. In addition to the type attribute, nodes have other possible attributes. These attributes depend on the type of the node (each node type supports or needs different attributes). Most node types have a name attribute, which refers to the  **name** of a field of the object on which we work.

.. i18n: As for the "browse" method on objects, field names in reports can use a notation similar to the notation found in object oriented programming languages. It means that "relation fields" can be used as "bridges" to fetch data from other (related) objects.
..

As for the "browse" method on objects, field names in reports can use a notation similar to the notation found in object oriented programming languages. It means that "relation fields" can be used as "bridges" to fetch data from other (related) objects.

.. i18n: Let's use the "account.transfer" object as an example. It contains a partner_id field. This field is a relation field ("many to one") pointing to the "res.partner" object. Let's suppose that we want to create a report for transfers and in this report, we want to use the name of the recipient partner. This name could be accessed using the following expression as the name of the field:
..

Let's use the "account.transfer" object as an example. It contains a partner_id field. This field is a relation field ("many to one") pointing to the "res.partner" object. Let's suppose that we want to create a report for transfers and in this report, we want to use the name of the recipient partner. This name could be accessed using the following expression as the name of the field:

.. i18n:     partner_id.name 
..

    partner_id.name 

.. i18n: Possible types
.. i18n: ++++++++++++++
..

Possible types
++++++++++++++

.. i18n: Here is the list of available field types:
..

Here is the list of available field types:

.. i18n:     * **field**: It is the simplest type. For nodes of this type, the server replaces the node content by the value of the field whose name is given in the name attribute. 
.. i18n: 
.. i18n:     * **fields**: when this type of node is used, the server will generate a node in the XML data file for each unique value of the field whose name is given in the name attribute. 
..

    * **field**: It is the simplest type. For nodes of this type, the server replaces the node content by the value of the field whose name is given in the name attribute. 

    * **fields**: when this type of node is used, the server will generate a node in the XML data file for each unique value of the field whose name is given in the name attribute. 

.. i18n:     Notes:
..

    Notes:

.. i18n:         ** This node type is often used with "id" as its name attribute. This has the effect of creating one node for each resource selected in the interface by the user. 
.. i18n:         ** The semantics of a node <node type="fields" name="field_name"> is similar to an SQL statement of the form "SELECT FROM object_table WHERE id in identifier_list **GROUP BY** field_name" where identifier_list is the list of ids of the resources selected by the ::user (in the interface). 
.. i18n: 
.. i18n:     * **eval**: This node type evaluate the expression given in the *expr* attribute. This expression may be any Python expression and may contain objects fields names. 
.. i18n: 
.. i18n:     * **zoom**: This node type allows to "enter" into the resource referenced by the relation field whose name is given in the name attribute. It means that its child nodes will be able to access the fields of that resource without having to prefix them with the field name that makes the link with the other object. In our example above, we could also have accessed the field name of the partner with the following: 
.. i18n: 
.. i18n:   ::
.. i18n: 
.. i18n: 	<partner type="zoom" name="partner_id">
.. i18n: 
.. i18n: 		<name type="field" name="name"/> 
.. i18n: 
.. i18n: 	</partner> 
.. i18n: 
.. i18n: 	In this precise case, there is of course no point in using this notation instead of the standard notation below: 
.. i18n: 
.. i18n: 	<name type="field" name="partner_id.name"/> 
..

        ** This node type is often used with "id" as its name attribute. This has the effect of creating one node for each resource selected in the interface by the user. 
        ** The semantics of a node <node type="fields" name="field_name"> is similar to an SQL statement of the form "SELECT FROM object_table WHERE id in identifier_list **GROUP BY** field_name" where identifier_list is the list of ids of the resources selected by the ::user (in the interface). 

    * **eval**: This node type evaluate the expression given in the *expr* attribute. This expression may be any Python expression and may contain objects fields names. 

    * **zoom**: This node type allows to "enter" into the resource referenced by the relation field whose name is given in the name attribute. It means that its child nodes will be able to access the fields of that resource without having to prefix them with the field name that makes the link with the other object. In our example above, we could also have accessed the field name of the partner with the following: 

  ::

	<partner type="zoom" name="partner_id">

		<name type="field" name="name"/> 

	</partner> 

	In this precise case, there is of course no point in using this notation instead of the standard notation below: 

	<name type="field" name="partner_id.name"/> 

.. i18n: The **zoom** type is only useful when we want to recover several fields in the same object.
..

The **zoom** type is only useful when we want to recover several fields in the same object.

.. i18n:     * **function**: returns the result of the call to the function whose name is given in the name attribute. This function must be part of the list of predefined functions. For the moment, the only available function is today, which returns the current date. 
.. i18n: 
.. i18n:     * **call**: calls the object method whose name is given in the name attribute with the arguments given in the args attribute. The result is stored into a dictionary of the form {'name_of_variable': value, ... } and can be accessed through child nodes. These nodes must have a value attribute which correspond to one of the keys of the dictionary returned by the method. 
..

    * **function**: returns the result of the call to the function whose name is given in the name attribute. This function must be part of the list of predefined functions. For the moment, the only available function is today, which returns the current date. 

    * **call**: calls the object method whose name is given in the name attribute with the arguments given in the args attribute. The result is stored into a dictionary of the form {'name_of_variable': value, ... } and can be accessed through child nodes. These nodes must have a value attribute which correspond to one of the keys of the dictionary returned by the method. 

.. i18n: **Example**:
.. i18n: ::
.. i18n: 
.. i18n: 	<cost type="call" name="compute_seller_costs" args="">
.. i18n: 
.. i18n: 	    <name value="name"/> 
.. i18n: 	    <amount value="amount"/> 
.. i18n: 
.. i18n: 	</cost> 
..

**Example**:
::

	<cost type="call" name="compute_seller_costs" args="">

	    <name value="name"/> 
	    <amount value="amount"/> 

	</cost> 

.. i18n: **TODO**: documenter format methode appellée def compute_buyer_costs(self, cr, uid, ids, \*args):
..

**TODO**: documenter format methode appellée def compute_buyer_costs(self, cr, uid, ids, \*args):

.. i18n:     * **attachment**: extract the first attachment of the resource whose id is taken from the field whose name is given in the name attribute, and put it as an image in the report. 
..

    * **attachment**: extract the first attachment of the resource whose id is taken from the field whose name is given in the name attribute, and put it as an image in the report. 

.. i18n: Example:
.. i18n: 	<image type="attachment" name="id"/> 
..

Example:
	<image type="attachment" name="id"/> 

.. i18n: **Example**
..

**Example**

.. i18n: Here is an example of XML file:
.. i18n: ::
.. i18n: 
.. i18n: 	    <?xml version="1.0" encoding="ISO-8859-1"?> 
.. i18n: 	    <transfer-list>
.. i18n: 
.. i18n: 		<transfer type="fields" name="id">
.. i18n: 
.. i18n: 		    <name type="field" name="name"/> 
.. i18n: 		    <partner_id type="field" name="partner_id.name"/> 
.. i18n: 		    <date type="field" name="date"/> 
.. i18n: 		    <type type="field" name="type"/> 
.. i18n: 		    <reference type="field" name="reference"/> 
.. i18n: 		    <amount type="field" name="amount"/> 
.. i18n: 		    <change type="field" name="change"/> 
.. i18n: 
.. i18n: 		</transfer> 
.. i18n: 
.. i18n: 	    </transfer-list> 
..

Here is an example of XML file:
::

	    <?xml version="1.0" encoding="ISO-8859-1"?> 
	    <transfer-list>

		<transfer type="fields" name="id">

		    <name type="field" name="name"/> 
		    <partner_id type="field" name="partner_id.name"/> 
		    <date type="field" name="date"/> 
		    <type type="field" name="type"/> 
		    <reference type="field" name="reference"/> 
		    <amount type="field" name="amount"/> 
		    <change type="field" name="change"/> 

		</transfer> 

	    </transfer-list> 

.. i18n: Introduction to RML
.. i18n: -------------------
..

Introduction to RML
-------------------

.. i18n: For more information on the RML format, please refer to the official Reportlab documentation.
..

For more information on the RML format, please refer to the official Reportlab documentation.

.. i18n:     * http://www.reportlab.com/docs/rml2pdf-userguide.pdf 
..

    * http://www.reportlab.com/docs/rml2pdf-userguide.pdf 

.. i18n: XSL:RML Stylesheet
.. i18n: ------------------
..

XSL:RML Stylesheet
------------------

.. i18n: There are two possibilities to do a XSL style sheet for a report. Either making everything by yourself, or use our predefined templates
..

There are two possibilities to do a XSL style sheet for a report. Either making everything by yourself, or use our predefined templates

.. i18n: Either freestyle or use corporate_defaults + rml_template
..

Either freestyle or use corporate_defaults + rml_template

.. i18n:     import rml_template.xsl 
..

    import rml_template.xsl 

.. i18n:         required templates:
..

        required templates:

.. i18n:             - frames? 
.. i18n:             - stylesheet 
.. i18n:             - story 
..

            - frames? 
            - stylesheet 
            - story 

.. i18n:         optional templates: 
..

        optional templates: 

.. i18n: Translations
.. i18n: ++++++++++++
..

Translations
++++++++++++

.. i18n: As OpenERP can be used in several languages, reports must be translatable. But in a report, everything doesn't have to be translated : only the actual text has to be translated, not the formatting codes. A field will be processed by the translation system if the XML tag which surrounds it (whatever it is) has a t="1" attribute. The server will translate all the fields with such attributes in the report generation process.
..

As OpenERP can be used in several languages, reports must be translatable. But in a report, everything doesn't have to be translated : only the actual text has to be translated, not the formatting codes. A field will be processed by the translation system if the XML tag which surrounds it (whatever it is) has a t="1" attribute. The server will translate all the fields with such attributes in the report generation process.

.. i18n: Useful links
.. i18n: ++++++++++++
..

Useful links
++++++++++++

.. i18n:     * url=http://www.reportlab.com/docs/rml2pdf-userguide.pdf RML UserGuide (pdf) (reportlab.com) 
.. i18n: 
.. i18n:     * http://www.zvon.org/xxl/XSLTutorial/Output/index.html XSL Tutorial (zvon.org)
.. i18n:     * http://www.zvon.org/xxl/XSLTreference/Output/index.html XSL Reference (zvon.org)
.. i18n:     * http://www.w3schools.com/xsl/ XSL tutorial and references (W3Schools)
.. i18n:     * http://www.w3.org/TR/xslt/ XSL Specification (W3C) 
..

    * url=http://www.reportlab.com/docs/rml2pdf-userguide.pdf RML UserGuide (pdf) (reportlab.com) 

    * http://www.zvon.org/xxl/XSLTutorial/Output/index.html XSL Tutorial (zvon.org)
    * http://www.zvon.org/xxl/XSLTreference/Output/index.html XSL Reference (zvon.org)
    * http://www.w3schools.com/xsl/ XSL tutorial and references (W3Schools)
    * http://www.w3.org/TR/xslt/ XSL Specification (W3C) 

.. i18n: Example (with corporate defaults)
.. i18n: +++++++++++++++++++++++++++++++++
.. i18n: ::
.. i18n: 
.. i18n: 	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
.. i18n: 
.. i18n: 		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
.. i18n: 		<xsl:import href="../../base/report/rml_template.xsl"/> 
.. i18n: 		<xsl:variable name="page_format">a4_normal</xsl:variable> 
.. i18n: 		<xsl:template match="/">
.. i18n: 
.. i18n: 		    <xsl:call-template name="rml"/> 
.. i18n: 
.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template name="stylesheet">
.. i18n: 
.. i18n: 		    </xsl:template> 
.. i18n: 
.. i18n: 		<xsl:template name="story">
.. i18n: 
.. i18n: 		    <xsl:apply-templates select="transfer-list"/> 
.. i18n: 
.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template match="transfer-list">
.. i18n: 
.. i18n: 		    <xsl:apply-templates select="transfer"/> 
.. i18n: 
.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template match="transfer">
.. i18n: 
.. i18n: 		    <setNextTemplate name="other_pages"/> 
.. i18n: 		    <para>
.. i18n: 
.. i18n: 		        Document: <xsl:value-of select="name"/> 
.. i18n: 
.. i18n: 		    </para><para>
.. i18n: 
.. i18n: 		        Type: <xsl:value-of select="type"/> 
.. i18n: 
.. i18n: 		    </para><para>
.. i18n: 
.. i18n: 		        Reference: <xsl:value-of select="reference"/> 
.. i18n: 
.. i18n: 		    </para><para>
.. i18n: 
.. i18n: 		        Partner ID: <xsl:value-of select="partner_id"/> 
.. i18n: 
.. i18n: 		    </para><para>
.. i18n: 
.. i18n: 		        Date: <xsl:value-of select="date"/> 
.. i18n: 
.. i18n: 		    </para><para>
.. i18n: 
.. i18n: 		        Amount: <xsl:value-of select="amount"/> 
.. i18n: 
.. i18n: 		    </para> 
.. i18n: 		    <xsl:if test="number(change)>0">
.. i18n: 
.. i18n: 		        <para>
.. i18n: 
.. i18n: 		            Change: <xsl:value-of select="change"/> 
.. i18n: 
.. i18n: 		        </para> 
.. i18n: 
.. i18n: 		    </xsl:if> 
.. i18n: 		    <setNextTemplate name="first_page"/> 
.. i18n: 		    <pageBreak/> 
.. i18n: 
.. i18n: 		</xsl:template> 
.. i18n: 
.. i18n: 	    </xsl:stylesheet> 
..

Example (with corporate defaults)
+++++++++++++++++++++++++++++++++
::

	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
		<xsl:import href="../../base/report/rml_template.xsl"/> 
		<xsl:variable name="page_format">a4_normal</xsl:variable> 
		<xsl:template match="/">

		    <xsl:call-template name="rml"/> 

		</xsl:template> 
		<xsl:template name="stylesheet">

		    </xsl:template> 

		<xsl:template name="story">

		    <xsl:apply-templates select="transfer-list"/> 

		</xsl:template> 
		<xsl:template match="transfer-list">

		    <xsl:apply-templates select="transfer"/> 

		</xsl:template> 
		<xsl:template match="transfer">

		    <setNextTemplate name="other_pages"/> 
		    <para>

		        Document: <xsl:value-of select="name"/> 

		    </para><para>

		        Type: <xsl:value-of select="type"/> 

		    </para><para>

		        Reference: <xsl:value-of select="reference"/> 

		    </para><para>

		        Partner ID: <xsl:value-of select="partner_id"/> 

		    </para><para>

		        Date: <xsl:value-of select="date"/> 

		    </para><para>

		        Amount: <xsl:value-of select="amount"/> 

		    </para> 
		    <xsl:if test="number(change)>0">

		        <para>

		            Change: <xsl:value-of select="change"/> 

		        </para> 

		    </xsl:if> 
		    <setNextTemplate name="first_page"/> 
		    <pageBreak/> 

		</xsl:template> 

	    </xsl:stylesheet> 

.. i18n: Reports without corporate header 
.. i18n: ================================
..

Reports without corporate header 
================================

.. i18n: **Example (with corporate defaults):**
.. i18n: ::
.. i18n: 
.. i18n: 	<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
.. i18n: 	     <xsl:import href="../../base/report/rml_template.xsl"/>
.. i18n: 	     <xsl:variable name="page_format">a4_normal</xsl:variable>
.. i18n: 	 
.. i18n: 	     <xsl:template match="/">
.. i18n: 		  <xsl:call-template name="rml"/>
.. i18n: 	     </xsl:template>
.. i18n: 	 
.. i18n: 	     <xsl:template name="stylesheet">
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template name="story">
.. i18n: 		   <xsl:apply-templates select="transfer-list"/>
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template match="transfer-list">
.. i18n: 		   <xsl:apply-templates select="transfer"/>
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template match="transfer">
.. i18n: 		   <setNextTemplate name="other_pages"/>
.. i18n: 	   
.. i18n: 		   <para>
.. i18n: 		         Document: <xsl:value-of select="name"/>
.. i18n: 		   </para><para>
.. i18n: 		         Type: <xsl:value-of select="type"/>
.. i18n: 		   </para><para>
.. i18n: 		         Reference: <xsl:value-of select="reference"/>
.. i18n: 		   </para><para>
.. i18n: 		         Partner ID: <xsl:value-of select="partner_id"/>
.. i18n: 		   </para><para>
.. i18n: 		         Date: <xsl:value-of select="date"/>
.. i18n: 		   </para><para>
.. i18n: 		         Amount: <xsl:value-of select="amount"/>
.. i18n: 		   </para>
.. i18n: 	   
.. i18n: 		   <xsl:if test="number(change)>0">
.. i18n: 		        <para>
.. i18n: 		              Change: <xsl:value-of select="change"/>
.. i18n: 		        </para>
.. i18n: 		   </xsl:if>
.. i18n: 	   
.. i18n: 		   <setNextTemplate name="first_page"/> 
.. i18n: 		  <pageBreak/>
.. i18n: 	     </xsl:template>
.. i18n: 	</xsl:stylesheet>
..

**Example (with corporate defaults):**
::

	<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
	     <xsl:import href="../../base/report/rml_template.xsl"/>
	     <xsl:variable name="page_format">a4_normal</xsl:variable>
	 
	     <xsl:template match="/">
		  <xsl:call-template name="rml"/>
	     </xsl:template>
	 
	     <xsl:template name="stylesheet">
	      </xsl:template>
	  
	      <xsl:template name="story">
		   <xsl:apply-templates select="transfer-list"/>
	      </xsl:template>
	  
	      <xsl:template match="transfer-list">
		   <xsl:apply-templates select="transfer"/>
	      </xsl:template>
	  
	      <xsl:template match="transfer">
		   <setNextTemplate name="other_pages"/>
	   
		   <para>
		         Document: <xsl:value-of select="name"/>
		   </para><para>
		         Type: <xsl:value-of select="type"/>
		   </para><para>
		         Reference: <xsl:value-of select="reference"/>
		   </para><para>
		         Partner ID: <xsl:value-of select="partner_id"/>
		   </para><para>
		         Date: <xsl:value-of select="date"/>
		   </para><para>
		         Amount: <xsl:value-of select="amount"/>
		   </para>
	   
		   <xsl:if test="number(change)>0">
		        <para>
		              Change: <xsl:value-of select="change"/>
		        </para>
		   </xsl:if>
	   
		   <setNextTemplate name="first_page"/> 
		  <pageBreak/>
	     </xsl:template>
	</xsl:stylesheet>

.. i18n: Each report with its own corporate header 
.. i18n: =========================================
..

Each report with its own corporate header 
=========================================

.. i18n: **Example (with corporate defaults):**
.. i18n: ::
.. i18n: 
.. i18n: 	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
.. i18n: 
.. i18n: 		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
.. i18n: 		<xsl:import href="../../base/report/rml_template.xsl"/> 
.. i18n: 		<xsl:variable name="page_format">a4_normal</xsl:variable> 
.. i18n: 		..................... 
.. i18n: 		</xsl:template> 
.. i18n: 
.. i18n: 	    </xsl:stylesheet> 
..

**Example (with corporate defaults):**
::

	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
		<xsl:import href="../../base/report/rml_template.xsl"/> 
		<xsl:variable name="page_format">a4_normal</xsl:variable> 
		..................... 
		</xsl:template> 

	    </xsl:stylesheet> 

.. i18n: Bar Codes 
.. i18n: =========
..

Bar Codes 
=========

.. i18n: Barcodes in RML files
.. i18n: ---------------------
..

Barcodes in RML files
---------------------

.. i18n: Barcodes can be generated using the <barCode> tag in RML files. The following formats are supported:
..

Barcodes can be generated using the <barCode> tag in RML files. The following formats are supported:

.. i18n:     * codabar
.. i18n:     * code11
.. i18n:     * code128 (default if no 'code' specified')
.. i18n:     * standard39
.. i18n:     * standard93
.. i18n:     * i2of5
.. i18n:     * extended39
.. i18n:     * extended93
.. i18n:     * msi
.. i18n:     * fim
.. i18n:     * postnet 
.. i18n:     * ean13
.. i18n:     * ean8
.. i18n:     * usps_4state
.. i18n:                                         
.. i18n:   
.. i18n: You can change the following attributes for rendering your barcode:
.. i18n: 
.. i18n:     * 'code': 'char'
.. i18n:     * 'ratio':'float'
.. i18n:     * 'xdim':'unit'
.. i18n:     * 'height':'unit'
.. i18n:     * 'checksum':'bool'
.. i18n:     * 'quiet':'bool' 
..

    * codabar
    * code11
    * code128 (default if no 'code' specified')
    * standard39
    * standard93
    * i2of5
    * extended39
    * extended93
    * msi
    * fim
    * postnet 
    * ean13
    * ean8
    * usps_4state
                                        
  
You can change the following attributes for rendering your barcode:

    * 'code': 'char'
    * 'ratio':'float'
    * 'xdim':'unit'
    * 'height':'unit'
    * 'checksum':'bool'
    * 'quiet':'bool' 

.. i18n: Examples:
..

Examples:

.. i18n:     <barcode code="code128" xdim="28cm" ratio="2.2">`SN12345678</barcode> 
..

    <barcode code="code128" xdim="28cm" ratio="2.2">`SN12345678</barcode> 

.. i18n: How to add a new report
.. i18n: =======================
..

How to add a new report
=======================

.. i18n: In 4.0.X
..

In 4.0.X

.. i18n:     Administration -> Custom -> Low Level -> Base->Actions -> ir.actions.report.xml 
..

    Administration -> Custom -> Low Level -> Base->Actions -> ir.actions.report.xml 

.. i18n: Usual TAGS
.. i18n: ==========
..

Usual TAGS
==========

.. i18n: Code within [[ ]] tags is python code
.. i18n: -------------------------------------
..

Code within [[ ]] tags is python code
-------------------------------------

.. i18n: The context of the code (the variable's values you can use) is the same as that 
.. i18n: described for :ref:`dynamic-report-content`.
..

The context of the code (the variable's values you can use) is the same as that 
described for :ref:`dynamic-report-content`.

.. i18n: Unicode reports 
.. i18n: ===============
..

Unicode reports 
===============

.. i18n: As of OpenERP 5.0-rc3 unicode printing with ReportLab is still not available. The problem is that OpenERP uses the PDF standard fonts (14 fonts, they are not embedded in the document but the reader provides them) that are Type1 and have only Latin1 characters.
..

As of OpenERP 5.0-rc3 unicode printing with ReportLab is still not available. The problem is that OpenERP uses the PDF standard fonts (14 fonts, they are not embedded in the document but the reader provides them) that are Type1 and have only Latin1 characters.

.. i18n: The solution consists of 3 parts
.. i18n: --------------------------------
..

The solution consists of 3 parts
--------------------------------

.. i18n:     * Provide TrueType fonts and make them accessible for ReportLab.
.. i18n:     * Register the TrueType fonts with ReportLab before using them in the reports.
.. i18n:     * Replace the old fontNames in xsl and rml templates with the TrueType ones. 
..

    * Provide TrueType fonts and make them accessible for ReportLab.
    * Register the TrueType fonts with ReportLab before using them in the reports.
    * Replace the old fontNames in xsl and rml templates with the TrueType ones. 

.. i18n: All these ideas are taken from the forums
.. i18n: -----------------------------------------
..

All these ideas are taken from the forums
-----------------------------------------

.. i18n: **Free TrueType fonts**
..

**Free TrueType fonts**

.. i18n: that can be used for this purpose are in the DejaVu family. http://dejavu-fonts.org/wiki/index.php?title=Main_Page They can be installed
..

that can be used for this purpose are in the DejaVu family. http://dejavu-fonts.org/wiki/index.php?title=Main_Page They can be installed

.. i18n:     * in the ReportLab's fonts directory,
.. i18n:     * system-wide and include that directory in rl_config.py,
.. i18n:     * in a subdirectory of the OpenERP installation and give that path to ReportLab during the font registration. 
..

    * in the ReportLab's fonts directory,
    * system-wide and include that directory in rl_config.py,
    * in a subdirectory of the OpenERP installation and give that path to ReportLab during the font registration. 

.. i18n: **In the server/bin/report/render/rml2pdf/__init__.py**
.. i18n: ::
.. i18n: 
.. i18n: 	import reportlab.rl_config
.. i18n: 	reportlab.rl_config.warnOnMissingFontGlyphs = 0
.. i18n: 
.. i18n: 	from reportlab.pdfbase import pdfmetrics
.. i18n: 	from reportlab.pdfbase.ttfonts import TTFont
.. i18n: 	import reportlab
.. i18n: 
.. i18n: 	enc = 'UTF-8'
.. i18n: 
.. i18n: 	#repeat these for all the fonts needed
.. i18n: 	pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf',enc))
.. i18n: 	pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf',enc))
.. i18n: 
.. i18n: 	from reportlab.lib.fonts import addMapping
.. i18n: 
.. i18n: 	#repeat these for all the fonts needed
.. i18n: 	addMapping('DejaVuSans', 0, 0, 'DejaVuSans') #normal
.. i18n: 	addMapping('DejaVuSans-Bold', 1, 0, 'DejaVuSans') #normal
..

**In the server/bin/report/render/rml2pdf/__init__.py**
::

	import reportlab.rl_config
	reportlab.rl_config.warnOnMissingFontGlyphs = 0

	from reportlab.pdfbase import pdfmetrics
	from reportlab.pdfbase.ttfonts import TTFont
	import reportlab

	enc = 'UTF-8'

	#repeat these for all the fonts needed
	pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf',enc))
	pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf',enc))

	from reportlab.lib.fonts import addMapping

	#repeat these for all the fonts needed
	addMapping('DejaVuSans', 0, 0, 'DejaVuSans') #normal
	addMapping('DejaVuSans-Bold', 1, 0, 'DejaVuSans') #normal

.. i18n: trml2pdf.py should be modified to load this if invoked from the command line.
..

trml2pdf.py should be modified to load this if invoked from the command line.

.. i18n: **All the xsl and rml files have to be modified**
..

**All the xsl and rml files have to be modified**

.. i18n: A list of possible alternatives:
.. i18n: ::
.. i18n: 
.. i18n: 	'Times-Roman',       'DejaVuSerif.ttf'
.. i18n: 	'Times-BoldItalic',  'DejaVuSerif-BoldItalic.ttf'
.. i18n: 	'Times-Bold',        'DejaVuSerif-Bold.ttf'
.. i18n: 	'Times-Italic',      'DejaVuSerif-Italic.ttf'
.. i18n: 
.. i18n: 	'Helvetica',     'DejaVuSans.ttf'
.. i18n: 	'Helvetica-BoldItalic',  'DejaVuSans-BoldOblique.ttf'
.. i18n: 	'Helvetica-Bold',    'DejaVuSans-Bold.ttf'
.. i18n: 	'Helvetica-Italic',  'DejaVuSans-Oblique.ttf'
.. i18n: 
.. i18n: 	'Courier',           'DejaVuSansMono.ttf'
.. i18n: 	'Courier-Bold',      'DejaVuSansMono-Bold.ttf'
.. i18n: 	'Courier-BoldItalic','DejaVuSansMono-BoldOblique.ttf'
.. i18n: 	'Courier-Italic',    'DejaVuSansMono-Oblique.ttf'
.. i18n: 
.. i18n: 	'Helvetica-ExtraLight',  'DejaVuSans-ExtraLight.ttf'
.. i18n: 
.. i18n: 	'TimesCondensed-Roman',      'DejaVuSerifCondensed.ttf'
.. i18n: 	'TimesCondensed-BoldItalic', 'DejaVuSerifCondensed-BoldItalic.ttf'
.. i18n: 	'TimesCondensed-Bold',       'DejaVuSerifCondensed-Bold.ttf'
.. i18n: 	'TimesCondensed-Italic',     'DejaVuSerifCondensed-Italic.ttf'
.. i18n: 
.. i18n: 	'HelveticaCondensed',        'DejaVuSansCondensed.ttf'
.. i18n: 	'HelveticaCondensed-BoldItalic', 'DejaVuSansCondensed-BoldOblique.ttf'
.. i18n: 	'HelveticaCondensed-Bold',   'DejaVuSansCondensed-Bold.ttf'
.. i18n: 	'HelveticaCondensed-Italic', 'DejaVuSansCondensed-Oblique.ttf
..

A list of possible alternatives:
::

	'Times-Roman',       'DejaVuSerif.ttf'
	'Times-BoldItalic',  'DejaVuSerif-BoldItalic.ttf'
	'Times-Bold',        'DejaVuSerif-Bold.ttf'
	'Times-Italic',      'DejaVuSerif-Italic.ttf'

	'Helvetica',     'DejaVuSans.ttf'
	'Helvetica-BoldItalic',  'DejaVuSans-BoldOblique.ttf'
	'Helvetica-Bold',    'DejaVuSans-Bold.ttf'
	'Helvetica-Italic',  'DejaVuSans-Oblique.ttf'

	'Courier',           'DejaVuSansMono.ttf'
	'Courier-Bold',      'DejaVuSansMono-Bold.ttf'
	'Courier-BoldItalic','DejaVuSansMono-BoldOblique.ttf'
	'Courier-Italic',    'DejaVuSansMono-Oblique.ttf'

	'Helvetica-ExtraLight',  'DejaVuSans-ExtraLight.ttf'

	'TimesCondensed-Roman',      'DejaVuSerifCondensed.ttf'
	'TimesCondensed-BoldItalic', 'DejaVuSerifCondensed-BoldItalic.ttf'
	'TimesCondensed-Bold',       'DejaVuSerifCondensed-Bold.ttf'
	'TimesCondensed-Italic',     'DejaVuSerifCondensed-Italic.ttf'

	'HelveticaCondensed',        'DejaVuSansCondensed.ttf'
	'HelveticaCondensed-BoldItalic', 'DejaVuSansCondensed-BoldOblique.ttf'
	'HelveticaCondensed-Bold',   'DejaVuSansCondensed-Bold.ttf'
	'HelveticaCondensed-Italic', 'DejaVuSansCondensed-Oblique.ttf

.. i18n: Html Reports Using Mako Templates
.. i18n: =================================
..

Html Reports Using Mako Templates
=================================

.. i18n: .. note:: Implemented in trunk only
.. i18n: 
.. i18n:    	Mako is a template library written in Python. It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance.
..

.. note:: Implemented in trunk only

   	Mako is a template library written in Python. It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance.

.. i18n: Mako Template
.. i18n: -------------
..

Mako Template
-------------

.. i18n: Syntax
.. i18n: ++++++
..

Syntax
++++++

.. i18n:   	A Mako template is parsed from a text stream containing any kind of content, XML, HTML, email text, etc. 
.. i18n:   	
.. i18n:   	The template can further contain Mako-specific directives which represent variable and/or expression substitutions, control structures (i.e. conditionals and loops), server-side comments, full blocks of Python code, as well as various tags that offer additional functionality. All of these constructs compile into real Python code. 
.. i18n:   	
.. i18n:   	This means that you can leverage the full power of Python in almost every aspect of a Mako template.
..

  	A Mako template is parsed from a text stream containing any kind of content, XML, HTML, email text, etc. 
  	
  	The template can further contain Mako-specific directives which represent variable and/or expression substitutions, control structures (i.e. conditionals and loops), server-side comments, full blocks of Python code, as well as various tags that offer additional functionality. All of these constructs compile into real Python code. 
  	
  	This means that you can leverage the full power of Python in almost every aspect of a Mako template.

.. i18n: Expression Substitution
.. i18n: +++++++++++++++++++++++
..

Expression Substitution
+++++++++++++++++++++++

.. i18n:   	The simplest expression is just a variable substitution. The syntax for this is the ${} construct instead of [[ ]] in rml.
..

  	The simplest expression is just a variable substitution. The syntax for this is the ${} construct instead of [[ ]] in rml.

.. i18n: eg::
.. i18n: 
.. i18n:     this is x: ${x}
.. i18n: 
.. i18n:   	Above, the string representation of x is applied to the template's output stream where x comes from the localcontext supplied to the template's rendering function.
.. i18n: 
.. i18n:   	The contents within the ${} tag are evaluated by Python directly.
..

eg::

    this is x: ${x}

  	Above, the string representation of x is applied to the template's output stream where x comes from the localcontext supplied to the template's rendering function.

  	The contents within the ${} tag are evaluated by Python directly.

.. i18n: :Control Structures:
..

:Control Structures:

.. i18n:     	In Mako, control structures (i.e. if/else, loops (like while and for), as well as things like try/except) are written using the % marker followed by a regular Python control expression, and are "closed" by using another % marker with the tag "end<name>", where "<name>" is the keyword of the expression:
..

    	In Mako, control structures (i.e. if/else, loops (like while and for), as well as things like try/except) are written using the % marker followed by a regular Python control expression, and are "closed" by using another % marker with the tag "end<name>", where "<name>" is the keyword of the expression:

.. i18n: eg::
.. i18n: 
.. i18n: 	% if x==5:
.. i18n:     	  this is some output
.. i18n: 	% endif
..

eg::

	% if x==5:
    	  this is some output
	% endif

.. i18n: Python Blocks
.. i18n: -------------
..

Python Blocks
-------------

.. i18n:     	Within <% %>, you're writing a regular block of Python code. While the code can appear with an arbitrary level of preceding whitespace, it has to be consistently formatted with itself. Mako's compiler will adjust the block of Python to be consistent with the surrounding generated Python code.
..

    	Within <% %>, you're writing a regular block of Python code. While the code can appear with an arbitrary level of preceding whitespace, it has to be consistently formatted with itself. Mako's compiler will adjust the block of Python to be consistent with the surrounding generated Python code.

.. i18n: Useful links:
.. i18n: 	http://www.makotemplates.org/docs/
..

Useful links:
	http://www.makotemplates.org/docs/

.. i18n: An Overview of Sale Order Example
.. i18n: +++++++++++++++++++++++++++++++++
..

An Overview of Sale Order Example
+++++++++++++++++++++++++++++++++

.. i18n: 	For Complete Example of Sale_order please Refer the module sale_report_html from :
..

	For Complete Example of Sale_order please Refer the module sale_report_html from :

.. i18n:             https://code.launchpad.net/~openerp-community/openobject-addons/trunk-addons-community
..

            https://code.launchpad.net/~openerp-community/openobject-addons/trunk-addons-community

.. i18n: .. code-block:: html
.. i18n: 
.. i18n:     ## -*- coding: utf-8 -*-
.. i18n:     <html>
.. i18n:     <head>
.. i18n: 	    <%include file="mako_header.html"/>
.. i18n:     </head>
.. i18n:     % for o in objects:
.. i18n:     <body>
.. i18n:      	<table width="100" border="0" cellspacing="0" cellpadding="0">
.. i18n: 	     	<tr>
.. i18n:      			<td>
.. i18n: 				    <p><small><b>Shipping address :</b></small>
.. i18n: 			    </td>
.. i18n: 		    </tr>
.. i18n: 		    <tr>
.. i18n: 			    <td>
.. i18n: 				    <small>${ o.partner_id.title or '' } ${ o.partner_id.name }</small>
.. i18n: 			    </td>
.. i18n: 		    </tr>
.. i18n: 		    <tr>
.. i18n:      			<td>
.. i18n: 				    <small>${ o.partner_shipping_id.state_id and o.partner_shipping_id.state_id.name or '' } ${ o.partner_shipping_id.country_id and o.partner_shipping_id.country_id.name or '' }</small>
.. i18n: 			    </td>
.. i18n: 		    </tr>
.. i18n: 	    </table>
.. i18n: 	    <table>
.. i18n: 		       <tr align="left">
.. i18n: 			      <th>Description</th>
.. i18n: 			      <th>VAT</th>
.. i18n: 			      <th>Quantity</th>
.. i18n: 			      <th>Unit Price</th>
.. i18n: 			      <th>Disc.(%)</th>
.. i18n: 			      <th>Price</th>
.. i18n: 			    </tr>
.. i18n: 		    % for line in o.order_line:
.. i18n: 			      <tr>
.. i18n: 			      <td>${line.name}</p>
.. i18n: 			      <td>${', '.join(map(lambda x: x.name, line.tax_id))}</td>
.. i18n: 			      <td>${line.product_uos and line.product_uos_qty or line.product_uom_qty}
.. i18n: 			      ${line.product_uos and line.product_uos.name or line.product_uom.name}</td>
.. i18n: 			      <td>${line.price_unit}</td>
.. i18n: 			      <td>${line.discount or 0.00 }</td>
.. i18n: 			      <td>${line.price_subtotal or 0.00 }</td>
.. i18n: 			      </tr>
.. i18n: 		      % if line['notes']:
.. i18n: 			      	<tr>
.. i18n: 			      	<td>${line.notes}</td>
.. i18n: 			      	</tr>
.. i18n: 
.. i18n: 		      % endif
.. i18n: 		      % endfor
.. i18n: 	    </table>
.. i18n:     </body>
.. i18n:     % endfor
.. i18n:     <%include file="mako_footer.html"/>
.. i18n:     </html>
..

.. code-block:: html

    ## -*- coding: utf-8 -*-
    <html>
    <head>
	    <%include file="mako_header.html"/>
    </head>
    % for o in objects:
    <body>
     	<table width="100" border="0" cellspacing="0" cellpadding="0">
	     	<tr>
     			<td>
				    <p><small><b>Shipping address :</b></small>
			    </td>
		    </tr>
		    <tr>
			    <td>
				    <small>${ o.partner_id.title or '' } ${ o.partner_id.name }</small>
			    </td>
		    </tr>
		    <tr>
     			<td>
				    <small>${ o.partner_shipping_id.state_id and o.partner_shipping_id.state_id.name or '' } ${ o.partner_shipping_id.country_id and o.partner_shipping_id.country_id.name or '' }</small>
			    </td>
		    </tr>
	    </table>
	    <table>
		       <tr align="left">
			      <th>Description</th>
			      <th>VAT</th>
			      <th>Quantity</th>
			      <th>Unit Price</th>
			      <th>Disc.(%)</th>
			      <th>Price</th>
			    </tr>
		    % for line in o.order_line:
			      <tr>
			      <td>${line.name}</p>
			      <td>${', '.join(map(lambda x: x.name, line.tax_id))}</td>
			      <td>${line.product_uos and line.product_uos_qty or line.product_uom_qty}
			      ${line.product_uos and line.product_uos.name or line.product_uom.name}</td>
			      <td>${line.price_unit}</td>
			      <td>${line.discount or 0.00 }</td>
			      <td>${line.price_subtotal or 0.00 }</td>
			      </tr>
		      % if line['notes']:
			      	<tr>
			      	<td>${line.notes}</td>
			      	</tr>

		      % endif
		      % endfor
	    </table>
    </body>
    % endfor
    <%include file="mako_footer.html"/>
    </html>

.. i18n: You can format the report as you need using HTML.
..

You can format the report as you need using HTML.

.. i18n: Report with header and footer
.. i18n: +++++++++++++++++++++++++++++
..

Report with header and footer
+++++++++++++++++++++++++++++

.. i18n: 	To create reports with your company header you need to include <%include file=”mako_header.html”/>
.. i18n: 	To create reports with your company footer you need to include <%include file=”mako_footer.html”/>
.. i18n: 	These files will bring the header and footer that you have defined for your company in the database.
..

	To create reports with your company header you need to include <%include file=”mako_header.html”/>
	To create reports with your company footer you need to include <%include file=”mako_footer.html”/>
	These files will bring the header and footer that you have defined for your company in the database.

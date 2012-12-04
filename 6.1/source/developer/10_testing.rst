=======
Testing
=======

Unit testing
============

Since version 4.2 of OpenERP, the XML api provides several features to test your modules. They allow you to

    * test the properties of your records, your class invariants etc.
    * test your methods
    * manipulate your objects to check your workflows and specific methods 

This thus allows you to simulate user interaction and automatically test your modules.

Generalities
------------
 
As you will see in the next pages, unit testing through OpenERP's XML can be done using three main tags: <assert>, <workflow> and <function>. All these tags share some common optional attributes:

:uid:

	allows you to do the tag interpretation through a specific User ID (you must specify the XML id of that user, for example "base.user_demo") 

:context:

	allows you to specify a context dictionary (given as a Python expression) to use when applicable (for <function> notice that not all objects methods take a context attribute so it won't be automatically transmitted to them, however it applies on <value>) 

These two attributes might be set on any of those tags (for <functions>, only the root <function> tag may accept it) or on the <data> tag itself. If you set a context attribute on both, they will be merged automatically.

Notice that Unit Testing tags will not be interpreted inside a <data> tag set in noupdate.

Using unit tests
----------------

You can declare unit tests in all your .XML files. We suggest you to name the files like this:

    * module_name_test.xml 

If your tests are declared as demo data in the __openerp__.py, they will be checked at the installation of the system with demo data. Example of usage, testing the demo sale order produce a correct amount in the generated invoice.

If your tests are declared like init data, they will be checked at all installation of the software. Use it to test the consistency of the software after installation.

If your tests are declared in update sections, the tests are checked at the installation and also at all updates. Use it to tests consistencies, invariants of the module. Example: The sum of the credits must be equal to the sum of the debits for all non draft entries in the accounting module. Putting tests in update sections is very useful to check consistencies of migrations or new version upgrades. 


Assert Tag
----------

The assert tag allows you to define some assertions that have to be checked at boot time. Example :

.. code-block:: xml
	
	<assert model="res.company" id="main_company" string="The main company name is Open sprl">
	    <test expr="name">Open sprl</test>
	</assert>

This assert will check that the company with id main_company has a name equal to "Open sprl". The expr field specifies a python expression to evaluate. The expression can access any field of the specified model and any python built-in function (such as sum, reduce etc.). The ref function, which gives the database id corresponding to a specified XML id, is also available (in the case that "ref" is also the name of an attribute of the specified model, you can use _ref instead). The resulting value is then compared with the text contained in the test tag. If the assertion fails, it is logged as a message containing the value of the string attribute and the test tag that failed.

For more complex tests it is not always sufficient to compare a result to a string. To do that you may instead omit the tag's content and just put an expression that must evaluate to True:

.. code-block:: xml
	
	<assert model="res.company" 
                id="main_company" 
                string="The main company's currency is €" severity="warning">
	    <test expr="currency_id.code == 'eur'.upper()"/>
	</assert>

The severity attribute defines the level of the assertion: debug, info, warning, error or critical. The default is error. If an assertion of too high severity fails, an exception is thrown and the parsing stops. If that happens during server initialization, the server will stop. Else the exception will be transmitted to the client. The level at which a failure will throw an exception is by default at warning, but can be specified at server launch through the ``--assert-exit-level`` argument.

As sometimes you do not know the id when you're writing the test, you can use a search instead. So we can define another example, which will be always true:

.. code-block:: xml
	
	<assert model="res.partner" 
                search="[('name','=','Agrolait')]" 
                string="The name of Agrolait is :Agrolait">
	    <test expr="name">Agrolait</test>
	</assert>

When you use the search, each resulting record is tested but the assertion is counted only once. Thus if an assertion fails, the remaining records won't be tested. In addition, if the search finds no record, nothing will be tested so the assertion will be considered successful. If you want to make sure that there are a certain number of results, you might use the count parameter:

.. code-block:: xml
	
	<assert model="res.partner" 
                search="[('name','=','Agrolait')]" 
                string="The name of Agrolait is :Agrolait" 
                count="1">
	    <test expr="name">Agrolait</test>
	</assert>

:Example:

Require the version of a module.

.. code-block:: xml
	
	<!-- modules requirement -->
	<assert model="ir.module.module" 
                search="[('name','=','common')]" 
                severity="critical" count="1">
	    <test expr="state == 'installed'" />
	    <!-- only check module version -->
	    <test expr="'.'.join(installed_version.split('.')[3:]) >= '2.4'" />
	</assert>
	
	
Workflow Tag
------------

The workflow tag allows you to call for a transition in a workflow by sending a signal to it. It is generally used to simulate an interaction with a user (clicking on a button…) for test purposes:

.. code-block:: xml
	
	<workflow model="sale.order" ref="test_order_1" action="order_confirm" />

This is the syntax to send the signal ``order_confirm`` to the sale order with id ``test_order_1``.

Notice that workflow tags (as all other tags) are interpreted as root which might be a problem if the signals handling needs to use some particular property of the user (typically the user's company, while root does not belong to one). In that case you might specify a user to switch to before handling the signal, through the uid property:

.. code-block:: xml
	
	<workflow model="sale.order" ref="test_order_1" action="manual_invoice" uid="base.user_admin" />

(here we had to specify the module base - from which user_admin comes - because this tag is supposed to be placed in an xml file of the sale module)

In some particular cases, when you write the test, you don't know the id of the object to manipulate through the workflow. It is thus allowed to replace the ref attribute with a value child tag:

.. code-block:: xml
	
	<workflow model="account.invoice" action="invoice_open">
	    <value model="sale.order" eval="obj(ref('test_order_1')).invoice_ids[0].id" />
	</workflow>

(notice that the eval part must evaluate to a valid database id) 


Function Tag
------------

The function tag allows to call some method of an object. The called method must have the following signature:

def mymethod(self, cr, uid [, …])

Where

    * cr is the database cursor
    * uid is the user id 

Most of the methods defined in Tiny respect that signature as cr and uid are required for a lot of operations, including database access.

The function tag can then be used to call that method:

.. code-block:: xml
	
	<function model="mypackage.myclass" name="mymethod" />

Most of the time you will want to call your method with additional arguments. Suppose the method has the following signature:

def mymethod(self, cr, uid, mynumber)

There are two ways to call that method:

    * either by using the eval attribute, which must be a python expression evaluating to the list of additional arguments: 

.. code-block:: xml
	
	<function model="mypackage.myclass" name="mymethod" eval="[42]" />

In that case you have access to all native python functions, to a function ``ref()`` that takes as its argument an XML id and returns the corresponding database id, and to a function ``obj()`` that takes a database id and returns an object with all fields loaded as well as related records.

    * or by putting a child node inside the function tag: 

.. code-block:: xml
	
	<function model="mypackage.myclass" name="mymethod">
	     <value eval="42" />
	</function>

Only value and function tags have meaning as function child nodes (using other tags will give unspecified results). This means that you can use the returned result of a method call as an argument of another call. You can put as many child nodes as you want, each one being an argument of the method call (keeping them in order). You can also mix child nodes and the eval attribute. In that case the attribute will be evaluated first and child nodes will be appended to the resulting list. 


Acceptance testing
==================

This document describes all tests that are made each time someone install OpenERP on a computer. You can then assume that all these tests are valid as we must launch them before publishing a new module or a release of OpenERP.

Integrity tests on migrations
-----------------------------

            * Sum credit = Sum debit
            * Balanced account chart 

... Describe all integrity tests here

Workflow tests
--------------

... Describe all processes tested here.


Record creation
---------------

More than 300 records are created, describe them here. 

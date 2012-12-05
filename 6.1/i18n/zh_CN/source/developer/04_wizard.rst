.. i18n: ===============================
.. i18n: Creating Wizard - (The Process)
.. i18n: ===============================
..

===============================
创建向导 - (The Process)
===============================

.. i18n: Introduction
.. i18n: ============
..

Introduction
============

.. i18n: Wizards describe interaction sequences between the client and the server.
..

Wizards describe interaction sequences between the client and the server.

.. i18n: Here is, as an example, a typical process for a wizard:
..

Here is, as an example, a typical process for a wizard:

.. i18n:    1. A window is sent to the client (a form to be completed)
.. i18n:    2. The client sends back the data from the fields which were filled in
.. i18n:    3. The server gets the result, usually execute a function and possibly sends another window/form to the client 
..

   1. A window is sent to the client (a form to be completed)
   2. The client sends back the data from the fields which were filled in
   3. The server gets the result, usually execute a function and possibly sends another window/form to the client 

.. i18n: .. image:: images/Wizard.png
..

.. image:: images/Wizard.png

.. i18n: Here is a screenshot of the wizard used to reconcile transactions (when you click on the gear icon in an account chart):
..

Here is a screenshot of the wizard used to reconcile transactions (when you click on the gear icon in an account chart):

.. i18n: .. image:: images/Wizard_screenshot.png 
.. i18n:    :width: 100% 
..

.. image:: images/Wizard_screenshot.png 
   :width: 100% 

.. i18n: Wizards - Principles
.. i18n: ====================
..

Wizards - Principles
====================

.. i18n: A wizard is a succession of steps. A step is composed of several actions;
..

A wizard is a succession of steps. A step is composed of several actions;

.. i18n: #. send a form to the client and some buttons
.. i18n: #. get the form result and the button pressed from the client
.. i18n: #. execute some actions
.. i18n: #. send a new action to the client (form, print, ...) 
..

#. send a form to the client and some buttons
#. get the form result and the button pressed from the client
#. execute some actions
#. send a new action to the client (form, print, ...) 

.. i18n: To define a wizard, you have to create a class inheriting from **wizard.interface** and instantiate it. Each wizard must have a unique name, which can be chosen arbitrarily except for the fact it has to start with the module name (for example: account.move.line.reconcile). The wizard must define a dictionary named **states** which defines all its steps.
.. i18n: A full example of a simple wizard can be found at  http://www.openobject.com/forum/post43900.html#43900
..

To define a wizard, you have to create a class inheriting from **wizard.interface** and instantiate it. Each wizard must have a unique name, which can be chosen arbitrarily except for the fact it has to start with the module name (for example: account.move.line.reconcile). The wizard must define a dictionary named **states** which defines all its steps.
A full example of a simple wizard can be found at  http://www.openobject.com/forum/post43900.html#43900

.. i18n: Here is an example of such a class:
..

Here is an example of such a class:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	class wiz_reconcile(wizard.interface):
.. i18n: 	      states = {
.. i18n: 		   'init': {
.. i18n: 		        'actions': [_trans_rec_get],
.. i18n: 		        'result': {'type': 'form', 
.. i18n: 		                   'arch': _transaction_form, 
.. i18n: 		                   'fields': _transaction_fields,  
.. i18n: 		                   'state':[('reconcile','Reconcile'),('end','Cancel')]}
.. i18n: 		  },
.. i18n: 		   'reconcile': {
.. i18n: 		        'actions': [_trans_rec_reconcile],
.. i18n: 		        'result': {'type': 'state', 'state':'end'}
.. i18n: 		  }
.. i18n: 	     }
.. i18n: 	wiz_reconcile('account.move.line.reconcile');
..

.. code-block:: python

	class wiz_reconcile(wizard.interface):
	      states = {
		   'init': {
		        'actions': [_trans_rec_get],
		        'result': {'type': 'form', 
		                   'arch': _transaction_form, 
		                   'fields': _transaction_fields,  
		                   'state':[('reconcile','Reconcile'),('end','Cancel')]}
		  },
		   'reconcile': {
		        'actions': [_trans_rec_reconcile],
		        'result': {'type': 'state', 'state':'end'}
		  }
	     }
	wiz_reconcile('account.move.line.reconcile');

.. i18n: The 'states' dictionary define all the states of the wizard. In this example; **init** and **reconcile**. There is another state which is named end which is implicit.
..

The 'states' dictionary define all the states of the wizard. In this example; **init** and **reconcile**. There is another state which is named end which is implicit.

.. i18n: A wizard always starts in the **init** state and ends in the **end** state.
..

A wizard always starts in the **init** state and ends in the **end** state.

.. i18n: A state define two things:
..

A state define two things:

.. i18n: 	#. a list of actions
.. i18n: 	#. a result 
..

	#. a list of actions
	#. a result 

.. i18n: The list of actions
.. i18n: -------------------
.. i18n: Each step/state of a wizard defines a list of actions which are executed when the wizard enters the state. This list can be empty.
..

The list of actions
-------------------
Each step/state of a wizard defines a list of actions which are executed when the wizard enters the state. This list can be empty.

.. i18n: The function (actions) must have the following signatures:
..

The function (actions) must have the following signatures:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _trans_rec_get(self, uid, data, res_get=False):
..

.. code-block:: python

	def _trans_rec_get(self, uid, data, res_get=False):

.. i18n: Where:
..

Where:

.. i18n:     * **self** is the pointer to the wizard object
.. i18n:     * **uid** is the user ID of the user which is executing the wizard
.. i18n:     * **data** is a dictionary containing the following data:
.. i18n:            * **ids**: the list of ids of resources selected when the user executed the wizard
.. i18n:            * **id**: the id highlighted when the user executed the wizard
.. i18n:            * **form**: a dictionary containing all the values the user completed in the preceding forms. If you change values in this dictionary, the following forms will be pre-completed. 
..

    * **self** is the pointer to the wizard object
    * **uid** is the user ID of the user which is executing the wizard
    * **data** is a dictionary containing the following data:
           * **ids**: the list of ids of resources selected when the user executed the wizard
           * **id**: the id highlighted when the user executed the wizard
           * **form**: a dictionary containing all the values the user completed in the preceding forms. If you change values in this dictionary, the following forms will be pre-completed. 

.. i18n: Each action function must return a dictionary. Any entries in this dictionary
.. i18n: will be merged with the data that is passed to the form when it's displayed.
..

Each action function must return a dictionary. Any entries in this dictionary
will be merged with the data that is passed to the form when it's displayed.

.. i18n: The result
.. i18n: ----------
..

The result
----------

.. i18n: Here are some result examples:
..

Here are some result examples:

.. i18n: Result: next step
..

Result: next step

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	'result': {'type': 'state', 
.. i18n: 	           'state':'end'}
..

.. code-block:: python

	'result': {'type': 'state', 
	           'state':'end'}

.. i18n: Indicate that the wizard has to continue to the next state: 'end'. If this is the 'end' state, the wizard stops.
..

Indicate that the wizard has to continue to the next state: 'end'. If this is the 'end' state, the wizard stops.

.. i18n: Result: new dialog for the client
..

Result: new dialog for the client

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	'result': {'type': 'form', 
.. i18n: 	           'arch': _form, 
.. i18n: 	           'fields': _fields, 
.. i18n: 	           'state':[('reconcile','Reconcile'),('end','Cancel')]}
..

.. code-block:: python

	'result': {'type': 'form', 
	           'arch': _form, 
	           'fields': _fields, 
	           'state':[('reconcile','Reconcile'),('end','Cancel')]}

.. i18n: The type=form indicate that this step is a dialog to the client. The dialog is composed of:
..

The type=form indicate that this step is a dialog to the client. The dialog is composed of:

.. i18n: #. a form : with fields description and a form description
.. i18n: #. some buttons : on which the user press after completing the form 
..

#. a form : with fields description and a form description
#. some buttons : on which the user press after completing the form 

.. i18n: The form description (arch) is like in the views objects. Here is an example of form:
..

The form description (arch) is like in the views objects. Here is an example of form:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	_form = """<?xml version="1.0"?>
.. i18n: 		<form title="Reconciliation">
.. i18n: 		  <separator string="Reconciliation transactions" colspan="4"/>
.. i18n: 		  <field name="trans_nbr"/>
.. i18n: 		  <newline/>
.. i18n: 		  <field name="credit"/>
.. i18n: 		  <field name="debit"/>
.. i18n: 		  <field name="state"/>
.. i18n: 		  <separator string="Write-Off" colspan="4"/>
.. i18n: 		  <field name="writeoff"/>
.. i18n: 		  <newline/>
.. i18n: 		  <field name="writeoff_acc_id" colspan="3"/>
.. i18n: 		</form>
.. i18n: 		"""
..

.. code-block:: xml

	_form = """<?xml version="1.0"?>
		<form title="Reconciliation">
		  <separator string="Reconciliation transactions" colspan="4"/>
		  <field name="trans_nbr"/>
		  <newline/>
		  <field name="credit"/>
		  <field name="debit"/>
		  <field name="state"/>
		  <separator string="Write-Off" colspan="4"/>
		  <field name="writeoff"/>
		  <newline/>
		  <field name="writeoff_acc_id" colspan="3"/>
		</form>
		"""

.. i18n: The fields description is similar to the fields described in the python ORM objects. Example:
..

The fields description is similar to the fields described in the python ORM objects. Example:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	_transaction_fields = {
.. i18n: 	      'trans_nbr': {'string':'# of Transaction', 'type':'integer', 'readonly':True},
.. i18n: 	      'credit': {'string':'Credit amount', 'type':'float', 'readonly':True},
.. i18n: 	      'debit': {'string':'Debit amount', 'type':'float', 'readonly':True},
.. i18n: 	      'state': { 
.. i18n:         		'string':"Date/Period Filter", 
.. i18n:         		'type':'selection', 
.. i18n:         		'selection':[('bydate','By Date'),
.. i18n:         			     ('byperiod','By Period'),
.. i18n:         			     ('all','By Date and Period'),
.. i18n:         			     ('none','No Filter')], 
.. i18n:         		'default': lambda *a:'none' 
.. i18n:     			}, 
.. i18n: 	      'writeoff': {'string':'Write-Off amount', 'type':'float', 'readonly':True},
.. i18n: 	      'writeoff_acc_id': {'string':'Write-Off account', 
.. i18n:                                    'type':'many2one', 
.. i18n:                                    'relation':'account.account'
.. i18n:                                  },
.. i18n: 	}
..

.. code-block:: python

	_transaction_fields = {
	      'trans_nbr': {'string':'# of Transaction', 'type':'integer', 'readonly':True},
	      'credit': {'string':'Credit amount', 'type':'float', 'readonly':True},
	      'debit': {'string':'Debit amount', 'type':'float', 'readonly':True},
	      'state': { 
        		'string':"Date/Period Filter", 
        		'type':'selection', 
        		'selection':[('bydate','By Date'),
        			     ('byperiod','By Period'),
        			     ('all','By Date and Period'),
        			     ('none','No Filter')], 
        		'default': lambda *a:'none' 
    			}, 
	      'writeoff': {'string':'Write-Off amount', 'type':'float', 'readonly':True},
	      'writeoff_acc_id': {'string':'Write-Off account', 
                                   'type':'many2one', 
                                   'relation':'account.account'
                                 },
	}

.. i18n: Each step/state of a wizard can have several buttons. Those are located on the bottom right of the dialog box. The list of buttons for each step of the wizard is declared in the state key of its result dictionary.
..

Each step/state of a wizard can have several buttons. Those are located on the bottom right of the dialog box. The list of buttons for each step of the wizard is declared in the state key of its result dictionary.

.. i18n: For example:
..

For example:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	'state':[('end', 'Cancel', 'gtk-cancel'), ('reconcile', 'Reconcile', '', True)]
..

.. code-block:: python

	'state':[('end', 'Cancel', 'gtk-cancel'), ('reconcile', 'Reconcile', '', True)]

.. i18n: #. the next step name (determine which state will be next)
.. i18n: #. the button string (to display for the client)
.. i18n: #. the gtk stock item without the stock prefix (since 4.2)
.. i18n: #. a boolean, if true the button is set as the default action (since 4.2) 
..

#. the next step name (determine which state will be next)
#. the button string (to display for the client)
#. the gtk stock item without the stock prefix (since 4.2)
#. a boolean, if true the button is set as the default action (since 4.2) 

.. i18n: Here is a screenshot of this form:
..

Here is a screenshot of this form:

.. i18n: .. image:: images/Wizard_screenshot1.png
.. i18n:    :width: 100%
..

.. image:: images/Wizard_screenshot1.png
   :width: 100%

.. i18n: Result: call a method to determine which state is next
..

Result: call a method to determine which state is next

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _check_refund(self, cr, uid, data, context):
.. i18n: 	    ...
.. i18n: 	    return datas['form']['refund_id'] and 'wait_invoice' or 'end'
.. i18n: 	 
.. i18n: 	    ...
.. i18n: 	 
.. i18n: 	    'result': {'type':'choice', 'next_state':_check_refund}
..

.. code-block:: python

	def _check_refund(self, cr, uid, data, context):
	    ...
	    return datas['form']['refund_id'] and 'wait_invoice' or 'end'
	 
	    ...
	 
	    'result': {'type':'choice', 'next_state':_check_refund}

.. i18n: Result: print a report
..

Result: print a report

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _get_invoice_id(self, uid, datas):
.. i18n: 	      ...
.. i18n: 	      return {'ids': [...]}
.. i18n: 	 
.. i18n: 	      ...
.. i18n: 	 
.. i18n: 	      'actions': [_get_invoice_id],
.. i18n: 	      'result': {'type':'print', 
.. i18n: 		         'report':'account.invoice', 
.. i18n: 		         'get_id_from_action': True, 
.. i18n: 		         'state':'check_refund'}
..

.. code-block:: python

	def _get_invoice_id(self, uid, datas):
	      ...
	      return {'ids': [...]}
	 
	      ...
	 
	      'actions': [_get_invoice_id],
	      'result': {'type':'print', 
		         'report':'account.invoice', 
		         'get_id_from_action': True, 
		         'state':'check_refund'}

.. i18n: Result: client run an action
..

Result: client run an action

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _makeInvoices(self, cr, uid, data, context):
.. i18n: 	    ...
.. i18n: 	    return {
.. i18n: 			'domain': "[('id','in', ["+','.join(map(str,newinv))+"])]",
.. i18n: 			'name': 'Invoices',
.. i18n: 			'view_type': 'form',
.. i18n: 			'view_mode': 'tree,form',
.. i18n: 			'res_model': 'account.invoice',
.. i18n: 			'view_id': False,
.. i18n: 			'context': "{'type':'out_refund'}",
.. i18n: 			'type': 'ir.actions.act_window'
.. i18n: 		}
.. i18n: 	 
.. i18n: 		...
.. i18n: 	 
.. i18n: 		'result': {'type': 'action', 
.. i18n: 		'action': _makeInvoices, 
.. i18n: 		'state': 'end'}
..

.. code-block:: python

	def _makeInvoices(self, cr, uid, data, context):
	    ...
	    return {
			'domain': "[('id','in', ["+','.join(map(str,newinv))+"])]",
			'name': 'Invoices',
			'view_type': 'form',
			'view_mode': 'tree,form',
			'res_model': 'account.invoice',
			'view_id': False,
			'context': "{'type':'out_refund'}",
			'type': 'ir.actions.act_window'
		}
	 
		...
	 
		'result': {'type': 'action', 
		'action': _makeInvoices, 
		'state': 'end'}

.. i18n: The result of the function must be an all the fields of an ir.actions.* Here it is an ir.action.act_window, so the client will open an new tab for the objects account.invoice For more information about the fields used click here.
..

The result of the function must be an all the fields of an ir.actions.* Here it is an ir.action.act_window, so the client will open an new tab for the objects account.invoice For more information about the fields used click here.

.. i18n: It is recommended to use the result of a read on the ir.actions object like this:
..

It is recommended to use the result of a read on the ir.actions object like this:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _account_chart_open_window(self, cr, uid, data, context):
.. i18n: 		mod_obj = pooler.get_pool(cr.dbname).get('ir.model.data')
.. i18n: 		act_obj = pooler.get_pool(cr.dbname).get('ir.actions.act_window')
.. i18n: 	 
.. i18n: 		result = mod_obj._get_id(cr, uid, 'account', 'action_account_tree')
.. i18n: 		id = mod_obj.read(cr, uid, [result], ['res_id'])[0]['res_id']
.. i18n: 		result = act_obj.read(cr, uid, [id])[0]
.. i18n: 		result['context'] = str({'fiscalyear': data['form']['fiscalyear']})
.. i18n: 		return result
.. i18n: 	 
.. i18n: 		...
.. i18n: 	 
.. i18n: 		'result': {'type': 'action', 
.. i18n: 		           'action': _account_chart_open_window, 
.. i18n: 		           'state':'end'}
..

.. code-block:: python

	def _account_chart_open_window(self, cr, uid, data, context):
		mod_obj = pooler.get_pool(cr.dbname).get('ir.model.data')
		act_obj = pooler.get_pool(cr.dbname).get('ir.actions.act_window')
	 
		result = mod_obj._get_id(cr, uid, 'account', 'action_account_tree')
		id = mod_obj.read(cr, uid, [result], ['res_id'])[0]['res_id']
		result = act_obj.read(cr, uid, [id])[0]
		result['context'] = str({'fiscalyear': data['form']['fiscalyear']})
		return result
	 
		...
	 
		'result': {'type': 'action', 
		           'action': _account_chart_open_window, 
		           'state':'end'}

.. i18n: Specification
.. i18n: =============
..

Specification
=============

.. i18n: Form
.. i18n: ----
..

Form
----

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	_form = '''<?xml version="1.0"?>
.. i18n: 	<form string="Your String">
.. i18n: 	    <field name="Field 1"/>
.. i18n: 	    <newline/>
.. i18n: 	    <field name="Field 2"/>
.. i18n: 	</form>'''
..

.. code-block:: xml

	_form = '''<?xml version="1.0"?>
	<form string="Your String">
	    <field name="Field 1"/>
	    <newline/>
	    <field name="Field 2"/>
	</form>'''

.. i18n: Fields
.. i18n: ------
..

Fields
------

.. i18n: Standard
.. i18n: +++++++++
..

Standard
+++++++++

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	Field type: char, integer, boolean, float, date, datetime
.. i18n: 
.. i18n: 	_fields = {
.. i18n: 	      'str_field': {'string':'product name', 'type':'char', 'readonly':True},
.. i18n: 	}
..

.. code-block:: python

	Field type: char, integer, boolean, float, date, datetime

	_fields = {
	      'str_field': {'string':'product name', 'type':'char', 'readonly':True},
	}

.. i18n: * **string**: Field label (required)
.. i18n: * **type**: (required)
.. i18n: * **readonly**: (optional) 
..

* **string**: Field label (required)
* **type**: (required)
* **readonly**: (optional) 

.. i18n: Relational
.. i18n: ++++++++++
..

Relational
++++++++++

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	Field type: one2one,many2one,one2many,many2many
.. i18n: 
.. i18n: 	_fields = {
.. i18n: 	    'field_id': {'string':'Write-Off account', 'type':'many2one', 'relation':'account.account'}
.. i18n: 	}
..

.. code-block:: python

	Field type: one2one,many2one,one2many,many2many

	_fields = {
	    'field_id': {'string':'Write-Off account', 'type':'many2one', 'relation':'account.account'}
	}

.. i18n: * **string**: Field label (required)
.. i18n: * **type**: (required)
.. i18n: * **relation**: name of the relation object 
..

* **string**: Field label (required)
* **type**: (required)
* **relation**: name of the relation object 

.. i18n: Selection
.. i18n: ++++++++++
..

Selection
++++++++++

.. i18n: .. code-block:: python
.. i18n:        
.. i18n:        Field type: selection
.. i18n:        
.. i18n:        _fields = {
.. i18n:            'field_id':  { 
.. i18n:         		'string':"Date/Period Filter", 
.. i18n:         		'type':'selection', 
.. i18n:         		'selection':[('bydate','By Date'),
.. i18n:         			     ('byperiod','By Period'),
.. i18n:         			     ('all','By Date and Period'),
.. i18n:         			     ('none','No Filter')], 
.. i18n:         		'default': lambda *a:'none' 
.. i18n:     			},
..

.. code-block:: python
       
       Field type: selection
       
       _fields = {
           'field_id':  { 
        		'string':"Date/Period Filter", 
        		'type':'selection', 
        		'selection':[('bydate','By Date'),
        			     ('byperiod','By Period'),
        			     ('all','By Date and Period'),
        			     ('none','No Filter')], 
        		'default': lambda *a:'none' 
    			},

.. i18n: * **string**: Field label (required)
.. i18n: * **type**: (required)
.. i18n: * **selection**: key and values for the selection field   
..

* **string**: Field label (required)
* **type**: (required)
* **selection**: key and values for the selection field   

.. i18n: Add A New Wizard
.. i18n: ================
..

Add A New Wizard
================

.. i18n: To create a new wizard, you must:
..

To create a new wizard, you must:

.. i18n:     * create the wizard definition in a .py file
.. i18n:           * wizards are usually defined in the wizard subdirectory of their module as in server/bin/addons/module_name/wizard/your_wizard_name.py 
.. i18n:     * add your wizard to the list of import statements in the __init__.py file of your module's wizard subdirectory.
.. i18n:     * declare your wizard in the database 
..

    * create the wizard definition in a .py file
          * wizards are usually defined in the wizard subdirectory of their module as in server/bin/addons/module_name/wizard/your_wizard_name.py 
    * add your wizard to the list of import statements in the __init__.py file of your module's wizard subdirectory.
    * declare your wizard in the database 

.. i18n: The declaration is needed to map the wizard with a key of the client; when to launch which client. To declare a new wizard, you need to add it to the module_name_wizard.xml file, which contains all the wizard declarations for the module. If that file does not exist, you need to create it first.
..

The declaration is needed to map the wizard with a key of the client; when to launch which client. To declare a new wizard, you need to add it to the module_name_wizard.xml file, which contains all the wizard declarations for the module. If that file does not exist, you need to create it first.

.. i18n: Here is an example of the account_wizard.xml file;
..

Here is an example of the account_wizard.xml file;

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 	<openerp>
.. i18n: 	    <data>
.. i18n: 		<delete model="ir.actions.wizard" search="[('wiz_name','like','account.')]" />
.. i18n: 		<wizard string="Reconcile Transactions" model="account.move.line" 
.. i18n:                         name="account.move.line.reconcile" />
.. i18n: 		<wizard string="Verify Transac steptions" model="account.move.line" 
.. i18n:                         name="account.move.line.check" keyword="tree_but_action" /> 
.. i18n: 		<wizard string="Verify Transactions" model="account.move.line"  
.. i18n:                         name="account.move.line.check" />
.. i18n: 		<wizard string="Print Journal" model="account.account" 
.. i18n:                         name="account.journal" />
.. i18n: 		<wizard string="Split Invoice" model="account.invoice" 
.. i18n:                         name="account.invoice.split" />
.. i18n: 		<wizard string="Refund Invoice" model="account.invoice" 
.. i18n:                         name="account.invoice.refund" />
.. i18n: 	    </data>
.. i18n: 	</openerp>
..

.. code-block:: python

	<?xml version="1.0"?>
	<openerp>
	    <data>
		<delete model="ir.actions.wizard" search="[('wiz_name','like','account.')]" />
		<wizard string="Reconcile Transactions" model="account.move.line" 
                        name="account.move.line.reconcile" />
		<wizard string="Verify Transac steptions" model="account.move.line" 
                        name="account.move.line.check" keyword="tree_but_action" /> 
		<wizard string="Verify Transactions" model="account.move.line"  
                        name="account.move.line.check" />
		<wizard string="Print Journal" model="account.account" 
                        name="account.journal" />
		<wizard string="Split Invoice" model="account.invoice" 
                        name="account.invoice.split" />
		<wizard string="Refund Invoice" model="account.invoice" 
                        name="account.invoice.refund" />
	    </data>
	</openerp>

.. i18n: Attributes for the wizard tag:
..

Attributes for the wizard tag:

.. i18n:     * **id**: Unique identifier for this wizard.
.. i18n:     * **string**: The string which will be displayed if there are several wizards for one resource. (The user will be presented a list with the wizards' names).
.. i18n:     * **model**: The name of the **model** where the data needed by the wizard is.
.. i18n:     * **name**: The name of the wizard. It is used internally and should be unique.
.. i18n:     * **replace** (optional): Whether or not the wizard should override **all** existing wizards for this model. Default value: False.
.. i18n:     * **menu** (optional): Whether or not (True|False) to link the wizard with the 'gears' button (i.e. show the button or not). Default value: True.
.. i18n:     * **keyword** (optional): Bind the wizard to another action (print icon, gear icon, ...). Possible values for the keyword attribute are:
.. i18n:           * **client_print_multi**: the print icon in a form
.. i18n:           * **client_action_multi**: the 'gears' icon in a form
.. i18n:           * **tree_but_action**: the 'gears' icon in a tree view (with the shortcuts on the left)
.. i18n:           * **tree_but_open**: the double click on a branch of a tree (with the shortcuts on the left). For example, this is used, to bind wizards in the menu. 
..

    * **id**: Unique identifier for this wizard.
    * **string**: The string which will be displayed if there are several wizards for one resource. (The user will be presented a list with the wizards' names).
    * **model**: The name of the **model** where the data needed by the wizard is.
    * **name**: The name of the wizard. It is used internally and should be unique.
    * **replace** (optional): Whether or not the wizard should override **all** existing wizards for this model. Default value: False.
    * **menu** (optional): Whether or not (True|False) to link the wizard with the 'gears' button (i.e. show the button or not). Default value: True.
    * **keyword** (optional): Bind the wizard to another action (print icon, gear icon, ...). Possible values for the keyword attribute are:
          * **client_print_multi**: the print icon in a form
          * **client_action_multi**: the 'gears' icon in a form
          * **tree_but_action**: the 'gears' icon in a tree view (with the shortcuts on the left)
          * **tree_but_open**: the double click on a branch of a tree (with the shortcuts on the left). For example, this is used, to bind wizards in the menu. 

.. i18n: **__openerp__.py**
..

**__openerp__.py**

.. i18n: If the wizard you created is the first one of its module, you probably had to create the modulename_wizard.xml file yourself. In that case, it should be added to the update_xml field of the __openerp__.py file of the module.
..

If the wizard you created is the first one of its module, you probably had to create the modulename_wizard.xml file yourself. In that case, it should be added to the update_xml field of the __openerp__.py file of the module.

.. i18n: Here is, for example, the **__openerp__.py** file for the account module.
..

Here is, for example, the **__openerp__.py** file for the account module.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	{
.. i18n: 	    "name": OpenERP Accounting",
.. i18n: 	    "version": "0.1",
.. i18n: 	    "depends": ["base"],
.. i18n: 	    "init_xml": ["account_workflow.xml", "account_data.xml"],
.. i18n: 	    "update_xml": ["account_view.xml","account_report.xml", "account_wizard.xml"],
.. i18n: 	}
..

.. code-block:: python

	{
	    "name": OpenERP Accounting",
	    "version": "0.1",
	    "depends": ["base"],
	    "init_xml": ["account_workflow.xml", "account_data.xml"],
	    "update_xml": ["account_view.xml","account_report.xml", "account_wizard.xml"],
	}

.. i18n: osv_memory Wizard System
.. i18n: ========================
.. i18n: To develop osv_memory wizard, just create a normal object, But instead of inheriting from osv.osv, Inherit from osv.osv_memory. Methods of "wizard" are in object and if the wizard is complex, You can define workflow on object. osv_memory object is managed in memory instead of storing in postgresql.
..

osv_memory Wizard System
========================
To develop osv_memory wizard, just create a normal object, But instead of inheriting from osv.osv, Inherit from osv.osv_memory. Methods of "wizard" are in object and if the wizard is complex, You can define workflow on object. osv_memory object is managed in memory instead of storing in postgresql.

.. i18n: That's all, nothing more than just changing the inherit. These wizards can be defined at any location unlike addons/modulename/modulename_wizard.py. 
.. i18n: Historically, the _wizard prefix is for actual (old-style) wizards, so there might be a connotation there, the "new-style" osv_memory based "wizards" are perfectly normal objects (just used to emulate the old wizards, so they don't really match the old separations. 
.. i18n: Furthermore, osv_memory based "wizards" tend to need more than one object (e.g. one osv_memory object for each state of the original wizard) so the correspondence is not exactly 1:1.
..

That's all, nothing more than just changing the inherit. These wizards can be defined at any location unlike addons/modulename/modulename_wizard.py. 
Historically, the _wizard prefix is for actual (old-style) wizards, so there might be a connotation there, the "new-style" osv_memory based "wizards" are perfectly normal objects (just used to emulate the old wizards, so they don't really match the old separations. 
Furthermore, osv_memory based "wizards" tend to need more than one object (e.g. one osv_memory object for each state of the original wizard) so the correspondence is not exactly 1:1.

.. i18n: So what makes them looks like 'old' wizards?
..

So what makes them looks like 'old' wizards?

.. i18n:     * In the action that opens the object, you can put 
..

    * In the action that opens the object, you can put 

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	<field name="target">new</field>
..

.. code-block:: python

	<field name="target">new</field>

.. i18n: It means the object will open in a new window instead of the current one.
..

It means the object will open in a new window instead of the current one.

.. i18n:     * On a button, you can use <button special="cancel" .../> to close the window. 
..

    * On a button, you can use <button special="cancel" .../> to close the window. 

.. i18n: Example : In project.py file.
..

Example : In project.py file.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	class config_compute_remaining(osv.osv_memory):
.. i18n: 	    _name='config.compute.remaining'
.. i18n: 	    def _get_remaining(self,cr, uid, ctx):
.. i18n: 		if 'active_id' in ctx:
.. i18n: 		    return self.pool.get('project.task').browse(cr,uid,ctx['active_id']).remaining_hours
.. i18n: 		return False
.. i18n: 	    _columns = {
.. i18n: 		'remaining_hours' : fields.float('Remaining Hours', digits=(16,2),),
.. i18n: 		    }
.. i18n: 	    _defaults = {
.. i18n: 		'remaining_hours': _get_remaining
.. i18n: 		}
.. i18n: 	    def compute_hours(self, cr, uid, ids, context=None):
.. i18n: 		if 'active_id' in context:
.. i18n: 		    remaining_hrs=self.browse(cr,uid,ids)[0].remaining_hours
.. i18n: 		    self.pool.get('project.task').write(cr,uid,context['active_id'],
.. i18n:                                                          {'remaining_hours' : remaining_hrs})
.. i18n: 		return {
.. i18n: 		        'type': 'ir.actions.act_window_close',
.. i18n: 		 }
.. i18n: 	config_compute_remaining()
..

.. code-block:: python

	class config_compute_remaining(osv.osv_memory):
	    _name='config.compute.remaining'
	    def _get_remaining(self,cr, uid, ctx):
		if 'active_id' in ctx:
		    return self.pool.get('project.task').browse(cr,uid,ctx['active_id']).remaining_hours
		return False
	    _columns = {
		'remaining_hours' : fields.float('Remaining Hours', digits=(16,2),),
		    }
	    _defaults = {
		'remaining_hours': _get_remaining
		}
	    def compute_hours(self, cr, uid, ids, context=None):
		if 'active_id' in context:
		    remaining_hrs=self.browse(cr,uid,ids)[0].remaining_hours
		    self.pool.get('project.task').write(cr,uid,context['active_id'],
                                                         {'remaining_hours' : remaining_hrs})
		return {
		        'type': 'ir.actions.act_window_close',
		 }
	config_compute_remaining()

.. i18n: * View is same as normal view (Note buttons). 
..

* View is same as normal view (Note buttons). 

.. i18n: Example :
..

Example :

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record id="view_config_compute_remaining" model="ir.ui.view">
.. i18n: 		    <field name="name">Compute Remaining Hours </field>
.. i18n: 		    <field name="model">config.compute.remaining</field>
.. i18n: 		    <field name="type">form</field>
.. i18n: 		    <field name="arch" type="xml">
.. i18n: 		        <form string="Remaining Hours">
.. i18n: 		            <separator colspan="4" string="Change Remaining Hours"/>
.. i18n: 		            <newline/>
.. i18n: 		            <field name="remaining_hours" widget="float_time"/>
.. i18n: 		            <group col="4" colspan="4">
.. i18n: 		                <button icon="gtk-cancel" special="cancel" string="Cancel"/>
.. i18n: 		                <button icon="gtk-ok" name="compute_hours" string="Update" type="object"/>
.. i18n: 		            </group>
.. i18n: 		        </form>
.. i18n: 		    </field>
.. i18n: 		</record>
..

.. code-block:: xml

	<record id="view_config_compute_remaining" model="ir.ui.view">
		    <field name="name">Compute Remaining Hours </field>
		    <field name="model">config.compute.remaining</field>
		    <field name="type">form</field>
		    <field name="arch" type="xml">
		        <form string="Remaining Hours">
		            <separator colspan="4" string="Change Remaining Hours"/>
		            <newline/>
		            <field name="remaining_hours" widget="float_time"/>
		            <group col="4" colspan="4">
		                <button icon="gtk-cancel" special="cancel" string="Cancel"/>
		                <button icon="gtk-ok" name="compute_hours" string="Update" type="object"/>
		            </group>
		        </form>
		    </field>
		</record>

.. i18n: * Action is also same as normal action (don't forget to add target attribute) 
..

* Action is also same as normal action (don't forget to add target attribute) 

.. i18n: Example :
..

Example :

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record id="action_config_compute_remaining" model="ir.actions.act_window">
.. i18n: 	    <field name="name">Compute Remaining Hours</field>
.. i18n: 	    <field name="type">ir.actions.act_window</field>
.. i18n: 	    <field name="res_model">config.compute.remaining</field>
.. i18n: 	    <field name="view_type">form</field>
.. i18n: 	    <field name="view_mode">form</field>
.. i18n: 	    <field name="target">new</field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record id="action_config_compute_remaining" model="ir.actions.act_window">
	    <field name="name">Compute Remaining Hours</field>
	    <field name="type">ir.actions.act_window</field>
	    <field name="res_model">config.compute.remaining</field>
	    <field name="view_type">form</field>
	    <field name="view_mode">form</field>
	    <field name="target">new</field>
	</record>

.. i18n: osv_memory configuration item
.. i18n: =============================
..

osv_memory configuration item
=============================

.. i18n: Sometimes, your addon can't do with configurable defaults and needs
.. i18n: upfront configuration settings to work correctly. In these cases, you
.. i18n: want to provide a configuration wizard right after installation, and
.. i18n: potentially one which can be re-run later if needed.
..

Sometimes, your addon can't do with configurable defaults and needs
upfront configuration settings to work correctly. In these cases, you
want to provide a configuration wizard right after installation, and
potentially one which can be re-run later if needed.

.. i18n: Up until 5.0, OpenERP had such a facility but it was hardly documented
.. i18n: and a very manual, arduous process. A simpler, more straightforward
.. i18n: solution has been implemented for those needs.
..

Up until 5.0, OpenERP had such a facility but it was hardly documented
and a very manual, arduous process. A simpler, more straightforward
solution has been implemented for those needs.

.. i18n: The basic concepts
.. i18n: ------------------
..

The basic concepts
------------------

.. i18n: The new implementation provides a base behavior ``osv_memory`` object
.. i18n: from which you need to inherit. This behavior handles the flow between
.. i18n: the configuration items of the various extensions, and inheriting from
.. i18n: it is therefore mandatory.
..

The new implementation provides a base behavior ``osv_memory`` object
from which you need to inherit. This behavior handles the flow between
the configuration items of the various extensions, and inheriting from
it is therefore mandatory.

.. i18n: There is also an inheritable view which provides a basic canvas,
.. i18n: through mechanisms which will be explained later it's highly
.. i18n: customizable. It's therefore strongly suggested that you should
.. i18n: inherit from that view from yours as well.
..

There is also an inheritable view which provides a basic canvas,
through mechanisms which will be explained later it's highly
customizable. It's therefore strongly suggested that you should
inherit from that view from yours as well.

.. i18n: Creating a basic configuration item
.. i18n: -----------------------------------
..

Creating a basic configuration item
-----------------------------------

.. i18n: Your configuration model
.. i18n: ++++++++++++++++++++++++
..

Your configuration model
++++++++++++++++++++++++

.. i18n: First comes the creation of the configuration item itself. This is a
.. i18n: normal ``osv_memory`` object with a few constraints:
..

First comes the creation of the configuration item itself. This is a
normal ``osv_memory`` object with a few constraints:

.. i18n: * it has to inherit from ``res.config``, which provides the basic
.. i18n:   configuration behaviors as well as the base event handlers and
.. i18n:   extension points
.. i18n: 
.. i18n: * it has to provide an ``execute`` method.[#]_ This method will be called
.. i18n:   when validating the configuration form and contains the validation
.. i18n:   logic. It shouldn't return anything.
..

* it has to inherit from ``res.config``, which provides the basic
  configuration behaviors as well as the base event handlers and
  extension points

* it has to provide an ``execute`` method.[#]_ This method will be called
  when validating the configuration form and contains the validation
  logic. It shouldn't return anything.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class my_item_config(osv.osv_memory):
.. i18n:         _name = 'my.model.config'
.. i18n:         _inherit = 'res.config' # mandatory
.. i18n: 
.. i18n:         _columns = {
.. i18n:             'my_field': fields.char('Field', size=64, required=True),
.. i18n:         }
.. i18n: 
.. i18n:         def execute(self, cr, uid, ids, context=None):
.. i18n:             'do whatever configuration work you need here'
.. i18n:     my_item_config()
..

.. code-block:: python

    class my_item_config(osv.osv_memory):
        _name = 'my.model.config'
        _inherit = 'res.config' # mandatory

        _columns = {
            'my_field': fields.char('Field', size=64, required=True),
        }

        def execute(self, cr, uid, ids, context=None):
            'do whatever configuration work you need here'
    my_item_config()

.. i18n: Your configuration view
.. i18n: +++++++++++++++++++++++
..

Your configuration view
+++++++++++++++++++++++

.. i18n: Then comes the configuration form. OpenERP provides a base view which
.. i18n: you can inherit so you don't have to deal with creating buttons and
.. i18n: handling the progress bar (which should be displayed at the bottom
.. i18n: left of all initial configuration dialogs). It's very strongly
.. i18n: recommended that you use this base view.
..

Then comes the configuration form. OpenERP provides a base view which
you can inherit so you don't have to deal with creating buttons and
handling the progress bar (which should be displayed at the bottom
left of all initial configuration dialogs). It's very strongly
recommended that you use this base view.

.. i18n: Simply add an ``inherit_id`` field to a regular ``ir.ui.view`` and
.. i18n: set its value to ``res_config_view_base``:
..

Simply add an ``inherit_id`` field to a regular ``ir.ui.view`` and
set its value to ``res_config_view_base``:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="my_config_view_form" model="ir.ui.view">
.. i18n:         <field name="name">my.item.config.view</field>
.. i18n:         <!-- this is the model defined above -->
.. i18n:         <field name="model">my.model.config</field>
.. i18n:         <field name="type">form</field>
.. i18n:         <field name="inherit_id" ref="base.res_config_view_base"/>
.. i18n:         ...
.. i18n:     </record>
..

.. code-block:: xml

    <record id="my_config_view_form" model="ir.ui.view">
        <field name="name">my.item.config.view</field>
        <!-- this is the model defined above -->
        <field name="model">my.model.config</field>
        <field name="type">form</field>
        <field name="inherit_id" ref="base.res_config_view_base"/>
        ...
    </record>

.. i18n: While this could be used as-is, it would display an empty dialog with
.. i18n: a progress bar and two buttons which isn't of much
.. i18n: interest. ``res_config_view_base`` has a special group hook which you
.. i18n: should replace with your own content like so:
..

While this could be used as-is, it would display an empty dialog with
a progress bar and two buttons which isn't of much
interest. ``res_config_view_base`` has a special group hook which you
should replace with your own content like so:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="arch" type="xml">
.. i18n:         <group string="res_config_contents" position="replace">
.. i18n:             <!-- your content should be inserted within this, the string
.. i18n:                  attribute of the previous group is used to easily find
.. i18n:                  it for replacement -->
.. i18n:             <label colspan="4" align="0.0" string="
.. i18n:                 Configure this item by defining its field"/>
.. i18n:             <field colspan="2" name="my_field"/>
.. i18n:         </group>
.. i18n:     </field>
..

.. code-block:: xml

    <field name="arch" type="xml">
        <group string="res_config_contents" position="replace">
            <!-- your content should be inserted within this, the string
                 attribute of the previous group is used to easily find
                 it for replacement -->
            <label colspan="4" align="0.0" string="
                Configure this item by defining its field"/>
            <field colspan="2" name="my_field"/>
        </group>
    </field>

.. i18n: Opening your window
.. i18n: +++++++++++++++++++
..

Opening your window
+++++++++++++++++++

.. i18n: The next step is to create the ``act_window`` which links to the
.. i18n: configuration model and the view:
..

The next step is to create the ``act_window`` which links to the
configuration model and the view:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="my_config_window" model="ir.actions.act_window">
.. i18n:         <field name="name">My config window</field>
.. i18n:         <field name="type">ir.actions.act_window</field>
.. i18n:         <field name="res_model">my.model.config</field>
.. i18n:         <field name="view_type">form</field>
.. i18n:         <field name="view_id" ref="my_config_view_form"/>
.. i18n:         <field name="view_mode">form</field>
.. i18n:         <field name="target">new</field>
.. i18n:     </record>
..

.. code-block:: xml

    <record id="my_config_window" model="ir.actions.act_window">
        <field name="name">My config window</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">my.model.config</field>
        <field name="view_type">form</field>
        <field name="view_id" ref="my_config_view_form"/>
        <field name="view_mode">form</field>
        <field name="target">new</field>
    </record>

.. i18n: Note that the ``name`` field of this ``act_window`` will be displayed
.. i18n: when listing the various configuration items in the Config Wizard
.. i18n: Steps submenu (in Administration > Configuration > Configuration
.. i18n: Wizards).
..

Note that the ``name`` field of this ``act_window`` will be displayed
when listing the various configuration items in the Config Wizard
Steps submenu (in Administration > Configuration > Configuration
Wizards).

.. i18n: Registering your action
.. i18n: +++++++++++++++++++++++
..

Registering your action
+++++++++++++++++++++++

.. i18n: Finally comes actually registering the configuration item with
.. i18n: OpenERP. This is done with an ``ir.actions.todo`` object, which
.. i18n: mandates a single ``action_id`` field referencing the ``act_window``
.. i18n: created previously:
..

Finally comes actually registering the configuration item with
OpenERP. This is done with an ``ir.actions.todo`` object, which
mandates a single ``action_id`` field referencing the ``act_window``
created previously:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="my_config_step" model="ir.actions.todo">
.. i18n:         <field name="action_id" ref="my_config_window"/>
.. i18n:     </record>
..

.. code-block:: xml

    <record id="my_config_step" model="ir.actions.todo">
        <field name="action_id" ref="my_config_window"/>
    </record>

.. i18n: ``ir.actions.todo`` also has 3 optional fields:
..

``ir.actions.todo`` also has 3 optional fields:

.. i18n: ``sequence`` (default: ``10``)
.. i18n:     The order in which the different steps are to be
.. i18n:     executed, lowest first.
..

``sequence`` (default: ``10``)
    The order in which the different steps are to be
    executed, lowest first.

.. i18n: ``active`` (default: ``True``)
.. i18n:     An inactive step will not be executed on the next round of
.. i18n:     configuration.
..

``active`` (default: ``True``)
    An inactive step will not be executed on the next round of
    configuration.

.. i18n: ``state`` (default: ``'open'``)
.. i18n:     The current state for the configuration step, mostly used to
.. i18n:     register what happened during its execution. The possible
.. i18n:     values are ``'open'``, ``'done'``, ``'skip'`` and
.. i18n:     ``'cancel'``.
..

``state`` (default: ``'open'``)
    The current state for the configuration step, mostly used to
    register what happened during its execution. The possible
    values are ``'open'``, ``'done'``, ``'skip'`` and
    ``'cancel'``.

.. i18n: The result at this point is the following:
..

The result at this point is the following:

.. i18n: .. image:: images/config_wizard_base.png
.. i18n:    :width: 100%
..

.. image:: images/config_wizard_base.png
   :width: 100%

.. i18n: Customizing your configuration item
.. i18n: -----------------------------------
..

Customizing your configuration item
-----------------------------------

.. i18n: While your current knowledge is certainly enough to configure your
.. i18n: addon, a bit of good customization can be the difference between a
.. i18n: good user experience and a great user experience.
..

While your current knowledge is certainly enough to configure your
addon, a bit of good customization can be the difference between a
good user experience and a great user experience.

.. i18n: More extensive view customization
.. i18n: +++++++++++++++++++++++++++++++++
..

More extensive view customization
+++++++++++++++++++++++++++++++++

.. i18n: As you might have noticed from the previous screen shot, by default
.. i18n: your configuration window doesn't have a *title*, which isn't a
.. i18n: problem but doesn't look very good either.
..

As you might have noticed from the previous screen shot, by default
your configuration window doesn't have a *title*, which isn't a
problem but doesn't look very good either.

.. i18n: Before setting a title, a small modification to the existing view is
.. i18n: needed though: the existing ``group`` needs to be wrapped in a
.. i18n: ``data`` element so it's possible to customize more than one item of
.. i18n: the parent view:
..

Before setting a title, a small modification to the existing view is
needed though: the existing ``group`` needs to be wrapped in a
``data`` element so it's possible to customize more than one item of
the parent view:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="my_config_view_form" model="ir.ui.view">
.. i18n:         <field name="name">my.item.config.view</field>
.. i18n:         <!-- this is the model defined above -->
.. i18n:         <field name="model">my.model.config</field>
.. i18n:         <field name="type">form</field>
.. i18n:         <field name="inherit_id">res_config_view_base</field>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <data>
.. i18n:                 <group string="res_config_contents" position="replace">
.. i18n:                     <!-- your content should be inserted within this, the
.. i18n:                          string attribute of the previous group is used to
.. i18n:                          easily find it for replacement
.. i18n:                      -->
.. i18n:                      <label colspan="4" align="0.0" string="
.. i18n:                             Configure this item by defining its field
.. i18n:                      ">
.. i18n:                      <field colspan="2" name="my_field"/>
.. i18n:                  </group>
.. i18n:              </data>
.. i18n:          </field>
.. i18n:     </record>
..

.. code-block:: xml

    <record id="my_config_view_form" model="ir.ui.view">
        <field name="name">my.item.config.view</field>
        <!-- this is the model defined above -->
        <field name="model">my.model.config</field>
        <field name="type">form</field>
        <field name="inherit_id">res_config_view_base</field>
        <field name="arch" type="xml">
            <data>
                <group string="res_config_contents" position="replace">
                    <!-- your content should be inserted within this, the
                         string attribute of the previous group is used to
                         easily find it for replacement
                     -->
                     <label colspan="4" align="0.0" string="
                            Configure this item by defining its field
                     ">
                     <field colspan="2" name="my_field"/>
                 </group>
             </data>
         </field>
    </record>

.. i18n: Then it becomes possible to alter the ``string`` attribute of the
.. i18n: original ``form`` by adding the following code within the ``data``
.. i18n: element (in this case, probably before ``group``):
..

Then it becomes possible to alter the ``string`` attribute of the
original ``form`` by adding the following code within the ``data``
element (in this case, probably before ``group``):

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <!-- position=attributes is new and is used to alter the
.. i18n:          element's attributes, instead of its content -->
.. i18n:     <form position="attributes">
.. i18n:         <!-- set the value of the 'string' attribute -->
.. i18n:         <attribute name="string">Set item field</attribute>
.. i18n:     </form>
..

.. code-block:: xml

    <!-- position=attributes is new and is used to alter the
         element's attributes, instead of its content -->
    <form position="attributes">
        <!-- set the value of the 'string' attribute -->
        <attribute name="string">Set item field</attribute>
    </form>

.. i18n: .. warning:: Comments in view overload
.. i18n: 
.. i18n:    At this point (December 2009) OpenERP cannot handle comments at the
.. i18n:    toplevel of the view element overload. When testing or reusing
.. i18n:    these examples, remember to strip out the comments or you will get
.. i18n:    runtime errors when testing the addon.
..

.. warning:: Comments in view overload

   At this point (December 2009) OpenERP cannot handle comments at the
   toplevel of the view element overload. When testing or reusing
   these examples, remember to strip out the comments or you will get
   runtime errors when testing the addon.

.. i18n: With this, the configuration form gets a nice title:
..

With this, the configuration form gets a nice title:

.. i18n: .. image:: images/config_wizard_title.png
.. i18n:    :width: 100%
..

.. image:: images/config_wizard_title.png
   :width: 100%

.. i18n: More interesting customizations might be to alter the buttons provided
.. i18n: by ``res_config_view_base`` at the bottom of the dialog: remove a
.. i18n: button (if the configuration action shouldn't be skipped), change
.. i18n: the button labels, ...
..

More interesting customizations might be to alter the buttons provided
by ``res_config_view_base`` at the bottom of the dialog: remove a
button (if the configuration action shouldn't be skipped), change
the button labels, ...

.. i18n: Since no specific hooks are provided for these alterations, they
.. i18n: require the use of xpath selectors (using the ``xpath`` element).
..

Since no specific hooks are provided for these alterations, they
require the use of xpath selectors (using the ``xpath`` element).

.. i18n: Removing the Skip button and changing the label of the Record button
.. i18n: to Set, for instance, would be done by adding the following after the
.. i18n: ``group`` element:
..

Removing the Skip button and changing the label of the Record button
to Set, for instance, would be done by adding the following after the
``group`` element:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <!-- select the button 'action_skip' of the original template
.. i18n:          and replace it by nothing, removing it -->
.. i18n:     <xpath expr="//button[@name='action_skip']"
.. i18n:         position="replace"/>
..

.. code-block:: xml

    <!-- select the button 'action_skip' of the original template
         and replace it by nothing, removing it -->
    <xpath expr="//button[@name='action_skip']"
        position="replace"/>

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <!-- select the button 'action_next' -->
.. i18n:     <xpath expr="//button[@name='action_next']"
.. i18n:            position="attributes">
.. i18n:         <!-- and change the attribute 'string' to 'Set' -->
.. i18n:         <attribute name="string">Set</attribute>
.. i18n:     </xpath>
..

.. code-block:: xml

    <!-- select the button 'action_next' -->
    <xpath expr="//button[@name='action_next']"
           position="attributes">
        <!-- and change the attribute 'string' to 'Set' -->
        <attribute name="string">Set</attribute>
    </xpath>

.. i18n: and yield:
..

and yield:

.. i18n: .. image:: images/config_wizard_buttons.png
.. i18n:    :width: 100%
..

.. image:: images/config_wizard_buttons.png
   :width: 100%

.. i18n: It is also possible to use this method to change the name of the
.. i18n: button, and thus the method invoked on the object (though that isn't
.. i18n: necessarily recommended).
..

It is also possible to use this method to change the name of the
button, and thus the method invoked on the object (though that isn't
necessarily recommended).

.. i18n: Model customization
.. i18n: +++++++++++++++++++
..

Model customization
+++++++++++++++++++

.. i18n: Though most of the requirements should be easy to fulfill using the
.. i18n: provided ``execute`` method hook, some addon-specific requirements
.. i18n: are a bit more complex. ``res.config`` should be able to provide all
.. i18n: the hooks necessary for more complex behaviors.
..

Though most of the requirements should be easy to fulfill using the
provided ``execute`` method hook, some addon-specific requirements
are a bit more complex. ``res.config`` should be able to provide all
the hooks necessary for more complex behaviors.

.. i18n: Ignoring the next step
.. i18n: ~~~~~~~~~~~~~~~~~~~~~~
..

Ignoring the next step
~~~~~~~~~~~~~~~~~~~~~~

.. i18n: Ultimately, the switch to the next configuration item is done by
.. i18n: calling the ``self.next`` method of ``res.config`` [#]_. This is the
.. i18n: last thing the base implementations of ``action_next`` and
.. i18n: ``action_skip`` do. But in some cases, looping on the current view or
.. i18n: implementing a workflow-like behavior is needed. In these cases, you
.. i18n: can simply return a dictionary from ``execute``, and ``res.config``
.. i18n: will jump to that view instead of the one returned by ``self.next``.
..

Ultimately, the switch to the next configuration item is done by
calling the ``self.next`` method of ``res.config`` [#]_. This is the
last thing the base implementations of ``action_next`` and
``action_skip`` do. But in some cases, looping on the current view or
implementing a workflow-like behavior is needed. In these cases, you
can simply return a dictionary from ``execute``, and ``res.config``
will jump to that view instead of the one returned by ``self.next``.

.. i18n: This is what the user creation item does, for instance, to let the
.. i18n: user create several new users in a row.
..

This is what the user creation item does, for instance, to let the
user create several new users in a row.

.. i18n: Performing an action on skipping
.. i18n: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..

Performing an action on skipping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. i18n: As opposed to ``action_next`` which requires that ``execute`` be
.. i18n: implemented by the children classes, ``action_skip`` comes fully
.. i18n: implemented in ``res.config``. But in the case where the child model
.. i18n: needs to perform an action upon skipping discovery, it also provides a
.. i18n: hook method called ``cancel`` which you can overload in a way similar
.. i18n: to ``execute``. Its behavior is identical to ``execute``'s: not only
.. i18n: is ``next`` called automatically at the end of ``cancel`` but it also
.. i18n: gives the possibility of `ignoring the next step`_.
..

As opposed to ``action_next`` which requires that ``execute`` be
implemented by the children classes, ``action_skip`` comes fully
implemented in ``res.config``. But in the case where the child model
needs to perform an action upon skipping discovery, it also provides a
hook method called ``cancel`` which you can overload in a way similar
to ``execute``. Its behavior is identical to ``execute``'s: not only
is ``next`` called automatically at the end of ``cancel`` but it also
gives the possibility of `ignoring the next step`_.

.. i18n: Alternative actions
.. i18n: ~~~~~~~~~~~~~~~~~~~
..

Alternative actions
~~~~~~~~~~~~~~~~~~~

.. i18n: It's also possible to either overload ``action_next`` and
.. i18n: ``action_skip`` or, more useful, to implement more actions than these
.. i18n: two, if more than two buttons are needed for instance.
..

It's also possible to either overload ``action_next`` and
``action_skip`` or, more useful, to implement more actions than these
two, if more than two buttons are needed for instance.

.. i18n: In this case, please remember that you should always provide a way to
.. i18n: reach ``self.next`` to the user, in order for him to be able to
.. i18n: configure the rest of his addons.
..

In this case, please remember that you should always provide a way to
reach ``self.next`` to the user, in order for him to be able to
configure the rest of his addons.

.. i18n: ``res.config``'s public API
.. i18n: ---------------------------
..

``res.config``'s public API
---------------------------

.. i18n: All of the public API methods take the standard OpenERP set of
.. i18n: arguments: ``self``, ``cr``, ``uid``, ``ids`` and ``context``.
..

All of the public API methods take the standard OpenERP set of
arguments: ``self``, ``cr``, ``uid``, ``ids`` and ``context``.

.. i18n: ``execute``
.. i18n: +++++++++++
..

``execute``
+++++++++++

.. i18n: Hook method called in case the ``action_next`` button
.. i18n: (default label: Record) is clicked. Should not return *anything*
.. i18n: unless you want to display another view than the next configuration
.. i18n: item. Returning anything other than a view dictionary will lead to
.. i18n: undefined behaviors.
..

Hook method called in case the ``action_next`` button
(default label: Record) is clicked. Should not return *anything*
unless you want to display another view than the next configuration
item. Returning anything other than a view dictionary will lead to
undefined behaviors.

.. i18n: It is mandatory to overload it. Failure to do so will result in a
.. i18n: ``NotImplementedError`` being raised at runtime.
..

It is mandatory to overload it. Failure to do so will result in a
``NotImplementedError`` being raised at runtime.

.. i18n: The default ``res.config`` implementation should not be called in the
.. i18n: overload (don't use ``super``).
..

The default ``res.config`` implementation should not be called in the
overload (don't use ``super``).

.. i18n: ``cancel``
.. i18n: ++++++++++
..

``cancel``
++++++++++

.. i18n: Hook method called in case the ``action_skip`` button
.. i18n: (default label: Skip) is clicked. Its behavior is the same as
.. i18n: `execute`_'s, except it's not mandatory to overload it.
..

Hook method called in case the ``action_skip`` button
(default label: Skip) is clicked. Its behavior is the same as
`execute`_'s, except it's not mandatory to overload it.

.. i18n: ``next``
.. i18n: ++++++++
..

``next``
++++++++

.. i18n: Method called to fetch the todo (and the corresponding action) for the
.. i18n: next configuration item. It can be overloaded if the configuration
.. i18n: item needs custom behavior common to all events.
..

Method called to fetch the todo (and the corresponding action) for the
next configuration item. It can be overloaded if the configuration
item needs custom behavior common to all events.

.. i18n: If overloaded, the default ``res.config`` implementation must be
.. i18n: called and its result returned in order to get and execute the next
.. i18n: configuration item.
..

If overloaded, the default ``res.config`` implementation must be
called and its result returned in order to get and execute the next
configuration item.

.. i18n: ``action_next`` and ``action_skip``
.. i18n: +++++++++++++++++++++++++++++++++++
..

``action_next`` and ``action_skip``
+++++++++++++++++++++++++++++++++++

.. i18n: Event handler for the buttons of the base view, overloading them
.. i18n: should never be necessary but in case it's needed the default
.. i18n: ``res.config`` implementation should be called (via ``super``) and its
.. i18n: result returned.
..

Event handler for the buttons of the base view, overloading them
should never be necessary but in case it's needed the default
``res.config`` implementation should be called (via ``super``) and its
result returned.

.. i18n: .. [#] This isn't completely true, as you will see when `Customizing
.. i18n:        your configuration item`_
..

.. [#] This isn't completely true, as you will see when `Customizing
       your configuration item`_

.. i18n: .. [#] this method is part of the official API and you're free to
.. i18n:        overload it if needed, but you should always call
.. i18n:        ``res.config``'s through ``super`` when your work is
.. i18n:        done. Overloading ``next`` is also probably overkill in most
.. i18n:        situations.
.. i18n:        
.. i18n: Guidelines on how to convert old-style wizard to new osv_memory style
.. i18n: ======================================================================
..

.. [#] this method is part of the official API and you're free to
       overload it if needed, but you should always call
       ``res.config``'s through ``super`` when your work is
       done. Overloading ``next`` is also probably overkill in most
       situations.
       
Guidelines on how to convert old-style wizard to new osv_memory style
======================================================================

.. i18n: OSV Memory Wizard
.. i18n: -----------------
.. i18n: provide important advantages over the pre-5.0 wizard system, with support features that were difficult to implement in wizards previously, such as:
..

OSV Memory Wizard
-----------------
provide important advantages over the pre-5.0 wizard system, with support features that were difficult to implement in wizards previously, such as:

.. i18n: #. inheritance
.. i18n: #. workflows
.. i18n: #. complex relation fields
.. i18n: #. computed fields
.. i18n: #. all kind of views (lists, graphs, ...)
..

#. inheritance
#. workflows
#. complex relation fields
#. computed fields
#. all kind of views (lists, graphs, ...)

.. i18n: The new wizards are also easier and more intuitive to write as they make use of the same syntax as other osv objects and views.
..

The new wizards are also easier and more intuitive to write as they make use of the same syntax as other osv objects and views.

.. i18n: This section will highlight the main steps usually required when porting a classical wizard to the new osv_memory wizard system.
.. i18n: For more details about the osv_memory wizard see also section XXX.
..

This section will highlight the main steps usually required when porting a classical wizard to the new osv_memory wizard system.
For more details about the osv_memory wizard see also section XXX.

.. i18n: Basically the idea is to create a regular osv object to hold the data structures and the logic of the wizard, but instead of inheriting from osv.osv, you inherit from osv.osv_memory. The methods of the old-style wizard will be moved as methods of the osv_memory object, and the various views changed into real views defined on the model of the wizard.
..

Basically the idea is to create a regular osv object to hold the data structures and the logic of the wizard, but instead of inheriting from osv.osv, you inherit from osv.osv_memory. The methods of the old-style wizard will be moved as methods of the osv_memory object, and the various views changed into real views defined on the model of the wizard.

.. i18n: If the wizard is complex, you could even define a workflow on the wizard object (see section XXX for details about workflows)
..

If the wizard is complex, you could even define a workflow on the wizard object (see section XXX for details about workflows)

.. i18n: Using a very simple wizard as an example, here is a step-by-step conversion to the new osv_memory system:
..

Using a very simple wizard as an example, here is a step-by-step conversion to the new osv_memory system:

.. i18n: Steps
.. i18n: -----
..

Steps
-----

.. i18n: 1. Create a new object that extends osv_memory, including the required fields and methods: 
..

1. Create a new object that extends osv_memory, including the required fields and methods: 

.. i18n: .. image:: images/wizard_window.png
..

.. image:: images/wizard_window.png

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def _action_open_window(self, cr, uid, data, context): 
.. i18n:     .
.. i18n:     .
.. i18n:     
.. i18n:     class product_margins(wizard.interface): 
.. i18n:         form1 = '''<?xml version="1.0"?> 
.. i18n:         <form string="View Stock of Products"> 
.. i18n:             <separator string="Select " colspan="4"/> 
.. i18n:             <field name="from_date"/> 
.. i18n:             <field name="to_date"/> 
.. i18n:             <field name="invoice_state"/> 
.. i18n:         </form>''' 
.. i18n: 
.. i18n:         form1_fields = { 
.. i18n: 	    'from_date': { 
.. i18n:                     'string': 'From', 
.. i18n:                     'type': 'date', 
.. i18n:                     'default': lambda *a:time.strftime('%Y-01-01'), 
.. i18n: 
.. i18n:             }, 
.. i18n: 	    'to_date': { 
.. i18n:                     'string': 'To', 
.. i18n:                     'type': 'date', 
.. i18n:                     'default': lambda *a:time.strftime('%Y-12-31'), 
.. i18n: 
.. i18n:             }, 
.. i18n: 	    'invoice_state': { 
.. i18n:                     'string': 'Invoice State', 
.. i18n:                     'type': 'selection', 
.. i18n:                     'selection': [('paid','Paid'),('open_paid','Open and Paid'),('draft_open_paid','Draft, Open and Paid'),], 
.. i18n:                     'required': True, 
.. i18n:                     'default': lambda *a:"open_paid", 
.. i18n:             }, 
.. i18n:         } 
.. i18n: 
.. i18n:         states = { 
.. i18n:           'init': { 
.. i18n:                 'actions': [], 
.. i18n:                 'result': {'type': 'form', 'arch':form1, 'fields':form1_fields, 'state': [('end', 'Cancel','gtk-cancel'),('open', 'Open Margins','gtk-ok')]} 
.. i18n:             }, 
.. i18n:         'open': { 
.. i18n:                 'actions': [], 
.. i18n:                 'result': {'type': 'action', 'action': _action_open_window, 'state':'end'} 
.. i18n:             } 
.. i18n:         } 
.. i18n:     product_margins('product.margins')
..

.. code-block:: python

    def _action_open_window(self, cr, uid, data, context): 
    .
    .
    
    class product_margins(wizard.interface): 
        form1 = '''<?xml version="1.0"?> 
        <form string="View Stock of Products"> 
            <separator string="Select " colspan="4"/> 
            <field name="from_date"/> 
            <field name="to_date"/> 
            <field name="invoice_state"/> 
        </form>''' 

        form1_fields = { 
	    'from_date': { 
                    'string': 'From', 
                    'type': 'date', 
                    'default': lambda *a:time.strftime('%Y-01-01'), 

            }, 
	    'to_date': { 
                    'string': 'To', 
                    'type': 'date', 
                    'default': lambda *a:time.strftime('%Y-12-31'), 

            }, 
	    'invoice_state': { 
                    'string': 'Invoice State', 
                    'type': 'selection', 
                    'selection': [('paid','Paid'),('open_paid','Open and Paid'),('draft_open_paid','Draft, Open and Paid'),], 
                    'required': True, 
                    'default': lambda *a:"open_paid", 
            }, 
        } 

        states = { 
          'init': { 
                'actions': [], 
                'result': {'type': 'form', 'arch':form1, 'fields':form1_fields, 'state': [('end', 'Cancel','gtk-cancel'),('open', 'Open Margins','gtk-ok')]} 
            }, 
        'open': { 
                'actions': [], 
                'result': {'type': 'action', 'action': _action_open_window, 'state':'end'} 
            } 
        } 
    product_margins('product.margins')

.. i18n: New Wizard File : <<module_name>>_<<filename>>.py
.. i18n: -------------------------------------------------
..

New Wizard File : <<module_name>>_<<filename>>.py
-------------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class product_margin(osv.osv_memory): 
.. i18n:         ''' 
.. i18n:         Product Margin 
.. i18n:         ''' 
.. i18n:         _name = 'product.margin' 
.. i18n:         _description = 'Product Margin' 
.. i18n: 
.. i18n:         def _action_open_window(self, cr, uid, ids, context): 
.. i18n: 	    . 
.. i18n: 	    . 
.. i18n: 	    . 
.. i18n: 
.. i18n:         _columns = { 
.. i18n:             #TODO : import time required to get correct date 
.. i18n:             'from_date': fields.date('From'), 
.. i18n:             #TODO : import time required to get correct date 
.. i18n:             'to_date': fields.date('To'), 
.. i18n:             'invoice_state':fields.selection([ 
.. i18n:                ('paid','Paid'), 
.. i18n:                ('open_paid','Open and Paid'), 
.. i18n:                ('draft_open_paid','Draft, Open and Paid'), 
.. i18n:             ],'Invoice State', select=True, required=True), 
.. i18n:         } 
.. i18n:         _defaults = { 
.. i18n:             'from_date':  lambda *a:time.strftime('%Y-01-01'), 
.. i18n:             'to_date': lambda *a:time.strftime('%Y-01-01'), 
.. i18n:             'invoice_state': lambda *a:"open_paid", 
.. i18n:         } 
.. i18n:     product_margin()
..

.. code-block:: python

    class product_margin(osv.osv_memory): 
        ''' 
        Product Margin 
        ''' 
        _name = 'product.margin' 
        _description = 'Product Margin' 

        def _action_open_window(self, cr, uid, ids, context): 
	    . 
	    . 
	    . 

        _columns = { 
            #TODO : import time required to get correct date 
            'from_date': fields.date('From'), 
            #TODO : import time required to get correct date 
            'to_date': fields.date('To'), 
            'invoice_state':fields.selection([ 
               ('paid','Paid'), 
               ('open_paid','Open and Paid'), 
               ('draft_open_paid','Draft, Open and Paid'), 
            ],'Invoice State', select=True, required=True), 
        } 
        _defaults = { 
            'from_date':  lambda *a:time.strftime('%Y-01-01'), 
            'to_date': lambda *a:time.strftime('%Y-01-01'), 
            'invoice_state': lambda *a:"open_paid", 
        } 
    product_margin()

.. i18n: Convert the views into real view records defined on the model of your wizard: 
..

Convert the views into real view records defined on the model of your wizard: 

.. i18n: Old Wizard File : wizard_product_margin.py
.. i18n: ------------------------------------------
..

Old Wizard File : wizard_product_margin.py
------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     form1 = '''<?xml version="1.0"?> 
.. i18n:     <form string="View Stock of Products"> 
.. i18n:         <separator string="Select " colspan="4"/> 
.. i18n:         <field name="date"/> 
.. i18n:         <field name="invoice_state"/> 
.. i18n:     </form>''' 
..

.. code-block:: python

    form1 = '''<?xml version="1.0"?> 
    <form string="View Stock of Products"> 
        <separator string="Select " colspan="4"/> 
        <field name="date"/> 
        <field name="invoice_state"/> 
    </form>''' 

.. i18n: New Wizard File : wizard/<<module_name>>_<<filename>>_view.xml
.. i18n: --------------------------------------------------------------
..

New Wizard File : wizard/<<module_name>>_<<filename>>_view.xml
--------------------------------------------------------------

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="product_margin_form_view" model="ir.ui.view"> 
.. i18n:         <field name="name">product.margin.form</field> 
.. i18n:         <field name="model">product.margin</field> 
.. i18n:         <field name="type">form</field> 
.. i18n:         <field name="arch" type="xml"> 
.. i18n:             <form string="Properties categories"> 
.. i18n: 		    <separator colspan="4" string="General Information"/> 
.. i18n: 		    <field name="from_date" /> 
.. i18n: 		    <field name="to_date" /> 
.. i18n: 		    <field name="invoice_state" /> 
.. i18n: 		    <group col="4" colspan="2"> 
.. i18n: 		        	<button special="cancel" string="Cancel" type="object"/> 
.. i18n: 		        	<button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/> 
.. i18n: 		    </group> 
.. i18n:             </form> 
.. i18n:         </field> 
.. i18n:     </record> 
..

.. code-block:: xml

    <record id="product_margin_form_view" model="ir.ui.view"> 
        <field name="name">product.margin.form</field> 
        <field name="model">product.margin</field> 
        <field name="type">form</field> 
        <field name="arch" type="xml"> 
            <form string="Properties categories"> 
		    <separator colspan="4" string="General Information"/> 
		    <field name="from_date" /> 
		    <field name="to_date" /> 
		    <field name="invoice_state" /> 
		    <group col="4" colspan="2"> 
		        	<button special="cancel" string="Cancel" type="object"/> 
		        	<button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/> 
		    </group> 
            </form> 
        </field> 
    </record> 

.. i18n: Default_focus attribute
.. i18n: -----------------------
..

Default_focus attribute
-----------------------

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/> 
..

.. code-block:: xml

    <button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/> 

.. i18n: **default_focus="1"** is a new attribute added in 5.2. While opening wizard default control will be on the widget having this attribute. There must be only one widget on a view having this attribute = 1 otherwise it will raise exception.
..

**default_focus="1"** is a new attribute added in 5.2. While opening wizard default control will be on the widget having this attribute. There must be only one widget on a view having this attribute = 1 otherwise it will raise exception.

.. i18n: Note: For all states in the old wizard, we need to create buttons in new approach.      
..

Note: For all states in the old wizard, we need to create buttons in new approach.      

.. i18n: 2. To open the new wizard, you need to register an action that opens the first view on your wizard object. You will need to do the same for each view if your wizard contains several views. To make the view open in a pop-up window you can add a special target='new' field in the action: 
..

2. To open the new wizard, you need to register an action that opens the first view on your wizard object. You will need to do the same for each view if your wizard contains several views. To make the view open in a pop-up window you can add a special target='new' field in the action: 

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <act_window name="Open Margin" 
.. i18n: 	    res_model="product.margin" 
.. i18n: 	    src_model="product.product" 
.. i18n: 	    view_mode="form" 
.. i18n: 	    target="new" 
.. i18n: 	    key2="client_action_multi"    
.. i18n: 	    id="product_margin_act_window"/>
..

.. code-block:: xml

    <act_window name="Open Margin" 
	    res_model="product.margin" 
	    src_model="product.product" 
	    view_mode="form" 
	    target="new" 
	    key2="client_action_multi"    
	    id="product_margin_act_window"/>

.. i18n: key2="client_action_multi" : While using it in the act_window, wizard will be added in the
..

key2="client_action_multi" : While using it in the act_window, wizard will be added in the

.. i18n: 1. Action
..

1. Action

.. i18n: .. image:: images/wizard_button.png
..

.. image:: images/wizard_button.png

.. i18n: 2. Sidebar
..

2. Sidebar

.. i18n: .. image:: images/wizard_panel.png
..

.. image:: images/wizard_panel.png

.. i18n: If key2 is omitted then it will be displayed only in sidebar.
..

If key2 is omitted then it will be displayed only in sidebar.

.. i18n: Note: The "src_model" attribute is only required if you want to put the
.. i18n: wizard in the side bar of an object, you can leave it out, for example
.. i18n: if you define an action to open the second view of a wizard.
..

Note: The "src_model" attribute is only required if you want to put the
wizard in the side bar of an object, you can leave it out, for example
if you define an action to open the second view of a wizard.

.. i18n: 3. You can register this new action as a menuitem or in the context bar of any object by using a <menuitem> or <act_window> record instead of the old <wizard> tag that can be removed:
..

3. You can register this new action as a menuitem or in the context bar of any object by using a <menuitem> or <act_window> record instead of the old <wizard> tag that can be removed:

.. i18n: In Menu Item
.. i18n: ------------
..

In Menu Item
------------

.. i18n: To open a wizard view via a menuitem you can use the following syntax for the menu, using the XML id of the corresponding act_window.
..

To open a wizard view via a menuitem you can use the following syntax for the menu, using the XML id of the corresponding act_window.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<menuitem id="main" name="OSV Memory Wizard Test"/>
.. i18n: 	<menuitem
.. i18n:             action="product_margin_act_window"
.. i18n:             id="menu_product_act"
.. i18n:             parent="main" />
..

.. code-block:: xml

	<menuitem id="main" name="OSV Memory Wizard Test"/>
	<menuitem
            action="product_margin_act_window"
            id="menu_product_act"
            parent="main" />

.. i18n: 4. To open a wizard view via a button in another form you can use the following syntax for the button, using the XML id of the corresponding act_window. This can be used to have multiple steps in your wizard:
..

4. To open a wizard view via a button in another form you can use the following syntax for the button, using the XML id of the corresponding act_window. This can be used to have multiple steps in your wizard:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <button name="%(product_margin.product_margin_act_window)d" 
.. i18n:             string="Test Wizard" type="action" states="draft"/>						
..

.. code-block:: xml

    <button name="%(product_margin.product_margin_act_window)d" 
            string="Test Wizard" type="action" states="draft"/>						

.. i18n: 5. Finally, you need to cleanup the module, update the python __init__.py files if you have changed the python file name for the wizard, and add your new XML files in the update_xml list in the __openerp__.py file.
..

5. Finally, you need to cleanup the module, update the python __init__.py files if you have changed the python file name for the wizard, and add your new XML files in the update_xml list in the __openerp__.py file.

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

简介
============

.. i18n: Wizards describe interaction sequences between the client and the server.
..

向导是描述客户端和服务器之间的相互动作的序列.

.. i18n: Here is, as an example, a typical process for a wizard:
..

以下是一个典型的向导进程:

.. i18n:    1. A window is sent to the client (a form to be completed)
.. i18n:    2. The client sends back the data from the fields which were filled in
.. i18n:    3. The server gets the result, usually execute a function and possibly sends another window/form to the client 
..

   1. 向客户端发送一个窗口(待完成的表格)
   2. 客户端发送在此表格中所填的数据
   3. 服务器收到结果，执行一个函数并发送一个新的窗口到客户端 

.. i18n: .. image:: images/Wizard.png
..

.. image:: images/Wizard.png

.. i18n: Here is a screenshot of the wizard used to reconcile transactions (when you click on the gear icon in an account chart):
..

以下是一个向导的截图，该向导是用于处理业务的 (when you click on the gear icon in an account chart):

.. i18n: .. image:: images/Wizard_screenshot.png 
.. i18n:    :width: 100% 
..

.. image:: images/Wizard_screenshot.png 
   :width: 100% 

.. i18n: Wizards - Principles
.. i18n: ====================
..

向导 - 原则
====================

.. i18n: A wizard is a succession of steps. A step is composed of several actions;
..

向导具有一连串的步骤，每一个步骤又多个动作组成;

.. i18n: #. send a form to the client and some buttons
.. i18n: #. get the form result and the button pressed from the client
.. i18n: #. execute some actions
.. i18n: #. send a new action to the client (form, print, ...) 
..

#. 发送表单给客户端或按钮
#. 客户端的按钮按下后，服务端获取表单的数据
#. 执行动作
#. 发送一个新动作给客户端（form，print, ...） 

.. i18n: To define a wizard, you have to create a class inheriting from **wizard.interface** and instantiate it. Each wizard must have a unique name, which can be chosen arbitrarily except for the fact it has to start with the module name (for example: account.move.line.reconcile). The wizard must define a dictionary named **states** which defines all its steps.
.. i18n: A full example of a simple wizard can be found at  http://www.openobject.com/forum/post43900.html#43900
..

为了定义一个向导，需要创建一个继承于wizard.interface的类，并将其实例化。每个向导都有一个唯一的名字，该名字可以随意取，但它必须以组件名开头（如：account.move.line.reconcile）.向导必须定义一个名为states的字典，该字典定义了它所有的步骤。一个简单的向导例子在  http://www.openobject.com/forum/post43900.html#43900

.. i18n: Here is an example of such a class:
..

以下为一个向导类的例子:

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

'states' 字典定义了向导的所有状态。在这个例子里; **init** 和 **reconcile**. 还有一个隐藏的状态叫 end .

.. i18n: A wizard always starts in the **init** state and ends in the **end** state.
..

向导一般从从 **init** 状态开始，到 **end** 状态结束.

.. i18n: A state define two things:
..

状态定义了以下两个东西:

.. i18n: 	#. a list of actions
.. i18n: 	#. a result 
..

	#. 动作列表
	#. 结果 

.. i18n: The list of actions
.. i18n: -------------------
.. i18n: Each step/state of a wizard defines a list of actions which are executed when the wizard enters the state. This list can be empty.
..

动作列表(The list of actions)
-------------------------------------
向导的每一步骤/状态都定义了动作列表，到向导进入该状态后便执行这些动作。动作列表可以是空的.

.. i18n: The function (actions) must have the following signatures:
..

函数（actions）的语法规范如下 :

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	def _trans_rec_get(self, uid, data, res_get=False):
..

.. code-block:: python

	def _trans_rec_get(self, uid, data, res_get=False):

.. i18n: Where:
..

其中:

.. i18n:     * **self** is the pointer to the wizard object
.. i18n:     * **uid** is the user ID of the user which is executing the wizard
.. i18n:     * **data** is a dictionary containing the following data:
.. i18n:            * **ids**: the list of ids of resources selected when the user executed the wizard
.. i18n:            * **id**: the id highlighted when the user executed the wizard
.. i18n:            * **form**: a dictionary containing all the values the user completed in the preceding forms. If you change values in this dictionary, the following forms will be pre-completed. 
..

    * **self** 是指向向导当前对象的指针
    * **uid** 是执行此向导的用户ID
    * **data** 是包含以下数据的字典:
           * **ids**: 用户执行向导时，所关联的资源的id列表
           * **id**: 当用户执行向导时高亮的id
           * **form**: 一个字典，该字典包含了之前发送的表单里用户填写的数据，若你改变了字典里的值，则表单里的数据就会被提前填写. 

.. i18n: Each action function must return a dictionary. Any entries in this dictionary
.. i18n: will be merged with the data that is passed to the form when it's displayed.
..

每个动作函数必须返回一个字典。字典中的每一项将会与发送来的表单中所填写的数据合并.

.. i18n: The result
.. i18n: ----------
..

结果(The result)
------------------------

.. i18n: Here are some result examples:
..

以下为一些result的例子:

.. i18n: Result: next step
..

Result: 下一步

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

表示向导得继续下一步的状态: 'end'. 如果这一步是 'end' 状态，则向导停止.

.. i18n: Result: new dialog for the client
..

Result: 发给客户端的新对话

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

type=form 表示这步骤是发送对话给客户端，对话由以下部分组成:

.. i18n: #. a form : with fields description and a form description
.. i18n: #. some buttons : on which the user press after completing the form 
..

#. a form : 带有字段的描述和表单的描述
#. some buttons : 用户填写完数据后，按此按钮提交 

.. i18n: The form description (arch) is like in the views objects. Here is an example of form:
..

表单的描述（arch）和视图一样，如下:

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

字段的描述和python对象里字段的描述类似。如:

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

向导中每一步/状态都有多个按钮，这些按钮都分布在对话框的右下方。向导的每一步所涉及的按钮列表在结果字典的状态键中声明.

.. i18n: For example:
..

例如:

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

#. 下一步的名称（决定下一个状态）
#. 按钮的名字 (用于在客户端上的展示)
#. the gtk stock item without the stock prefix (自 4.2)
#. a boolean, 如果为true，按钮被设置为默认的动作 (自 4.2) 

.. i18n: Here is a screenshot of this form:
..

以下为这种表单的截图:

.. i18n: .. image:: images/Wizard_screenshot1.png
.. i18n:    :width: 100%
..

.. image:: images/Wizard_screenshot1.png
   :width: 100%

.. i18n: Result: call a method to determine which state is next
..

Result: 调用方法决定下一个状态

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

Result: 打印一个报表

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

Result: 客户端执行一个动作

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

函数的返回的结果必须为 ir.actions.* 的所有字段. 这里为ir.action.act_window，所以客户端会打开一个新的标签页，新的标签页包含了account.invoicd的信息.

.. i18n: It is recommended to use the result of a read on the ir.actions object like this:
..

建议用一下方式读取 ir.actions 对象:

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

规范
=============

.. i18n: Form
.. i18n: ----
..

表单(Form)
------------

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

字段(Fields)
--------------

.. i18n: Standard
.. i18n: +++++++++
..

标准(Standard)
++++++++++++++++++

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

* **string**: 字段的标签(必填)
* **type**: (必填)
* **readonly**: (可选) 

.. i18n: Relational
.. i18n: ++++++++++
..

关系(Relational)
+++++++++++++++++++++

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

* **string**: 字段标签 (必填)
* **type**: (必填)
* **relation**: 所关系的对象名称 

.. i18n: Selection
.. i18n: ++++++++++
..

选择(Selection)
++++++++++++++++++

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

* **string**: 字段标签 (必填)
* **type**: (必填)
* **selection**: 选择字段中的键和值   

.. i18n: Add A New Wizard
.. i18n: ================
..

添加一个新向导
================

.. i18n: To create a new wizard, you must:
..

创建一个新向导，你应该:

.. i18n:     * create the wizard definition in a .py file
.. i18n:           * wizards are usually defined in the wizard subdirectory of their module as in server/bin/addons/module_name/wizard/your_wizard_name.py 
.. i18n:     * add your wizard to the list of import statements in the __init__.py file of your module's wizard subdirectory.
.. i18n:     * declare your wizard in the database 
..

    * 在一个 .py 文件中创建向导定义
          * 向导一般都是定义在组件中的向导子文件夹中 server/bin/addons/module_name/wizard/your_wizard_name.py 
    * 把向导添加到导入的声明列表，该列表位于组件向导子目录的 __init__.py 文件.
    * 在数据库中声明向导

.. i18n: The declaration is needed to map the wizard with a key of the client; when to launch which client. To declare a new wizard, you need to add it to the module_name_wizard.xml file, which contains all the wizard declarations for the module. If that file does not exist, you need to create it first.
..

声明需要映射向导和客户端键之间的关系，从而才能启动相应的客户端。声明一个新向导，需要把它加到 module_name_wizard.xml 文件里，该文件包含了此组件所有的向导声明。若该文件不存在，则需先创建.

.. i18n: Here is an example of the account_wizard.xml file;
..

这里以 account_wizard.xml 文件做一个例子;

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

向导的标签属性:

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

    * **id**: 此向导的唯一标识.
    * **string**: 如果一个资源关联多个向导，此字符串会显示）.
    * **model**: 对象从该模型中获取所需数据.
    * **name**: 向导的名称，只可内部使用并且唯一.
    * **replace** (可选): 此向导是否要重写 **all** 所有已经存在的向导。缺省值: False.
    * **menu** (可选): 是否 (True|False) 把向导和 'gears' 按钮 (i.e. show the button or not) 关联到一起。缺省值: True.
    * **keyword** (可选): 向导绑定另一动作 (print icon, gear icon, ...). 关键字属性的可能值为:
          * **client_print_multi**: 表单中的打印图标
          * **client_action_multi**: 表单中的 'gears' 图标
          * **tree_but_action**: 列表中的 'gears' 图标 (在左侧的快捷方式)
          * **tree_but_open**: 在树的一个分支，双击 (在左侧的快捷方式). 例如，有这样的应用，在菜单中来绑定向导. 

.. i18n: **__openerp__.py**
..

**__openerp__.py**

.. i18n: If the wizard you created is the first one of its module, you probably had to create the modulename_wizard.xml file yourself. In that case, it should be added to the update_xml field of the __openerp__.py file of the module.
..

若创建的向导是模块中的第一个，还需要创建 modulename_wizard.xml 文件. 在这样的情况下，需要在 __openerp__.py 模块文件中增加 update_xml 文件.

.. i18n: Here is, for example, the **__openerp__.py** file for the account module.
..

例如 ，下面的 account 模块 account_wizard.xml 需要添加到 **__openerp__.py** 文件.

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

osv_memory 向导系统
========================
开发一个 osv_memory 向导, 只需创建一普通的对象，不是继承至 osv.osv, 而是继承至 osv.osv_memory. 向导 "wizard" 的方法是在对象中的，如果向导很复杂，可以在对象中定义工作流. osv_memory 对象是存储在内存中的，而不是存储在 postgresql.

.. i18n: That's all, nothing more than just changing the inherit. These wizards can be defined at any location unlike addons/modulename/modulename_wizard.py. 
.. i18n: Historically, the _wizard prefix is for actual (old-style) wizards, so there might be a connotation there, the "new-style" osv_memory based "wizards" are perfectly normal objects (just used to emulate the old wizards, so they don't really match the old separations. 
.. i18n: Furthermore, osv_memory based "wizards" tend to need more than one object (e.g. one osv_memory object for each state of the original wizard) so the correspondence is not exactly 1:1.
..

就这些，仅仅是改变了继承。这些向导可以被定义在任意位置，而不仅仅是 addons/modulename/modulename_wizard.py. 
从历史上看，_wizard前缀的是（旧式）向导，所以有可能是一个osv_memory为基础的“新风格”“向导”是完全正常的对象（只是用来模拟旧的向导，并没有完全脱离旧式的向导. 
此外，osv_memory的“向导”，往往需要多个对象 (例如. 一个osv_memory对象为每个状态的原始向导) 所以对应的是不完全的 1:1.

.. i18n: So what makes them looks like 'old' wizards?
..

所以，为何他们看着想旧式的向导呢?

.. i18n:     * In the action that opens the object, you can put 
..

    * 在打开对象的动作中，你可以写入以下 

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	<field name="target">new</field>
..

.. code-block:: python

	<field name="target">new</field>

.. i18n: It means the object will open in a new window instead of the current one.
..

这表示对象会在一个新的窗口中打开，而非当前这个.

.. i18n:     * On a button, you can use <button special="cancel" .../> to close the window. 
..

    * 可以使用 <button special="cancel" .../> 来关闭窗口. 

.. i18n: Example : In project.py file.
..

例如 : 在 project.py 文件中.

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

* 视图也和普通的视图一样 (注意按钮). 

.. i18n: Example :
..

例如 :

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

* 动作也和普通的动作一样 (不要忘了添加一个target 属性) 

.. i18n: Example :
..

例如 :

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

osv_memory 配置项
=============================

.. i18n: Sometimes, your addon can't do with configurable defaults and needs
.. i18n: upfront configuration settings to work correctly. In these cases, you
.. i18n: want to provide a configuration wizard right after installation, and
.. i18n: potentially one which can be re-run later if needed.
..

有时，你的插件不希望用默认的配置，而需要进一步的配置从而工作的更好。在这种情况下，
你希望在安装之后能有一个配置向导，并在今后需要重新配置时能再次调用该向导.

.. i18n: Up until 5.0, OpenERP had such a facility but it was hardly documented
.. i18n: and a very manual, arduous process. A simpler, more straightforward
.. i18n: solution has been implemented for those needs.
..

5.0以上的openerp有这样的功能，但却无相应的文档，而且需要手工操作。为了这样的需求，
一个简单明了的新的解决方案已经出现.

.. i18n: The basic concepts
.. i18n: ------------------
..

基础概念
------------------

.. i18n: The new implementation provides a base behavior ``osv_memory`` object
.. i18n: from which you need to inherit. This behavior handles the flow between
.. i18n: the configuration items of the various extensions, and inheriting from
.. i18n: it is therefore mandatory.
..

新的解决方案提供一个具有基本的行为 ``osv_memory`` 对象，你必须继承该对象。这行为
是用来控制配置项和扩展之间的流的，而且必须继承自此对象.

.. i18n: There is also an inheritable view which provides a basic canvas,
.. i18n: through mechanisms which will be explained later it's highly
.. i18n: customizable. It's therefore strongly suggested that you should
.. i18n: inherit from that view from yours as well.
..

同时，还有一个可继承的视图，该视图提供一个基本的框架，通过这种机制从而达到很强的可定制性。所以强烈建议你继承该视图.

.. i18n: Creating a basic configuration item
.. i18n: -----------------------------------
..

创建基本的配置项
-----------------------------------

.. i18n: Your configuration model
.. i18n: ++++++++++++++++++++++++
..

你的配置模型
++++++++++++++++++++++++

.. i18n: First comes the creation of the configuration item itself. This is a
.. i18n: normal ``osv_memory`` object with a few constraints:
..

首先是创建配置项本身，这是以个普通的 ``osv_memory`` 对象，该对象有一些限制:

.. i18n: * it has to inherit from ``res.config``, which provides the basic
.. i18n:   configuration behaviors as well as the base event handlers and
.. i18n:   extension points
.. i18n: 
.. i18n: * it has to provide an ``execute`` method.[#]_ This method will be called
.. i18n:   when validating the configuration form and contains the validation
.. i18n:   logic. It shouldn't return anything.
..

* 必须继承至 ``res.config``, 提供一个基本的配置行为和基本的事件控制器和扩展点

* 必须提供一个 ``execute`` 方法.[#]_ 当验证配置表单和包含验证逻辑时，就会调用这个方法。方法没有返回值.

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

配置视图
+++++++++++++++++++++++

.. i18n: Then comes the configuration form. OpenERP provides a base view which
.. i18n: you can inherit so you don't have to deal with creating buttons and
.. i18n: handling the progress bar (which should be displayed at the bottom
.. i18n: left of all initial configuration dialogs). It's very strongly
.. i18n: recommended that you use this base view.
..

接下来是配置表单。Openerp提供一个基础视图，你可以继承这个基础视图，所以你
不需要自己创建按钮和控制进度条。强烈推荐使用这个基本视图.

.. i18n: Simply add an ``inherit_id`` field to a regular ``ir.ui.view`` and
.. i18n: set its value to ``res_config_view_base``:
..

在 ``ir.ui.view`` 中加入一个 ``inherit_id`` 字段，把它的值设为 ``res_config_view_base``:

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

当不做任何改变时，会展示出一个对话框，该对话框中包含一个进度条和两个按钮，
毫无生趣. ``res_config_view_base`` 有一个特别的group hook，你可以用你自己
的代码代替它，如下:

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

打开你的窗口
+++++++++++++++++++

.. i18n: The next step is to create the ``act_window`` which links to the
.. i18n: configuration model and the view:
..

下一步是创建 ``act_window`` ，用于连接模型和视图的配置:

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

当在配置向导步骤的子菜单中列出多种配置选项时，注意到 ``act_window`` 的 ``name`` 字段会被显示出来
 (在 Administration > Configuration > Configuration > Wizards).


.. i18n: Registering your action
.. i18n: +++++++++++++++++++++++
..

注册你的动作
+++++++++++++++++++++++

.. i18n: Finally comes actually registering the configuration item with
.. i18n: OpenERP. This is done with an ``ir.actions.todo`` object, which
.. i18n: mandates a single ``action_id`` field referencing the ``act_window``
.. i18n: created previously:
..

最后是在openerp中注册配置项。这是在 ``ir.actions.todo`` 对象中完成的，
需要一个 ``action_id`` 字段关联到之前创建的 ``act_window``:

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

``ir.actions.todo`` 有3个可选字段:

.. i18n: ``sequence`` (default: ``10``)
.. i18n:     The order in which the different steps are to be
.. i18n:     executed, lowest first.
..

``sequence`` (default: ``10``)
    执行次序，数值小的先执行.

.. i18n: ``active`` (default: ``True``)
.. i18n:     An inactive step will not be executed on the next round of
.. i18n:     configuration.
..

``active`` (default: ``True``)
    不活跃的步骤在下一轮配置时将不会被执行.

.. i18n: ``state`` (default: ``'open'``)
.. i18n:     The current state for the configuration step, mostly used to
.. i18n:     register what happened during its execution. The possible
.. i18n:     values are ``'open'``, ``'done'``, ``'skip'`` and
.. i18n:     ``'cancel'``.
..

``state`` (default: ``'open'``)
    配置步骤的当前状态，用于记录执行过程中所发生的时间，值包含有 ``'open'``, ``'done'``, ``'skip'`` and
    ``'cancel'``.

.. i18n: The result at this point is the following:
..

结果如下图:

.. i18n: .. image:: images/config_wizard_base.png
.. i18n:    :width: 100%
..

.. image:: images/config_wizard_base.png
   :width: 100%

.. i18n: Customizing your configuration item
.. i18n: -----------------------------------
..

定制你的配置项
-----------------------------------

.. i18n: While your current knowledge is certainly enough to configure your
.. i18n: addon, a bit of good customization can be the difference between a
.. i18n: good user experience and a great user experience.
..

目前所具备的知识已经足够配置你的插件了，但做一些好的定制能得到更好的用户体验.

.. i18n: More extensive view customization
.. i18n: +++++++++++++++++++++++++++++++++
..

更进一步的视图的定制
+++++++++++++++++++++++++++++++++

.. i18n: As you might have noticed from the previous screen shot, by default
.. i18n: your configuration window doesn't have a *title*, which isn't a
.. i18n: problem but doesn't look very good either.
..

也许你已经注意到之前的截图，在默认的情况下，窗口是没有标题的，虽然并无大碍但却影响美观.

.. i18n: Before setting a title, a small modification to the existing view is
.. i18n: needed though: the existing ``group`` needs to be wrapped in a
.. i18n: ``data`` element so it's possible to customize more than one item of
.. i18n: the parent view:
..

在设置一个标题之前，需要在视图里做一些微小的改动:  ``group`` 标签中需要填入 ``data`` ，这样就能修改父窗口中的多项配置:

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

然后，就能通过增加以下代码 ``data`` 元件，从而转换原始 ``form`` 的 ``string`` 属性 (这个例子,或许在 ``group`` 前):

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

完成这步后，配置的表单有用了一个标题:

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

更有趣的配置比如改变按钮，按钮是由对话框底部的 ``res_config_view_base`` 提供的：
删除一个按钮（若配置无法被跳过），改变按钮标签, ...

.. i18n: Since no specific hooks are provided for these alterations, they
.. i18n: require the use of xpath selectors (using the ``xpath`` element).
..

由于这些改变无具体的与之关联的属性，需要使用xpath选择器（使用 ``xpath`` 元素).

.. i18n: Removing the Skip button and changing the label of the Record button
.. i18n: to Set, for instance, would be done by adding the following after the
.. i18n: ``group`` element:
..

删除Skip按钮，把Recond按钮的标签改成Set。例如，可以在
``group`` 元素后加入以下代码，如下:

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

还可以用这种方法改变按钮的名称, 这样方法在对象中被唤醒 (不推荐).

.. i18n: Model customization
.. i18n: +++++++++++++++++++
..

定制模型
+++++++++++++++++++

.. i18n: Though most of the requirements should be easy to fulfill using the
.. i18n: provided ``execute`` method hook, some addon-specific requirements
.. i18n: are a bit more complex. ``res.config`` should be able to provide all
.. i18n: the hooks necessary for more complex behaviors.
..

使用 ``execute`` method hook, 可以很轻易的实现许多要求，但addon-specific要求会
更复杂点. ``res.config`` 必须提供所有的hooks用于复杂的行为.

.. i18n: Ignoring the next step
.. i18n: ~~~~~~~~~~~~~~~~~~~~~~
..

忽略下一步
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. i18n: Ultimately, the switch to the next configuration item is done by
.. i18n: calling the ``self.next`` method of ``res.config`` [#]_. This is the
.. i18n: last thing the base implementations of ``action_next`` and
.. i18n: ``action_skip`` do. But in some cases, looping on the current view or
.. i18n: implementing a workflow-like behavior is needed. In these cases, you
.. i18n: can simply return a dictionary from ``execute``, and ``res.config``
.. i18n: will jump to that view instead of the one returned by ``self.next``.
..

最后，通过调用 ``res.config`` 中的 ``self.next`` 方法，进入下一步的配置项。 ``action_next`` 和 ``action_skip`` 最后
做的事。但是在某些情况下，循环当前的视图或实现一个和工作流一样的行为是必要的。在这样的情况下，
你可以通过 ``execute`` 返回一个字典， ``res.config`` 会跳转到那个视图，而不是 ``self.next`` 返回的那个 .

.. i18n: This is what the user creation item does, for instance, to let the
.. i18n: user create several new users in a row.
..

这是创建项目所必须做的，例如，让用户在一行中创建多个新用户.

.. i18n: Performing an action on skipping
.. i18n: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..

在 skipping 执行一个动作
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

和 ``action_next`` 对比（ ``action_next`` 要求 ``execute`` 被子类实现）， ``action_skip`` 是实现 ``res.config`` 的。
但是在子模型需要完成sipping discovery的动作的情况下，它需要提供一个方法，该方法名为 ``cancel`` ，
你可以用和 ``execute`` 一样的方法重载此函数。这是和 ``execute`` 一致的：不仅在 ``cancel`` 结束时可以自动调用 ``next`` 方法，
而且能 `忽略下一步`_ 


.. i18n: Alternative actions
.. i18n: ~~~~~~~~~~~~~~~~~~~
..

选取动作
~~~~~~~~~~~~~~~~~~~

.. i18n: It's also possible to either overload ``action_next`` and
.. i18n: ``action_skip`` or, more useful, to implement more actions than these
.. i18n: two, if more than two buttons are needed for instance.
..

既可以选择action重载 ``action_next`` 和
``action_skip`` 方法，也可以实现更多的函数，如果此实例中的按钮多余两.

.. i18n: In this case, please remember that you should always provide a way to
.. i18n: reach ``self.next`` to the user, in order for him to be able to
.. i18n: configure the rest of his addons.
..

在这样的情况下，请记住，你需要提供一个方法，让用户能调用self.next函数，这样他才能配置他剩下的插件.

.. i18n: ``res.config``'s public API
.. i18n: ---------------------------
..

``res.config`` 的公开接口
---------------------------

.. i18n: All of the public API methods take the standard OpenERP set of
.. i18n: arguments: ``self``, ``cr``, ``uid``, ``ids`` and ``context``.
..

接口和标准的Openerp的变量一致: ``self``, ``cr``, ``uid``, ``ids`` and ``context``.

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

Hook 方法会被 ``action_next`` 按钮（默认标签：Record）唤醒. 除非你想展示一个
新的视图而非下一步的配置项，否则不要返回任何内容 *anything* 。返回字典以为的东西将会导致未定义的行为.

.. i18n: It is mandatory to overload it. Failure to do so will result in a
.. i18n: ``NotImplementedError`` being raised at runtime.
..

重写它是必须的。如果不这么做，将会导致 ``NotImplementedError`` 错误.

.. i18n: The default ``res.config`` implementation should not be called in the
.. i18n: overload (don't use ``super``).
..

默认的 ``res.config`` 在重载时不能被调用 (don't use ``super``).

.. i18n: ``cancel``
.. i18n: ++++++++++
..

``cancel``
++++++++++

.. i18n: Hook method called in case the ``action_skip`` button
.. i18n: (default label: Skip) is clicked. Its behavior is the same as
.. i18n: `execute`_'s, except it's not mandatory to overload it.
..

``action_skip`` 按钮 (default label: Skip) 会调用相关的方法，他和 `execute`_' 是一样的，除了它不是必须被重载.

.. i18n: ``next``
.. i18n: ++++++++
..

``next``
++++++++

.. i18n: Method called to fetch the todo (and the corresponding action) for the
.. i18n: next configuration item. It can be overloaded if the configuration
.. i18n: item needs custom behavior common to all events.
..

下一步配置项调用绑定的方法.若配置项需要定制，则它可以被重载.

.. i18n: If overloaded, the default ``res.config`` implementation must be
.. i18n: called and its result returned in order to get and execute the next
.. i18n: configuration item.
..

如果被重载，默认的 ``res.config`` 的实现将会被调用，返回值是为了下一步的配置项.

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

基础视图中的时间控制按钮，重载他们是不需要的，但是在默认的
``res.config`` 实现被调用 (via ``super``) 且有返回值的情况下是必须的.

.. i18n: .. [#] This isn't completely true, as you will see when `Customizing
.. i18n:        your configuration item`_
..

.. [#] This isn't completely true, as you will see when `定制你的配置项`_

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

转换视图到实际视图(real view)显示你的向导模块定义：

.. i18n: Old Wizard File : wizard_product_margin.py
.. i18n: ------------------------------------------
..

旧的向导文件 : wizard_product_margin.py
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

新的向导文件 : wizard/<<module_name>>_<<filename>>_view.xml
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

Note: 在旧向导全部状态下，我们应该用新途径建立按钮。

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

菜单选项
------------

.. i18n: To open a wizard view via a menuitem you can use the following syntax for the menu, using the XML id of the corresponding act_window.

你可以使用下面的菜单语法打开一个向导视图(wizard view),  使用相应的act_window的XML id.

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

4.打开向导视图(wizard view)经由“其他”按钮你可以使用下面的语法，应用相应的act_window里的XML id，构建按钮。这个常被应用到制作多步骤向导中。

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

5.最后，你必须清理模块，如果你修改该了向导python文件名，那么必须更新__init__.py的python文件，同时对你新的XML文件加入到__openerp__.py文件的update_xml字段中。

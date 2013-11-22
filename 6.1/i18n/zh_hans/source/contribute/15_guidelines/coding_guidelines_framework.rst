.. i18n: .. sectnum::
.. i18n:     :start: 2
..

.. sectnum::
    :start: 2

.. i18n: OpenERP Specific Guidelines
.. i18n: +++++++++++++++++++++++++++
..

OpenERP 特别指引
+++++++++++++++++++++++++++

.. i18n: Bazaar is your historian
.. i18n: ------------------------
.. i18n: Do not comment out code if you want to disable it. The code is versioned in
.. i18n: Bazaar, and regardless of your opinion about Bazaar, it does not lose
.. i18n: the file history.
..

Bazaar 是你的历史档案
------------------------
不要通过注释来禁用代码。代码的各个版本会记录在Bazaar里面，把你的意见写到里面，它不会丢失这些文件的记录的。

.. i18n: Leaving comments just makes the code messier and harder to read. And don't
.. i18n: worry about making your changes obvious, that's the purpose of ``diff``::
.. i18n: 
.. i18n:     # no example for this one, code was really removed ;-)
..

留下注释只会让代码更加难以阅读。``diff`` 的目的就是让你不用担心直接更改代码::

    # no example for this one, code was really removed ;-)

.. i18n: Call your fish a fish
.. i18n: ---------------------
.. i18n: Always give your variables a meaningful name.
.. i18n: You may know what it is referring to now, but you won't in 2 months, and
.. i18n: others don't either. One-letter variables are acceptable only in lambda 
.. i18n: expressions and loop indices, or perhaps in pure maths expressions
.. i18n: (and even there it doesn't hurt to use a real name)::
.. i18n: 
.. i18n:     # unclear and misleading
.. i18n:     a = {}
.. i18n:     ffields = {}
.. i18n: 
.. i18n:     # better
.. i18n:     results = {}
.. i18n:     selected_fields = {}
..

命名要言之有物
---------------------
Always give your variables a meaningful name.
You may know what it is referring to now, but you won't in 2 months, and
others don't either. One-letter variables are acceptable only in lambda 
expressions and loop indices, or perhaps in pure maths expressions
(and even there it doesn't hurt to use a real name)::

    # unclear and misleading
    a = {}
    ffields = {}

    # better
    results = {}
    selected_fields = {}

.. i18n: Do not bypass the ORM
.. i18n: ---------------------
.. i18n: You should never use the database cursor directly when the ORM can do the
.. i18n: same thing! By doing so you are bypassing all the ORM features,
.. i18n: possibly the transactions, access rights and so on.
..

不要绕过ORM
---------------------
You should never use the database cursor directly when the ORM can do the
same thing! By doing so you are bypassing all the ORM features,
possibly the transactions, access rights and so on.

.. i18n: And chances are that you are also making the code harder to read and
.. i18n: probably less secure (see also next guideline)::
.. i18n: 
.. i18n:     # very very wrong
.. i18n:     cr.execute('select id from auction_lots where auction_id in (' +
.. i18n:                ','.join(map(str,ids))+') and state=%s and obj_price>0',
.. i18n:                ('draft',))
.. i18n:     auction_lots_ids = [x[0] for x in cr.fetchall()]
.. i18n: 
.. i18n:     # no injection, but still wrong
.. i18n:     cr.execute('select id from auction_lots where auction_id in %s '\
.. i18n:                'and state=%s and obj_price>0',
.. i18n:                (tuple(ids),'draft',))
.. i18n:     auction_lots_ids = [x[0] for x in cr.fetchall()]
.. i18n: 
.. i18n:     # better
.. i18n:     auction_lots_ids = self.search(cr,uid,
.. i18n:                                    [('auction_id','in',ids),
.. i18n:                                     ('state','=','draft'),
.. i18n:                                     ('obj_price','>',0)])
..

And chances are that you are also making the code harder to read and
probably less secure (see also next guideline)::

    # very very wrong
    cr.execute('select id from auction_lots where auction_id in (' +
               ','.join(map(str,ids))+') and state=%s and obj_price>0',
               ('draft',))
    auction_lots_ids = [x[0] for x in cr.fetchall()]

    # no injection, but still wrong
    cr.execute('select id from auction_lots where auction_id in %s '\
               'and state=%s and obj_price>0',
               (tuple(ids),'draft',))
    auction_lots_ids = [x[0] for x in cr.fetchall()]

    # better
    auction_lots_ids = self.search(cr,uid,
                                   [('auction_id','in',ids),
                                    ('state','=','draft'),
                                    ('obj_price','>',0)])

.. i18n: No SQL injections, please!
.. i18n: --------------------------
.. i18n: Care must be taken not to introduce SQL injections vulnerabilities when using
.. i18n: manual SQL queries.  The vulnerability is present when user input is either
.. i18n: incorrectly filtered or badly quoted, allowing an attacker to introduce
.. i18n: undesirable clauses to a SQL query (such as circumventing filters or executing
.. i18n: **UPDATE** or **DELETE** commands).
..

请不要SQL注入
--------------------------
Care must be taken not to introduce SQL injections vulnerabilities when using
manual SQL queries.  The vulnerability is present when user input is either
incorrectly filtered or badly quoted, allowing an attacker to introduce
undesirable clauses to a SQL query (such as circumventing filters or executing
**UPDATE** or **DELETE** commands).

.. i18n: The best way to be safe is to never, NEVER use Python string concatenation (+)
.. i18n: or string parameters interpolation (%) to pass variables to a SQL query string.
..

The best way to be safe is to never, NEVER use Python string concatenation (+)
or string parameters interpolation (%) to pass variables to a SQL query string.

.. i18n: The second reason, which is almost as important, is that it is the job of the
.. i18n: database abstraction layer (psycopg2) to decide how to format query parameters,
.. i18n: not your job!
.. i18n: For example psycopg2 knows that when you pass a list of values it needs to 
.. i18n: format them as a comma-separated list, enclosed in parentheses!
..

The second reason, which is almost as important, is that it is the job of the
database abstraction layer (psycopg2) to decide how to format query parameters,
not your job!
For example psycopg2 knows that when you pass a list of values it needs to 
format them as a comma-separated list, enclosed in parentheses!

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     # the following is very bad:
.. i18n:     #   - it's a SQL injection vulnerability
.. i18n:     #   - it's unreadable
.. i18n:     #   - it's not your job to format the list of ids
.. i18n:     cr.execute('select distinct child_id from account_account_consol_rel ' +
.. i18n:                'where parent_id in ('+','.join(map(str, ids))+')')
.. i18n: 
.. i18n:     # better
.. i18n:     cr.execute('SELECT DISTINCT child_id '\
.. i18n:                'FROM account_account_consol_rel '\
.. i18n:                'WHERE parent_id IN %s',
.. i18n:                (tuple(ids),))
..

.. code-block:: python

    # the following is very bad:
    #   - it's a SQL injection vulnerability
    #   - it's unreadable
    #   - it's not your job to format the list of ids
    cr.execute('select distinct child_id from account_account_consol_rel ' +
               'where parent_id in ('+','.join(map(str, ids))+')')

    # better
    cr.execute('SELECT DISTINCT child_id '\
               'FROM account_account_consol_rel '\
               'WHERE parent_id IN %s',
               (tuple(ids),))

.. i18n: This is very important, so please be careful also when refactoring, and most
.. i18n: importantly do not copy these patterns!
..

This is very important, so please be careful also when refactoring, and most
importantly do not copy these patterns!

.. i18n: Here is a `memorable example <http://www.bobby-tables.com>`_ to help
.. i18n: you remember what the issue is about (but do not copy the code there).
..

Here is a `memorable example <http://www.bobby-tables.com>`_ to help
you remember what the issue is about (but do not copy the code there).

.. i18n: Before continuing, please be sure to read the online documentation of pyscopg2
.. i18n: to learn of to use it properly:
..

Before continuing, please be sure to read the online documentation of pyscopg2
to learn of to use it properly:

.. i18n:  * `The problem with query parameters <http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters>`_
.. i18n:  * `How to pass parameters with psycopg2 <http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries>`_
.. i18n:  * `Advanced parameter types <http://initd.org/psycopg/docs/usage.html#adaptation-of-python-values-to-sql-types>`_
..

 * `The problem with query parameters <http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters>`_
 * `How to pass parameters with psycopg2 <http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries>`_
 * `Advanced parameter types <http://initd.org/psycopg/docs/usage.html#adaptation-of-python-values-to-sql-types>`_

.. i18n: Factor out the code
.. i18n: -------------------
.. i18n: If you are writing the same code over and over and it is more than one line,
.. i18n: then you must factor it out into a reusable function or method::
.. i18n: 
.. i18n:     # after writing this multiple times:
.. i18n:     terp = get_module_resource(module, '__openerp__.py')
.. i18n:     if not os.path.isfile(terp):
.. i18n:        terp = addons.get_module_resource(module, '__terp__.py')
.. i18n:        info = eval(tools.file_open(terp).read())
.. i18n: 
.. i18n:     # make a function out of it
.. i18n:     def _load_information_from_description_file(module):
.. i18n:         for filename in ['__openerp__.py', '__terp__.py']:
.. i18n:             description_file = addons.get_module_resource(module, filename)
.. i18n:             if os.path.isfile(description_file):
.. i18n:                 return eval(tools.file_open(description_file).read())
.. i18n:         raise Exception('The module %s does not contain a description file!')
..

合理抽象
-------------------
If you are writing the same code over and over and it is more than one line,
then you must factor it out into a reusable function or method::

    # after writing this multiple times:
    terp = get_module_resource(module, '__openerp__.py')
    if not os.path.isfile(terp):
       terp = addons.get_module_resource(module, '__terp__.py')
       info = eval(tools.file_open(terp).read())

    # make a function out of it
    def _load_information_from_description_file(module):
        for filename in ['__openerp__.py', '__terp__.py']:
            description_file = addons.get_module_resource(module, filename)
            if os.path.isfile(description_file):
                return eval(tools.file_open(description_file).read())
        raise Exception('The module %s does not contain a description file!')

.. i18n: The infamous context
.. i18n: --------------------
.. i18n: Do not use mutable objects as default values for functions, because they are
.. i18n: created as constants (evaluated only once), so you will have possible
.. i18n: side-effects if you modify them.
.. i18n: The usual example of this is the ``context`` argument to all ORM methods::
.. i18n: 
.. i18n:     # bad, this could have side-effects
.. i18n:     def spam(eggs, context={}):
.. i18n:        setting = context.get('foo')
.. i18n:        #...
.. i18n: 
.. i18n:     # this is better if your need to use the context
.. i18n:     def spam(eggs, context=None):
.. i18n:        if context is None:
.. i18n:           context = {}
.. i18n:        setting = context.get('foo')
.. i18n:        #...
..

警惕context
--------------------
Do not use mutable objects as default values for functions, because they are
created as constants (evaluated only once), so you will have possible
side-effects if you modify them.
The usual example of this is the ``context`` argument to all ORM methods::

    # bad, this could have side-effects
    def spam(eggs, context={}):
       setting = context.get('foo')
       #...

    # this is better if your need to use the context
    def spam(eggs, context=None):
       if context is None:
          context = {}
       setting = context.get('foo')
       #...

.. i18n: Also be careful with boolean tests on lists and maps, because an empty
.. i18n: dict, list or tuple will evaluate as ``False``::
.. i18n: 
.. i18n:     # bad, you shadow the original context if it's empty
.. i18n:     def spam(eggs, context=None):
.. i18n:        if not context:
.. i18n:           context = {}
.. i18n:        setting = context.get('foo')
.. i18n:        #...
..

Also be careful with boolean tests on lists and maps, because an empty
dict, list or tuple will evaluate as ``False``::

    # bad, you shadow the original context if it's empty
    def spam(eggs, context=None):
       if not context:
          context = {}
       setting = context.get('foo')
       #...

.. i18n: And it's okay if you only need to forward it, you can pass ``None`` and
.. i18n: let the downstream code handle it::
.. i18n: 
.. i18n:     # fine
.. i18n:     def spam(eggs, context=None):
.. i18n:         setting = get_setting(True, context=context)
..

And it's okay if you only need to forward it, you can pass ``None`` and
let the downstream code handle it::

    # fine
    def spam(eggs, context=None):
        setting = get_setting(True, context=context)

.. i18n: See also `launchpad bug 525808 <https://bugs.launchpad.net/openobject-server/+bug/525808>`_.
..

See also `launchpad bug 525808 <https://bugs.launchpad.net/openobject-server/+bug/525808>`_.

.. i18n: There is better than lambda, sometimes
.. i18n: --------------------------------------
.. i18n: Instead of writing trivial lambda expression to extract items or attributes
.. i18n: from a list of data structures, learn to use list comprehension
.. i18n: or ``operator.itemgetter`` and ``operator.attrgetter`` instead, which are
.. i18n: often more readable and faster::
.. i18n: 
.. i18n:     # not very readable
.. i18n:     partner_tuples = map(lambda x: (x['id'], x['name']), partners)
.. i18n: 
.. i18n:     # better with list comprehension for just one item/attribute
.. i18n:     partner_ids = [partner['id'] for partner in partners]
.. i18n: 
.. i18n:     # better with operator for many items/attributes
.. i18n:     from operator import itemgetter
.. i18n:     # ...
.. i18n:     partner_tuples = map(itemgetter('id', 'name'), partners)
..

有时候这比 lambda 好
--------------------------------------
Instead of writing trivial lambda expression to extract items or attributes
from a list of data structures, learn to use list comprehension
or ``operator.itemgetter`` and ``operator.attrgetter`` instead, which are
often more readable and faster::

    # not very readable
    partner_tuples = map(lambda x: (x['id'], x['name']), partners)

    # better with list comprehension for just one item/attribute
    partner_ids = [partner['id'] for partner in partners]

    # better with operator for many items/attributes
    from operator import itemgetter
    # ...
    partner_tuples = map(itemgetter('id', 'name'), partners)

.. i18n: See also http://docs.python.org/library/operator.html#operator.attrgetter
..

See also http://docs.python.org/library/operator.html#operator.attrgetter

.. i18n: As of version 6.0 you can also use literal values as defaults for
.. i18n: your ORM columns, which means that you can stop writing these::
.. i18n: 
.. i18n:     # lots of trivial one-liners in 5.0
.. i18n:     _defaults = {
.. i18n:         'active': lambda *x: True,
.. i18n:         'state': lambda *x: 'draft',
.. i18n:     }
.. i18n: 
.. i18n:     # much simpler as of 6.0
.. i18n:     _defaults = {
.. i18n:         'active': True,
.. i18n:         'state': 'draft',
.. i18n:     }
..

As of version 6.0 you can also use literal values as defaults for
your ORM columns, which means that you can stop writing these::

    # lots of trivial one-liners in 5.0
    _defaults = {
        'active': lambda *x: True,
        'state': lambda *x: 'draft',
    }

    # much simpler as of 6.0
    _defaults = {
        'active': True,
        'state': 'draft',
    }

.. i18n: .. warning::
.. i18n: 
.. i18n:     Be careful with this, because non-callable defaults are only evaluated
.. i18n:     once! If you want to generate new default values for each
.. i18n:     record you really need to keep the ``lambda`` or make it a callable.
..

.. warning::

    Be careful with this, because non-callable defaults are only evaluated
    once! If you want to generate new default values for each
    record you really need to keep the ``lambda`` or make it a callable.

.. i18n: The most frequent error is with timestamps, as in the following example::
.. i18n: 
.. i18n:     # This will always give the server start time!
.. i18n:     _defaults = {
.. i18n:         'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
.. i18n:     }
.. i18n: 
.. i18n:     # You need to keep it callable, e.g:
.. i18n:     _defaults = {
.. i18n:         'timestamp': lambda *x: time.strftime('%Y-%m-%d %H:%M:%S'),
.. i18n:     }
..

The most frequent error is with timestamps, as in the following example::

    # This will always give the server start time!
    _defaults = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
    }

    # You need to keep it callable, e.g:
    _defaults = {
        'timestamp': lambda *x: time.strftime('%Y-%m-%d %H:%M:%S'),
    }

.. i18n: Keep your methods short/simple when possible
.. i18n: --------------------------------------------
.. i18n: Functions and methods should not contain too much logic: having a lot of small and simple methods is more advisable than having few
.. i18n: large and complex methods. A good rule of thumb is to split a method as soon as:
..

保持您的方法尽量简洁/简单
--------------------------------------------
Functions and methods should not contain too much logic: having a lot of small and simple methods is more advisable than having few
large and complex methods. A good rule of thumb is to split a method as soon as:

.. i18n:     * it has more than one responsibility (see http://en.wikipedia.org/wiki/Single_responsibility_principle)
.. i18n:     * it is too big to fit on one screen.
..

    * it has more than one responsibility (see http://en.wikipedia.org/wiki/Single_responsibility_principle)
    * it is too big to fit on one screen.

.. i18n: Also, name your functions accordingly: small and properly named functions are the starting point of readable/maintainable code and tighter documentation.
..

Also, name your functions accordingly: small and properly named functions are the starting point of readable/maintainable code and tighter documentation.

.. i18n: This recommendation is also relevant for classes, files, modules and packages. (See also http://en.wikipedia.org/wiki/Cyclomatic_complexity )
..

This recommendation is also relevant for classes, files, modules and packages. (See also http://en.wikipedia.org/wiki/Cyclomatic_complexity )

.. i18n: Never commit the transaction
.. i18n: ----------------------------
.. i18n: The OpenERP/OpenObject framework is in charge of providing the transactional context for all RPC calls.
.. i18n: The principle is that a new database cursor is opened at the beginning of each RPC call, and committed
.. i18n: when the call has returned, just before transmitting the answer to the RPC client, approximately like this::
.. i18n: 
.. i18n:     def execute(self, db_name, uid, obj, method, *args, **kw):
.. i18n:         db, pool = pooler.get_db_and_pool(db_name)
.. i18n:         # create transaction cursor
.. i18n:         cr = db.cursor()
.. i18n:         try:
.. i18n:             res = pool.execute_cr(cr, uid, obj, method, *args, **kw)
.. i18n:             cr.commit() # all good, we commit
.. i18n:         except Exception:
.. i18n:             cr.rollback() # error, rollback everything atomically
.. i18n:             raise
.. i18n:         finally:
.. i18n:             cr.close() # always close cursor opened manually
.. i18n:         return res
..

不要提交事务
----------------------------
The OpenERP/OpenObject framework is in charge of providing the transactional context for all RPC calls.
The principle is that a new database cursor is opened at the beginning of each RPC call, and committed
when the call has returned, just before transmitting the answer to the RPC client, approximately like this::

    def execute(self, db_name, uid, obj, method, *args, **kw):
        db, pool = pooler.get_db_and_pool(db_name)
        # create transaction cursor
        cr = db.cursor()
        try:
            res = pool.execute_cr(cr, uid, obj, method, *args, **kw)
            cr.commit() # all good, we commit
        except Exception:
            cr.rollback() # error, rollback everything atomically
            raise
        finally:
            cr.close() # always close cursor opened manually
        return res

.. i18n: If any error occurs during the execution of the RPC call, the transaction is rolled back atomically,
.. i18n: preserving the state of the system.
..

If any error occurs during the execution of the RPC call, the transaction is rolled back atomically,
preserving the state of the system.

.. i18n: Similarly, the system also provides a dedicated transaction during the execution of tests suites,
.. i18n: so it can be rolled back or not depending on the server startup options.
..

Similarly, the system also provides a dedicated transaction during the execution of tests suites,
so it can be rolled back or not depending on the server startup options.

.. i18n: The consequence is that if you manually call ``cr.commit()`` anywhere there is a very high chance
.. i18n: that you **will** break the system in various ways, because you will cause partial commits, and thus
.. i18n: partial and unclean rollbacks, causing among others:
..

The consequence is that if you manually call ``cr.commit()`` anywhere there is a very high chance
that you **will** break the system in various ways, because you will cause partial commits, and thus
partial and unclean rollbacks, causing among others:

.. i18n:  - inconsistent business data, usually data loss ;
.. i18n:  - workflow desynchronization, documents stuck permanently ;
.. i18n:  - tests that can't be rolled back cleanly, and will start polluting the database,
.. i18n:    and triggering error (this is true even if no error occurs during the transaction) ;
..

 - inconsistent business data, usually data loss ;
 - workflow desynchronization, documents stuck permanently ;
 - tests that can't be rolled back cleanly, and will start polluting the database,
   and triggering error (this is true even if no error occurs during the transaction) ;

.. i18n: Here is the very simple rule:
..

Here is the very simple rule:

.. i18n: .. warning:: **You should NEVER call cr.commit() yourself, UNLESS you have created your own 
.. i18n:    database cursor explicitly! And the situations where you need to do that are exceptional!**
..

.. warning:: **You should NEVER call cr.commit() yourself, UNLESS you have created your own 
   database cursor explicitly! And the situations where you need to do that are exceptional!**

.. i18n: And by the way if you did create your own cursor, then you need to handle error cases and proper
.. i18n: rollback, as well as properly close the cursor when you're done with it.
..

And by the way if you did create your own cursor, then you need to handle error cases and proper
rollback, as well as properly close the cursor when you're done with it.

.. i18n: And contrary to popular belief, you do *not* even need to call ``cr.commit()`` in the following
.. i18n: situations:
..

And contrary to popular belief, you do *not* even need to call ``cr.commit()`` in the following
situations:

.. i18n:  - in the ``_auto_init()`` method of an ``osv.osv`` object: this is taken care of by the addons
.. i18n:    initialization method, or by the ORM transaction when creating custom models ;
.. i18n:  - in reports: the ``commit()`` is handled by the framework too, so you can update the database
.. i18n:    even from within a report ;
.. i18n:  - within ``osv.osv_memory`` methods: these methods are called exactly like regular ``osv.osv``
.. i18n:    ones, within a transaction and with the corresponding ``cr.commit()``/``rollback()`` at the end ;
.. i18n:  - etc. (see general rule above if you have in doubt!)
..

 - in the ``_auto_init()`` method of an ``osv.osv`` object: this is taken care of by the addons
   initialization method, or by the ORM transaction when creating custom models ;
 - in reports: the ``commit()`` is handled by the framework too, so you can update the database
   even from within a report ;
 - within ``osv.osv_memory`` methods: these methods are called exactly like regular ``osv.osv``
   ones, within a transaction and with the corresponding ``cr.commit()``/``rollback()`` at the end ;
 - etc. (see general rule above if you have in doubt!)

.. i18n: And another very simple rule:
..

And another very simple rule:

.. i18n: .. warning:: **All cr.commit() calls outside of the server framework from now on must have an explicit
.. i18n:    comment explaining why they are absolutely necessary, why they are indeed correct, and why
.. i18n:    they do not break the transactions. Otherwise they can and will be removed!**
..

.. warning:: **All cr.commit() calls outside of the server framework from now on must have an explicit
   comment explaining why they are absolutely necessary, why they are indeed correct, and why
   they do not break the transactions. Otherwise they can and will be removed!**

.. i18n: Use the gettext method correctly
.. i18n: --------------------------------
..

正确使用 gettext 方法
--------------------------------

.. i18n: OpenERP uses a GetText-like method named "underscore" ``_( )`` to indicate that a static
.. i18n: string used in the code needs to be translated at runtime using the language of the context.
.. i18n: This pseudo-method is accessed within your code by importing as follows::
.. i18n: 
.. i18n:     from tools.translate import _
..

OpenERP uses a GetText-like method named "underscore" ``_( )`` to indicate that a static
string used in the code needs to be translated at runtime using the language of the context.
This pseudo-method is accessed within your code by importing as follows::

    from tools.translate import _

.. i18n: A few very important rules must be followed when using it, in order for it to work and to
.. i18n: avoid filling the translations with useless junk.
..

A few very important rules must be followed when using it, in order for it to work and to
avoid filling the translations with useless junk.

.. i18n: Basically, this method should only be used for static strings written manually in the code,
.. i18n: it will not work to translate field *values*, such as Product names, etc. This must be
.. i18n: done instead using the ``translate`` flag on the corresponding field.
..

Basically, this method should only be used for static strings written manually in the code,
it will not work to translate field *values*, such as Product names, etc. This must be
done instead using the ``translate`` flag on the corresponding field.

.. i18n: The rule is very simple: calls to the underscore method should *always* be in the form ``_('literal string')``
.. i18n: and nothing else::
.. i18n: 
.. i18n:     # Good: plain strings
.. i18n:     error = _('This record is locked!')
.. i18n: 
.. i18n:     # Good: strings with formatting patterns included
.. i18n:     error = _('Record %s cannot be modified!') % record
.. i18n: 
.. i18n:     # OK too: multi-line literal strings
.. i18n:     error = _("""This is a bad multiline example
.. i18n:                  about record %s!""") % record
.. i18n:     error = _('Record %s cannot be modified' \
.. i18n:               'after being validated!') % record
.. i18n: 
.. i18n:     # BAD: tries to translate after string formatting 
.. i18n:     #      (pay attention to brackets!)
.. i18n:     # This does NOT work and messes up the translations!
.. i18n:     error = _('Record %s cannot be modified!' % record)
.. i18n: 
.. i18n:     # BAD: dynamic string, string concatenation, etc are forbidden!
.. i18n:     # This does NOT work and messes up the translations!
.. i18n:     error = _("'" + que_rec['question'] + "' \n")
.. i18n: 
.. i18n:     # BAD: field values are automatically translated by the framework
.. i18n:     # This is useless and will not work the way you think:
.. i18n:     error = _("Product %s is out of stock!") % _(product.name)
.. i18n:     # and the following will of course not work as already explained:
.. i18n:     error = _("Product %s is out of stock!" % product.name)
.. i18n: 
.. i18n:     # BAD: field values are automatically translated by the framework
.. i18n:     # This is useless and will not work the way you think:
.. i18n:     error = _("Product %s is not available!") % _(product.name)
.. i18n:     # and the following will of course not work as already explained:
.. i18n:     error = _("Product %s is not available!" % product.name)
.. i18n: 
.. i18n:     # Instead you can do the following and everything will be translated,
.. i18n:     # including the product name if its field definition has the
.. i18n:     # translate flag properly set:
.. i18n:     error = _("Product %s is not available!") % product.name
..

The rule is very simple: calls to the underscore method should *always* be in the form ``_('literal string')``
and nothing else::

    # Good: plain strings
    error = _('This record is locked!')

    # Good: strings with formatting patterns included
    error = _('Record %s cannot be modified!') % record

    # OK too: multi-line literal strings
    error = _("""This is a bad multiline example
                 about record %s!""") % record
    error = _('Record %s cannot be modified' \
              'after being validated!') % record

    # BAD: tries to translate after string formatting 
    #      (pay attention to brackets!)
    # This does NOT work and messes up the translations!
    error = _('Record %s cannot be modified!' % record)

    # BAD: dynamic string, string concatenation, etc are forbidden!
    # This does NOT work and messes up the translations!
    error = _("'" + que_rec['question'] + "' \n")

    # BAD: field values are automatically translated by the framework
    # This is useless and will not work the way you think:
    error = _("Product %s is out of stock!") % _(product.name)
    # and the following will of course not work as already explained:
    error = _("Product %s is out of stock!" % product.name)

    # BAD: field values are automatically translated by the framework
    # This is useless and will not work the way you think:
    error = _("Product %s is not available!") % _(product.name)
    # and the following will of course not work as already explained:
    error = _("Product %s is not available!" % product.name)

    # Instead you can do the following and everything will be translated,
    # including the product name if its field definition has the
    # translate flag properly set:
    error = _("Product %s is not available!") % product.name

.. i18n: Also, keep in mind that translators will have to work with the literal values that are passed
.. i18n: to the underscore function, so please try to make them easy to understand and keep spurious
.. i18n: characters and formatting to a minimum. Translators must be aware that formatting patterns such
.. i18n: as ``%s`` or ``%d``, newlines, etc. need to be preserved, but it's important to use these
.. i18n: in a sensible and obvious manner::
.. i18n: 
.. i18n:     # Bad: makes the translations hard to work with
.. i18n:     error = "'" + question + _("' \nPlease enter an integer value ")
.. i18n: 
.. i18n:     # Better (pay attention to position of the brackets too!)
.. i18n:     error = _("Answer to question %s is not valid.\n" \
.. i18n:               "Please enter an integer value.") % question
..

Also, keep in mind that translators will have to work with the literal values that are passed
to the underscore function, so please try to make them easy to understand and keep spurious
characters and formatting to a minimum. Translators must be aware that formatting patterns such
as ``%s`` or ``%d``, newlines, etc. need to be preserved, but it's important to use these
in a sensible and obvious manner::

    # Bad: makes the translations hard to work with
    error = "'" + question + _("' \nPlease enter an integer value ")

    # Better (pay attention to position of the brackets too!)
    error = _("Answer to question %s is not valid.\n" \
              "Please enter an integer value.") % question

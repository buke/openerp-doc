
.. sectnum::
    :start: 2

OpenERP Specific Guidelines
+++++++++++++++++++++++++++

Bazaar is your historian
------------------------
Do not comment out code if you want to disable it. The code is versioned in
Bazaar, and regardless of your opinion about Bazaar, it does not lose
the file history.

Leaving comments just makes the code messier and harder to read. And don't
worry about making your changes obvious, that's the purpose of ``diff``::

    # no example for this one, code was really removed ;-)

Call your fish a fish
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

Do not bypass the ORM
---------------------
You should never use the database cursor directly when the ORM can do the
same thing! By doing so you are bypassing all the ORM features,
possibly the transactions, access rights and so on.

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



No SQL injections, please!
--------------------------
Care must be taken not to introduce SQL injections vulnerabilities when using
manual SQL queries.  The vulnerability is present when user input is either
incorrectly filtered or badly quoted, allowing an attacker to introduce
undesirable clauses to a SQL query (such as circumventing filters or executing
**UPDATE** or **DELETE** commands).

The best way to be safe is to never, NEVER use Python string concatenation (+)
or string parameters interpolation (%) to pass variables to a SQL query string.

The second reason, which is almost as important, is that it is the job of the
database abstraction layer (psycopg2) to decide how to format query parameters,
not your job!
For example psycopg2 knows that when you pass a list of values it needs to 
format them as a comma-separated list, enclosed in parentheses!

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

This is very important, so please be careful also when refactoring, and most
importantly do not copy these patterns!

Here is a `memorable example <http://www.bobby-tables.com>`_ to help
you remember what the issue is about (but do not copy the code there).

Before continuing, please be sure to read the online documentation of pyscopg2
to learn of to use it properly:

 * `The problem with query parameters <http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters>`_
 * `How to pass parameters with psycopg2 <http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries>`_
 * `Advanced parameter types <http://initd.org/psycopg/docs/usage.html#adaptation-of-python-values-to-sql-types>`_


Factor out the code
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

The infamous context
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

Also be careful with boolean tests on lists and maps, because an empty
dict, list or tuple will evaluate as ``False``::

    # bad, you shadow the original context if it's empty
    def spam(eggs, context=None):
       if not context:
          context = {}
       setting = context.get('foo')
       #...


And it's okay if you only need to forward it, you can pass ``None`` and
let the downstream code handle it::

    # fine
    def spam(eggs, context=None):
        setting = get_setting(True, context=context)

See also `launchpad bug 525808 <https://bugs.launchpad.net/openobject-server/+bug/525808>`_.


There is better than lambda, sometimes
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

See also http://docs.python.org/library/operator.html#operator.attrgetter

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

.. warning::

    Be careful with this, because non-callable defaults are only evaluated
    once! If you want to generate new default values for each
    record you really need to keep the ``lambda`` or make it a callable.

The most frequent error is with timestamps, as in the following example::

    # This will always give the server start time!
    _defaults = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
    }

    # You need to keep it callable, e.g:
    _defaults = {
        'timestamp': lambda *x: time.strftime('%Y-%m-%d %H:%M:%S'),
    }



Keep your methods short/simple when possible
--------------------------------------------
Functions and methods should not contain too much logic: having a lot of small and simple methods is more advisable than having few
large and complex methods. A good rule of thumb is to split a method as soon as:

    * it has more than one responsibility (see http://en.wikipedia.org/wiki/Single_responsibility_principle)
    * it is too big to fit on one screen.

Also, name your functions accordingly: small and properly named functions are the starting point of readable/maintainable code and tighter documentation.

This recommendation is also relevant for classes, files, modules and packages. (See also http://en.wikipedia.org/wiki/Cyclomatic_complexity )

Never commit the transaction
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

If any error occurs during the execution of the RPC call, the transaction is rolled back atomically,
preserving the state of the system.

Similarly, the system also provides a dedicated transaction during the execution of tests suites,
so it can be rolled back or not depending on the server startup options.

The consequence is that if you manually call ``cr.commit()`` anywhere there is a very high chance
that you **will** break the system in various ways, because you will cause partial commits, and thus
partial and unclean rollbacks, causing among others:

 - inconsistent business data, usually data loss ;
 - workflow desynchronization, documents stuck permanently ;
 - tests that can't be rolled back cleanly, and will start polluting the database,
   and triggering error (this is true even if no error occurs during the transaction) ;

Here is the very simple rule:

.. warning:: **You should NEVER call cr.commit() yourself, UNLESS you have created your own 
   database cursor explicitly! And the situations where you need to do that are exceptional!**

And by the way if you did create your own cursor, then you need to handle error cases and proper
rollback, as well as properly close the cursor when you're done with it.

And contrary to popular belief, you do *not* even need to call ``cr.commit()`` in the following
situations:

 - in the ``_auto_init()`` method of an ``osv.osv`` object: this is taken care of by the addons
   initialization method, or by the ORM transaction when creating custom models ;
 - in reports: the ``commit()`` is handled by the framework too, so you can update the database
   even from within a report ;
 - within ``osv.osv_memory`` methods: these methods are called exactly like regular ``osv.osv``
   ones, within a transaction and with the corresponding ``cr.commit()``/``rollback()`` at the end ;
 - etc. (see general rule above if you have in doubt!)

And another very simple rule:

.. warning:: **All cr.commit() calls outside of the server framework from now on must have an explicit
   comment explaining why they are absolutely necessary, why they are indeed correct, and why
   they do not break the transactions. Otherwise they can and will be removed!**

Use the gettext method correctly
--------------------------------

OpenERP uses a GetText-like method named "underscore" ``_( )`` to indicate that a static
string used in the code needs to be translated at runtime using the language of the context.
This pseudo-method is accessed within your code by importing as follows::

    from tools.translate import _

A few very important rules must be followed when using it, in order for it to work and to
avoid filling the translations with useless junk.

Basically, this method should only be used for static strings written manually in the code,
it will not work to translate field *values*, such as Product names, etc. This must be
done instead using the ``translate`` flag on the corresponding field.

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


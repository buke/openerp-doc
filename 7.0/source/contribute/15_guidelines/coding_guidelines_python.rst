
.. sectnum::
    :start: 1


Python style guide
++++++++++++++++++
In additions to these guidelines, you may also find the following link
interesting:

 * http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html (a little bit outdated, but quite relevant)


magic methods
-------------
magic methods (starting *and* ending with two underscores) should *not* have to be called directly unless you're overriding a method of the same name.

magic methods are used to implement specific protocols and are called for you, either due to operator access or due to some special operation using them:

.. code-block:: python

        # bad
        levels.__contains__(name)
        # good
        name in levels
        # very bad
        kw.__setitem__('nodes',nodes)
        # much better
        kw['nodes'] = nodes

.clone()
--------
rarely necessary (unless you really have no idea what the type of the variable you're trying to clone is), never necessary for built-in collections: just call the constructor with your existing collection:

.. code-block:: python

        # bad
        new_dict = my_dict.clone()
        # good
        new_dict = dict(my_dict)
        # bad
        new_list = old_list.clone()
        # good
        new_list = list(old_list)

And don't clone manually, please:

.. code-block:: python

        # surely you jest!
        values = []
        for val in view_items:
                values += [val]
        # sane
        values = list(view_items)

the "clone and update"
----------------------
the ``dict`` constructor takes both a single (optional) positional argument (either a dictionary-like object or an iterable of 2-tuples) and an unlimited number of keyword arguments. Thus, you can "merge" two different dictionaries into a third, new, dictionary:

.. code-block:: python

        # bad
        dictionary3 = dictionary1.clone()
        dictionary3.update(dictionary2)
        # worse
        dictionary3 = {}
        dictionary3.update(d1)
        dictionary3.update(d2)
        # good
        dictionary3 = dict(dictionary1, **dictionary2)

.. **

You can use those properties for simpler operations, such as cloning an existing dict and (re) setting a key:

.. code-block:: python

        # no
        context = kw.clone()
        context['foo'] = 'bar'
        # yes
        context = dict(kw, foo='bar')

"manual update"
---------------
the signature of dict.update is the same as ``dict()``: a single, optional, positional argument and an unlimited number of keyword arguments.

Thus the following are possible:

merging a dict from another one:

.. code-block:: python

        # bad
        for key, value in other_dict.iteritems():
                my_dict[key] = value
        # good
        my_dict.update(other_dict)

Setting a bunch of keys at the same time:

.. code-block:: python

        # bad
        my_dict['foo'] = 3
        my_dict['bar'] = 4
        my_dict['baz'] = 5
        # good
        my_dict.update(
                foo=3,
                bar=4,
                baz=5)

Java dictionary creation
------------------------
Python isn't java, it has literals:

.. code-block:: python

        # very very very bad
        my_dict = {}
        my_dict['foo'] = 3
        my_dict['bar'] = 4
        my_dict['baz'] = 5
        # good
        my_dict = {
                'foo': 3,
                'bar': 4,
                'baz': 5
        }

"temporary kwargs"
------------------
keyword arguments are a good way to get a bunch of unspecified supplementary arguments if e.g. you just want to forward them:

.. code-block:: python

        def foo(**kwargs):
                logging.debug('Calling foo with arguments %s', kwargs)
                return bar(**kwargs)

or if you retrieved a ready-made dict (from another function) and want to pass its content to another function or method:

.. code-block:: python

        sessions = some_function_returning_a_dict_of_sessions()
        some_other_function(**sessions)

but there is no point whatsoever in creating a dict for the sake of passing it as ``**kwargs``, just provide the damn keyword arguments:

.. ``

.. code-block:: python

        # waste of time and space
        my_dict = {
                'foo': 3,
                'bar': 4,
                'baz': 5
        }
        some_func(**my_dict)
        # good
        some_func(foo=3, bar=4, baz=5)

.. **

deprecated methods (formally or informally)
-------------------------------------------
``dict.has_key(key)`` is deprecated, please use the ``in`` operator:

.. code-block:: python

        # bad
        kw.has_key('cross_on_pages')
        # good
        'cross_on_pages' in kw

useless intermediate variables
------------------------------
Temporary variables can make the code clearer by giving names to objects, but that doesn't mean you should create temporary variables all the time:

.. code-block:: python

        # pointless
        schema = kw['schema']
        params = {'schema': schema}
        # simpler
        params = {'schema': kw['schema']}

3 strikes, and the code's out
-----------------------------
A bit of redundancy can be accepted: maybe you have to get the content of an axis:

.. code-block:: python

        col_axes = []
        if kw.has_key('col_axis'):
            col_axes = self.axes(kw['col_axis'])

and a second one:

.. code-block:: python

        col_axes = []
        if kw.has_key('col_axis'):
            col_axes = self.axes(kw['col_axis'])
        page_axes= []
        if kw.has_key('page_axis'):
            page_axes = self.axes(kw['page_axis'])

But at the third strike, chances are you're going to need the thing again and again. Time to refactor:

.. code-block:: python

        def get_axis(self, name, kw):
                if name not in kw:
                    return []
                return self.axes(kw[name])
        #[…]
        col_axes = self.get_axis('col_axis', kw)
        page_axes = self.get_axis('page_axis', kw)

The refactoring could also be an improvement of a method already called (be sure to check where the method is called in order not to break other pieces of code. Or write tests):

.. code-block:: python

        # from
        def axes(self, axis):
                axes = []
                if type(axis) == type([]):
                        axes.extend(axis)
                else:
                        axes.append(axis)
                return axes

        def output(self, **kw):
                col_axes = []
                if kw.has_key('col_axis'):
                        col_axes = self.axes(kw['col_axis'])
                page_axes = []
                if kw.has_key('page_axis'):
                        page_axes = self.axes(kw['page_axis'])
                cross_on_rows = []
                if kw.has_key('cross_on_rows'):
                         cross_on_rows = self.axes(kw['cross_on_rows'])

        # to:
        def axes(self, axis):
                if axis is None: return []
                axes = []
                if type(axis) == type([]):
                        axes.extend(axis)
                else:
                        axes.append(axis)
                return axes

        def output(self, **kw):
                col_axes = self.axes(kw.get('col_axis'))
                page_axes = self.axes(kw.get('page_axis'))
                cross_on_rows = self.axes(kw.get('cross_on_rows'))

.. **

Multiple return points are OK, when they're simpler
---------------------------------------------------

.. code-block:: python

        # a bit complex and with a redundant temp variable
        def axes(self, axis):
                axes = []
                if type(axis) == type([]):
                        axes.extend(axis)
                else:
                        axes.append(axis)
                return axes

         # clearer
        def axes(self, axis):
                if type(axis) == type([]):
                        return list(axis) # clone the axis
                else:
                        return [axis] # single-element list

Try to avoid type-testing
-------------------------

Python is a dynamically typed languages, if you don't absolutely need to
receive a list, then don't test for a list, just do your stuff (e.g. iterating
on it, then caller can provide any kind of iterator or container)

Don't use ``type`` if you already know what the type you want is
----------------------------------------------------------------

The type of a list is ``list``, the type of a dict is ``dict``:

.. code-block:: python

        # bad
        def axes(self, axis):
                if type(axis) == type([]): # we already know what the type of [] is
                        return list(axis)
                else:
                        return [axis]
        # good
        def axes(self, axis):
                if type(axis) == list:
                        return list(axis)
                else:
                        return [axis]

plus Python types are singletons, so you can just test for identity, it reads better:

.. code-block:: python

        # better
        def axes(self, axis):
                if type(axis) is list:
                        return list(axis)
                else:
                        return [axis]

But really, if you need type testing just use the tools python provides
-----------------------------------------------------------------------

The previous piece of code will fail if the caller provided a *subclass* of ``list`` (which is possible and allowed), because ``==`` and ``is`` don't check for subtypes. ``isinstance`` does:

.. code-block:: python

        # shiny
        def axes(self, axis):
                if isinstance(axis, list):
                        return list(axis) # clone the axis
                else:
                        return [axis] # single-element list

Don't create functions just to call callables
---------------------------------------------

.. code-block:: python

        # dumb, ``str`` is already callable
        parent_id = map(lambda x: str(x), parent_id.split(','))
        # better
        parent_id = map(str, parent_id.split(','))

Know your builtins
------------------

You should at least have a basic understanding of all the Python builtins (http://docs.python.org/library/functions.html)

For example, ``isinstance`` can take more than one type as its second argument, so you could write:

.. code-block:: python

        def axes(self, axis):
                if isinstance(axis, (list, set, dict)):
                        return list(axis)
                else:
                        return [axis]

Another one is ``dict.get``, whose second argument defaults to ``None``:

.. code-block:: python

        # very very redundant
        value = my_dict.get('key', None)
        # good
        value= my_dict.get('key')

Also, ``if 'key' in my_dict`` and ``if my_dict.get('key')`` have very different meaning, be sure that you're using the right one.

Learn list comprehensions
-------------------------

When used correctly, list comprehensions can greatly enhance the quality of a piece of code when mapping and/or filtering collections:

.. code-block:: python

        # not very good
        cube = []
        for i in res:
                cube.append((i['id'],i['name']))
        # better
        cube = [(i['id'], i['name']) for i in res]

But beware: with great power comes great responsibility, and list comprehensions can become overly complex. In that case, either revert back to "normal" ``for`` loops, extract functions or do your transformation in multiple steps

Learn your standard library
---------------------------

Python is provided "with batteries included", but these batteries are often
criminally underused. Some standard modules to know are ``itertools``,
``operator`` and ``collections``, among others (though be careful to note the
python version at which functions and objects were introduced, don't break
compatibility with the officially supported versions for your tool):

.. code-block:: python

        # no
        cube = map(lambda i: (i['id'], i['name']), res)
        # still no
        cube = [(i['id'], i['name']) for i in res]
        # yes, with operator.itemgetter
        cube = map(itemgetter('id', 'name'), res)

Excellent resources for this are the official stdlib documentation (http://docs.python.org/library/index.html ) and Python Module of the Week (http://www.doughellmann.com/projects/PyMOTW/, do subscribe to its RSS feed)

Collections are booleans too
----------------------------

In python, many objects have "boolean-ish" value when evaluated in a boolean context (such as an ``if``). Among these are collections (lists, dicts, sets, …) which are "falsy" when empty and "truthy" when containing items:

.. code-block:: python

        bool([]) is False
        bool([1]) is True
        bool([False]) is True

therefore, no need to call ``len``:

.. code-block:: python

        # redundant
        if len(some_collection):
                "do something..."
        # simpler
        if some_collection:
                "do something..."

You can append a single object to a list, it's ok
-------------------------------------------------

.. code-block:: python

        # no
        some_list += [some_item]
        # yes
        some_list.append(some_item)
        # very no
        view += [(code, values)]
        # yes
        view.append((code, values))

Add lists into bigger lists
---------------------------

.. code-block:: python

        # obscure
        my_list = []
        my_list += list1
        my_list += list2
        # simpler
        my_list = list1 + list2

Learn your standard library (2)
-------------------------------

Itertools is your friend for all things iterable:

.. code-block:: python

        # ugly
        my_list = []
        my_list += list1
        my_list += list2
        for element in my_list:
                "do something..."
        # unclear, creates a pointless temporary list
        for element in list1 + list2:
                "do something..."
        # says what I mean
        for element in itertools.chain(list1, list2):
                "do something..."

Iterate on iterables
--------------------

.. code-block:: python

        # creates a temporary list and looks bar
        for key in my_dict.keys():
                "do something..."
        # better
        for key in my_dict:
                "do something..."
        # creates a temporary list
        for key, value in my_dict.items():
                "do something..."
        # only iterates
        for key, value in my_dict.iteritems():
                "do something..."

Chaining calls is ok, as long as you don't abuse it (too much)
--------------------------------------------------------------

.. code-block:: python

        # what's the point of the ``graph`` temporary variable?
        # plus it shadows the ``graph`` module, bad move
        graph = graph.Graph(kw)
        mdx = ustr(graph.display())
        # just as readable
        mdx = ustr(grah.Graph(kw).display())


NOTE:

yes, here the temporary variable `graph` is redundant but sometimes using such
temporary variables simplify code debugging when you want to inspect the
variable and you put breakpoint on the single line expression it's difficult to
know when to do step-in and step-out.


Use dict.setdefault
-------------------

If you need to modify a nested container for example:

.. code-block:: python

        # longer.. harder to read
        values = {}
        for element in iterable:
            if element not in values:
                values[element] = []
            values[element].append(other_value)

        # better.. use dict.setdefault method
        values = {}
        for element in iterable:
            values.setdefault(element, []).append(other_value)


* `Documentation for dict.setdefault <http://docs.python.org/library/stdtypes.html?highlight=setdefault#dict.setdefault>`_

Use constants and avoid magic numbers
-------------------------------------

.. code-block:: python

        # bad
        limit = 20

        # bad
        search(cr, uid, ids, domain, limit=20, context=context)

You should use a constant, name it correctly, and perhaps add a comment on it
explaining where the value comes from. And of course it's cleaner, easier
to read and there's only one place to modify.
Oh and that is true not just for numbers, but for any literal value that is
semantically a constant!

.. code-block:: python

        # better
        DEFAULT_SEARCH_LIMIT = 20  # limit to 20 results due to screen size

        search(cr, uid, ids, domain, limit=DEFAULT_LIMIT, context=context)

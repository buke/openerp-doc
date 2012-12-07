.. i18n: .. sectnum::
.. i18n:     :start: 1
..

.. sectnum::
    :start: 1

.. i18n: Python style guide
.. i18n: ++++++++++++++++++
.. i18n: In additions to these guidelines, you may also find the following link
.. i18n: interesting:
..

Python代码风格指南
++++++++++++++++++
In additions to these guidelines, you may also find the following link
interesting:

.. i18n:  * http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html (a little bit outdated, but quite relevant)
..

 * http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html (a little bit outdated, but quite relevant)

.. i18n: magic methods
.. i18n: -------------
.. i18n: magic methods (starting *and* ending with two underscores) should *not* have to be called directly unless you're overriding a method of the same name.
..

魔术方法
-------------
magic methods (starting *and* ending with two underscores) should *not* have to be called directly unless you're overriding a method of the same name.

.. i18n: magic methods are used to implement specific protocols and are called for you, either due to operator access or due to some special operation using them:
..

magic methods are used to implement specific protocols and are called for you, either due to operator access or due to some special operation using them:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         levels.__contains__(name)
.. i18n:         # good
.. i18n:         name in levels
.. i18n:         # very bad
.. i18n:         kw.__setitem__('nodes',nodes)
.. i18n:         # much better
.. i18n:         kw['nodes'] = nodes
..

.. code-block:: python

        # bad
        levels.__contains__(name)
        # good
        name in levels
        # very bad
        kw.__setitem__('nodes',nodes)
        # much better
        kw['nodes'] = nodes

.. i18n: .clone()
.. i18n: --------
.. i18n: rarely necessary (unless you really have no idea what the type of the variable you're trying to clone is), never necessary for built-in collections: just call the constructor with your existing collection:
..

.clone()
--------
rarely necessary (unless you really have no idea what the type of the variable you're trying to clone is), never necessary for built-in collections: just call the constructor with your existing collection:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         new_dict = my_dict.clone()
.. i18n:         # good
.. i18n:         new_dict = dict(my_dict)
.. i18n:         # bad
.. i18n:         new_list = old_list.clone()
.. i18n:         # good
.. i18n:         new_list = list(old_list)
..

.. code-block:: python

        # bad
        new_dict = my_dict.clone()
        # good
        new_dict = dict(my_dict)
        # bad
        new_list = old_list.clone()
        # good
        new_list = list(old_list)

.. i18n: And don't clone manually, please:
..

And don't clone manually, please:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # surely you jest!
.. i18n:         values = []
.. i18n:         for val in view_items:
.. i18n:                 values += [val]
.. i18n:         # sane
.. i18n:         values = list(view_items)
..

.. code-block:: python

        # surely you jest!
        values = []
        for val in view_items:
                values += [val]
        # sane
        values = list(view_items)

.. i18n: the "clone and update"
.. i18n: ----------------------
.. i18n: the ``dict`` constructor takes both a single (optional) positional argument (either a dictionary-like object or an iterable of 2-tuples) and an unlimited number of keyword arguments. Thus, you can "merge" two different dictionaries into a third, new, dictionary:
..

"clone 和 update"
----------------------
the ``dict`` constructor takes both a single (optional) positional argument (either a dictionary-like object or an iterable of 2-tuples) and an unlimited number of keyword arguments. Thus, you can "merge" two different dictionaries into a third, new, dictionary:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         dictionary3 = dictionary1.clone()
.. i18n:         dictionary3.update(dictionary2)
.. i18n:         # worse
.. i18n:         dictionary3 = {}
.. i18n:         dictionary3.update(d1)
.. i18n:         dictionary3.update(d2)
.. i18n:         # good
.. i18n:         dictionary3 = dict(dictionary1, **dictionary2)
..

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

.. i18n: .. **
..

.. **

.. i18n: You can use those properties for simpler operations, such as cloning an existing dict and (re) setting a key:
..

You can use those properties for simpler operations, such as cloning an existing dict and (re) setting a key:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # no
.. i18n:         context = kw.clone()
.. i18n:         context['foo'] = 'bar'
.. i18n:         # yes
.. i18n:         context = dict(kw, foo='bar')
..

.. code-block:: python

        # no
        context = kw.clone()
        context['foo'] = 'bar'
        # yes
        context = dict(kw, foo='bar')

.. i18n: "manual update"
.. i18n: ---------------
.. i18n: the signature of dict.update is the same as ``dict()``: a single, optional, positional argument and an unlimited number of keyword arguments.
..

"手动 update"
---------------
the signature of dict.update is the same as ``dict()``: a single, optional, positional argument and an unlimited number of keyword arguments.

.. i18n: Thus the following are possible:
..

Thus the following are possible:

.. i18n: merging a dict from another one:
..

merging a dict from another one:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         for key, value in other_dict.iteritems():
.. i18n:                 my_dict[key] = value
.. i18n:         # good
.. i18n:         my_dict.update(other_dict)
..

.. code-block:: python

        # bad
        for key, value in other_dict.iteritems():
                my_dict[key] = value
        # good
        my_dict.update(other_dict)

.. i18n: Setting a bunch of keys at the same time:
..

Setting a bunch of keys at the same time:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         my_dict['foo'] = 3
.. i18n:         my_dict['bar'] = 4
.. i18n:         my_dict['baz'] = 5
.. i18n:         # good
.. i18n:         my_dict.update(
.. i18n:                 foo=3,
.. i18n:                 bar=4,
.. i18n:                 baz=5)
..

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

.. i18n: Java dictionary creation
.. i18n: ------------------------
.. i18n: Python isn't java, it has literals:
..

Java 的字典创建方式
------------------------
Python isn't java, it has literals:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # very very very bad
.. i18n:         my_dict = {}
.. i18n:         my_dict['foo'] = 3
.. i18n:         my_dict['bar'] = 4
.. i18n:         my_dict['baz'] = 5
.. i18n:         # good
.. i18n:         my_dict = {
.. i18n:                 'foo': 3,
.. i18n:                 'bar': 4,
.. i18n:                 'baz': 5
.. i18n:         }
..

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

.. i18n: "temporary kwargs"
.. i18n: ------------------
.. i18n: keyword arguments are a good way to get a bunch of unspecified supplementary arguments if e.g. you just want to forward them:
..

"临时的 kwargs"
------------------
keyword arguments are a good way to get a bunch of unspecified supplementary arguments if e.g. you just want to forward them:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         def foo(**kwargs):
.. i18n:                 logging.debug('Calling foo with arguments %s', kwargs)
.. i18n:                 return bar(**kwargs)
..

.. code-block:: python

        def foo(**kwargs):
                logging.debug('Calling foo with arguments %s', kwargs)
                return bar(**kwargs)

.. i18n: or if you retrieved a ready-made dict (from another function) and want to pass its content to another function or method:
..

or if you retrieved a ready-made dict (from another function) and want to pass its content to another function or method:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         sessions = some_function_returning_a_dict_of_sessions()
.. i18n:         some_other_function(**sessions)
..

.. code-block:: python

        sessions = some_function_returning_a_dict_of_sessions()
        some_other_function(**sessions)

.. i18n: but there is no point whatsoever in creating a dict for the sake of passing it as ``**kwargs``, just provide the damn keyword arguments:
..

but there is no point whatsoever in creating a dict for the sake of passing it as ``**kwargs``, just provide the damn keyword arguments:

.. i18n: .. ``
..

.. ``

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # waste of time and space
.. i18n:         my_dict = {
.. i18n:                 'foo': 3,
.. i18n:                 'bar': 4,
.. i18n:                 'baz': 5
.. i18n:         }
.. i18n:         some_func(**my_dict)
.. i18n:         # good
.. i18n:         some_func(foo=3, bar=4, baz=5)
..

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

.. i18n: .. **
..

.. **

.. i18n: deprecated methods (formally or informally)
.. i18n: -------------------------------------------
.. i18n: ``dict.has_key(key)`` is deprecated, please use the ``in`` operator:
..

deprecated methods (formally or informally)
-------------------------------------------
``dict.has_key(key)`` is deprecated, please use the ``in`` operator:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         kw.has_key('cross_on_pages')
.. i18n:         # good
.. i18n:         'cross_on_pages' in kw
..

.. code-block:: python

        # bad
        kw.has_key('cross_on_pages')
        # good
        'cross_on_pages' in kw

.. i18n: useless intermediate variables
.. i18n: ------------------------------
.. i18n: Temporary variables can make the code clearer by giving names to objects, but that doesn't mean you should create temporary variables all the time:
..

useless intermediate variables
------------------------------
Temporary variables can make the code clearer by giving names to objects, but that doesn't mean you should create temporary variables all the time:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # pointless
.. i18n:         schema = kw['schema']
.. i18n:         params = {'schema': schema}
.. i18n:         # simpler
.. i18n:         params = {'schema': kw['schema']}
..

.. code-block:: python

        # pointless
        schema = kw['schema']
        params = {'schema': schema}
        # simpler
        params = {'schema': kw['schema']}

.. i18n: 3 strikes, and the code's out
.. i18n: -----------------------------
.. i18n: A bit of redundancy can be accepted: maybe you have to get the content of an axis:
..

3 strikes, and the code's out
-----------------------------
A bit of redundancy can be accepted: maybe you have to get the content of an axis:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         col_axes = []
.. i18n:         if kw.has_key('col_axis'):
.. i18n:             col_axes = self.axes(kw['col_axis'])
..

.. code-block:: python

        col_axes = []
        if kw.has_key('col_axis'):
            col_axes = self.axes(kw['col_axis'])

.. i18n: and a second one:
..

and a second one:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         col_axes = []
.. i18n:         if kw.has_key('col_axis'):
.. i18n:             col_axes = self.axes(kw['col_axis'])
.. i18n:         page_axes= []
.. i18n:         if kw.has_key('page_axis'):
.. i18n:             page_axes = self.axes(kw['page_axis'])
..

.. code-block:: python

        col_axes = []
        if kw.has_key('col_axis'):
            col_axes = self.axes(kw['col_axis'])
        page_axes= []
        if kw.has_key('page_axis'):
            page_axes = self.axes(kw['page_axis'])

.. i18n: But at the third strike, chances are you're going to need the thing again and again. Time to refactor:
..

But at the third strike, chances are you're going to need the thing again and again. Time to refactor:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         def get_axis(self, name, kw):
.. i18n:                 if name not in kw:
.. i18n:                     return []
.. i18n:                 return self.axes(kw[name])
.. i18n:         #[…]
.. i18n:         col_axes = self.get_axis('col_axis', kw)
.. i18n:         page_axes = self.get_axis('page_axis', kw)
..

.. code-block:: python

        def get_axis(self, name, kw):
                if name not in kw:
                    return []
                return self.axes(kw[name])
        #[…]
        col_axes = self.get_axis('col_axis', kw)
        page_axes = self.get_axis('page_axis', kw)

.. i18n: The refactoring could also be an improvement of a method already called (be sure to check where the method is called in order not to break other pieces of code. Or write tests):
..

The refactoring could also be an improvement of a method already called (be sure to check where the method is called in order not to break other pieces of code. Or write tests):

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # from
.. i18n:         def axes(self, axis):
.. i18n:                 axes = []
.. i18n:                 if type(axis) == type([]):
.. i18n:                         axes.extend(axis)
.. i18n:                 else:
.. i18n:                         axes.append(axis)
.. i18n:                 return axes
.. i18n: 
.. i18n:         def output(self, **kw):
.. i18n:                 col_axes = []
.. i18n:                 if kw.has_key('col_axis'):
.. i18n:                         col_axes = self.axes(kw['col_axis'])
.. i18n:                 page_axes = []
.. i18n:                 if kw.has_key('page_axis'):
.. i18n:                         page_axes = self.axes(kw['page_axis'])
.. i18n:                 cross_on_rows = []
.. i18n:                 if kw.has_key('cross_on_rows'):
.. i18n:                          cross_on_rows = self.axes(kw['cross_on_rows'])
.. i18n: 
.. i18n:         # to:
.. i18n:         def axes(self, axis):
.. i18n:                 if axis is None: return []
.. i18n:                 axes = []
.. i18n:                 if type(axis) == type([]):
.. i18n:                         axes.extend(axis)
.. i18n:                 else:
.. i18n:                         axes.append(axis)
.. i18n:                 return axes
.. i18n: 
.. i18n:         def output(self, **kw):
.. i18n:                 col_axes = self.axes(kw.get('col_axis'))
.. i18n:                 page_axes = self.axes(kw.get('page_axis'))
.. i18n:                 cross_on_rows = self.axes(kw.get('cross_on_rows'))
..

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

.. i18n: .. **
..

.. **

.. i18n: Multiple return points are OK, when they're simpler
.. i18n: ---------------------------------------------------
..

Multiple return points are OK, when they're simpler
---------------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # a bit complex and with a redundant temp variable
.. i18n:         def axes(self, axis):
.. i18n:                 axes = []
.. i18n:                 if type(axis) == type([]):
.. i18n:                         axes.extend(axis)
.. i18n:                 else:
.. i18n:                         axes.append(axis)
.. i18n:                 return axes
.. i18n: 
.. i18n:          # clearer
.. i18n:         def axes(self, axis):
.. i18n:                 if type(axis) == type([]):
.. i18n:                         return list(axis) # clone the axis
.. i18n:                 else:
.. i18n:                         return [axis] # single-element list
..

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

.. i18n: Try to avoid type-testing
.. i18n: -------------------------
..

Try to avoid type-testing
-------------------------

.. i18n: Python is a dynamically typed languages, if you don't absolutely need to
.. i18n: receive a list, then don't test for a list, just do your stuff (e.g. iterating
.. i18n: on it, then caller can provide any kind of iterator or container)
..

Python is a dynamically typed languages, if you don't absolutely need to
receive a list, then don't test for a list, just do your stuff (e.g. iterating
on it, then caller can provide any kind of iterator or container)

.. i18n: Don't use ``type`` if you already know what the type you want is
.. i18n: ----------------------------------------------------------------
..

Don't use ``type`` if you already know what the type you want is
----------------------------------------------------------------

.. i18n: The type of a list is ``list``, the type of a dict is ``dict``:
..

The type of a list is ``list``, the type of a dict is ``dict``:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         def axes(self, axis):
.. i18n:                 if type(axis) == type([]): # we already know what the type of [] is
.. i18n:                         return list(axis)
.. i18n:                 else:
.. i18n:                         return [axis]
.. i18n:         # good
.. i18n:         def axes(self, axis):
.. i18n:                 if type(axis) == list:
.. i18n:                         return list(axis)
.. i18n:                 else:
.. i18n:                         return [axis]
..

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

.. i18n: plus Python types are singletons, so you can just test for identity, it reads better:
..

plus Python types are singletons, so you can just test for identity, it reads better:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # better
.. i18n:         def axes(self, axis):
.. i18n:                 if type(axis) is list:
.. i18n:                         return list(axis)
.. i18n:                 else:
.. i18n:                         return [axis]
..

.. code-block:: python

        # better
        def axes(self, axis):
                if type(axis) is list:
                        return list(axis)
                else:
                        return [axis]

.. i18n: But really, if you need type testing just use the tools python provides
.. i18n: -----------------------------------------------------------------------
..

But really, if you need type testing just use the tools python provides
-----------------------------------------------------------------------

.. i18n: The previous piece of code will fail if the caller provided a *subclass* of ``list`` (which is possible and allowed), because ``==`` and ``is`` don't check for subtypes. ``isinstance`` does:
..

The previous piece of code will fail if the caller provided a *subclass* of ``list`` (which is possible and allowed), because ``==`` and ``is`` don't check for subtypes. ``isinstance`` does:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # shiny
.. i18n:         def axes(self, axis):
.. i18n:                 if isinstance(axis, list):
.. i18n:                         return list(axis) # clone the axis
.. i18n:                 else:
.. i18n:                         return [axis] # single-element list
..

.. code-block:: python

        # shiny
        def axes(self, axis):
                if isinstance(axis, list):
                        return list(axis) # clone the axis
                else:
                        return [axis] # single-element list

.. i18n: Don't create functions just to call callables
.. i18n: ---------------------------------------------
..

Don't create functions just to call callables
---------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # dumb, ``str`` is already callable
.. i18n:         parent_id = map(lambda x: str(x), parent_id.split(','))
.. i18n:         # better
.. i18n:         parent_id = map(str, parent_id.split(','))
..

.. code-block:: python

        # dumb, ``str`` is already callable
        parent_id = map(lambda x: str(x), parent_id.split(','))
        # better
        parent_id = map(str, parent_id.split(','))

.. i18n: Know your builtins
.. i18n: ------------------
..

Know your builtins
------------------

.. i18n: You should at least have a basic understanding of all the Python builtins (http://docs.python.org/library/functions.html)
..

You should at least have a basic understanding of all the Python builtins (http://docs.python.org/library/functions.html)

.. i18n: For example, ``isinstance`` can take more than one type as its second argument, so you could write:
..

For example, ``isinstance`` can take more than one type as its second argument, so you could write:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         def axes(self, axis):
.. i18n:                 if isinstance(axis, (list, set, dict)):
.. i18n:                         return list(axis)
.. i18n:                 else:
.. i18n:                         return [axis]
..

.. code-block:: python

        def axes(self, axis):
                if isinstance(axis, (list, set, dict)):
                        return list(axis)
                else:
                        return [axis]

.. i18n: Another one is ``dict.get``, whose second argument defaults to ``None``:
..

Another one is ``dict.get``, whose second argument defaults to ``None``:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # very very redundant
.. i18n:         value = my_dict.get('key', None)
.. i18n:         # good
.. i18n:         value= my_dict.get('key')
..

.. code-block:: python

        # very very redundant
        value = my_dict.get('key', None)
        # good
        value= my_dict.get('key')

.. i18n: Also, ``if 'key' in my_dict`` and ``if my_dict.get('key')`` have very different meaning, be sure that you're using the right one.
..

Also, ``if 'key' in my_dict`` and ``if my_dict.get('key')`` have very different meaning, be sure that you're using the right one.

.. i18n: Learn list comprehensions
.. i18n: -------------------------
..

Learn list comprehensions
-------------------------

.. i18n: When used correctly, list comprehensions can greatly enhance the quality of a piece of code when mapping and/or filtering collections:
..

When used correctly, list comprehensions can greatly enhance the quality of a piece of code when mapping and/or filtering collections:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # not very good
.. i18n:         cube = []
.. i18n:         for i in res:
.. i18n:                 cube.append((i['id'],i['name']))
.. i18n:         # better
.. i18n:         cube = [(i['id'], i['name']) for i in res]
..

.. code-block:: python

        # not very good
        cube = []
        for i in res:
                cube.append((i['id'],i['name']))
        # better
        cube = [(i['id'], i['name']) for i in res]

.. i18n: But beware: with great power comes great responsibility, and list comprehensions can become overly complex. In that case, either revert back to "normal" ``for`` loops, extract functions or do your transformation in multiple steps
..

But beware: with great power comes great responsibility, and list comprehensions can become overly complex. In that case, either revert back to "normal" ``for`` loops, extract functions or do your transformation in multiple steps

.. i18n: Learn your standard library
.. i18n: ---------------------------
..

Learn your standard library
---------------------------

.. i18n: Python is provided "with batteries included", but these batteries are often
.. i18n: criminally underused. Some standard modules to know are ``itertools``,
.. i18n: ``operator`` and ``collections``, among others (though be careful to note the
.. i18n: python version at which functions and objects were introduced, don't break
.. i18n: compatibility with the officially supported versions for your tool):
..

Python is provided "with batteries included", but these batteries are often
criminally underused. Some standard modules to know are ``itertools``,
``operator`` and ``collections``, among others (though be careful to note the
python version at which functions and objects were introduced, don't break
compatibility with the officially supported versions for your tool):

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # no
.. i18n:         cube = map(lambda i: (i['id'], i['name']), res)
.. i18n:         # still no
.. i18n:         cube = [(i['id'], i['name']) for i in res]
.. i18n:         # yes, with operator.itemgetter
.. i18n:         cube = map(itemgetter('id', 'name'), res)
..

.. code-block:: python

        # no
        cube = map(lambda i: (i['id'], i['name']), res)
        # still no
        cube = [(i['id'], i['name']) for i in res]
        # yes, with operator.itemgetter
        cube = map(itemgetter('id', 'name'), res)

.. i18n: Excellent resources for this are the official stdlib documentation (http://docs.python.org/library/index.html ) and Python Module of the Week (http://www.doughellmann.com/projects/PyMOTW/, do subscribe to its RSS feed)
..

Excellent resources for this are the official stdlib documentation (http://docs.python.org/library/index.html ) and Python Module of the Week (http://www.doughellmann.com/projects/PyMOTW/, do subscribe to its RSS feed)

.. i18n: Collections are booleans too
.. i18n: ----------------------------
..

Collections are booleans too
----------------------------

.. i18n: In python, many objects have "boolean-ish" value when evaluated in a boolean context (such as an ``if``). Among these are collections (lists, dicts, sets, …) which are "falsy" when empty and "truthy" when containing items:
..

In python, many objects have "boolean-ish" value when evaluated in a boolean context (such as an ``if``). Among these are collections (lists, dicts, sets, …) which are "falsy" when empty and "truthy" when containing items:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         bool([]) is False
.. i18n:         bool([1]) is True
.. i18n:         bool([False]) is True
..

.. code-block:: python

        bool([]) is False
        bool([1]) is True
        bool([False]) is True

.. i18n: therefore, no need to call ``len``:
..

therefore, no need to call ``len``:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # redundant
.. i18n:         if len(some_collection):
.. i18n:                 "do something..."
.. i18n:         # simpler
.. i18n:         if some_collection:
.. i18n:                 "do something..."
..

.. code-block:: python

        # redundant
        if len(some_collection):
                "do something..."
        # simpler
        if some_collection:
                "do something..."

.. i18n: You can append a single object to a list, it's ok
.. i18n: -------------------------------------------------
..

You can append a single object to a list, it's ok
-------------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # no
.. i18n:         some_list += [some_item]
.. i18n:         # yes
.. i18n:         some_list.append(some_item)
.. i18n:         # very no
.. i18n:         view += [(code, values)]
.. i18n:         # yes
.. i18n:         view.append((code, values))
..

.. code-block:: python

        # no
        some_list += [some_item]
        # yes
        some_list.append(some_item)
        # very no
        view += [(code, values)]
        # yes
        view.append((code, values))

.. i18n: Add lists into bigger lists
.. i18n: ---------------------------
..

Add lists into bigger lists
---------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # obscure
.. i18n:         my_list = []
.. i18n:         my_list += list1
.. i18n:         my_list += list2
.. i18n:         # simpler
.. i18n:         my_list = list1 + list2
..

.. code-block:: python

        # obscure
        my_list = []
        my_list += list1
        my_list += list2
        # simpler
        my_list = list1 + list2

.. i18n: Learn your standard library (2)
.. i18n: -------------------------------
..

Learn your standard library (2)
-------------------------------

.. i18n: Itertools is your friend for all things iterable:
..

Itertools is your friend for all things iterable:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # ugly
.. i18n:         my_list = []
.. i18n:         my_list += list1
.. i18n:         my_list += list2
.. i18n:         for element in my_list:
.. i18n:                 "do something..."
.. i18n:         # unclear, creates a pointless temporary list
.. i18n:         for element in list1 + list2:
.. i18n:                 "do something..."
.. i18n:         # says what I mean
.. i18n:         for element in itertools.chain(list1, list2):
.. i18n:                 "do something..."
..

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

.. i18n: Iterate on iterables
.. i18n: --------------------
..

Iterate on iterables
--------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # creates a temporary list and looks bar
.. i18n:         for key in my_dict.keys():
.. i18n:                 "do something..."
.. i18n:         # better
.. i18n:         for key in my_dict:
.. i18n:                 "do something..."
.. i18n:         # creates a temporary list
.. i18n:         for key, value in my_dict.items():
.. i18n:                 "do something..."
.. i18n:         # only iterates
.. i18n:         for key, value in my_dict.iteritems():
.. i18n:                 "do something..."
..

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

.. i18n: Chaining calls is ok, as long as you don't abuse it (too much)
.. i18n: --------------------------------------------------------------
..

Chaining calls is ok, as long as you don't abuse it (too much)
--------------------------------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # what's the point of the ``graph`` temporary variable?
.. i18n:         # plus it shadows the ``graph`` module, bad move
.. i18n:         graph = graph.Graph(kw)
.. i18n:         mdx = ustr(graph.display())
.. i18n:         # just as readable
.. i18n:         mdx = ustr(grah.Graph(kw).display())
..

.. code-block:: python

        # what's the point of the ``graph`` temporary variable?
        # plus it shadows the ``graph`` module, bad move
        graph = graph.Graph(kw)
        mdx = ustr(graph.display())
        # just as readable
        mdx = ustr(grah.Graph(kw).display())

.. i18n: NOTE:
..

NOTE:

.. i18n: yes, here the temporary variable `graph` is redundant but sometimes using such
.. i18n: temporary variables simplify code debugging when you want to inspect the
.. i18n: variable and you put breakpoint on the single line expression it's difficult to
.. i18n: know when to do step-in and step-out.
..

yes, here the temporary variable `graph` is redundant but sometimes using such
temporary variables simplify code debugging when you want to inspect the
variable and you put breakpoint on the single line expression it's difficult to
know when to do step-in and step-out.

.. i18n: Use dict.setdefault
.. i18n: -------------------
..

Use dict.setdefault
-------------------

.. i18n: If you need to modify a nested container for example:
..

If you need to modify a nested container for example:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # longer.. harder to read
.. i18n:         values = {}
.. i18n:         for element in iterable:
.. i18n:             if element not in values:
.. i18n:                 values[element] = []
.. i18n:             values[element].append(other_value)
.. i18n: 
.. i18n:         # better.. use dict.setdefault method
.. i18n:         values = {}
.. i18n:         for element in iterable:
.. i18n:             values.setdefault(element, []).append(other_value)
..

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

.. i18n: * `Documentation for dict.setdefault <http://docs.python.org/library/stdtypes.html?highlight=setdefault#dict.setdefault>`_
..

* `Documentation for dict.setdefault <http://docs.python.org/library/stdtypes.html?highlight=setdefault#dict.setdefault>`_

.. i18n: Use constants and avoid magic numbers
.. i18n: -------------------------------------
..

Use constants and avoid magic numbers
-------------------------------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # bad
.. i18n:         limit = 20
.. i18n: 
.. i18n:         # bad
.. i18n:         search(cr, uid, ids, domain, limit=20, context=context)
..

.. code-block:: python

        # bad
        limit = 20

        # bad
        search(cr, uid, ids, domain, limit=20, context=context)

.. i18n: You should use a constant, name it correctly, and perhaps add a comment on it
.. i18n: explaining where the value comes from. And of course it's cleaner, easier
.. i18n: to read and there's only one place to modify.
.. i18n: Oh and that is true not just for numbers, but for any literal value that is
.. i18n: semantically a constant!
..

You should use a constant, name it correctly, and perhaps add a comment on it
explaining where the value comes from. And of course it's cleaner, easier
to read and there's only one place to modify.
Oh and that is true not just for numbers, but for any literal value that is
semantically a constant!

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         # better
.. i18n:         DEFAULT_SEARCH_LIMIT = 20  # limit to 20 results due to screen size
.. i18n: 
.. i18n:         search(cr, uid, ids, domain, limit=DEFAULT_LIMIT, context=context)
..

.. code-block:: python

        # better
        DEFAULT_SEARCH_LIMIT = 20  # limit to 20 results due to screen size

        search(cr, uid, ids, domain, limit=DEFAULT_LIMIT, context=context)

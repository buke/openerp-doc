.. i18n: .. _coding-guidelines-link:
.. i18n: 
.. i18n: =================
.. i18n: Coding Guidelines
.. i18n: =================
.. i18n: This list is populated incrementally by the OpenERP Quality Team as part of the code review process.
.. i18n: It contains a set of OpenERP specific
.. i18n: good/bad practices, as well as a selection of more generic Python coding
.. i18n: recommendations.
..

.. _coding-guidelines-link:

=================
编程指引
=================
以下条目由OpenERP质量团队维护并且作为质量审查的一部分。
包含了OpenERP的推荐的/不推荐的实现方式，以及通用的Python编程建议。


.. i18n: Both sections are a MUST READ for every OpenERP developer and contributor.
..

这两部分是每一个OpenERP的开发、贡献者都必须阅读的。

.. i18n: As an introductory rule, you should always keep in mind the following:
..

请谨记以下几点普遍的规则：

.. i18n:   **Every line you write will be written only once, but read many times
.. i18n:   by others (including yourself)**
..

  **Every line you write will be written only once, but read many times
  by others (including yourself)**

.. i18n: At the risk of stating the obvious, this means that while following the
.. i18n: other guidelines, you should always use your best judgement in order to
.. i18n: achieve the best readability. And if writing readable code requires an
.. i18n: additional effort, it's worth it a thousand times.
..

At the risk of stating the obvious, this means that while following the
other guidelines, you should always use your best judgement in order to
achieve the best readability. And if writing readable code requires an
additional effort, it's worth it a thousand times.

.. i18n: .. Be careful if you change the following, you don't want to mess up the
.. i18n:    guidelines numbering -- see the sectnum:: directives !!
..

.. Be careful if you change the following, you don't want to mess up the
   guidelines numbering -- see the sectnum:: directives !!

.. i18n: .. toctree::
.. i18n: 
.. i18n:     coding_guidelines_python
.. i18n:     coding_guidelines_framework
.. i18n:     coding_guidelines_testing
..

.. toctree::

    coding_guidelines_python
    coding_guidelines_framework
    coding_guidelines_testing

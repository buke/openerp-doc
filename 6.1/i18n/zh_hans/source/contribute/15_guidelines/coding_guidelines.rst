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
编码指引
=================
以下条目由OpenERP质量团队维护并且作为质量审查的一部分。
It contains a set of OpenERP specific
good/bad practices, as well as a selection of more generic Python coding
recommendations.

.. i18n: Both sections are a MUST READ for every OpenERP developer and contributor.
..

Both sections are a MUST READ for every OpenERP developer and contributor.

.. i18n: As an introductory rule, you should always keep in mind the following:
..

As an introductory rule, you should always keep in mind the following:

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

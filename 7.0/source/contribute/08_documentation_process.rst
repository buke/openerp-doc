
Documentation Process
---------------------

Books
+++++

The main documentation of OpenERP is composed of a set of books according to
the business need. These books are reviewed once a year. We are working with
authors/contributors/employees/translators to build chapters on the different
aspects of the ERP. 

This section describes how we collaborate with authors and translators to
provide very good documentation on OpenERP. To motivate people to write
quality documentation/chapters we set up author rights to pay each contributor
and translator according to their effort.

Building a Book
"""""""""""""""

We have contracts with several editors to publish books in different countries.

Once we have enough chapters written, we can compose a book and publish it.

Books are first published in a paper version. Three months after, we release it online.

..  Guidelines
..  """"""""""

.. See the documentation-guidelines-link_ section.

Author Rights
"""""""""""""

The typical author rights are between 8% and 10% on the public price, according
to the authors, the country and the editor in which the book will be published.
This commission is on the public price, no matter of the final selling price
per item.

These author rights have to be divided according to people working on the book:

  * Reviewers: 10% to be divided by number of reviewers
  * Translators: 30% to be divided by the number of translators
  * Authors: the rest (60%-90%) to be divided by number of authors

As an example, Geoff and Fabien worked on the French and English book on
OpenERP. This book is sold at a public price of 35 EUR with 10% author rights.
We had one reviewer for this book from Eyrolles. So author rights are split
in that way:

  * Geoff: 1.575 EUR/book (= 35 * 0.1 * (0.9 / 2))
  * Fabien: 1.575 EUR/book
  * Reviewer: 0.35 EUR/book (= 35 * 0.1 * 0.1)

Once this book will be translated to Hungarian, with a public price of 30 EUR
and author rights of 10% (0.1) we will have:

  * Geoff: 1.05 EUR/book (=30 * 0.1 * 0.7 / 2)
  * Fabien: 1.05 EUR/book
  * Hungarian translator: 0.90 EUR/book (=30 * 0.1 * 0.30)

Author rights are paid every 3 months, after one month. (to be verified
according to what we can do with editors)

People
++++++

Authors
"""""""

Anyone can be an author and write a complete book or just one or several
chapters on particular aspects of OpenERP. Chapters are then review

Authors from Tiny
"""""""""""""""""

At Tiny (the editor of OpenERP), each employee can write a few chapters based
on new module he wrote for specific customers, at the end of the project. As
employees get a salary to write these chapters during their working hours,
author rights are computed slightly differently:

  * Computed rights are divided by two for the employee: 50%
  * Valid while the employee works for Tiny

..  Translators
..  """""""""""

..  Reviewers
..  """""""""


.. _building_documentation:

Building the documentation
++++++++++++++++++++++++++
The Sources for the documentation can be downloaded from:
::   
 
  bzr branch lp:openobject-doc

We use Sphinx_, a documentation generator, to build
the documentation. So, Sphinx should be installed on your system and you should
know how to use it.

You can install it with easy_install_. For example, on Ubuntu: ::

  sudo easy_install sphinx


Sphinx is built on top of the reStructuredText_ project that lets you write
documents in plain text files and then generate HTML, PDF or other formats from
them. A good introduction to reStructuredText is the `Quick reStructuredText`_
reference page. reStructuredText defines the layout and formatting of a single
page. Sphinx lets you organise several pages into a large document with a
table of contents and cross references.

.. note:: if you step into this error message (line number can vary):

    ::

        ! Undefined control sequence.
        l.462 \capstart

    This sometimes means that you have a buggy version of sphinx. Try
    to install Sphinx version 1.0.2:

    ::

        sudo easy_install sphinx==1.0.2 --upgrade


Building the documentation in HTML and in PDF requires a few dependencies,
namely for the LaTeX system (additional packages and fonts). On Ubuntu you can
install the required packages with the following command:::

    # Install Latex extras
    sudo apt-get install texlive-latex-extra texlive-fonts-recommended
    # Install ImageMagick for images conversion
    sudo apt-get install imagemagick

.. describe:: building the documentation in html:

::

  make clean
  make html

.. describe:: building the documentation in pdf:

::

  make clean
  make latex
  cd build/latex
  make all-pdf

.. describe:: building a book:

For example, if you want to build the *OpenERP for Retail and Industrial Management* book:

::

  cd books/book_mrp
  make clean
  make latex
  cd build/latex
  make all-pdf

Linking to docstrings in source code
++++++++++++++++++++++++++++++++++++

Some of the pages include links to classes in the project's source code. One
example is `developer/2_5_Objects_Fields_Methods/methods.rst`. You can add more
links to source code documentation using the `Sphinx autodoc extension`_. This
will import classes and methods along with their docstring documentation. If you
don't tell Sphinx how to find the project's source code, then the import will
fail with a warning. If you want to make the import work, follow these steps:

#. It seems like you need at least version 1.0 of Sphinx. If your version hasn't
   automatically upgraded that far, see the easy_install instructions above. To
   see what version you have, run the following: 
   
   ::
   
     sphinx-build --help
  
#. You need to have a copy of the OpenERP server code. The web site builds 
   against the trunk version.
  
#. You need to tweak `server/bin/tools/config.py` by commenting out the call to
   config.parse_config() on the last line. Hopefully that will get cleaned up 
   eventually, but for now you either need a second copy of the server just for 
   building the docs from or you need to add and remove this tweak every time you
   work on the docs.
  
#. You need to add server/bin to your PYTHONPATH environment variable. The 
   simplest way to do that is to launch `make` like this:

   ::
   
     PYTHONPATH=/path/to/server/bin make html

FAQ
+++

.. describe:: How much items can we expect to sell for a book ?

The first French book we wrote is sold at 500 items per month. It's good as it
was our the first book on OpenERP but we can expect better results with an
English version. So probably between 250 and 1500 items per month for an
English book.


.. _Sphinx: http://sphinx.pocoo.org
.. _Sphinx autodoc extension: http://sphinx.pocoo.org/ext/autodoc.html
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Quick reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html

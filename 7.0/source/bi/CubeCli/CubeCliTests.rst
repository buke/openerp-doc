Running Automated Test Cases
----------------------------

We can check all the queries on :ref:`CLI <CLI-link>` by making a file with queries to be tested with the syntax given in :ref:`CLI <CLI-link>`

For example we can create *test_query* file with the content like 

.. :ref:`test_query <test_query-link>`

-------

::

  DATABASE='terp'

::

  ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br />{[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} <br />on columns from res_partner"

::

  ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br /> {[measures].[credit_limit],[measures].[count]} on rows, {[user].[all],[user].children} <br /> on columns from res_partner"

-------

The file can be run at the command prompt. It will give output on success or an error message on failure

The output of this file can be viewed CubeCliExample test_query

.. i18n: ============
.. i18n: Introduction
.. i18n: ============
..

============
介绍
============

.. i18n: How to load data ?
.. i18n: ==================
..

如何加载数据 ?
==================

.. i18n:    #. Postgresql
.. i18n:           * Simple, standard
.. i18n:           * Does not respect the WORKFLOW !!!
.. i18n:    #. XML files (with –update=)
.. i18n:    #. XML-RPC
.. i18n:           * Script, same as website interface
..

   #. Postgresql
          * Simple, standard
          * Does not respect the WORKFLOW !!!
   #. XML files (with –update=)
   #. XML-RPC
          * Script, same as website interface

.. i18n: How to backup/restore a Postgresql database?
.. i18n: ============================================
..

如何备份/恢复Postgresql 数据库?
============================================

.. i18n: :backup:
..

:backup:

.. i18n:     pg_dump terp >terp.sql
..

    pg_dump terp >terp.sql

.. i18n: :restore:
..

:restore:

.. i18n:     createdb terp --encoding=unicode
.. i18n:     psql terp < terp.sql
.. i18n:     or
.. i18n:     psql -d terp -f terp.sql
..

    createdb terp --encoding=unicode
    psql terp < terp.sql
    or
    psql -d terp -f terp.sql

.. i18n: The objects methods
.. i18n: ===================
..

对象方法
===================

.. i18n:    #. create({'field':'value'})
.. i18n:           * return ID created
.. i18n:    #. search([('arg1','=','value1')...], offset=0, limit=1000)
.. i18n:           * return [IDS] found
.. i18n:    #. read([IDS], ['field1','field2',...])
.. i18n:           * return [{'id':1, 'field1':..., 'field2':..., ...}, ...]
.. i18n:    #. write([IDS], {'field1':'value1','field2':3})
.. i18n:           * return True
.. i18n:    #. unlink([IDS])
.. i18n:           * return True
..

   #. create({'field':'value'})
          * return ID created
   #. search([('arg1','=','value1')...], offset=0, limit=1000)
          * return [IDS] found
   #. read([IDS], ['field1','field2',...])
          * return [{'id':1, 'field1':..., 'field2':..., ...}, ...]
   #. write([IDS], {'field1':'value1','field2':3})
          * return True
   #. unlink([IDS])
          * return True

.. i18n: =================
.. i18n: WebservicesXMLRPC
.. i18n: =================
..

=================
WebservicesXMLRPC
=================

.. i18n: #. XML-RPC
.. i18n:       * standard: http://www.xmlrpc.org
.. i18n:       * RPC Over HTTP
.. i18n:       * Function Parameters & Result encoded in XML
.. i18n: #. Principle;
.. i18n:       * calls to objects methodes;
.. i18n:             - read, write
.. i18n:             - create
.. i18n:             - unlink (=delete)
..

#. XML-RPC
      * 标准: http://www.xmlrpc.org
      * RPC Over HTTP
      * 函数参数 & xml格式的返回值
#. 规则;
      * 调用对象方法;
            - read, write
            - create
            - unlink (=delete)

.. i18n: XML-RPC is known as a web service. Web services are a set of tools that let one build distributed applications on top of existing web infrastructures. These applications use the Web as a kind of "transport layer" but don't offer a direct human interface via the browser.[1] Extensible Markup Language (XML) provides a vocabulary for describing Remote Procedure Calls (RPC), which is then transmitted between computers using the HyperText Transfer Protocol (HTTP). Effectively, RPC gives developers a mechanism for defining interfaces that can be called over a network. These interfaces can be as simple as a single function call or as complex as a large API.
..

XML-RPC is known as a web service. Web services are a set of tools that let one build distributed applications on top of existing web infrastructures. These applications use the Web as a kind of "transport layer" but don't offer a direct human interface via the browser.[1] Extensible Markup Language (XML) provides a vocabulary for describing Remote Procedure Calls (RPC), which is then transmitted between computers using the HyperText Transfer Protocol (HTTP). Effectively, RPC gives developers a mechanism for defining interfaces that can be called over a network. These interfaces can be as simple as a single function call or as complex as a large API.

.. i18n: XML-RPC therefore allows two or more computers running different operating systems and programs written in different languages to share processing. For example, a Java application could talk with a Perl program, which in turn talks with Python application that talks with ASP, and so on. System integrators often build custom connections between different systems, creating their own formats and protocols to make communications possible, but one can often end up with a large number of poorly documented single-use protocols. The RPC approach spares programmers the trouble of having to learn about underlying protocols, networking, and various implementation details.
..

XML-RPC therefore allows two or more computers running different operating systems and programs written in different languages to share processing. For example, a Java application could talk with a Perl program, which in turn talks with Python application that talks with ASP, and so on. System integrators often build custom connections between different systems, creating their own formats and protocols to make communications possible, but one can often end up with a large number of poorly documented single-use protocols. The RPC approach spares programmers the trouble of having to learn about underlying protocols, networking, and various implementation details.

.. i18n: XML-RPC can be used with Python, Java, Perl, PHP, C, C++, Ruby, Microsoft’s .NET and many other programming languages. Implementations are widely available for platforms such as Unix, Linux, Windows and the Macintosh.
..

XML-RPC can be used with Python, Java, Perl, PHP, C, C++, Ruby, Microsoft’s .NET and many other programming languages. Implementations are widely available for platforms such as Unix, Linux, Windows and the Macintosh.

.. i18n: An XML-RPC call is conducted between two parties: the client (the calling process) and the server (the called process). A server is made available at a particular URL (such as http://example.org:8080/rpcserv/).
..

An XML-RPC call is conducted between two parties: the client (the calling process) and the server (the called process). A server is made available at a particular URL (such as http://example.org:8080/rpcserv/).

.. i18n: The above text just touches the surface of XML-RPC. I recommend O'Reilly's "Programming Web Service with XML-RPC" for further reading. One may also wish to review the following links:
..

The above text just touches the surface of XML-RPC. I recommend O'Reilly's "Programming Web Service with XML-RPC" for further reading. One may also wish to review the following links:

.. i18n: XML-RPC Home Page\\\\ XML-RPC for C and C++\\\\ The Apache XML-RPC Project\\\\ Expat: The XML Parser\\\\
..

XML-RPC Home Page\\\\ XML-RPC for C and C++\\\\ The Apache XML-RPC Project\\\\ Expat: The XML Parser\\\\

.. i18n: =================
.. i18n: An example in PHP
.. i18n: =================
..

=================
PHP 例子
=================

.. i18n: Here is an example on how to insert a new partner using PHP. This example makes use the phpxmlrpc library, available on sourceforge.
..

这是一个使用php插入合作伙伴的例子.这个例子使用phpxmlrpc类库，可以在sourceforge上找到。

.. i18n: .. code-block:: php
.. i18n: 
.. i18n:     <?
.. i18n: 
.. i18n:         include('xmlrpc.inc');
.. i18n: 
.. i18n:         $arrayVal = array(
.. i18n:         'name'=>new xmlrpcval('Fabien Pinckaers', "string") ,
.. i18n:         'vat'=>new xmlrpcval('BE477472701' , "string")
.. i18n:         );
.. i18n: 
.. i18n:         $client = new xmlrpc_client("http://localhost:8069/xmlrpc/object");
.. i18n: 
.. i18n:         $msg = new xmlrpcmsg('execute');
.. i18n:         $msg->addParam(new xmlrpcval("dbname", "string"));
.. i18n:         $msg->addParam(new xmlrpcval("3", "int"));
.. i18n:         $msg->addParam(new xmlrpcval("demo", "string"));
.. i18n:         $msg->addParam(new xmlrpcval("res.partner", "string"));
.. i18n:         $msg->addParam(new xmlrpcval("create", "string"));
.. i18n:         $msg->addParam(new xmlrpcval($arrayVal, "struct"));
.. i18n: 
.. i18n:         $resp = $client->send($msg);
.. i18n: 
.. i18n:         if ($resp->faultCode())
.. i18n: 
.. i18n:             echo 'Error: '.$resp->faultString();
.. i18n: 
.. i18n:         else
.. i18n: 
.. i18n:             echo 'Partner '.$resp->value()->scalarval().' created !';
.. i18n: 
.. i18n:     ?>
..

.. code-block:: php

    <?

        include('xmlrpc.inc');

        $arrayVal = array(
        'name'=>new xmlrpcval('Fabien Pinckaers', "string") ,
        'vat'=>new xmlrpcval('BE477472701' , "string")
        );

        $client = new xmlrpc_client("http://localhost:8069/xmlrpc/object");

        $msg = new xmlrpcmsg('execute');
        $msg->addParam(new xmlrpcval("dbname", "string"));
        $msg->addParam(new xmlrpcval("3", "int"));
        $msg->addParam(new xmlrpcval("demo", "string"));
        $msg->addParam(new xmlrpcval("res.partner", "string"));
        $msg->addParam(new xmlrpcval("create", "string"));
        $msg->addParam(new xmlrpcval($arrayVal, "struct"));

        $resp = $client->send($msg);

        if ($resp->faultCode())

            echo 'Error: '.$resp->faultString();

        else

            echo 'Partner '.$resp->value()->scalarval().' created !';

    ?>

.. i18n: ====================
.. i18n: An example in Python
.. i18n: ====================
..

====================
Python 例子
====================

.. i18n: Example of creation of a partner and their address.
..

创建合作伙伴及其地址的例子。

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     import xmlrpclib
.. i18n: 
.. i18n:     sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
.. i18n:     uid = 1
.. i18n:     pwd = 'demo'
.. i18n: 
.. i18n:     partner = {
.. i18n:         'title': 'Monsieur',
.. i18n:         'name': 'Fabien Pinckaers',
.. i18n:         'lang': 'fr',
.. i18n:         'active': True,
.. i18n:     }
.. i18n: 
.. i18n:     partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
.. i18n: 
.. i18n:     address = {
.. i18n:         'partner_id': partner_id,
.. i18n:         'type': 'default',
.. i18n:         'street': 'Rue du vieux chateau, 21',
.. i18n:         'zip': '1457',
.. i18n:         'city': 'Walhain',
.. i18n:         'phone': '(+32)10.68.94.39',
.. i18n:         'fax': '(+32)10.68.94.39',
.. i18n:     }
.. i18n: 
.. i18n:     sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)
..

.. code-block:: python

    import xmlrpclib

    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
    uid = 1
    pwd = 'demo'

    partner = {
        'title': 'Monsieur',
        'name': 'Fabien Pinckaers',
        'lang': 'fr',
        'active': True,
    }

    partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)

    address = {
        'partner_id': partner_id,
        'type': 'default',
        'street': 'Rue du vieux chateau, 21',
        'zip': '1457',
        'city': 'Walhain',
        'phone': '(+32)10.68.94.39',
        'fax': '(+32)10.68.94.39',
    }

    sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)

.. i18n: To get the UID of a user, you can use the following script:
..

可以通过下面的脚本取得用户的UID:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
.. i18n:     UID = sock.login('terp3', 'admin', 'admin')
..

.. code-block:: python

    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    UID = sock.login('terp3', 'admin', 'admin')

.. i18n: CRUD example:
..

增删改查例子：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     """
.. i18n:     :The login function is under
.. i18n:     ::    http://localhost:8069/xmlrpc/common
.. i18n:     :For object retrieval use:
.. i18n:     ::    http://localhost:8069/xmlrpc/object
.. i18n:     """
.. i18n:     import xmlrpclib
.. i18n: 
.. i18n:     user = 'admin'
.. i18n:     pwd = 'admin'
.. i18n:     dbname = 'terp3'
.. i18n:     model = 'res.partner'
.. i18n: 
.. i18n:     sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
.. i18n:     uid = sock.login(dbname ,user ,pwd)
.. i18n: 
.. i18n:     sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
.. i18n: 
.. i18n:     # CREATE A PARTNER
.. i18n:     partner_data = {'name':'Tiny', 'active':True, 'vat':'ZZZZZ'}
.. i18n:     partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)
.. i18n: 
.. i18n:     # The relation between res.partner and res.partner.category is of type many2many
.. i18n:     # To add  categories to a partner use the following format:
.. i18n:     partner_data = {'name':'Provider2', 'category_id': [(6,0,[3, 2, 1])]}
.. i18n:     # Where [3, 2, 1] are id fields of lines in res.partner.category
.. i18n: 
.. i18n:     # SEARCH PARTNERS
.. i18n:     args = [('vat', '=', 'ZZZZZ'),]
.. i18n:     ids = sock.execute(dbname, uid, pwd, model, 'search', args)
.. i18n: 
.. i18n:     # READ PARTNER DATA
.. i18n:     fields = ['name', 'active', 'vat', 'ref']
.. i18n:     results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
.. i18n:     print results
.. i18n: 
.. i18n:     # EDIT PARTNER DATA
.. i18n:     values = {'vat':'ZZ1ZZ'}
.. i18n:     results = sock.execute(dbname, uid, pwd, model, 'write', ids, values)
.. i18n: 
.. i18n:     # DELETE PARTNER DATA
.. i18n:     results = sock.execute(dbname, uid, pwd, model, 'unlink', ids)
..

.. code-block:: python

    """
    :The login function is under
    ::    http://localhost:8069/xmlrpc/common
    :For object retrieval use:
    ::    http://localhost:8069/xmlrpc/object
    """
    import xmlrpclib

    user = 'admin'
    pwd = 'admin'
    dbname = 'terp3'
    model = 'res.partner'

    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    uid = sock.login(dbname ,user ,pwd)

    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

    # CREATE A PARTNER
    partner_data = {'name':'Tiny', 'active':True, 'vat':'ZZZZZ'}
    partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)

    # The relation between res.partner and res.partner.category is of type many2many
    # To add  categories to a partner use the following format:
    partner_data = {'name':'Provider2', 'category_id': [(6,0,[3, 2, 1])]}
    # Where [3, 2, 1] are id fields of lines in res.partner.category

    # SEARCH PARTNERS
    args = [('vat', '=', 'ZZZZZ'),]
    ids = sock.execute(dbname, uid, pwd, model, 'search', args)

    # READ PARTNER DATA
    fields = ['name', 'active', 'vat', 'ref']
    results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
    print results

    # EDIT PARTNER DATA
    values = {'vat':'ZZ1ZZ'}
    results = sock.execute(dbname, uid, pwd, model, 'write', ids, values)

    # DELETE PARTNER DATA
    results = sock.execute(dbname, uid, pwd, model, 'unlink', ids)

.. i18n: :PRINT example:
..

:PRINT example:

.. i18n:    1. PRINT INVOICE
.. i18n:    2. IDS is the invoice ID, as returned by:
.. i18n:    3. ids = sock.execute(dbname, uid, pwd, 'account.invoice', 'search', [('number', 'ilike', invoicenumber), ('type', '=', 'out_invoice')])
..

   1. 打印发票
   2. IDS就是发票的ID:
   3. ids = sock.execute(dbname, uid, pwd, 'account.invoice', 'search', [('number', 'ilike', invoicenumber), ('type', '=', 'out_invoice')])

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     import time
.. i18n:     import base64
.. i18n:     printsock = xmlrpclib.ServerProxy('http://server:8069/xmlrpc/report')
.. i18n:     model = 'account.invoice'
.. i18n:     id_report = printsock.report(dbname, uid, pwd, model, ids, {'model': model, 'id': ids[0], 'report_type':'pdf'})
.. i18n:     time.sleep(5)
.. i18n:     state = False
.. i18n:     attempt = 0
.. i18n:     while not state:
.. i18n:         report = printsock.report_get(dbname, uid, pwd, id_report)
.. i18n:         state = report['state']
.. i18n:         if not state:
.. i18n:             time.sleep(1)
.. i18n:             attempt += 1
.. i18n:         if attempt>200:
.. i18n:             print 'Printing aborted, too long delay !'
.. i18n: 
.. i18n:         string_pdf = base64.decodestring(report['result'])
.. i18n:         file_pdf = open('/tmp/file.pdf','w')
.. i18n:         file_pdf.write(string_pdf)
.. i18n:         file_pdf.close()
..

.. code-block:: python

    import time
    import base64
    printsock = xmlrpclib.ServerProxy('http://server:8069/xmlrpc/report')
    model = 'account.invoice'
    id_report = printsock.report(dbname, uid, pwd, model, ids, {'model': model, 'id': ids[0], 'report_type':'pdf'})
    time.sleep(5)
    state = False
    attempt = 0
    while not state:
        report = printsock.report_get(dbname, uid, pwd, id_report)
        state = report['state']
        if not state:
            time.sleep(1)
            attempt += 1
        if attempt>200:
            print 'Printing aborted, too long delay !'

        string_pdf = base64.decodestring(report['result'])
        file_pdf = open('/tmp/file.pdf','w')
        file_pdf.write(string_pdf)
        file_pdf.close()

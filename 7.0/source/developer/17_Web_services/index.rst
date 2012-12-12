
============
Introduction
============

How to load data ?
==================

   #. Postgresql
          * Simple, standard
          * Does not respect the WORKFLOW !!!
   #. XML files (with –update=)
   #. XML-RPC
          * Script, same as website interface

How to backup/restore a Postgresql database?
============================================

:backup:

    pg_dump terp >terp.sql

:restore:

    createdb terp --encoding=unicode
    psql terp < terp.sql
    or
    psql -d terp -f terp.sql

The objects methods
===================

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

=================
WebservicesXMLRPC
=================

#. XML-RPC
      * standard: http://www.xmlrpc.org
      * RPC Over HTTP
      * Function Parameters & Result encoded in XML
#. Principle;
      * calls to objects methodes;
            - read, write
            - create
            - unlink (=delete)

XML-RPC is known as a web service. Web services are a set of tools that let one build distributed applications on top of existing web infrastructures. These applications use the Web as a kind of "transport layer" but don't offer a direct human interface via the browser.[1] Extensible Markup Language (XML) provides a vocabulary for describing Remote Procedure Calls (RPC), which is then transmitted between computers using the HyperText Transfer Protocol (HTTP). Effectively, RPC gives developers a mechanism for defining interfaces that can be called over a network. These interfaces can be as simple as a single function call or as complex as a large API.

XML-RPC therefore allows two or more computers running different operating systems and programs written in different languages to share processing. For example, a Java application could talk with a Perl program, which in turn talks with Python application that talks with ASP, and so on. System integrators often build custom connections between different systems, creating their own formats and protocols to make communications possible, but one can often end up with a large number of poorly documented single-use protocols. The RPC approach spares programmers the trouble of having to learn about underlying protocols, networking, and various implementation details.

XML-RPC can be used with Python, Java, Perl, PHP, C, C++, Ruby, Microsoft’s .NET and many other programming languages. Implementations are widely available for platforms such as Unix, Linux, Windows and the Macintosh.

An XML-RPC call is conducted between two parties: the client (the calling process) and the server (the called process). A server is made available at a particular URL (such as http://example.org:8080/rpcserv/).

The above text just touches the surface of XML-RPC. I recommend O'Reilly's "Programming Web Service with XML-RPC" for further reading. One may also wish to review the following links:

XML-RPC Home Page\\\\ XML-RPC for C and C++\\\\ The Apache XML-RPC Project\\\\ Expat: The XML Parser\\\\


=================
An example in PHP
=================

Here is an example on how to insert a new partner using PHP. This example makes use the phpxmlrpc library, available on sourceforge.

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


====================
An example in Python
====================

Example of creation of a partner and their address.

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

To get the UID of a user, you can use the following script:

.. code-block:: python

    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
    UID = sock.login('terp3', 'admin', 'admin')


CRUD example:

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



:PRINT example:

   1. PRINT INVOICE
   2. IDS is the invoice ID, as returned by:
   3. ids = sock.execute(dbname, uid, pwd, 'account.invoice', 'search', [('number', 'ilike', invoicenumber), ('type', '=', 'out_invoice')])


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


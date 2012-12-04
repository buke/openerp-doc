.. sectnum::
    :start: 3

.. _yaml-testing-guidelines:

==============================
Automated YAML Tests Guideline
==============================

.. note::

    Please see also section :ref:`yaml-serialization`

This is a guideline for project managers and developers on automated tests. 

Syntax
------

    Write scenarios using the YAML syntax, not the "cucumber" syntax,  so
    that we can directly integrate these tests in OpenERP modules (and implement
    them later).

Tests are run on the server side
--------------------------------

As tests are performed server side, you don't need to write things like

    ::

        # wrong
        * Given I am logged in as admin user with proper password
        * module pos is installed

    The user is admin by default, so no need to write this in each test
    file. Instead of saying 'I check that the module pos is installed',
    just write the name of the module where you will put this test. The first
    line would then be **"module: pos"**.

Be precise about the goal of the test
------------------------------------------
Try to use functional terms instead of object

    * This is not good enough::

        I will test the manufacturing order

    * An example of a good introduction::

         In order to test the CRM in OpenERP, I will do a customer qualification 
         process that begins with the first customer contact (a lead), 
         which will be converted to a business opportunity and a partner.

    ::

        # wrong
        *In caldav testing of creation of calendar as Admin

        # better
        *In order to test the calendar synchronisation with mobile phones and
        outlook, I will test the caldav interface for meetings.


        # wrong:
        In order to test the manufacturing order process and modules as an       
        administrator I want to see if the features work correctly.

        # better:
          In order to test the manufacturing of products, I will test the
          features of the manufacturing order document: consume raw materials,
          produce finished goods, scrap some products and split in production
          lots.

        # wrong:
        Testing of Document for ftp server is running and being connected or
        not
        # better:
          In order to test the document management system, I will try different
          operations on the FTP interface, and check their impacts on OpenERP's
          documents.

Avoid relying on data that can be changed by the user before launching the test
-------------------------------------------------------------------------------
    ::

        # wrong (mrp):
        Then my manufacturing order turned into 'Waiting for goods' state.
        And one picking was also generated for my manufacturing order:
        'INT/00001'.

    This is not a good test, who knows if it will be 'INT/0001' or another
    sequence 'INT/0002' ? Because the user may have created internal
    pickings before they installed the mrp module.

    ::

        # wrong (pos):
        I press new record from toolbar.
        Some default values are filled automatically like:
        Company>Tinysprl,Journal>x Sales Journal

    You can not test if the company is 'Tiny SPRL'. The user may have
    configured it to his own company name. It's better to test:
    "The company is set by default to the company of the admin user."

    Take care of these data dependencies, because it may crash the tests
    simply because the user changed some demo data before launching the tests.

    You can rely on demo data defined by the module where you put your test
    file, but if the demo data are defined by another module, try to either
    create your own data or find a way to work with ids instead of names.

Write things in test that can be easily tested by the YAML system
-----------------------------------------------------------------

**For** **example,**
the mail gateway. You can not write this::

       First I have made one fetchmail rc script using the proper syntax
       with specific email server and address information and used crm.lead
       as model Then I run the fetchmail command like: fetchmail -f <created
       rc file name> The script should exit successfully

Because you can not set-up an email pop account to test this.

I would rather do::

       I have a list of different emails with different encoding and
       different kind of attachments stored in the directory test/emails.
       I test to pass all these documents through the mailgateway script:
         something like:
           for each email file:
             call the script with stdin<this email file

If possible call in python directly, not using os.system.

For the FTP, it can be tested by the YAML as you simply have to use the Python
FTP client in your yaml code::

        import ftplib

Avoid relying on existing demo data if the user can change it.
--------------------------------------------------------------

   **Bad** **example**:

   When I pressed *'Confirm Production'* button.
   Then I could see the Finished Products into Products to Consume with
   quantity 10.00.

   Then my manufacturing order turned into 'Waiting for goods' state.
   And one picking was also generated for my manufacturing order:
   'INT/00001'.

   .. csv-table::  And the following values appeared in the Products to Consume
      :header: "product_id","product_qty","product_uom","location_id","||","||"
      :widths: 30,6,6,15,2,2

      "[CPU_GEN] Regular processor config","10.00","PCE","Stock","||","||"
      "[HDD1] HDD Seagate 7200.8 80GB","10.00","PCE","Stock","||","||"
      "[TOW1] ATX Mid-size Tower","10.00","PCE","Stock","||","||"
      "[MOU] Mouse","10.00","PCE","Stock","||","||"
      "[KEYA] Keyboard -AZERTY","10.00","PCE","Stock","||","||"

   For such an example, I would have created a few products and a bom in the test scenario. And test the manufacturing order on these test data.

Don't check the full text of an exception
-----------------------------------------
   Then I got the following error message:

   xmlrpclib.Fault: <Fault warning -- Error::

        Couldn't find bill of material for product: 'Traceback (most recent call last):
        File in dispatch
        result = ExportService.getService(service_name).dispatch(method, auth, params)
         File "/home/uco/workspace/Trunk/openobject-server/bin/service/web_services.py", line 587, in dispatch
         res = fn(db, uid, *params)
         File "/home/uco/workspace/Trunk/openobject-server/bin/osv/osv.py", line 64, in wrapper
         self.abortResponse(1, inst.name, inst.exc_type, inst.value)
         File "/home/uco/workspace/Trunk/openobject-server/bin/netsvc.py", line 66, in abortResponse
         raise Exception("%s -- %s\\n\\n%s"%(origin, description, details))
        Exception: warning -- Error
        
        Couldn\'t find bill of material for product\n'>

    Simply do::

      And it should generate an exception to say that it cannot find a BoM
      defined for this product.


Be more functional, explain what the user means to do, not where she clicks
---------------------------------------------------------------------------

::

        # wrong:
        I press new record from toolbar of lead's view
        Some default values are filled automatically like: priority>Normal,user_id>Administrator, state>Draft
        Then I give some values for lead:
        |name|section_id|partner_name|phone|mobile|
        |Carrie Helle|Sales Department|Stonage IT|(855) 924-4364|(333) 715-1450|
        Then I press the save button from toolbar
        The lead is created successfully

No need to write the all the data of the form in the English text
(phone, mobile, ...). These data will be written in the final YAML, when
you implement the test. A better final YAML for the above example should
look like this::

    -
     As I met a new customer in a fair, I create a new lead "Stonage IT"
     to record his data.
    -
     !record {model:rcrm.lead, id:partner_carrie}
       name: Stonage IT
       contact_name: Carrie Helle
       phone: (855) 924-4364
       mobile: (333) 715-1450
    -
      I check that the state field is set automatically by default.
    -
      !assert {model:crm.lead, id:partner_carrie} state


You can use "onchange" calls in your tests, to simulate the client interface
----------------------------------------------------------------------------

    -
      I create a new sale order by filling the partner.
      I want addresses to be filled up by the onchange call but I still need to
      provide dummy addresses (required fields) to allow the record to be created.
    -
      !record {model: sale.order, id: my_order}:
        partner_id: base.res_partner_asus
        pricelist_id: product.list0
        partner_order_id: base.main_address
        partner_invoice_id: base.main_address
        partner_shipping_id: base.main_address
    -
      I then call the onchange method and update the record with the returned value.
    -
      !python {model: sale.order}: |
        my_order = self.browse(cr, uid, ref('my_order'))
        value = my_order.onchange_partner_id(my_order['partner_id']).get('value', {})
        my_order.write(value)


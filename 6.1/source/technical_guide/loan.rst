
.. module:: loan
    :synopsis: Loan Management 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/loan"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Loan Management (*loan*)
========================
:Module: loan
:Name: Loan Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: loan
:Web: http://tinyerpindia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Loan Management System
      Integrated with the Payroll System

Download links
--------------

You can download this module as a zip file in the following version:

* `5.0 <http://www.openerp.com/download/modules/5.0/loan.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

 * Loan Paper

Menus
-------

 * Financial Management/Configuration/Loan/Proof Type
 * Financial Management/Configuration/Loan/Loan Period
 * Financial Management/Loan/Personal Loan
 * Financial Management/Loan/Personal Loan/Apprived Loans
 * Financial Management/Loan/Personal Loan/Small Loans
 * Financial Management/Loan/Personal Loan/Medium Loans
 * Financial Management/Loan/Personal Loan/Large Loans
 * Financial Management/Loan/Cheque
 * Financial Management/Loan/Cheque/Draft
 * Financial Management/Loan/Cheque/Posted
 * Financial Management/Loan/Installment
 * Financial Management/Configuration/Loan/Interest/Interest List
 * Financial Management/Configuration/Loan/Interest/Interest Version
 * Financial Management/Loan/Report Of Partner Loan

Views
-----

 * account.loan.proof.type.form (form)
 * account.loan.proof.type.tree (tree)
 * loan.installment.period.form (form)
 * loan.installment.period.tree (tree)
 * \* INHERIT res.partner.form.inherit (form)
 * account.loan.proof.tree (tree)
 * account.loan.installment.tree (tree)
 * account.loan.proof.form (form)
 * account.loan.tree (tree)
 * account.loan.form (form)
 * account.loan.bank.cheque.form (form)
 * account.loan.bank.cheque.tree (tree)
 * account.loan.installment.form (form)
 * account.loan.installment.tree (tree)
 * account.loan.loantype.form (form)
 * account.loan.loantype.tree (tree)
 * account.loan.loantype.interestversion.form (form)
 * account.loan.loantype.interestversion.tree (tree)
 * account.loan.loantype.interestversionline.form (form)
 * account.loan.loantype.interestversionline.tree (tree)


Objects
-------

Object: account.loan (account.loan)
###################################


Object: account.loan.proof.type (account.loan.proof.type)
#########################################################


Object: account.loan.proof (account.loan.proof)
###############################################


Object: account loan type  (account.loan.loantype)
##################################################


Object: account.loan.loantype.interestversion (account.loan.loantype.interestversion)
#####################################################################################


Object: account.loan.loantype.interestversionline (account.loan.loantype.interestversionline)
#############################################################################################


Object: Bank Account Cheque (account.loan.bank.cheque)
######################################################


Object: account.loan.installment (account.loan.installment)
###########################################################


Object: loan.installment.period (loan.installment.period)
#########################################################

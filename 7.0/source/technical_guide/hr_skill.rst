
.. module:: hr_skill
    :synopsis: Skill Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_skill"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Skill Management (*hr_skill*)
=============================
:Module: hr_skill
:Name: Skill Management
:Version: 5.0.0.1
:Author: Tiny
:Directory: hr_skill
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Generic and powerfull skill management system. This module allows you to manage your company and employees skills, interviews, ...

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_skill.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_skill.zip>`_


Dependencies
------------

 * :mod:`hr`

Reports
-------

 * Evaluation report

Menus
-------

 * Human Resources/Configuration/Skills Management
 * Human Resources/Configuration/Skills Management/Skills
 * Human Resources/Configuration/Skills Management/Skills Structure
 * Human Resources/Configuration/Skills Management/Positions
 * Human Resources/Configuration/Skills Management/Profiles
 * Human Resources/Configuration/Skills Management/Weight Categories
 * Human Resources/Configuration/Skills Management/Weights
 * Human Resources/Configuration/Skills Management/Experience Categories
 * Human Resources/Configuration/Skills Management/Experiences
 * Human Resources/Configuration/Skills Management/Evaluations
 * Human Resources/Configuration/Skills Management/Languages
 * Human Resources/Configuration/Skills Management/Scale Grade 
 * Human Resources/Configuration/Skills Management/Employees Status

Views
-----

 * hr_skill.skill.form (form)
 * hr_skill.skill.tree (tree)
 * hr_skill.position.form (form)
 * hr_skill.profile.form (form)
 * hr_skill.weight.category.form (form)
 * hr_skill.weight.form (form)
 * hr_skill.experience.category.form (form)
 * hr_skill.experience.form (form)
 * hr_skill.evaluation.form (form)
 * hr_skill.evaluation.tree (tree)
 * \* INHERIT hr.employee.form (form)
 * Languages (form)
 * Languages (tree)
 * Languages (form)
 * Languages (tree)
 * \* INHERIT employee.grade.form1.inherit (form)
 * Pay Scales (form)
 * Pay Scales (tree)
 * employee.status.form (form)


Objects
-------

Object: hr_skill.weight.category (hr_skill.weight.category)
###########################################################



:name: Name, char, required




Object: hr_skill.weight (hr_skill.weight)
#########################################



:category_id: Category, many2one, required





:name: Name, char, required





:value: Numerical value, float, required




Object: hr_skill.skill (hr_skill.skill)
#######################################



:name: Name, char, required





:weight: Weight, float, required





:child_ids: Childs, one2many





:parent_id: Parent, many2one





:weight_category_id: Weight Category, many2one





:active: Active, boolean





:view: Skill, selection, required




Object: hr_skill.experience.category (hr_skill.experience.category)
###################################################################



:name: Name, char, required




Object: hr_skill.experience (hr_skill.experience)
#################################################



:skill_ids: Skills, one2many





:category_id: Category, many2one





:name: Name, char, required





:sequence: Sequence, integer




Object: hr_skill.evaluation.category (hr_skill.evaluation.category)
###################################################################



:name: Name, char, required




Object: hr_skill.evaluation (hr_skill.evaluation)
#################################################



:experience_ids: Experience, one2many





:employee_id: Evaluated Employee, many2one





:name: Evaluation name, char, required





:reference: Reference, char





:skill_ids: Skill, one2many





:interviewer_name: Evaluator, char, required





:interviewee_name: Evaluated People, char, required





:note: Notes, text





:date: Date, date, required





:category_id: Category, many2one




Object: hr_skill.profile (hr_skill.profile)
###########################################



:skill_ids: Skills, one2many





:name: Name, char, required




Object: hr_skill.position (hr_skill.position)
#############################################



:status: Status, selection





:profile_ids: Profiles, one2many





:employee_id: Assigned Employee, many2one





:name: Name, char, required




Object: hr_skill.position.profile (hr_skill.position.profile)
#############################################################



:position_id: Position, many2one, required





:weight_id: Weight, many2one, required





:profile_id: Profile, many2one, required





:name: Name, char




Object: hr_skill.experience.skill (hr_skill.experience.skill)
#############################################################



:weight_id: Weight, many2one, required





:experience_id: Experience, many2one, required





:name: Name, char, required





:skill_id: Skill, many2one, required




Object: hr_skill.profile.skill (hr_skill.profile.skill)
#######################################################



:weight_id: Weight, many2one, required





:profile_id: Profile, many2one, required





:name: Name, char





:skill_id: Skill, many2one, required




Object: hr_skill.evaluation.experience (hr_skill.evaluation.experience)
#######################################################################



:weight_id: Weight, many2one, required





:evaluation_id: Evaluation, many2one, required





:name: Name, char, required





:experience_id: Experience, many2one, required




Object: hr_skill.evaluation.skill (hr_skill.evaluation.skill)
#############################################################



:weight_id: Weight, many2one, required





:evaluation_id: Evaluation, many2one, required





:name: Name, char





:skill_id: Skill, many2one, required




Object: Languages (hr.lang)
###########################



:name: Language, char




Object: Languages (emp.lang)
############################



:read: Read, boolean





:write: Write, boolean





:speak: Speak, boolean





:name: Language, many2one





:ii_id: languages known, many2one




Object: Pay Scales (hr.scale)
#############################



:code: Code, char





:name: Name, char





:increase: Step Increase, integer





:min_sal: Minimum Salary, integer





:max_sal: Maximum Salary, integer





:cur: Currency, selection




Object: employee.status (employee.status)
#########################################



:name: Status Name, char, required



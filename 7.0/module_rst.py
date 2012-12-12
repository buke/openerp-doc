# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import os, sys
import zipfile
import optparse

class DocRst:
    def __init__(self, zipTerp):
        self.dico = {}
        key = ['module_name', 'name', 'version', 'website', 'description', 'depends', 'certificate', 'author']
        
        for value in key:            
            
            if zipTerp.has_key(value) == True:
                if value == key[0]:
                    self.dico['name'] = unicode(zipTerp[value],'utf_8')
                if value == key[1]:
                    self.dico['shortdesc'] = unicode(zipTerp[value],'utf_8')
                if value == key[2]:
                    self.dico['latest_version'] = zipTerp[value]
                if value == key[3]:
                    self.dico['website'] = zipTerp[value]
                if value == key[4]:
                    self.dico['description'] = self._handle_text(unicode(zipTerp[value],'utf_8') or 'None')                    
                if value == key[5]:
                    self.dico['depends'] = zipTerp[value]
                if value == key[6]:
                    self.dico['quality_certified'] = bool(zipTerp[value]) and 'yes' or 'no'
                    self.dico['official_module'] = str(zipTerp[value])[:2] == '00' and 'yes' or 'no'
                    self.dico['quality_certified_label'] = self._quality_certified_label(zipTerp[value])                    
                if value == key[7]:
                    self.dico['author'] = unicode(zipTerp[value],'utf_8')
            else:
                if value == key[0]:
                    self.dico['name'] = ''
                if value == key[1]:
                    self.dico['shortdesc'] = ''
                if value == key[2]:
                    self.dico['latest_version'] = ''
                if value == key[3]:
                    self.dico['website'] = ''
                if value == key[4]:
                    self.dico['description'] = ''                    
                if value == key[5]:
                    self.dico['depends'] = ''
                if value == key[6]:
                    self.dico['quality_certified'] = 'no'
                    self.dico['official_module'] = 'no'                    
                    self.dico['quality_certified_label'] = self._quality_certified_label(None)                    
                if value == key[7]:
                    self.dico['author'] = ''

        self.dico['report_list'] = ''
        self.dico['menu_list'] = ''
        self.dico['view_list'] = ''
        self.objects = None
                         
    def _quality_certified_label(self, certificate):
        '''
            Function to add label weather module is quality certified and official 
            
            return label text
        '''
        """"""
        label = ""        
        if certificate and len(certificate) > 1:
            if certificate[:2] == '00':
                # addons
                label = "(Official, Quality Certified)"
            elif certificate[:2] == '01':
                # extra addons
                label = "(Quality Certified)"

        return label

    def _handle_list_items(self, list_item_as_string):
        list_item_as_string = list_item_as_string.strip()
        if list_item_as_string:
            return [item.replace('*', '\*') for item in list_item_as_string.split('\n')]
        else:
            return []

    def _handle_text(self, txt):
        lst = ['  %s' % line for line in txt.split('\n')]
        return '\n'.join(lst)

    def _write_header(self):
        '''
            Function to parse header part of module rst file
            
            return string header text 
        '''
        dico = self.dico
        title = "%s (*%s*)" % (dico['shortdesc'], dico['name'])
        title_underline = "=" * len(title)
        dico['title'] = title
        dico['title_underline'] = title_underline

        sl = [
            "",
            ".. module:: %(name)s",
            "    :synopsis: %(shortdesc)s %(quality_certified_label)s",
            "    :noindex:",
            ".. ",
            "",
            ".. raw:: html",
            "",
            """    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />""",
            "",
            "%(title)s",
            "%(title_underline)s",
            ":Module: %(name)s",
            ":Name: %(shortdesc)s",
            ":Version: %(latest_version)s",
            ":Author: %(author)s",
            ":Directory: %(name)s",
            ":Web: %(website)s",
            ":Official module: %(official_module)s",
            ":Quality certified: %(quality_certified)s",
            "",
            "Description",
            "-----------",
            "",
            "::",
            "",
            "%(description)s",
            ""]
        return '\n'.join(sl) % (dico)

    def _write_reports(self):
        sl = ["",
              "Reports",
              "-------"]
        reports = self.dico['report_list']
        if reports:
            for report in reports:
                if report:
                    sl.append("")
                    sl.append(" * %s" % report)
        else:
            sl.extend(["", "None", ""])

        sl.append("")
        return '\n'.join(sl)

    def _write_menus(self):
        sl = ["",
              "Menus",
              "-------",
              ""]
        menus = self.dico['menu_list']
        if menus:
            for menu in menus:
                if menu:
                    sl.append(" * %s" % menu)
        else:
            sl.extend(["", "None", ""])

        sl.append("")
        return '\n'.join(sl)

    def _write_views(self):
        sl = ["",
              "Views",
              "-----",
              ""]
        views = self.dico['view_list']
        if views:
            for view in views:
                if view:
                    sl.append(" * %s" % view)
        else:
            sl.extend(["", "None", ""])

        sl.append("")
        return '\n'.join(sl)

    def _write_depends(self):
        sl = ["",
              "Dependencies",
              "------------",
              ""]
        depends = self.dico['depends']
        
        if depends:
            for dependency in depends:
                sl.append(" * :mod:`%s`" % (dependency))
        else:
            sl.extend(["", "None", ""])
        sl.append("")
        return '\n'.join(sl)

    def _write_objects(self):
        def write_field(field_def):
            if not isinstance(field_def, tuple):
                logger = netsvc.Logger()
                msg = "Error on Object %s: field_def: %s [type: %s]" % (obj_name.encode('utf8'), field_def.encode('utf8'), type(field_def))
                logger.notifyChannel("error", netsvc.LOG_ERROR, msg)
                return ""

            field_name = field_def[0]
            field_dict = field_def[1]
            field_required = field_dict.get('required', '') and ', required'
            field_readonly = field_dict.get('readonly', '') and ', readonly'

            field_help_s = field_dict.get('help', '').strip()
            if field_help_s:
                field_help_s = "*%s*" % (field_help_s)
                field_help = '\n'.join(['    %s' % line.strip() for line in field_help_s.split('\n')])
            else:
                field_help = ''

            sl = ["",
                  ":%s: %s, %s%s%s" % (field_name, field_dict.get('string', 'Unknown'), field_dict['type'], field_required, field_readonly),
                  "",
                  field_help,
                 ]
            return '\n'.join(sl)

        sl = ["",
              "",
              "Objects",
              "-------"]
        if self.objects:
            for obj in self.objects:
                obj_name = obj['object'].name
                obj_model = obj['object'].model
                title = "Object: %s (%s)" % (obj_name, obj_model)
                slo = [
                       "",
                       title,
                       '#' * len(title),
                       "",
                       #".. index::",
                       #"  single: %s object" % (obj_name),
                       #".. ",
                      ]

                for field in obj['fields']:
                    slf = [
                           "",
                           write_field(field),
                           "",
                           #".. index::",
                           #"  single: %s field" % (field[0]),
                           #".. ",
                           #"",
                           #"",
                          ]
                    slo.extend(slf)
                sl.extend(slo)
        else:
            sl.extend(["", "None", ""])

        return '\n'.join(sl)

    def write(self):
        s = ''
        s += self._write_header()
        s += self._write_depends()
        s += self._write_reports()
        s += self._write_menus()
        s += self._write_views()
        s += self._write_objects()

        return s

def dirCounter(zipPath, rstPath):
    '''
        Function to compair and find which module not have rst file
        
        return [no.of zip file name]  
    '''
        
    dir_count  = 0
    file_count = 0
    rst_count = 0
    no_zip = []
        
    for root, dirs, files in os.walk(zipPath):      
         
        for f in files:
            zipName = f.split('.')[0]            
            if fileType(f) == 0:
                file_count += 1
                rstFile = zipName + '.rst'                                                          
                if checkRstFile(rstPath+rstFile) == 0:
                    rst_count += 1
                else:
                    no_zip.append(f) 

        for d in dirs:
            
            if os.path.isdir(os.path.join(zipPath, d)):
                dir_count += 1
                rstFile = d + '.rst'                                                          
                if checkRstFile(rstPath+rstFile) == 0:
                    rst_count += 1
                else:
                    no_zip.append(d)

    
    if file_count == 0 and dir_count == 0:
        return 0
    else:
        return no_zip 

def fileType(fileName):
    type = fileName.split('.')[-1]
    
    if type != 'zip':        
        return 1
    else:
        return 0

def checkRstFile(rstfile):
    
    if os.path.isfile(rstfile):
        return 0
    else:
        return 1


def main():
    
    try:
        print '\n'
        parser = optparse.OptionParser("usage: python %prog [options] modulespath rstpath")
        parser.add_option("-S", "--src", dest="source", type="string", default='',help="Path for modules directory")
        parser.add_option("-D", "--dest", dest="destination",  type="string", default='',help="Path for rst directory ")
        
        (options,  args) = parser.parse_args()
        
        if ((len(args)) != 2 and (options.source == '' and options.destination == '')) or ((len(args)) != 2 and (options.source == '' and options.destination != '')) or ((len(args)) != 2 and (options.source != '' and options.destination == '')):
            parser.error("Incorrect number of argument - For help option type  -h,  --help")                
        elif (len(args)) == 2 and (options.source == '' and options.destination == ''):
            zipFolder = args[0]
            rstFolder = args[1]
        elif (len(args)) != 2 and (options.source != '' and options.destination != ''):
            zipFolder = options.source
            rstFolder = options.destination
        
               
        fileRst = ''
                    
        zipModule = dirCounter(zipFolder , rstFolder)
        
        if len(zipModule) != 0:
            print "\nBelow files have not rst file\n"
            print zipModule
            print "\n"
            
            for f in zipModule:
    
                if os.path.isdir(os.path.join(zipFolder, f)): # Read only directory

                    dir = os.listdir(os.path.join(zipFolder, f))  
                    for aDirFile in dir:
                        
                        if aDirFile == '__terp__.py':
                            
                            dirOpen = open(zipFolder + f + '/' + aDirFile, 'r').read()   # Reading zip file form zip folder
                                
                            fileObj = eval(dirOpen)
 
                            fileObj["module_name"] = f
                            
                            rstObj = DocRst(fileObj)            # Rst class object 
                            rstOut = rstObj.write()             # Function to generate rst file base on __terp__.py file
                            
                            try:
                                fileRst += '\t\t\t\t'+ f + '.rst\n'
                                rstFileObj = open( rstFolder + f + '.rst', 'w')     # Create rst file                
                                rstFileObj.write(rstOut.encode('utf_8'))                                    # Write text in rst file
                            finally:
                                rstFileObj.close()
                                                                
                            break                    
                else:                                           # Read only zip file
                              
                    zip = zipfile.ZipFile(zipFolder + f, 'r' )  # Zip file object 
                            
                    for aFile in zip.namelist():
            
                        path, filename = os.path.split(aFile)
                        
                        if filename == '__terp__.py':
                            
                            zipopen = zip.read(aFile)           # Reading zip file form zip folder
                            
                            zipName = f.split('.')[0]
                            
                            fileObj = eval(zipopen) 
                            fileObj["module_name"] = zipName
                            
                            rstObj = DocRst(fileObj)            # Rst class object 
                            rstOut = rstObj.write()             # Function to generate rst file base on __terp__.py file
                            
                            try:
                                fileRst += '\t\t\t\t'+ zipName + '.rst\n'
                                rstFileObj = open( rstFolder + zipName + '.rst', 'w')     # Create rst file                
                                rstFileObj.write(rstOut.encode('utf_8'))                                    # Write text in rst file
                            finally:
                                rstFileObj.close()
                                
                            break
                    
            if fileRst == '':        
                print 'No rst file created'
            else:
                print 'Successfully generated files list at : '+ rstFolder + '\n\n' + fileRst
            
        else:
                        
            if zipModule == 0:
                print "\nFolder doesn't contain any file"
        
    except:
        print ''        
        
            
    print "\n"
    

if __name__ ==  '__main__':
    main()

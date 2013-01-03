# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Projects-IDU (Instituto de Desarrollo Urbano) Customization for Project Management",
    "version" : "openerp7.0-rev",
    "author" : "Angel María Fonseca, Andres Ignacio Baez Alba and Cinxgler Mariaca Minda",
    "website" : "www.idu.gov.co",
    "category" : "Project",
    "description": """Custom project management for IDU""",
    "depends" : ['project'],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'project_idu_view.xml',
    ],
    "installable": True
}
    
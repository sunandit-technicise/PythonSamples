import json     # For handling JSON data from given JSON file
import sys      # For handling command line arguments
import xml.etree.cElementTree as ET     # To create template for XML. Name of our XML template is templete/model.xml
import jinja2          # To create Controller for our template templete/model.xml to impart changes
import os

def create_Dynamic_xml_list(Object_list, fp_out):
    # Create environmental variable in the location of our template (/templete/model.xml)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["./templete"]))
    template = env.get_template("model.xml") # Get our template model.xml from env
    Model_Object_list = Object_list # Value (Object_list), a list is assigned to jinja variable Model_Object_list in model.xml  
    result = template.render(Model_Object_list=Model_Object_list) # General rendering or imparting changes on Model_Object_list variable 
    fp_out.write(result) # New modified XML file is created with user given name


def create_Dynamic_xml_dict(Object_dict, fp_out):
    # Create environmental variable in the location of our template (/templete/model.xml)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["./templete"]))
    template = env.get_template("More_Generic_Template.xml") # Get our template model.xml from env
    json_dict = dict()
    for element in Object_dict:
	if element == '__modelname__':
		model_name = Object_dict[element]
	else:
		json_dict[element] = Object_dict[element]
    #json_dict = Object_dict # Value (Object_list), a list is assigned to jinja variable Model_Object_list in model.xml  
    result = template.render(json_dict=json_dict, model_name =model_name) # General rendering or imparting changes on Model_Object_list variable 
    fp_out.write(result) # New modified XML file is created with user given name
    

								# MAIN NAMESPACE
print 'Number of arguments:', len(sys.argv), 'arguments.'
argv_list = sys.argv
print 'Argument List:', argv_list
print"Name of Input JSON file:",		# Please enter Input JSON file with .json extension
print argv_list[1]
print"Name of Output XML file:",		# Please enter Output XML file with .xml extension
print argv_list[2]
json1_file = open(str(argv_list[1]), "r")
json1_str = json1_file.read()
print"Given JSON object(s):"
print json1_str
Output_XML_fp = open(str(argv_list[2]), 'w')  # Open Output XML file
json1_object = json.loads(json1_str)   # Given JSON Object(s) in form dictionary
json1_object_list = list()             # List of JSON objects
json1_object_list.append(json1_object) # Create an array of JSON objects
print json1_object_list

#create_Dynamic_xml_list(json1_object_list, Output_XML_fp)  # Controller function to render changes over default template and produce XML with user given name using list 

create_Dynamic_xml_dict(json1_object, Output_XML_fp)  # Controller function to render changes over default template and produce XML with user given name using Dictionary



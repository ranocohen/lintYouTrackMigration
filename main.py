from youtrack.connection import Connection
import xml.etree.ElementTree as ET

connection = Connection('https://365scoresui.myjetbrains.com/youtrack', 'shalom@365scores.com', '0melamed0')

tree = ET.parse('AndroidLintOverdraw.xml')
root = tree.getroot()

print connection.getProjects()

for problem in root:
    file = problem.find('file').text
    line = problem.find('line').text
    module = problem.find('module').text
    entry_point = problem.find('entry_point').text
    problem_class = problem.find('problem_class')
    problem_summary = problem_class.text
    problem_class_attrib = problem_class.attrib
    problem_type = problem_class_attrib.get('severity')
    description = problem.find('description').text
    desc = "file: %s \nline: %s \nmodule: %s \nentry point: %s \ndescription: %s \n" % (file, line, module, entry_point, description)
    connection.createIssue('LOO', 'ran', problem_summary, desc,'Normal', 'Performance Problem')





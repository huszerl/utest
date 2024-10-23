import xml.etree.ElementTree as ET
import os

#
#   process_xml
#

def process_xml(tree):
    root = tree.getroot()

    ns = {'ute': 'urn:ute'}

    for street in root.findall('ute:streets/street', ns):
        streetname = street.attrib["name"]
        print("   "+streetname)
        out.write('''<li>''' + streetname + '''</li>''')
    return

#
#   MAIN
#

print ('START')
streetdict = {}
out = open('..\\gen\\UTEwien_streets.html', 'w', encoding="utf-8")
out.write('''<!!DOCTYPE html>
<html>
<head>
   <title>UTEwien streets</title>
   <link rel="icon" type="image/x-icon" href="..\\static\\logo.png">
</head>
<body>
   <h1>Street list for test purposes</h1>
   <ul>''')

for filename in os.listdir("../data"):
    if filename.endswith(".xml"):
        # parses all XML files present in data subfolder
        filename = "../data/" + filename
        print(filename, end=" ")
        try:
            tree = ET.parse(filename)
        except ET.ParseError:
            print("        PARSE ERROR\n^^^^^^^^^^^\n\n\n")
        print("PARSED")
        process_xml(tree)

out.write('''   </ul>
Back to <a href="..\\static\\index.html">main page</a>
</body>
</html>''')
print ('STOP')

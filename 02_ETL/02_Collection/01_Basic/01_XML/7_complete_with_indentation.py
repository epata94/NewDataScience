from xml.etree.ElementTree import Element,dump,SubElement,ElementTree

def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)

SubElement(note,"from").text = "Jani"

dummy = Element("dummy")
note.insert(1,dummy)
note.remove(dummy)

note.attrib["date"]="20120104"

SubElement(note,"heading").text = "Reminder"
SubElement(note,"body").text = "Don't forget me this weekend!"

indent(note)

dump(note)

ElementTree(note).write("note.xml")
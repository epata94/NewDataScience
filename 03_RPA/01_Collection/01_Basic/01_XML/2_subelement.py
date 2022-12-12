from xml.etree.ElementTree import Element,dump, SubElement

note = Element('note')

to = Element('to')
to.text ="Tove"
note.append(to)

SubElement(note,"from").text="Jani" #SubElement를 활용하여 자식 노드 추가
# 아래와 동일한 결과이다.
# from_tag = Element("from")
# from_tag.text = "Jani"
# note.append(from_tag)

dump(note)
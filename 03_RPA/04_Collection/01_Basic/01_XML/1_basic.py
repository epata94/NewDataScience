# <note date="20190722" method="gmail"> <= 노드 중 최상의 노드
# 	<to>Tove</to> <= 자식 노드
# 	<from>Jani</from> <= <from name="Jani/>
# 	<heading>Reminder</heading>
# 	<Body>Don't forget me this weekend!</body>
# </note>

from xml.etree.ElementTree import Element,dump

note = Element('note')

to = Element('to') #자식 노드
to.text ="Tove" #현재 엘리먼트(Tag)에 값 추가
note.append(to) #부모 노드에 자식노드 추가

dump(note)
dump(to)
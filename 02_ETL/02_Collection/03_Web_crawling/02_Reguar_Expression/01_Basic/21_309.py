import re
p=re.compile('Crow|Servo')
m = p.match('Nothing') #Not match
print(m)
m = p.match('Crow') #match
print(m)
m = p.match('Servo') #match
print(m)
m = p.match('CrowServo') #match
print(m)
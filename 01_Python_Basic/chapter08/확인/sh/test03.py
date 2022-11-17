# with open('life.txt','r') as file:
#
#     lines=file.readlines()
#     with open('life.txt','w') as file2:
#         lines[2]=lines[2].replace('java','python')
#
#         message=''.join(lines)
#
#         file2.write(message)

with open('life.txt','r') as file:
    text =  file.read()
    text = text.replace('java','python')
    with open('life2.txt', 'w') as file2:
        file2.write(text)

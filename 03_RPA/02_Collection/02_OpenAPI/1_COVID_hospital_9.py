from xml.etree.ElementTree import parse

column_list = ['adtFrDd','sgguNm', 'sidoNm', 'spclAdmTyCd', 'telno','yadmNm']
column_list = {'adtFrDd':'운영가능일자','sgguNm':'시군구명', 'sidoNm':'시도명', 'spclAdmTyCd':'구분코드', 'telno': '전화번호','yadmNm':'기관명'}

def xml_to_oracle(data_root, data_root_name):

    for row in data_root.iter(data_root_name):
        is_first = True
        for column in row.iter():
            if is_first:
                is_first = False
                continue
            sidoNm = row.find('sidoNm')
            pass




tree = parse('코로나19관련_병원정보_응답.xml')
data_root = tree.getroot().find('body').find('items')

xml_to_oracle(data_root, 'item')



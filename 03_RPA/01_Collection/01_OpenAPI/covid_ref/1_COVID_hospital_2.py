# STEP1] 응답 받은 XML 데이터의 원본을 에디터로 붙여 넣는다. (추천 Notepad++)
raw_xml='''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg></header><body><items><item><adtFrDd>20200220</adtFrDd><sgguNm>강동구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>02-517-1728</telno><yadmNm>(의)한국필의료재단 한국의원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>광명시</sgguNm><sidoNm>경기</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1899-1510</telno><yadmNm>의료법인 신원의료재단 신원의원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>관악구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>02-1877-8875</telno><yadmNm>에이치플러스 양지병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>동작구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1800-1114</telno><yadmNm>중앙대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>부산진구</sgguNm><sidoNm>부산</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>051-890-6114</telno><yadmNm>인제대학교부산백병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>중구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-200-5114</telno><yadmNm>경북대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>달서구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1577-6622</telno><yadmNm>계명대학교동산병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>남구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-623-8001</telno><yadmNm>영남대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>북구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-200-2000</telno><yadmNm>칠곡경북대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>창원시 성산구</sgguNm><sidoNm>경남</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>055-214-2000</telno><yadmNm>창원경상국립대학교병원</yadmNm></item></items><numOfRows>10</numOfRows><pageNo>1</pageNo><totalCount>102</totalCount></body></response>
'''
# STEP2] XML의 셈플 포멧을 파악한다.

xml_format='''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<response>
	<header>
	<resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
		<items>
			<item>
				<adtFrDd>20200220</adtFrDd><sgguNm>강동구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>02-517-1728</telno><yadmNm>(의)한국필의료재단 한국의원</yadmNm></item>
			<item><adtFrDd>20200220</adtFrDd><sgguNm>광명시</sgguNm><sidoNm>경기</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1899-1510</telno><yadmNm>의료법인 신원의료재단 신원의원</yadmNm></item>
			<item><adtFrDd>20200220</adtFrDd><sgguNm>관악구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>02-1877-8875</telno><yadmNm>에이치플러스 양지병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>동작구</sgguNm><sidoNm>서울</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1800-1114</telno><yadmNm>중앙대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>부산진구</sgguNm><sidoNm>부산</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>051-890-6114</telno><yadmNm>인제대학교부산백병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>중구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-200-5114</telno><yadmNm>경북대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>달서구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>1577-6622</telno><yadmNm>계명대학교동산병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>남구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-623-8001</telno><yadmNm>영남대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>북구</sgguNm><sidoNm>대구</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>053-200-2000</telno><yadmNm>칠곡경북대학교병원</yadmNm></item><item><adtFrDd>20200220</adtFrDd><sgguNm>창원시 성산구</sgguNm><sidoNm>경남</sidoNm><spclAdmTyCd>97</spclAdmTyCd><telno>055-214-2000</telno><yadmNm>창원경상국립대학교병원</yadmNm></item></items>
			<numOfRows>10</numOfRows>
			<pageNo>1</pageNo>
			<totalCount>102</totalCount>
	</body>
</response>
'''

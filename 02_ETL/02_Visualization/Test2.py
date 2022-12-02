import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

import random

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)


sex_range=['남성', '여성']
age_range=[20,21,22,23,24,25,26,27,28,29]
marrage_range=['독신','기혼','재혼']
income_range=['저소득자','3000만원대','4000만원대','5000만원대','6000만원대','고소득자']

MAX_RECORD=100000

sex_list=[]

# random.choices(range(0,len(sex_range)), weights=[0.35,0.65])

for i in range(MAX_RECORD):
    sex_list.append(
        sex_range[
            random.choices(range(0,len(sex_range)), weights=[0.35,0.65])[0]
        ]
    )

pd.Series(sex_list).value_counts()
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt
import pandas as pd

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)

xs_data1 = pd.Series([1,2,3,4])

df_data = pd.DataFrame()


plt.plot(xs_data1,[1,2,3,4],'r-',[1,2,3,4],[3,4,5,6],'v-')

# plt.plot([1,2,3,4],[1,2,3,4],[1,2,3,4],[3,4,5,6])
plt.xlabel('X축 라벨')
plt.ylabel('Y축 라벨')
plt.show()
# 목적: 여러 개의 그래프 그리기
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,1,1)
plt.plot([1,2,3,4],[1,2,3,4],'ro')
plt.subplot(2,1,2)
plt.plot([5,6,7,8],[5,6,7,8],'b')
plt.show()
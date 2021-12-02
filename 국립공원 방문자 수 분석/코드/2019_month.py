import pandas as pd
import matplotlib.pyplot as plt

name = '태백산'
data = pd.read_csv("visitors_per_month_2019.csv", header = 0, index_col = 0)
t_data = data.T[name][1:]
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('2019년 월별 ' + name + ' 국립공원 방문자 수 변화')
plt.plot(t_data,'gray', label = name)
plt.ylabel('방문자 수')
plt.legend()
plt.show()

# coding:utf-8
# 利用matplot库显示一些离散的点

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [item**3 for item in x_values]

# 设置每个点的x值和y值，点的大小s，点的边缘
# c是以哪些值作为颜色，cmap是颜色映射
plt.scatter(x_values,y_values,edgecolor='none',s=5,\
            c=y_values, cmap=plt.cm.Blues)

# set chart's title, add labels to axsis
plt.title("Triple Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Triple of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标抽的取值范围
plt.axis([0, 5500, 0, 5100**3])

# show me the chart
plt.show()
# or save the chart as a picture
# file saved in current working place,
# "tight" means cut the margin of picture
#plt.savefig("myfile.png",bbox_inches='tight')


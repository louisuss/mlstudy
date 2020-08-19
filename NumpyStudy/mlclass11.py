### matplotlib 그래프 표현

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = x ** 2 + x + 2 + np.random.randn(11)

print(x)
print(y)

### plot 함수 - 선 그래프
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.plot(x,y)
# plt.show()

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)
plt.plot(x, y)
# plt.show()

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)
plt.xlim(0, 20)
plt.ylim(0, 200)
plt.plot(x, y)
# plt.show()

### 점 그래프
plt.scatter(x,y)
plt.show()


### plot 함수 파라미터
# 색깔
plt.plot(x,y,'r')
plt.show()

plt.plot(x, y, '-.')
plt.show()

plt.plot(x, y, 'g^')
plt.show()

plt.plot(x, y, 'm:')
plt.show()

plt.plot(x,y, 'm:', linewidth=9)
plt.show()

plt.plot(x,y, color='black', linestyle='--', marker='^', markerfacecolor='blue', markersize=6)
plt.show()

### subplot
# - 구획을 구별하여 각각의 subplot에 그래프 출력
# - 여러 그래프를 한번에 그림
plt.subplot(2,2,1)
plt.plot(x,y,'r')

plt.subplot(2,2,2)
plt.plot(x,y,'g')

plt.subplot(2,2,3)
plt.plot(y,x,'k')

plt.subplot(2,2,4)
plt.plot(x,np.exp(x), 'b')
plt.show()

### hist 함수
# - histogram (막대그래프)

data = np.random.randint(1,100, size=200)
# bins 막대기 개수, alpha 투명도
plt.hist(data, bins=20, alpha=0.3)
plt.xlabel('data')
plt.ylabel('cnt')
plt.grid(True)
plt.show()
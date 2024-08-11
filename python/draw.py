import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk, Scale, HORIZONTAL, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 8x8x8 크기의 3차원 배열 생성
rgb_cube = np.zeros((8, 8, 8, 3), dtype=int)

# 초기 슬라이더 값
r_value = 0
g_value = 0
b_value = 0
z_value = 0

# Tkinter 초기화
root = Tk()
root.title("3D Dot Drawer")

# 도트 찍기 함수
def draw_dot(event):
    if event.xdata is not None and event.ydata is not None:
        x = int(np.clip(round(event.xdata), 0, 7))
        y = int(np.clip(round(event.ydata), 0, 7))
        z = z_value  # Z 좌표는 슬라이더로 조절
        if 0 <= x < 8 and 0 <= y < 8 and 0 <= z < 8:
            rgb_cube[x, y, z] = [r_value, g_value, b_value]  # 선택된 RGB 값으로 설정
            color = (r_value / 15, g_value / 15, b_value / 15)
            ax.scatter(x, y, z, c=[color], s=100)  # 색상은 정규화된 RGB 값으로 설정
            canvas.draw()

# RGB 및 Z 슬라이더 업데이트 함수
def update_r(val):
    global r_value
    r_value = int(val)

def update_g(val):
    global g_value
    g_value = int(val)

def update_b(val):
    global b_value
    b_value = int(val)

def update_z(val):
    global z_value
    z_value = int(val)

# 초기 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_zlim(0, 7)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 클릭 이벤트 연결
fig.canvas.mpl_connect('button_press_event', draw_dot)

# Tkinter 위젯 설정
r_slider = Scale(root, from_=0, to=15, orient=HORIZONTAL, label='Red', command=update_r)
g_slider = Scale(root, from_=0, to=15, orient=HORIZONTAL, label='Green', command=update_g)
b_slider = Scale(root, from_=0, to=15, orient=HORIZONTAL, label='Blue', command=update_b)
z_slider = Scale(root, from_=0, to=7, orient=HORIZONTAL, label='Z', command=update_z)

# 슬라이더 배치
r_slider.pack()
g_slider.pack()
b_slider.pack()
z_slider.pack()

# Matplotlib 캔버스 생성 및 배치
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Tkinter 메인 루프 시작
root.mainloop()

# 3차원 배열 출력
print(rgb_cube)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk, Scale, HORIZONTAL, VERTICAL, Frame, Button, Entry, Canvas, LEFT, RIGHT, Scrollbar, Y, Label
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
def on_canvas_click(event):
    x = int(event.x // (canvas_width // 8))
    y = 7 - int(event.y // (canvas_height // 8))  # y 좌표 변환
    z = z_value
    if 0 <= x < 8 and 0 <= y < 8 and 0 <= z < 8:
        rgb_cube[x, y, z] = [r_value, g_value, b_value]  # 선택된 RGB 값으로 설정
        update_plot()  # 플롯 업데이트

        # 팔레트에 색상 추가
        color_code = f'#{r_value*16:02X}{g_value*16:02X}{b_value*16:02X}'
        if color_code not in palette_dict:
            add_to_palette(color_code)

def update_plot():
    ax.cla()  # Clear the 3D plot
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    ax.set_zlim(0, 7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 3D 플롯에 점 추가
    for x in range(8):
        for y in range(8):
            for z in range(8):
                color = rgb_cube[x, y, z] / 15  # 색상은 정규화된 RGB 값으로 설정
                if np.any(color):  # 색상이 설정된 점만 추가
                    ax.scatter(x, y, z, c=[color], s=100, marker='o')  # 색상 업데이트

    canvas.draw()

# RGB 및 Z 슬라이더 업데이트 함수
def update_r(val):
    global r_value
    r_value = int(val)
    update_color_display()

def update_g(val):
    global g_value
    g_value = int(val)
    update_color_display()

def update_b(val):
    global b_value
    b_value = int(val)
    update_color_display()

def update_z(val):
    global z_value
    z_value = int(val)

def update_color_display():
    # 현재 색상 업데이트
    color_code = f'#{r_value*16:02X}{g_value*16:02X}{b_value*16:02X}'
    color_display.config(bg=color_code)

def clear_all():
    global rgb_cube
    rgb_cube = np.zeros((8, 8, 8, 3), dtype=int)
    update_plot()  # 플롯 업데이트

def format_array(arr):
    def format_layer(layer):
        return '{{{}}}'.format(
            ', '.join(
                '{{{}}}'.format(
                    ', '.join(map(str, row))
                ) for row in layer
            )
        )

    def format_array(arr):
        return '{{{}}}'.format(
            ', '.join(
                format_layer(layer)
                for layer in arr
            )
        )

    return format_array(arr)

def export_to_arduino():
    R = rgb_cube[:, :, :, 0]
    G = rgb_cube[:, :, :, 1]
    B = rgb_cube[:, :, :, 2]
    
    print("R[8][8][8] =", format_array(R))
    print("G[8][8][8] =", format_array(G))
    print("B[8][8][8] =", format_array(B))

def quit_application():
    root.destroy()

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def update_from_hex(event):
    hex_color = hex_entry.get()
    if len(hex_color) == 7 and hex_color[0] == '#':
        try:
            r, g, b = hex_to_rgb(hex_color)
            r_slider.set(r // 16)  # Normalize 0-255 to 0-15 for slider
            g_slider.set(g // 16)
            b_slider.set(b // 16)
            update_color_display()
        except ValueError:
            pass  # Invalid hex color code

def add_to_palette(color_code):
    if color_code not in palette_dict:
        # 팔레트에 색상 박스를 추가하고 클릭 시 색상으로 설정
        row = len(palette_dict) // num_columns
        column = len(palette_dict) % num_columns
        color_box = Canvas(palette_inner_frame, width=30, height=30, bg=color_code, highlightthickness=1, borderwidth=1, relief='solid')
        color_box.bind("<Button-1>", lambda e: set_color_from_palette(color_code))
        color_box.grid(row=row, column=column, padx=2, pady=2)  # 그리드에 배치

        # 팔레트의 스크롤 영역 업데이트
        palette_canvas.update_idletasks()
        palette_canvas.configure(scrollregion=palette_canvas.bbox("all"))

        # 색상 박스를 딕셔너리에 추가
        palette_dict[color_code] = color_box

def set_color_from_palette(color_code):
    global r_value, g_value, b_value
    r, g, b = hex_to_rgb(color_code)
    r_value, g_value, b_value = r // 16, g // 16, b // 16
    r_slider.set(r_value)
    g_slider.set(g_value)
    b_slider.set(b_value)
    update_color_display()

def draw_grid():
    grid_canvas.delete("all")
    cell_width = canvas_width // 8
    cell_height = canvas_height // 8
    for i in range(9):
        grid_canvas.create_line(i * cell_width, 0, i * cell_width, canvas_height, fill='black')
        grid_canvas.create_line(0, i * cell_height, canvas_width, i * cell_height, fill='black')

def update_palette_scrollregion(event):
    # 팔레트의 스크롤 영역을 캔버스의 바운스로 설정
    palette_canvas.configure(scrollregion=palette_canvas.bbox("all"))

# 초기 설정
fig = plt.figure(figsize=(8, 8))  # 정사각형 모양으로 설정
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_zlim(0, 7)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Matplotlib의 Axes3D.set_box_aspect 메서드를 사용하여 축 비율을 맞춤
ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1

# Tkinter의 Canvas 위젯을 이용해 격자판 그리기
canvas_width = 400
canvas_height = 400

# 메인 프레임 설정
main_frame = Frame(root, bg='#f0f0f0')
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# 3D 플롯 프레임
plot_frame = Frame(main_frame, bg='#ffffff', relief='sunken', borderwidth=2)
plot_frame.pack(side='left', padx=10, pady=10)

right_frame = Frame(main_frame)
right_frame.pack(side="right", padx=10, pady=10)

# Matplotlib 캔버스 생성 및 배치
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(side='left', fill='both', expand=True)

# 격자판 및 Z 슬라이더 프레임
grid_z_frame = Frame(right_frame, bg='#ffffff', relief='sunken', borderwidth=2)
grid_z_frame.pack(side='top', padx=10, pady=10)

# 격자판
grid_canvas = Canvas(grid_z_frame, width=canvas_width, height=canvas_height, bg='white')
grid_canvas.pack(side='left', fill='both', expand=True)

# Z 슬라이더
z_slider = Scale(grid_z_frame, from_=7, to=0, orient=VERTICAL, label='Z', command=update_z, length=canvas_height)
z_slider.pack(side='right', padx=5)

draw_grid()
grid_canvas_id = grid_canvas.bind("<Button-1>", on_canvas_click)

# 슬라이더 및 색상 표시 프레임
slider_color_frame = Frame(right_frame, bg='#ffffff', relief='sunken', borderwidth=2)
slider_color_frame.pack(side='bottom', fill='x', pady=5)

# RGB 슬라이더
slider_frame = Frame(slider_color_frame, bg='#ffffff')
slider_frame.pack(side='left', padx=10, pady=5)

# 색상 표시

color_frame = Frame(slider_frame, bg="#ffffff")
color_frame.pack(side="top")

color_display = Canvas(color_frame, width=30, height=30, bg='#000000', relief='solid')
color_display.pack(side='left', padx=10, pady=10)


# HEX 코드 입력 및 팔레트
import_frame = Frame(color_frame, bg='#ffffff')
import_frame.pack(side="left", padx=10, pady=10)

import_label = Label(import_frame, text="Import HEX code:", bg='#ffffff')
import_label.pack(side='left')

hex_entry = Entry(import_frame, width=10)
hex_entry.pack(side='left', padx=5)
hex_entry.bind("<Return>", update_from_hex)

r_slider = Scale(slider_frame, from_=0, to=15, orient=HORIZONTAL, label='Red', command=update_r, length=200)
r_slider.pack(side='top', padx=5)

g_slider = Scale(slider_frame, from_=0, to=15, orient=HORIZONTAL, label='Green', command=update_g, length=200)
g_slider.pack(side='top', padx=5)

b_slider = Scale(slider_frame, from_=0, to=15, orient=HORIZONTAL, label='Blue', command=update_b, length=200)
b_slider.pack(side='top', padx=5)


# 팔레트 설정
palette_frame = Frame(slider_color_frame, bg='#ffffff')
palette_frame.pack(side='bottom', fill='both', pady=5)

# 팔레트 캔버스 및 스크롤바 설정
palette_canvas = Canvas(palette_frame, bg='white')
palette_scrollbar = Scrollbar(palette_frame, orient='vertical', command=palette_canvas.yview)
palette_canvas.configure(yscrollcommand=palette_scrollbar.set)

palette_canvas.pack(side=LEFT, fill='both', expand=True)
palette_scrollbar.pack(side=RIGHT, fill=Y)

# 팔레트 프레임을 캔버스에 넣기
palette_inner_frame = Frame(palette_canvas)
palette_canvas.create_window((0, 0), window=palette_inner_frame, anchor='nw')

palette_inner_frame.bind("<Configure>", update_palette_scrollregion)

# 팔레트 색상 박스의 열 수 설정
num_columns = 10

# 색상 딕셔너리 초기화
palette_dict = {}

# 버튼 설정
button_frame = Frame(slider_color_frame, bg='#ffffff')
button_frame.pack(side='bottom', fill='x', pady=5)

clear_button = Button(button_frame, text="Clear", command=clear_all, width=12)
clear_button.pack(side='left', padx=5)

export_button = Button(button_frame, text="Export to Arduino", command=export_to_arduino, width=18)
export_button.pack(side='left', padx=5)

quit_button = Button(button_frame, text="Quit", command=quit_application, width=12)
quit_button.pack(side='left', padx=5)

# Tkinter 메인 루프 시작
root.mainloop()

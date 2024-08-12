import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk, Scale, HORIZONTAL, VERTICAL, Frame, Button, Entry, Canvas, LEFT, RIGHT, Scrollbar, Y, Label
from tkinter import filedialog  # 파일 대화 상자 추가
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import time
import random
import threading

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

def on_canvas_right_click(event):
    x = int(event.x // (canvas_width // 8))
    y = 7 - int(event.y // (canvas_height // 8))
    z = z_value
    if 0 <= x < 8 and 0 <= y < 8 and 0 <= z < 8:
        color = rgb_cube[x, y, z]
        if np.any(color):  # 색상이 설정된 점만 업데이트
            color_code = f'#{color[0]*16:02X}{color[1]*16:02X}{color[2]*16:02X}'
            r_slider.set(color[0])
            g_slider.set(color[1])
            b_slider.set(color[2])
            update_color_display()

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
                color = rgb_cube[x, y, z]  # 색상은 정규화된 RGB 값으로 설정
                if np.any(color):  # 색상이 설정된 점만 추가
                    ax.plot(x, y, z, c=f'#{color[0]*16:02X}{color[1]*16:02X}{color[2]*16:02X}', markersize=10, marker='o')  # 색상 업데이트

    # 현재 Z 층에 가상의 X, Y 선 추가 (격자 무늬)
    draw_grid_lines()

    canvas.draw()
    draw_grid()

def LED(x, y, z, red, green, blue):
    if 0 <= x < 8 and 0 <= y < 8 and 0 <= z < 8:
        rgb_cube[x, y, z] = [red, green, blue]
        update_plot()

def draw_grid_lines():
    z = z_value
    step = 1  # 격자의 간격

    # X 방향 선
    for y in range(0, 8, step):
        ax.plot([0, 7], [y, y], zs=z, color='black', linestyle='--', linewidth=2)

    # Y 방향 선
    for x in range(0, 8, step):
        ax.plot([x, x], [0, 7], zs=z, color='black', linestyle='--', linewidth=2)

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
    update_plot()  # Z 값 변경 시 플롯 업데이트
    draw_grid()

def update_color_display():
    # 현재 색상 업데이트
    color_code = f'#{r_value*16:02X}{g_value*16:02X}{b_value*16:02X}'
    color_display.config(bg=color_code)

def clear_all():
    global rgb_cube
    rgb_cube = np.zeros((8, 8, 8, 3), dtype=int)
    update_plot()  # 플롯 업데이트
    draw_grid()

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
    # 파일 저장 대화 상자 열기
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            R = rgb_cube[:, :, :, 0]
            G = rgb_cube[:, :, :, 1]
            B = rgb_cube[:, :, :, 2]
            
            file.write("R[8][8][8] = " + format_array(R) + ';' + "\n")
            file.write("G[8][8][8] = " + format_array(G) + ';' + "\n")
            file.write("B[8][8][8] = " + format_array(B) + ';' + "\n")

def import_from_arduino():
    # 파일 열기 대화 상자
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            global rgb_cube

            # R, G, B 배열 추출
            R_start = content.find("R[8][8][8] = ") + len("R[8][8][8] = ") 
            G_start = content.find("G[8][8][8] = ") + len("G[8][8][8] = ") 
            B_start = content.find("B[8][8][8] = ") + len("B[8][8][8] = ") 

            R_end = content.find(";", R_start)
            G_end = content.find(";", G_start)
            B_end = content.find(";", B_start)

            R_data = content[R_start:R_end].strip()
            G_data = content[G_start:G_end].strip()
            B_data = content[B_start:B_end].strip()

            def parse_data(data):
                # 중괄호를 대괄호로 바꾸고 데이터를 파싱합니다.
                data = data.replace('{', '[').replace('}', ']')
                # 배열 형태의 문자열을 eval로 평가하여 리스트로 변환합니다.
                return eval(data)

            R = parse_data(R_data)
            G = parse_data(G_data)
            B = parse_data(B_data)

            # rgb_cube 배열 업데이트
            rgb_cube[:, :, :, 0] = np.array(R)
            rgb_cube[:, :, :, 1] = np.array(G)
            rgb_cube[:, :, :, 2] = np.array(B)

            update_plot()  # 플롯 업데이트

def convert_arduino_function(arduino_code):
    # Find the function definition
    conversions = [
        (r'{', ''),
        (r'}', ''),
        (r'  ', '    '),
        (r'random\((\d+), (\d+)\)', r'random.randint(\1, \2 - 1)'),
        (r'random\((\d+)\)', r'random.randint(0, \1 - 1)'),
        (r"\bwhile\s*(.*?)(?=\s*[\n;#])", r"while \1:"),
        (r'\bmillis\(\)', 'time.time() * 1000'),
        (r'\bfor\s*\((\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\d+);\s*\1\+\+\)', r'for \1 in range(\2, \3):'),  # for 루프
        (r'\bfor\s*\((\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\d+);\s*\1\s*\-\-\)', r'for \1 in range(\2, \3, -1):'),
        (r"\bif\s*\(([^)]+)\)", r"if \1:"),
        (r'\bvoid (\w+)\(\)', r'def \1():'),
        (r"^([^()]*?)(\b\w+ = [^,]+)(, )", r"\1; "),
        (r'\bint \b', ''),  # Remove int declarations
        (r'//(.*)', r'#\1'),
        (r'\bdelay\((\d+)\)', r'time.sleep(\1 / 1000)'),
        (r',\s*$', '', re.MULTILINE),
    ]
    python_code = arduino_code
    for conversion in conversions:
        if len(conversion) == 2:
            pattern, replacement = conversion
            python_code = re.sub(pattern, replacement, python_code)
        elif len(conversion) == 3:
            pattern, replacement, flags = conversion
            python_code = re.sub(pattern, replacement, python_code, flags=flags)
        
    return python_code

def load_and_run_arduino_function():
    file_path = filedialog.askopenfilename(filetypes=[("Arduino Files", "*.ino")])
    if not file_path:
        return

    with open(file_path, 'r') as file:
        arduino_code = file.read()

    python_function = convert_arduino_function(arduino_code)

    if python_function:
        # Create a new function in Python
        exec(python_function, globals())
        #print(python_function)

def exe(event):
    func_name = export_entry.get()
    func_to_call = globals()[func_name]
    thread = threading.Thread(target=func_to_call)
    thread.start()

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
    step_x = canvas_width // 8
    step_y = canvas_height // 8

    for i in range(8):
        for j in range(8):
            color = rgb_cube[i, 7 - j, z_value]
            color_code = f'#{color[0]*16:02X}{color[1]*16:02X}{color[2]*16:02X}'
            grid_canvas.create_rectangle(i * step_x, j * step_y, (i + 1) * step_x, (j + 1) * step_y, fill=color_code, outline="gray", tags="grid")

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
grid_canvas_id = grid_canvas.bind("<Button-3>", on_canvas_right_click)

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
color_display.pack(side='left', pady=10)

# HEX 코드 입력 및 팔레트
import_frame = Frame(color_frame, bg='#ffffff')
import_frame.pack(side="left", pady=10)

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
palette_frame = Frame(slider_color_frame, bg='#ffffff', )
palette_frame.pack(side='bottom', fill='both', pady=5)

# 팔레트 캔버스 및 스크롤바 설정
palette_canvas = Canvas(palette_frame, bg='white', width=150, height=120)
palette_scrollbar = Scrollbar(palette_frame, orient='vertical', command=palette_canvas.yview)
palette_canvas.configure(yscrollcommand=palette_scrollbar.set)

palette_canvas.pack(side=LEFT, fill='both', expand=True)
palette_scrollbar.pack(side=RIGHT, fill=Y)

# 팔레트 프레임을 캔버스에 넣기
palette_inner_frame = Frame(palette_canvas)
palette_canvas.create_window((0, 0), window=palette_inner_frame, anchor='nw')

palette_inner_frame.bind("<Configure>", update_palette_scrollregion)

# 팔레트 색상 박스의 열 수 설정
num_columns = 6

# 색상 딕셔너리 초기화
palette_dict = {}

# 버튼 설정
button_frame = Frame(slider_color_frame, bg='#ffffff')
button_frame.pack(side='bottom', fill='x', pady=5)

button_top_frame = Frame(button_frame, bg='#ffffff')
button_top_frame.pack(side='top', fill='x', pady=5)

button_middle_frame = Frame(button_frame, bg='#ffffff')
button_middle_frame.pack(side='top', fill='x', pady=5)

button_bottom_frame = Frame(button_frame, bg='#ffffff')
button_bottom_frame.pack(side='top', fill='x', pady=5)

export_button = Button(button_top_frame, text="Import func from Arduino", command=load_and_run_arduino_function, width=22)
export_button.pack(side='left', padx=5)

export_entry = Entry(button_top_frame, width=8)
export_entry.pack(side='left', padx=5)
export_entry.bind("<Return>", exe)

export_button = Button(button_middle_frame, text="Export to Arduino", command=export_to_arduino, width=18)
export_button.pack(side='left', padx=5)

clear_button = Button(button_middle_frame, text="Clear", command=clear_all, width=12)
clear_button.pack(side='left', padx=5)

import_button = Button(button_bottom_frame, text="Import from Arduino", command=import_from_arduino, width=18)
import_button.pack(side='left', padx=5)

quit_button = Button(button_bottom_frame, text="Quit", command=quit_application, width=12)
quit_button.pack(side='left', padx=5)

# Tkinter 메인 루프 시작
root.mainloop()

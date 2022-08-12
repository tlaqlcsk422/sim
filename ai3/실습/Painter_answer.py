from tkinter import *
#윈도우 생성


window = Tk()
window.title("도형 그림판")

#프레임 생성
info_frame = Frame(window)
info_frame.grid(row=1, column=0, columnspan=2)

#마우스 엔트리창
mouse_text = StringVar()
mouse_entry = Entry(info_frame, textvariable = mouse_text, width=20)
mouse_entry.grid(row=0, column=0)

#텍스트 레이블
input_label = Label = Label(info_frame, text="     Text Input:")
input_label.grid(row=0, column=1)

#텍스트 엔트리창
input_text = StringVar()
input_entry = Entry(info_frame, textvariable=input_text, width=15)
input_entry.grid(row=0, column=2)

#캔버스 프레임 생성
canvas_frame = Frame(window, bd=2, bg='black')
canvas_frame.grid(row=2, column=0, columnspan=2, sticky=W)

#캔버스 생성
canvas = Canvas(canvas_frame, width=400, height=300, bg='white')

#x1, y1: 시작점
x1 = None
y1 = None

#x2, y2: 끝점
x2 = None
y2 = None

#선택=0, 점=1, 선=2, 네모=3, 원=4, 텍스트=5
draw_mode = 1
#색
draw_color = 'black'


#점 그리기 버튼 함수
def pointButton():
    global draw_mode
    draw_mode = 1

def lineButton():
    global draw_mode
    draw_mode = 2

def rectangleButton():
    global draw_mode
    draw_mode = 3

def circleButton():
    global draw_mode
    draw_mode = 4

def textButton():
    global draw_mode
    draw_mode = 5

#색 설정 함수
#white, black, red, yellow, blue
def whiteButton():
    global draw_color
    draw_color = 'white'

def blackButton():
    global draw_color
    draw_color = 'black'

def redButton():
    global draw_color
    draw_color = 'red'

def yellowButton():
    global draw_color
    draw_color = 'yellow'

def blueButton():
    global draw_color
    draw_color = 'blue'

def greenButton():
    global draw_color
    draw_color = 'green'

#마우스 왼쪽 버튼 클릭
def mouseLDown(event):
    global x1, y1, draw_mode
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Down")
    #점 그리기 모드
    if draw_mode == 1:
        canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill=draw_color)
    #글씨 쓰기 모드
    elif draw_mode == 5:
        canvas.create_text(event.x, event.y, text=input_text.get(), fill=draw_color)
    elif draw_mode >= 2 and draw_mode <=4:
        x1 = event.x
        y1 = event.y

#마우스를 움직일 때
def mouseMove(event):
    global x1, y1
    mouse_text.set("x:"+str(event.x)+" Y:"+str(event.y)+"Move")

#마우스 왼쪽 버튼을 뗄 때
def mouseLUp(event):
    global x1, y1
    mouse_text.set("x:"+str(event.x)+" Y:"+str(event.y)+"L UP")

    #선 그리기 모드
    if draw_mode == 2:
        canvas.create_line(x1, y1, event.x, event.y, width=2, fill=draw_color)
    #네모 그리기 모드
    elif draw_mode == 3:
        canvas.create_rectangle(x1, y1, event.x, event.y, width=2, fill=draw_color)
    #원 그리기 모드
    elif draw_mode == 4:
        canvas.create_oval(x1, y1, event.x, event.y, outline=draw_color)

def clearButton():
    canvas.delete("all")

#스타일 프레임 생성
style_frame = Frame(window)
style_frame.grid(row=0, column=0, sticky=W)

#스타일 선택 버튼 생성
#선택, 점그리기, 선그리기, 네모그리기, 원 그리기, 글씨쓰기
point_button = Button(style_frame, text=".", width=3, command=pointButton)
line_button = Button(style_frame, text="/", width=3, command=lineButton)
rectangle_button = Button(style_frame, text="□", width=3, command=rectangleButton)
circle_button = Button(style_frame, text="○", width=3, command=circleButton)
text_button = Button(style_frame, text="T", width=3, command=textButton)
clear_button = Button(style_frame, text="C", width=3, command=clearButton)


#색상 프레임 생성
color_frame = Frame(window)
color_frame.grid(row=0, column=1, sticky=E)

#색상 선택 버튼 생성
#흰색, 검은색, 빨간색, 파란색, 노랑색, 초록색
white_button = Button(color_frame, bg='white', width=3, command=whiteButton)
black_button = Button(color_frame, bg='black', width=3, command=blackButton)
red_button = Button(color_frame, bg='red', width=3, command=redButton)
blue_button = Button(color_frame, bg='blue', width=3, command=blueButton)
yellow_button = Button(color_frame, bg='yellow', width=3, command=yellowButton)
green_button = Button(color_frame, bg='green', width=3, command=greenButton)

#버튼 붙이기
point_button.grid(row=0, column=0, sticky=W)
line_button.grid(row=0, column=1, sticky=W)
rectangle_button.grid(row=0, column=2, sticky=W)
circle_button.grid(row=0, column=3, sticky=W)
text_button.grid(row=0, column=4, sticky=W)
clear_button.grid(row=0, column=5, sticky=W)

white_button.grid(row=0, column=0, sticky=E)
black_button.grid(row=0, column=1, sticky=E)
red_button.grid(row=0, column=2, sticky=E)
blue_button.grid(row=0, column=3, sticky=E)
yellow_button.grid(row=0, column=4, sticky=E)
blue_button.grid(row=0, column=5, sticky=E)


#마우스 이벤트 연결
canvas.bind("<Button-1>", mouseLDown)
canvas.bind("<Motion>", mouseMove)
canvas.bind("<ButtonRelease-1>", mouseLUp)
canvas.pack()

window.mainloop()



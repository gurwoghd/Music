import tkinter
import tkinter.font
import tkinter.filedialog
import tkinter.ttk
from pygame import mixer

window = tkinter.Tk()
mixer.init()

def initGUI(): # GUI 초기화
    global WIDTH, HEIGHT, isPaused, index

    WIDTH = 600
    HEIGHT = 700
    isPaused = False # 일시정지 되었는가?
    index = -1

    window.title("음악플레이어")
    window.geometry(str(WIDTH) + "x" + str(HEIGHT) + "+100+100")
    window.resizable(False, False)

def Setscreen():
    global WIDTH, nextButton, pastButton, pauseButton, listbox, music_list, countLabel

    music_list = []
    obj_width = 84

    font = tkinter.font.Font(family = "맑은 고딕", slant = "roman", size=30, weight = "bold")
    label = tkinter.Label(window, text="음악플레이어", font=font)
    countLabel = tkinter.Label(window, text="노래 개수 : 0")
    listbox = tkinter.Listbox(window, selectmode="extended", height=20, width=obj_width)
    pastButton = tkinter.Button(window, text="이전음악", overrelief="solid", width=27, command=PlayPast)
    nextButton = tkinter.Button(window, text="다음음악", overrelief="solid", width=27, command=PlayNext)
    pauseButton = tkinter.Button(window, text="재생/일시정지", overrelief="solid", width=27, command=Pause)
    addButton = tkinter.Button(window, text="추가", overrelief="solid", width=41, command=AddMusic)
    deleteButton = tkinter.Button(window, text="삭제", overrelief="solid", width=41, command=DeleteMusic)

    label.place(x=170, y=0)
    countLabel.place(x=0, y=80)
    listbox.place(x=0, y=100)
    pastButton.place(x=0, y=430)
    pauseButton.place(x=200, y=430)
    nextButton.place(x=400, y=430)
    addButton.place(x=0, y=460)
    deleteButton.place(x=303, y=460)

def PlayNext():
    global listbox, index, music_list

    if not IsEmpty():
        # 현재 음악이 마지막 항목이면 첫번째로 이동한다
        if index >= 0: listbox.itemconfig(index, {'bg' : 'white'})
        if index == len(music_list) - 1:
            index = 0
        else:
            index += 1
        currentMusic()

def PlayPast():
    global listbox, music_list, index

    if not IsEmpty():
        if index >= 0: listbox.itemconfig(index, {'bg' : 'white'})
        # 현재 음악이 첫번째 항목이면 마지막으로 이동한다.
        if index <= 0:
            index = len(music_list) - 1
        else:
            index -= 1
        currentMusic()

def Pause():
    global isPaused

    if isPaused:
        mixer.music.unpause()
        print("재생되었습니다.")
    else:
        mixer.music.pause()
        print("일시정지되었습니다.")
    isPaused = not isPaused

def DeleteMusic():
    global listbox, music_list, index

    selection_size = len(listbox.curselection()) # 선택된 항목들의 개수

    if selection_size: 
        selections = listbox.curselection()
        selection_start = selections[0]

        for s in range(selection_size): # listbox에서 제거
            listbox.delete(selection_start, selection_start)
        
        del music_list[selections[0]:selections[-1] + 1] # music_list에서 노래를 삭제
        
        # 삭제되는 항목 중에 현재 재생되고 있는 음악도 포함이 된다면
        if index in selections:
            mixer.music.stop()
            if index >= len(music_list):
                index = len(music_list) - 1
                currentMusic()
            else:
                currentMusic()
        
    else:
        print('선택된 노래 또는 리스트상에 노래가 없습니다')

    HowMany()

def AddMusic():
    global listbox, music_list

    lastest = listbox.size()
    music_list.append(tkinter.filedialog.askopenfilename())
    listbox.insert(lastest, music_list[-1])
    HowMany()

def HowMany(): # 노래 개수를 gui상에 보여주는 함수
    global music_list, countLabel

    countLabel.config(text="노래 개수 : " + str(len(music_list)))

def currentMusic():
    global listbox, index, music_list

    if index >= 0: # 음악이 1개라도 존재하여야 한다.
        listbox.itemconfig(index, {'bg' : 'orange'})
        mixer.music.load(music_list[index])
        mixer.music.play()
    else:
        print('노래가 없어요')

def IsEmpty():
    global music_list
    if len(music_list):
        return False
    else:
        return True

initGUI()
Setscreen()
window.mainloop()
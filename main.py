from tkinter import *

잔여시간 = 0
cnt = 0
timer_job = None     # after() id 저장(None이면 예약이 없는 상태)
running = False      # 타이머 동작 여부
#######
#after()는 일정 시간이 지난 뒤에 특정 함수를 실행하게 예약하는 역할 - 반환값이 작업의 id
#after_cancel()은 예약된 after()작업을 취소하는 역할 - after_cancel(작업id)
#######
def start_timer(): # 중복 예약 방지: 기존 타이머 취소
    global 잔여시간, timer_job, running, cnt
    #만약 예약이 걸려있으면 이것을 취소해라!
    if timer_job is not None:
        tk.after_cancel(timer_job)
    #다양한 변수 초기화
    잔여시간 = 5
    cnt = 0
    lb.config(text='현재 횟수:0')
    timer_label.config(text = f'Time left: {잔여시간} seconds')
    bt1.config(state=NORMAL, command = click)
    start_button.config(state=DISABLED)
    running=True
    #update_timer()호출
    update_timer()
    
def update_timer():
    global 잔여시간, timer_job, running, cnt
    #잔여시간(레이블) 띄우기
    timer_label.config(text=f'Time left: {잔여시간} seconds')
    #종료처리
    if 잔여시간 <=0:
        running=False
        bt1.config(state=DISABLED)
        lb.config(text='최종 횟수: '+str(cnt))
        timer_label.config(text='TIME OVER')
        start_button.config(state=NORMAL) #다시 시작 가능~~~
        timer_job = None
        return 
    #잔여시간 관리
    잔여시간 -=1
    timer_job = tk.after(1000, update_timer)
def click():
    global cnt
    if running:
        cnt += 1
        lb.config(text='현재 횟수: ' + str(cnt))

def reset():
    global cnt
    cnt = 0
    lb.config(text='현재 횟수: 0')

tk = Tk()
tk.geometry('500x220')
tk.title('주어진 시간동안 최대한 많이 클릭하세요!')

timer_label = Label(tk, text="Time left: 0 seconds", font=("Arial", 20), fg="black")
timer_label.pack(pady=10)

start_button = Button(tk, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

lb = Label(tk, text='현재 횟수: 0', fg='blue', font=("Arial", 16))
lb.pack()

bt1 = Button(tk, text='Button', command=click, state=DISABLED)
bt1.pack(padx=10, pady=6)

bt2 = Button(tk, text='reset', command=reset)
bt2.pack(padx=10, pady=6)

tk.mainloop()

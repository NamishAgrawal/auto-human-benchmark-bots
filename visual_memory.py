import pyautogui as py
import time as t
import keyboard as keyboard

t.sleep(0.5)
outbox_list = [(47, 146, 219),(48, 147, 221),(49, 150, 223),(50, 153, 226),(53, 160, 232),(54, 162, 235),(55, 165, 237)]
#square of min 70x7- pixels
#730,350 starting point
#721,336 
# #(255,255,255)
# height,width =480
def check_for_new():
    pixel_color = py.pixel(1610, 777)
    if pixel_color in outbox_list:
        return True
    else:
        return False

c =0
sequence =[(1610,777)]
start_time = t.perf_counter()

def clicking(r):
    global c
    global sequence
    global start_time
    # if(c >=k):
    #     return
    for x in range (0,480,r):
        for y in range(0,480,r):
            p = py.pixel(x+730,y+350)
            if(p == (255,255,255)):
                # print("hi")
                if((x+730,y+350) not in sequence):
                    sequence.append((x+730,y+350))
                    
                    print(sequence)
                start_time = t.perf_counter()
    
    end_time = t.perf_counter()
    elapsed_time = end_time - start_time
    if elapsed_time >= 1:
        for i in sequence:
            if i!=(1610,777):
                py.click(i[0],i[1])
                # print("clicked on ",i[0],i[1])
                t.sleep(0.01)
        sequence =[(1610,777)]
        start_time = t.perf_counter()

# def clicking(r):
#     global c
#     global sequence
#     global start_time
    
#     # Create a copy of the current sequence
#     current_sequence = list(sequence)
    
#     for x in range(0, 480, r):
#         for y in range(0, 480, r):
#             p = py.pixel(x + 730, y + 350)
#             if p == (255, 255, 255):
#                 if (x + 730, y + 350) not in current_sequence:
#                     current_sequence.append((x + 730, y + 350))
#                     print(current_sequence)
#                 start_time = t.perf_counter()
    
#     end_time = t.perf_counter()
#     elapsed_time = end_time - start_time
#     if elapsed_time >= 1:
#         for i in sequence:
#             if i != (1610, 777):
#                 py.click(i[0], i[1])
#                 t.sleep(0.01)
#         sequence = [(1610, 777)]  # Update the sequence to the current state
#         start_time = t.perf_counter()


while True:
    if keyboard.is_pressed('s'):
        break
    if check_for_new():
        print("new level:")
        print(sequence)
        sequence =[(1610,777)]

    if(c<=3):
        clicking(100)
    if c<=5 and c>3:
        clicking(90)
    else:
        clicking(70)
    c+=1
    # for x in range (0,480,65):
    #     for y in range(0,480,65):
    #         p = py.pixel(x+730,y+350)
    #         if(p == (255,255,255)):
    #             print("hi")
    #             sequence.append((x+730,y+350))
    #             start_time = t.perf_counter()
    
    # end_time = t.perf_counter()
    # elapsed_time = end_time - start_time
    # if elapsed_time >= 1:
    #     for i in sequence:
    #         if i!=(1610,777):
    #             py.click(i[0],i[1])
    #             print("clicked on ",i[0],i[1])
    #     sequence =[(1610,777)]
    #     start_time = t.perf_counter()
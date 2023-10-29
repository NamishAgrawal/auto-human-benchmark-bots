import pyautogui as py
import time as t
import keyboard as keyboard
t.sleep(0.5)

# the list of colors that change when a level is cleared:
outbox_list = [(47, 146, 219),(48, 147, 221),(49, 150, 223),(50, 153, 226),(53, 160, 232),(54, 162, 235),(55, 165, 237)]

#the list of colors that go on in the box when looking for sequence:
# inbox_list = [(255, 255, 255),(190, 204, 228),(75, 124, 190),(66, 119, 188),(59, 115, 187),(53, 113, 187)]
inbox_list = [(255, 255, 255),(190, 204, 228),(66, 119, 188)]


def check_for_sequence(x,y):
    if(py.pixel(x,y) in inbox_list):
        return True
    else :
        return False

def check_for_new():
    if py.pixel(1610, 777) in outbox_list:
        return True
    else:
        return False

coords = ((793,400),(952,390),(1110,395),(781,560),(946,557),(1114,566),(781,725),(943,778),(1111,722))
def print_coord(cord):
    print("the coord detected is ",coords.index(cord)+1)
    

def print_seq(seq):
    print("sequence is")
    seqq =[]
    for i in seq:
        if i!=(1610,777):
            seqq.append(coords.index(i)+1)
    print(seqq)

sequence =[(1610,777)]
c =0
round =1
start_time = t.perf_counter()

while keyboard.is_pressed('s') == False:
    if check_for_new():
        print("new level:")
        print_seq(sequence)
        sequence =[(1610,777)]
        print("c, round =",c,round)

    for coord in coords:
        if check_for_sequence(coord[0],coord[1]):
            if(sequence[-1]!=coord):
                print_coord(coord)
                sequence.append(coord)
                print_seq(sequence)
                c+=1
                print("c, round =",c,round)
                start_time = t.perf_counter()


        end_time = t.perf_counter()
        elapsed_time = end_time - start_time
      #it can also be if c== rounds, but sometimes due to packet loss or something, a new level is not detected, so it might break this:
        if elapsed_time >= 3:    
            t.sleep(1)
            if(round<len(sequence)-1):
                print("i am working")
                sub = sequence[-round:]
                print_seq(sub)
                for i in sub:
                    if i!=(1610,777):
                        py.click(i[0],i[1])
                        print("clicked on ",coords.index(i)+1)
            else:
                for i in sequence:
                    if i!=(1610,777):
                        py.click(i[0],i[1])
                        print("clicked on ",coords.index(i)+1)
            round +=1
            c=0
            start_time = t.perf_counter()
            sequence =[(1610,777)]

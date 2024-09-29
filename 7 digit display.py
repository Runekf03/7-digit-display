from machine import Pin
import time

Pin(14, Pin.OUT).on()
button = Pin(20, Pin.IN, Pin.PULL_UP)
x = 9
y = 0

digit_to_segments = {
    0: [0, 0, 0, 0, 0, 0, 1],
    1: [1, 0, 0, 1, 1, 1, 1],
    2: [0, 0, 1, 0, 0, 1, 0],
    3: [0, 0, 0, 0, 1, 1, 0],
    4: [1, 0, 0, 1, 1, 0, 0],
    5: [0, 1, 0, 0, 1, 0, 0],
    6: [0, 1, 0, 0, 0, 0, 0],
    7: [0, 0, 0, 1, 1, 1, 1],
    8: [0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 1, 0, 0],
}

pins = [6, 7, 8, 9, 10, 11, 12]

segments = [Pin(pin, Pin.OUT) for pin in pins]

def display(digit=0):
    if digit < 0 or digit > len(digit_to_segments) - 1:
        raise ValueError("Digit must be between 0 and {}".format(len(digit_to_segments) - 1))

    segments_state = digit_to_segments[digit]
    for segment, state in zip(segments, segments_state):
        segment.value(state)

    print("{}: {}".format(digit, digit_to_segments[digit]))
    
z = 0
def blink():
    global z
    if z == 1:
        Pin(13, Pin.OUT).on()
        z = 0
    else:
        z = 1
        Pin(13, Pin.OUT).off()
        
s = 0
def wait():
    for i in range(10):
        time.sleep(0.1)
        global s
        s = 1-(i/10)
        if  button.value() == 0:
            return
        
while True:
    while button.value() == 1:
        for cnt in range(y,10):
            display(cnt)
            x = cnt-1
            blink()
            wait()
            if  button.value() == 0:
                break
        y = 0
    time.sleep(s)
    blink()
    time.sleep(1)
    
    while button.value() == 1:
        for cnt in range(x,-1,-1):
            display(cnt)
            y = cnt + 1
            blink()
            wait()
            if button.value() == 0:
                break
        x = 9
    time.sleep(s)
    blink()
    time.sleep(1)      
#!/usr/bin/env python3

def loops():
    for i in range(10):
        print("i = " + str(i))
    
    values = range(10)
    i = len(values) - 1
    while i > 0:
        if values[i] == 3:
            break

        print("values[" + str(i) + "] = " + str(values[i]))
        i -= 1

    sum = 0
    for i in range(10):
        for j in range(4):
            if sum > 20:
                break
            sum += j

        print("sum = " + str(sum))

if __name__ == "__main__":
    loops()
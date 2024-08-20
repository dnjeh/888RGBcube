import time
import random

def folder():
    xx, yy, zz = 0, 0, 0
    pullback = [0] * 16
    state = 0
    backorfront = 7
    folderaddr = [-7, -6, -5, -4, -3, -2, -1, 0]
    LED_Old = [0] * 16
    oldpullback = [0] * 16
    ranx = random.randint(1, 16)
    rany = random.randint(1, 16)
    ranz = random.randint(1, 16)
    ranselect = 0
    bot, top, right, left, back, front, side = 0, 1, 0, 0, 0, 0, 0
    side_select = 0

    start = time.time()
    while time.time() - start < 10:  # 10초 동안 실행
        if top == 1:
            if side == 0:
                for yy in range(8):
                    for xx in range(8):
                        LED(7 - LED_Old[yy], yy - oldpullback[yy], xx, 0, 0, 0)
                        LED(7 - folderaddr[yy], yy - pullback[yy], xx, ranx, rany, ranz)
            if side == 2:
                for yy in range(8):
                    for xx in range(8):
                        LED(7 - LED_Old[yy], xx, yy - oldpullback[yy], 0, 0, 0)
                        LED(7 - folderaddr[yy], xx, yy - pullback[yy], ranx, rany, ranz)
            if side == 3:
                for yy in range(8):
                    for xx in range(8):
                        LED(7 - LED_Old[7 - yy], xx, yy + oldpullback[yy], 0, 0, 0)
                        LED(7 - folderaddr[7 - yy], xx, yy + pullback[yy], ranx, rany, ranz)
            if side == 1:
                for yy in range(8):
                    for xx in range(8):
                        LED(7 - LED_Old[7 - yy], yy + oldpullback[yy], xx, 0, 0, 0)
                        LED(7 - folderaddr[7 - yy], yy + pullback[yy], xx, ranx, rany, ranz)

        if right == 1:
            if side == 4:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy + oldpullback[7 - yy], 7 - LED_Old[7 - yy], xx, 0, 0, 0)
                        LED(yy + pullback[7 - yy], 7 - folderaddr[7 - yy], xx, ranx, rany, ranz)
            if side == 3:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, 7 - LED_Old[7 - yy], yy + oldpullback[yy], 0, 0, 0)
                        LED(xx, 7 - folderaddr[7 - yy], yy + pullback[yy], ranx, rany, ranz)
            if side == 2:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, 7 - LED_Old[yy], yy - oldpullback[yy], 0, 0, 0)
                        LED(xx, 7 - folderaddr[yy], yy - pullback[yy], ranx, rany, ranz)
            if side == 5:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy - oldpullback[yy], 7 - LED_Old[yy], xx, 0, 0, 0)
                        LED(yy - pullback[yy], 7 - folderaddr[yy], xx, ranx, rany, ranz)

        if left == 1:
            if side == 4:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy + oldpullback[yy], LED_Old[7 - yy], xx, 0, 0, 0)
                        LED(yy + pullback[yy], folderaddr[7 - yy], xx, ranx, rany, ranz)
            if side == 3:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, LED_Old[7 - yy], yy + oldpullback[yy], 0, 0, 0)
                        LED(xx, folderaddr[7 - yy], yy + pullback[yy], ranx, rany, ranz)
            if side == 2:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, LED_Old[yy], yy - oldpullback[yy], 0, 0, 0)
                        LED(xx, folderaddr[yy], yy - pullback[yy], ranx, rany, ranz)
            if side == 5:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy - oldpullback[yy], LED_Old[yy], xx, 0, 0, 0)
                        LED(yy - pullback[yy], folderaddr[yy], xx, ranx, rany, ranz)

        if back == 1:
            if side == 1:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, yy + oldpullback[yy], LED_Old[7 - yy], 0, 0, 0)
                        LED(xx, yy + pullback[yy], folderaddr[7 - yy], ranx, rany, ranz)
            if side == 4:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy + oldpullback[yy], xx, LED_Old[7 - yy], 0, 0, 0)
                        LED(yy + pullback[yy], xx, folderaddr[7 - yy], ranx, rany, ranz)
            if side == 5:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy - oldpullback[yy], xx, LED_Old[yy], 0, 0, 0)
                        LED(yy - pullback[yy], xx, folderaddr[yy], ranx, rany, ranz)
            if side == 0:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, yy - oldpullback[yy], LED_Old[yy], 0, 0, 0)
                        LED(xx, yy - pullback[yy], folderaddr[yy], ranx, rany, ranz)

        if bot == 1:
            if side == 1:
                for yy in range(8):
                    for xx in range(8):
                        LED(LED_Old[7 - yy], yy + oldpullback[yy], xx, 0, 0, 0)
                        LED(folderaddr[7 - yy], yy + pullback[yy], xx, ranx, rany, ranz)
            if side == 3:
                for yy in range(8):
                    for xx in range(8):
                        LED(LED_Old[7 - yy], xx, yy + oldpullback[yy], 0, 0, 0)
                        LED(folderaddr[7 - yy], xx, yy + pullback[yy], ranx, rany, ranz)
            if side == 2:
                for yy in range(8):
                    for xx in range(8):
                        LED(LED_Old[yy], xx, yy - oldpullback[yy], 0, 0, 0)
                        LED(folderaddr[yy], xx, yy - pullback[yy], ranx, rany, ranz)
            if side == 0:
                for yy in range(8):
                    for xx in range(8):
                        LED(LED_Old[yy], yy - oldpullback[yy], xx, 0, 0, 0)
                        LED(folderaddr[yy], yy - pullback[yy], xx, ranx, rany, ranz)

        if front == 1:
            if side == 0:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, yy - oldpullback[yy], 7 - LED_Old[yy], 0, 0, 0)
                        LED(xx, yy - pullback[yy], 7 - folderaddr[yy], ranx, rany, ranz)
            if side == 4:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy + oldpullback[yy], xx, 7 - LED_Old[yy], 0, 0, 0)
                        LED(yy + pullback[yy], xx, 7 - folderaddr[yy], ranx, rany, ranz)
            if side == 5:
                for yy in range(8):
                    for xx in range(8):
                        LED(yy - oldpullback[yy], xx, 7 - LED_Old[7 - yy], 0, 0, 0)
                        LED(yy - pullback[yy], xx, 7 - folderaddr[7 - yy], ranx, rany, ranz)
            if side == 1:
                for yy in range(8):
                    for xx in range(8):
                        LED(xx, yy + oldpullback[yy], 7 - LED_Old[7 - yy], 0, 0, 0)
                        LED(xx, yy + pullback[yy], 7 - folderaddr[7 - yy], ranx, rany, ranz)

        # Update pullback and other variables
        for x in range(8):
            oldpullback[x] = pullback[x]
            LED_Old[x] = folderaddr[x]

        pullback[0] += 1
        pullback[7] += 1
        pullback[2] += 1
        pullback[5] += 1

        folderaddr[0] = folderaddr[1]
        folderaddr[7] = folderaddr[6]
        folderaddr[2] = folderaddr[3]
        folderaddr[5] = folderaddr[4]

        if pullback[0] > 7:
            pullback[0] = 0
            folderaddr[0] = 0
        if pullback[7] > 7:
            pullback[7] = 0
            folderaddr[7] = 0
        if pullback[2] > 7:
            pullback[2] = 0
            folderaddr[2] = 0
        if pullback[5] > 7:
            pullback[5] = 0
            folderaddr[5] = 0

        time.sleep(1)
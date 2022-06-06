import cv2 as cv
import numpy as np

canvas = np.zeros((800, 600, 1), np.uint8)

canvas.fill(255)

x = 0
y = 0

drawing = False


# Mouse callback
def draw(event, current_x, current_y, flags, params):
    global x, y, drawing

    # Mouse down event
    if event == cv.EVENT_LBUTTONDOWN:
        x = current_x
        y = current_y
        drawing = True

    # Get xy pos
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.line(canvas, (current_x, current_y), (x, y), 0, thickness=2)

            x, y = current_x, current_y

    # mouse up event
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


cv.imshow('Draw', canvas)
cv.setMouseCallback('Draw', draw)

while True:
    cv.imshow('Draw', canvas)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
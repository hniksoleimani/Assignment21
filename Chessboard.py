import numpy as np
import cv2

#-------------------------------------------------------------------------------------


def chess(board):
    board_image[::2, ::2] = 1
    print(board_image)
    board_image[1::2, 1::2] = 1
    print(board_image)
    for i in range(chess_size[0]):
        for j in range(chess_size[1]):
            if  (i+j) % 2 == 0:
                board_image[(i * 100): ((i+1)*100), (j * 100):((j+1)*100)] = 255
    return(board_image)

#-------------------------------------------------------------------------------------

chess_size = (8 ,8)
board_image = np.zeros((800, 800), dtype=np.uint8)
varr=chess(board_image)

#-------------------------------------------------------------------------------------

cv2.imwrite('chess_board.jpg', varr)
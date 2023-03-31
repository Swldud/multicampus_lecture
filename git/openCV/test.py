import cv2

## 이미지 읽기
scr = cv2.imread('images/picture01.jpg')


# 이미지 처리/편집 코드
dst1 = cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY)
dst2 = scr.copy()
_ , dst2 = cv2.threshold(dst2, 127, 255, cv2.THRESH_BINARY)
                


# 이미지를 화면에 표시
cv2.imshow('scr', scr)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)


# 마무리_ 이미지를 끄기 위해서는 아무 키나 누르세요
cv2.waitKey(0) 
cv2.destroyAllWindows() 




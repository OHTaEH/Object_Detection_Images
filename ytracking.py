# pip uninstall opencv-python -> pip install opencv-python
# yolo가 에러 나는 경우가 많아서 uninstall-> install 필요

import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()


    if ret: # 카메라에 정보가 잘 들어갔으면
        results = model.track(frame, persist=True) # yolov8n.pt에서 학습된 데이터를 통해 트랙킹 시작
        frame = results[0].plot() # 현재 객체가 있는 바운딩박스를 그려줌

        cv2.imshow('tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
























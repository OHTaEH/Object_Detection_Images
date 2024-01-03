from ultralytics import YOLO

model = YOLO('runs/detect/train7/weights/best.pt')
results = model.predict(source= 'Fish.jpg', show =False, save= True)

for results in results:
    boxes = results.boxes
    print(boxes)

print(boxes.xywh) # 바운딩 박스 좌표
print(boxes.cls)  # 클래스 이름

from ultralytics import  YOLO

model = YOLO('yolov8n.pt')
results = model.track(source='https://youtu.be/Zgi9g1ksQHc')

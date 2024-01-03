import torch
import ultralytics
from ultralytics import YOLO
import os


if __name__ == '__main__':
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    print(torch.cuda.is_available())
    print(ultralytics.checks())

    model = YOLO('yolov8n.pt')
    model.train(data='runs/Fish-44/data.yaml', imgsz=640, batch=4, epochs=30)

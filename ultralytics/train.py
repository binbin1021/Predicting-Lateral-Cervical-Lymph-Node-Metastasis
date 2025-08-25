from ultralytics import YOLO
from ultralytics import RTDETR

if __name__ == '__main__':

    model = YOLO("yolov8s-seg.yaml")
    model.train(data='mydatasets.yaml', batch=16, epochs=150, imgsz=640, optimizer="SGD", task="segment")
    metrics = model.val(batch=1, split="val")
    metrics = model.val(batch=1, split="test")
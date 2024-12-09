from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt')

results = model(source="0", show=True, save=True)
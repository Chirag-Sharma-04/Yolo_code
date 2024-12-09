from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

# results = model('https://ultralytics.com/images/bus.jpg', show=True, save=True)

results = model(source="0", show=True, save=True)   #' 0' is for webcam
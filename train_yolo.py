from ultralytics import YOLO

# Initialize model
model = YOLO("yolov8m.yaml")

# Train
results = model.train(data="train_config.yaml", epochs=3, imgsz=(1392, 1040))  #, device="cpu")

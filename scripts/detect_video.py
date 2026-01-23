from ultralytics import YOLO

# Load model
model = YOLO("models/yolov8n.pt")

# Run detection on video
model(
    "data/videos/test.mp4",
    conf=0.5,
    save=True
)

print("Video detection selesai")

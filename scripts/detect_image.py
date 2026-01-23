from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

model("data/images/test.jpg", save=True, conf=0.5)

print("Deteksi selesai")

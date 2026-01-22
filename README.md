# YOLO Object Detection – Python Mini Project

Mini project ini bertujuan sebagai **pengenalan praktis penggunaan YOLO (You Only Look Once) untuk object detection menggunakan Python**.  
Project ini dibuat sebagai **fondasi sebelum integrasi ke Unity dan Meta Quest 3 (AR/VR)**.

Fokus utama:
- Memahami alur kerja YOLO secara aplikatif
- Menjalankan object detection pada gambar dan video
- Menyiapkan struktur project yang rapi dan scalable

---

## 🎯 Project Goals

- Menjalankan YOLOv8 menggunakan Python
- Melakukan object detection pada:
  - Gambar
  - Video
- Memahami output YOLO (bounding box, class, confidence)
- Menjadi dasar untuk:
  - Custom dataset training
  - Export model (ONNX)
  - Integrasi ke Unity / AR / VR

---

## 🛠️ Tech Stack

- Python 3.9+
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy

---

## 📁 Project Structure

yolo-object-detection-python/
│
├── README.md
├── requirements.txt
│
├── data/
│ ├── images/
│ │ └── test.jpg
│ └── videos/
│ └── test.mp4
│
├── models/
│ └── yolov8n.pt
│
├── scripts/
│ ├── detect_image.py
│ ├── detect_video.py
│ └── detect_camera.py # optional
│
└── outputs/
├── images/
└── videos/

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/yolo-object-detection-python.git
cd yolo-object-detection-python

### 2️⃣ Install Dependencies

Disarankan menggunakan virtual environment.
```bash
pip install -r requirements.txt


▶️ Usage
🔍 Object Detection on Image
```bash
python scripts/detect_image.py

Input:
```bash
data/images/test.jpg

Output:
Hasil deteksi otomatis tersimpan di folder runs/detect/

🎥 Object Detection on Video
```bash
python scripts/detect_video.py

Input:
```bash
data/videos/test.mp4

Output:
Video hasil deteksi dengan bounding box

🧠 YOLO Model
Project ini menggunakan:
YOLOv8 Nano (yolov8n.pt)

Model ini dipilih karena:
Ringan
Cepat
Cocok untuk eksperimen dan real-time application

📦 Model Export (Optional)
Model dapat diexport ke format lain (misalnya ONNX) untuk integrasi ke Unity.
```bash
yolo export model=models/yolov8n.pt format=onnx

🔮 Next Development Plan

 Custom object detection (custom dataset)
 Output deteksi dalam format JSON
 Integrasi dengan Unity
 Deployment ke Meta Quest 3 (Passthrough AR)

📌 Notes

Project ini tidak menggunakan webcam Meta Quest
Semua inference dilakukan menggunakan Python
Meta Quest 3 akan digunakan pada tahap integrasi selanjutnya

📄 License

This project is for educational and research purposes.

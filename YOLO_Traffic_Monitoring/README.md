# 🚦 YOLO-Based Traffic Monitoring System with NLP Chatbot

## 📌 Project Overview

This project is a YOLOv8-based Traffic Monitoring System that detects and counts different types of vehicles from traffic images and videos. It also includes an NLP-based chatbot that answers user queries related to traffic rules, road signs, and driving regulations. The application is built with a Streamlit frontend.

---

## ✨ Features

- 🚗 Vehicle detection using YOLOv8
- 📊 Vehicle counting
- 🖼️ Image upload and detection
- 🎥 Video upload and detection
- 🤖 NLP chatbot for traffic rules
- 📥 Download processed image/video
- 🖥️ User-friendly Streamlit interface

---

## 🛠️ Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- NLP (Rule-based Chatbot)

---

## 📂 Project Structure

```
YOLO_Traffic_Monitoring/
│
├── app.py
├── requirements.txt
├── README.md
│
├── detection/
│   ├── detector.py
│   └── counter.py
│
├── chatbot/
│   ├── chatbot.py
│   └── traffic_rules.txt
│
├── pages/
│   ├── 1_Prediction.py
│   └── 2_Chatbot.py
│
├── sample_images/
│
├── sample_videos/
│
└── outputs/
```

---

## 🚀 Installation

1. Clone the repository

```bash
git clone <repository-link>
```

2. Move into the project folder

```bash
cd YOLO_Traffic_Monitoring
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

---

## 📷 How to Use

### Home Page
- View the project overview and features.

### Prediction Page
- Choose **Image** or **Video**.
- Upload a traffic image or video.
- View detected vehicles and their counts.
- Download the processed output.

### Chatbot Page
Ask questions such as:
- What does a red signal mean?
- Is wearing a helmet compulsory?
- What is the speed limit?
- What is a zebra crossing?

---

## 🚘 Vehicle Classes Detected

- Car
- Motorcycle
- Bus
- Truck
- Bicycle

---

## 📸 Sample Output

- Vehicle detection with bounding boxes
- Vehicle count table
- Processed image/video download
- Traffic rules chatbot responses

---

## 👩‍💻 Author

**Britty S Biju**

---

## 📜 License

This project is developed for educational and academic purposes.
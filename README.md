# 🚨 Smart Surveillance System

An intelligent real-time surveillance system built using OpenCV and Flask.  
The system detects motion using computer vision techniques and provides a web-based dashboard to monitor captured events.

---

## 🔥 Features

- 🎯 Motion Detection using frame differencing  
- 📸 Automatic Image Capture  
- 🌐 Web Dashboard for monitoring  
- 🖥️ Responsive UI (works on laptop/mobile)  
- ⚡ Efficient storage (prevents continuous spam saving)  

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- Flask  
- HTML, CSS  

---

## 📂 Project Structure

```text
smart-surveillance/
│
├── main.py
├── app.py
├── logs.txt
│
├── modules/
│   ├── camera.py
│   ├── motion_detector.py
│   ├── human_detector.py
│   ├── alert_system.py
│   ├── logger.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── alerts/
```

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install opencv-python flask
```

### 2. Start motion detection
```bash
python main.py
```

### 3. Start dashboard server
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📸 Output

- Detects motion in real-time  
- Captures images when movement is detected  
- Displays saved images in dashboard  

---

## ⚠️ Important Note

This project is hardware-dependent (uses a webcam),  
so it runs locally. GitHub is used for code hosting only.

---

## 🎯 Future Improvements

- 🤖 Face Detection (AI-based)  
- 📧 Email Alert System  
- ☁️ Cloud Storage Integration  
- 🔐 Login Authentication System  

---

## 👨‍💻 Author

**Vivek Upadhyay**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

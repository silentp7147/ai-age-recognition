# 🎯 Age Recognition — AI Webcam App

A real-time age, gender & emotion detection app using your webcam, built with Python + DeepFace.

---

## 📋 Requirements

- Python 3.10
- A working webcam
- Windows PC

---

## 📦 First Time Setup (Do this only once)

Install the required libraries by running this in cmd:

```
pip install opencv-python deepface tf-keras Pillow requests
```

> ⚠️ First run will download AI model weights (~100MB). This is normal, just wait for it to finish.

---

## 🚀 How to Run

**Step 1** — Open the folder where `age_recognition.py` and `age_env` are saved together.

**Step 2** — Open CMD in that folder.
> Right-click inside the folder → "Open in Terminal" or type `cmd` in the address bar.

**Step 3** — Run the following commands one by one:

```
age_env\Scripts\activate
```
```
python age_recognition.py
```

✅ **Congrats! Your program is now running.**

---

## 🖥️ What You'll See

| Color | Meaning |
|-------|---------|
| 🟩 Green box | Male face detected |
| 🩷 Pink box | Female face detected |

Each detected face shows:
- **Gender** — Male / Female
- **Age range** — e.g. `Age: 17-23`
- **Emotion** — Happy, Sad, Neutral, etc.

---

## ❌ How to Exit

Press **Q** on your keyboard while the camera window is open.

The program will stop.

---

## 🗂️ Project Files

```
📁 your-folder/
├── age_recognition.py   ← main program
├── age_env/             ← Python virtual environment
└── README.md            ← this file
```

---

## ⚠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| `No module named 'cv2'` | Make sure you activated `age_env` first |
| Camera not opening | Check if another app is using your webcam |
| No face detected | Wait for model to finish downloading, improve lighting |
| Age seems off | DeepFace has ~5yr margin of error, this is normal |

---

## 👨‍💻 Built With

- [OpenCV](https://opencv.org/) — webcam & video processing
- [DeepFace](https://github.com/serengil/deepface) — AI face analysis
- Python 3.10

---

*Made with Python 🐍*

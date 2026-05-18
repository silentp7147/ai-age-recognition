# 🎯 Age Recognition — AI Webcam App

A real-time age, gender & emotion detection app using your webcam, built with Python + DeepFace.

---

## 📋 Requirements

- Python 3.10
- A working webcam
- Windows PC

---

## 📦 First Time Setup (Do this only once)

**Step 1** — Create a virtual environment:
```
py -3.10 -m venv env
```

**Step 2** — Activate it:
```
env\Scripts\activate
```

**Step 3** — Install the required libraries:
```
pip install opencv-python deepface tf-keras Pillow requests
```

> ⚠️ First run will download AI model weights (~100MB). This is normal, just wait for it to finish.

---

## 🚀 How to Run

**Step 1** — Open the folder where `age_recognition.py` is saved.

**Step 2** — Open CMD in that folder.
> Right-click inside the folder → "Open in Terminal" or type `cmd` in the address bar.

**Step 3** — Run the following commands one by one:

```
env\Scripts\activate
```
```
python age_recognition.py
```

✅ **Congrats! Your program is now running.**

> 💡 Every time you open a new terminal, activate `env` first before running the script!

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
├── env/                 ← Python virtual environment (create locally)
└── README.md            ← this file
```

---

## ⚠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| `No module named 'cv2'` | Run `env\Scripts\activate` first |
| `env\Scripts\activate` not found | Run `py -3.10 -m venv env` first to create it |
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

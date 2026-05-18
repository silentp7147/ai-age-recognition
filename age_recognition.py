import cv2
from deepface import DeepFace
import threading
from datetime import datetime

# ──────────────────────────────────────────
#  Config
# ──────────────────────────────────────────
FRAME_SKIP    = 8
FONT          = cv2.FONT_HERSHEY_SIMPLEX
GREEN         = (0, 220, 0)
RED           = (0, 0, 220)
GRAY          = (180, 180, 180)

# ──────────────────────────────────────────
#  Shared state
# ──────────────────────────────────────────
latest_results = []
analyzing      = False


def calibrate_age(raw):
    age = int(raw)
    if age < 20:
        age = max(13, age - 4)
    elif age < 30:
        age = max(15, age - 6)
    elif age < 50:
        age = max(20, age - 3)
    return age


def analyze_frame(frame):
    global latest_results, analyzing
    try:
        results = DeepFace.analyze(
            frame,
            actions=["age", "gender", "emotion"],
            enforce_detection=False,
            detector_backend="opencv",
            align=True,
            silent=True
        )
        if isinstance(results, dict):
            results = [results]

        parsed = []
        for r in results:
            gender  = r.get("dominant_gender", "?")
            region  = r.get("region", {})
            raw_age = r.get("age", 25)
            age     = calibrate_age(raw_age)
            emotion = r.get("dominant_emotion", "?").capitalize()
            parsed.append({
                "box":     (region.get("x", 0), region.get("y", 0),
                            region.get("w", 0), region.get("h", 0)),
                "age":     age,
                "gender":  "Male" if gender.lower() == "man" else "Female",
                "emotion": emotion,
            })
        latest_results = parsed
    except Exception:
        latest_results = []
    finally:
        analyzing = False


def draw_overlay(frame, results):
    for face in results:
        x, y, w, h = face["box"]
        age        = face["age"]
        emotion    = face["emotion"]
        age_label  = f"Age: {max(1, age - 3)}-{age + 3}"

        box_color = GREEN if face['gender'] == 'Male' else (255, 105, 180)
        cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

        # Corner accents
        c, t = 16, 2
        for px, py, dx, dy in [(x,y,1,1),(x+w,y,-1,1),(x,y+h,1,-1),(x+w,y+h,-1,-1)]:
            cv2.line(frame, (px, py), (px + dx*c, py), box_color, t)
            cv2.line(frame, (px, py), (px, py + dy*c), box_color, t)

        color = GREEN if face["gender"] == "Male" else (255, 105, 180)
        cv2.putText(frame, face["gender"], (x, y - 42), FONT, 0.62, color, 2, cv2.LINE_AA)
        cv2.putText(frame, age_label,      (x, y - 22), FONT, 0.62, color, 2, cv2.LINE_AA)
        cv2.putText(frame, emotion,        (x, y -  4), FONT, 0.52, color, 1, cv2.LINE_AA)

    return frame


def draw_hud(frame):
    h, w  = frame.shape[:2]
    now   = datetime.now().strftime("%H:%M:%S")
    count = f"Faces detected: {len(latest_results)}"

    cv2.rectangle(frame, (0, 0), (w, 34), (15, 15, 15), -1)
    cv2.putText(frame, "Age Recognition",
                (10, 22), FONT, 0.6, GREEN, 1, cv2.LINE_AA)
    cv2.putText(frame, now,
                (w - 90, 22), FONT, 0.55, GRAY, 1, cv2.LINE_AA)

    cv2.rectangle(frame, (0, h - 30), (w, h), (15, 15, 15), -1)
    cv2.putText(frame, count,
                (10, h - 10), FONT, 0.5, GRAY, 1, cv2.LINE_AA)
    cv2.putText(frame, "Q: Quit",
                (w - 70, h - 10), FONT, 0.45, GRAY, 1, cv2.LINE_AA)

    if not latest_results:
        cv2.putText(frame, "No face detected",
                    (20, 60), FONT, 0.75, RED, 2, cv2.LINE_AA)

    return frame


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    print("Webcam opened. Press Q to quit.")
    frame_count  = 0
    scan_running = False

    def run_scan(f):
        nonlocal scan_running
        analyze_frame(f)
        scan_running = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        if frame_count % FRAME_SKIP == 0 and not scan_running:
            scan_running = True
            threading.Thread(
                target=run_scan,
                args=(frame.copy(),),
                daemon=True
            ).start()

        display = draw_overlay(frame.copy(), latest_results)
        display = draw_hud(display)
        cv2.imshow("Age Recognition", display)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

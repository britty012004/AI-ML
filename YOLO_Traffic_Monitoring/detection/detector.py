from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck", "bicycle"]


# =========================
# IMAGE DETECTION
# =========================
def detect_vehicles(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    results = model(image, imgsz=640, verbose=False)

    vehicle_count = {}

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]

            if label in vehicle_classes:
                vehicle_count[label] = vehicle_count.get(label, 0) + 1

    annotated_image = results[0].plot()

    return annotated_image, vehicle_count


# =========================
# VIDEO DETECTION
# =========================
def detect_video(video_path, output_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Unable to open video.")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 30

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    vehicle_count = {}

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # YOLO Detection
        results = model(frame, imgsz=640, verbose=False)

        # Count vehicles
        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                label = model.names[class_id]

                if label in vehicle_classes:
                    vehicle_count[label] = vehicle_count.get(label, 0) + 1

        # Draw detections
        annotated_frame = results[0].plot()

        # Ensure frame size matches VideoWriter size
        annotated_frame = cv2.resize(
            annotated_frame,
            (width, height)
        )

        out.write(annotated_frame)

    cap.release()
    out.release()

    return output_path, vehicle_count
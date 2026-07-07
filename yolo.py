from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # nano model (fastest & lightweight)

# Load image

img = cv2.imread("lake.jpg")


# Run detection
results = model(img)

# Plot annotated image
annotated_img = results[0].plot()

annotated_img = cv2.resize(annotated_img, (600, 400))

# Show output
cv2.imshow("YOLO Image Detection", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
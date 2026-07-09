from detection.detector import detect_vehicles
import cv2

image_path = "sample_images/traffic1.jpg"

image, counts = detect_vehicles(image_path)

print("Vehicle Counts:")
print(counts)

cv2.imshow("Detected Vehicles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import pytesseract

# Set path to Tesseract executable (optional)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open video capture (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Perform OCR on the frame
    text_data = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)

    for i in range(len(text_data['text'])):
        # Extract coordinates and dimensions
        x, y, w, h = text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i]

        # Draw bounding box if confidence is high enough (adjust as needed)
        if int(text_data['conf'][i]) > 60:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text_data['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame with OCR text and bounding boxes
    cv2.imshow('OCR Real-Time', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

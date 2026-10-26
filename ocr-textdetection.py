import easyocr
import cv2
import matplotlib.pyplot as plt

# Load the OCR model
reader = easyocr.Reader(["en"], gpu=False)

# Read the document image
image_path = "sample_id_document.png"

results = reader.readtext(image_path)

# Load the image using OpenCV
image = cv2.imread(image_path)

# Process every detected text region
for result in results:

    coordinates = result[0]
    text = result[1]

    # Draw a rectangle around the text
    x1 = int(coordinates[0][0])
    y1 = int(coordinates[0][1])

    x2 = int(coordinates[2][0])
    y2 = int(coordinates[2][1])

    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

# Convert image colors for displaying with Matplotlib
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the result
plt.imshow(image)
plt.axis("off")
plt.show()
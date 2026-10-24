from pil import Image, ImageDraw
import matplotlib.pyplot as plt
image = Image.new("RGB", (800, 300), "white")
draw = ImageDraw.Draw(image)

draw.text(
    (30, 50),
    "Sample Identity Document",
    fill="black"
)

draw.text(
    (30, 100),
    "name: arjun sharma",
    fill="black"
)

draw.text(
    (30, 150),
    "dob: 01/01/1990",
    fill="black"
)

image.save("sample_id_document.png")
plt.imshow(image)
plt.axis("off")
plt.show()


import easyocr

reader = easyocr.Reader(["en"], gpu=False)

results = reader.readtext("sample_document.png")

for result in results:
    print("Text:", result[1])
    print("Confidence:", result[2])
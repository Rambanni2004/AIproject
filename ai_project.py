# Install OpenCV with extra modules (for sketch, watercolor, etc.)
!pip install opencv-contrib-python
# Upload an image file from your computer
from google.colab import files
uploaded = files.upload()
# Load the image using OpenCV
import cv2
from google.colab.patches import cv2_imshow
import numpy as np

filename = list(uploaded.keys())[0]
img = cv2.imread(filename)

# Check and resize if needed
if img is None:
    print("❌ Error: Could not load image.")
else:
    print("✅ Image loaded successfully!")

    # Resize if width > 800 px (to avoid lag or over-scaling)
    if img.shape[1] > 800:
        img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])), interpolation=cv2.INTER_AREA)
# Ask the user which style they want
print("\nChoose a style to apply:")
print("1. Cartoon")
print("2. Sketch")
print("3. Watercolor")
print("4. HDR (Hyper Realistic)")

style = input("Enter your choice (1/2/3/4): ").strip()
# Apply the selected style
if style == "1":
    # === CARTOON STYLE ===
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=9, C=2
    )
    color = cv2.bilateralFilter(img, d=12, sigmaColor=250, sigmaSpace=250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2_imshow(cartoon)
    cv2.imwrite("cartoon_output.jpg", cartoon)
    print("🎨 Cartoon image saved as cartoon_output.jpg")

elif style == "2":
    # === SKETCH STYLE ===
    gray_sketch, _ = cv2.pencilSketch(
        img,
        sigma_s=70,
        sigma_r=0.05,
        shade_factor=0.04
    )
    cv2_imshow(gray_sketch)
    cv2.imwrite("sketch_output.jpg", gray_sketch)
    print("✏ Sketch image saved as sketch_output.jpg")

elif style == "3":
    # === WATERCOLOR STYLE ===
    watercolor = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    cv2_imshow(watercolor)
    cv2.imwrite("watercolor_output.jpg", watercolor)
    print("🖌 Watercolor image saved as watercolor_output.jpg")

elif style == "4":
    # === HDR STYLE ===
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    cv2_imshow(hdr)
    cv2.imwrite("hdr_output.jpg", hdr)
    print("📸 HDR image saved as hdr_output.jpg")

else:
    print("⚠ Invalid choice. Please run the cell again and enter 1, 2, 3, or 4.")
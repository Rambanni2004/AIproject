AI Image Style Transfer - OpenCV Project
This project is a simple Python tool that transforms your personal photos into artistic styles with just a few clicks. Choose from Cartoon, Pencil Sketch, Watercolor, or HDR (Hyper Realistic) effects using the power of OpenCV’s advanced image processing. Perfect for students, hobbyists, or anyone looking to create amazing stylized images without deep technical knowledge!

Features
Cartoon: Turns your photo into a comic-style artwork.

Sketch: Produces pencil-drawn black-and-white sketch versions.

Watercolor: Applies a stylized watercolor painting look.

HDR: Enhances detail with a hyper-realistic HDR effect.

Automatic resizing for large images (max width: 800px) to prevent lag.

Requirements
Python 3.x

OpenCV-contrib-python (includes extra modules for stylization)

Google Colab (recommended) or any Jupyter Notebook environment

Numpy

How to Use
Clone this repository or download the ai_project.py file.

Open the script in Google Colab (best experience):

Open Google Colab

Upload ai_project.py and run all the cells.

Install dependencies
If not using Colab, install OpenCV with:

python
!pip install opencv-contrib-python
Upload your image when prompted (JPG, PNG, etc.)

Choose a style (type 1, 2, 3, or 4 when prompted):

1 for Cartoon

2 for Sketch

3 for Watercolor

4 for HDR

View and save results:
The stylized image will appear in the notebook and be saved as a file (e.g., cartoon_output.jpg) for download.

Example
bash
Choose a style to apply:
1. Cartoon
2. Sketch
3. Watercolor
4. HDR (Hyper Realistic)
Enter your choice (1/2/3/4): 1
✅ Cartoon image saved as cartoon_output.jpg
File Output
Each run saves your output as one of:

cartoon_output.jpg

sketch_output.jpg

watercolor_output.jpg

hdr_output.jpg

Notes
For the sketch and watercolor styles, OpenCV’s extra "contrib" modules are required.

Image uploads in Colab are supported via the simple upload dialog.

Troubleshooting
If you see Error: Could not load image.

Make sure the uploaded file is a valid image.

Check file name compatibility.

For any environment other than Google Colab:

Adapt or remove Colab-specific lines (like cv2_imshow).

License
This project is provided as-is for personal or educational use. Check OpenCV and Colab licenses for any restrictions.

Enjoy making art with AI & OpenCV!


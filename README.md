# OpenCV Computer Vision Project

A collection of Python scripts demonstrating various computer vision techniques using OpenCV (cv2). This project includes image processing, video capture, face detection, contour detection, and bitwise operations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Script Descriptions](#script-descriptions)
- [Haar Cascade Files](#haar-cascade-files)
- [Contributing](#contributing)

## Features

- **Face Detection**: Real-time face, eye, and smile detection using Haar Cascades
- **Image Processing**: Grayscale conversion, image flipping, and sharpening
- **Contour Detection**: Shape recognition (triangle, rectangle, pentagon, circle)
- **Bitwise Operations**: Demonstrate AND, OR, and NOT operations on images
- **Drawing Tools**: Interactive drawing on images with user input
- **Video Recording**: Webcam capture and video recording functionality

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Clone this repository or download the project files

2. Install the required dependencies:

```bash
pip install opencv-python numpy
```

3. Ensure all Haar Cascade XML files are in the same directory as the scripts:
   - `haarcascade_frontalface_default.xml`
   - `haarcascade_eye.xml`
   - `haarcascade_smile.xml`

## Project Structure

```
.
├── main.py                                 # Smart face detector with webcam
├── image.py                                # Image loading and grayscale conversion
├── video.py                                # Video recording from webcam
├── contour.py                              # Shape detection using contours
├── bitwise.py                              # Bitwise operations demonstration
├── drawaing.py                             # Interactive drawing on images
├── resize.py                               # Image flipping operations
├── sharpen.py                              # Image sharpening filter
├── haarcascade_frontalface_default.xml     # Face detection cascade
├── haarcascade_eye.xml                     # Eye detection cascade
└── haarcascade_smile.xml                   # Smile detection cascade
```

## Usage

### Smart Face Detector (main.py)

Real-time face detection with eye and smile recognition:

```bash
python main.py
```

- Press **'q'** to quit the application
- Detects faces and draws green rectangles around them
- Shows "Eyes Detected" when eyes are found
- Shows "Smiling" when a smile is detected

### Image Processing (image.py)

Load and convert images to grayscale:

```bash
python image.py
```

Follow the prompts to:
1. Enter the file path of your image
2. Choose to display or save the grayscale image

### Video Recording (video.py)

Record video from your webcam:

```bash
python video.py
```

- Records video and displays live feed
- Press **'q'** to stop recording
- Saves output as `my_video.mp4`

### Contour Detection (contour.py)

Detect and label shapes in images:

```bash
python contour.py
```

Note: Update the file path in the script to point to your image:
```python
image = cv2.imread("your_image_path.png")
```

Detects and labels:
- Triangles (3 corners)
- Rectangles (4 corners)
- Pentagons (5 corners)
- Circles (>5 corners)

### Bitwise Operations (bitwise.py)

Demonstrates bitwise operations on images:

```bash
python bitwise.py
```

Creates visual demonstrations of:
- AND operation
- OR operation
- NOT operation

### Interactive Drawing (drawaing.py)

Draw lines on images interactively:

```bash
python drawaing.py
```

Follow the prompts to:
1. Enter line coordinates (x1, y1, x2, y2)
2. Choose RGB color values
3. Set line thickness
4. Save or display the result

### Image Flipping (resize.py)

Flip images in different directions:

```bash
python resize.py
```

Note: Update the file path in the script:
```python
image = cv2.imread("your_image_path.png")
```

Displays:
- Original image
- Vertically flipped
- Horizontally flipped
- Both directions flipped

### Image Sharpening (sharpen.py)

Apply a sharpening filter to images:

```bash
python sharpen.py
```

Note: Update the file path in the script:
```python
image = cv2.imread("your_image_path.png")
```

Uses a custom kernel for edge enhancement.

## Script Descriptions

| Script | Description | Key Functions |
|--------|-------------|---------------|
| `main.py` | Real-time face, eye, and smile detection | `detectMultiScale()`, `VideoCapture()` |
| `image.py` | Basic image loading and grayscale conversion | `imread()`, `cvtColor()` |
| `video.py` | Webcam video recording | `VideoCapture()`, `VideoWriter()` |
| `contour.py` | Shape detection and labeling | `findContours()`, `approxPolyDP()` |
| `bitwise.py` | Bitwise operation demonstrations | `bitwise_and()`, `bitwise_or()`, `bitwise_not()` |
| `drawaing.py` | Interactive line drawing on images | `line()`, `imwrite()` |
| `resize.py` | Image flipping in multiple directions | `flip()` |
| `sharpen.py` | Image sharpening using convolution | `filter2D()` |

## Haar Cascade Files

The project uses pre-trained Haar Cascade classifiers for face detection:

- **haarcascade_frontalface_default.xml**: Detects frontal faces
- **haarcascade_eye.xml**: Detects eyes within face regions
- **haarcascade_smile.xml**: Detects smiles within face regions

These XML files contain the trained data for object detection and must be present in the working directory.

## Notes

- Some scripts have hardcoded file paths (e.g., `"AI\ML\minhas.png"`). Update these to match your directory structure.
- For Windows users, use backslashes `\` or raw strings `r"path\to\file"`. For Linux/Mac, use forward slashes `/`.
- Ensure your webcam is accessible for scripts using `cv2.VideoCapture(0)`.
- Press **'q'** to exit most video/webcam applications.

## Troubleshooting

**Image not found errors:**
- Verify the file path is correct
- Use absolute paths if relative paths don't work
- Check file extensions (.png, .jpg, etc.)

**Webcam not working:**
- Ensure no other application is using the camera
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` for external cameras
- Check camera permissions in your OS settings

**Haar Cascade errors:**
- Ensure all `.xml` files are in the same directory as the Python scripts
- Download missing cascades from the OpenCV GitHub repository

## Contributing

Feel free to fork this project and submit pull requests for improvements or additional features!

## License

This project is open source and available for educational purposes.

---

**Happy Coding! 🚀**

# CloakVision — Real-Time Invisible Cloak 🪄

A real-time computer vision project built with **Python, OpenCV, and NumPy** that creates an invisibility effect by detecting a specific cloak color and replacing it with the previously captured background.

## ✨ Demo

The application uses your webcam to detect the cloak in real time.

```text
             LIVE CAMERA
                  │
                  ▼
          ┌───────────────┐
          │ Capture Frame │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Convert to HSV│
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Detect Cloak  │
          │    Color      │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Create Mask   │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Replace with  │
          │  Background   │
          └───────┬───────┘
                  │
                  ▼
             🪄 INVISIBLE
```

## 🎯 Project Objective

The goal of this project is to demonstrate how basic computer vision techniques can be combined to create an **invisibility effect in real time**.

Instead of actually making an object invisible, the system:

1. Detects the cloak using its color.
2. Creates a mask around the detected region.
3. Removes the detected region from the current frame.
4. Replaces that region with the corresponding area from the captured background.

## 🛠️ Technologies Used

| Technology          | Purpose                     |
| ------------------- | --------------------------- |
| **Python**          | Core programming language   |
| **OpenCV**          | Image and video processing  |
| **NumPy**           | Array and matrix operations |
| **Webcam**          | Real-time video input       |
| **HSV Color Space** | Reliable color segmentation |

## 🧠 How It Works

### 1. Background Capture

Before the cloak enters the camera view, the application captures the background.

```text
Background
┌─────────────────────┐
│                     │
│      Empty Room     │
│                     │
└─────────────────────┘
```

This background is stored and later used to replace the cloak.

### 2. Color Detection

The camera continuously captures frames.

The frame is converted from **BGR to HSV** because HSV makes it easier to isolate a particular color range.

```text
BGR Image
   ↓
HSV Conversion
   ↓
Color Threshold
   ↓
Binary Mask
```

### 3. Mask Generation

The system identifies pixels belonging to the cloak.

```text
White → Cloak detected
Black → Everything else
```

This produces a binary mask representing the cloak region.

### 4. Background Replacement

The detected cloak region is replaced with the corresponding region from the previously captured background.

```text
Current Frame
      +
Background
      ↓
Mask-based replacement
      ↓
Invisible Cloak Effect
```

## 📁 Project Structure

```text
CloakVision/
│
├── src/
│   ├── invisible_cloak.py
│   ├── background_capture.py
│   ├── hsv_test.py
│   └── hsv_tuner.py
│
├── assets/
│   ├── demo.gif
│   └── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CloakVision.git
cd CloakVision
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Run:

```bash
python src/invisible_cloak.py
```

The webcam will open.

### Usage

1. Start the application.
2. Stay away from the camera initially.
3. Allow the application to capture the background.
4. Wear the selected cloak.
5. Move in front of the camera.
6. The cloak should appear invisible.

Press:

```text
Q
```

to exit the application.

## 📦 Requirements

`requirements.txt`:

```text
opencv-python
numpy
```

## 🔬 Computer Vision Concepts

This project demonstrates:

* Image processing
* Real-time video processing
* Color segmentation
* HSV color space
* Binary masking
* Morphological operations
* Background subtraction/replacement
* Pixel-level image manipulation
* Webcam processing

## 🚀 Future Improvements

The basic implementation can be extended with:

* [ ] Support for multiple cloak colors
* [ ] Automatic HSV calibration
* [ ] Improved noise removal
* [ ] Morphological mask refinement
* [ ] Real-time FPS monitoring
* [ ] GUI controls for color selection
* [ ] Video recording
* [ ] Better handling of lighting changes
* [ ] Person segmentation using deep learning
* [ ] Object detection integration
* [ ] Web-based interface

## 🌟 Advanced Version

A future version of CloakVision can move beyond simple color segmentation.

```text
                 CloakVision
                     │
        ┌────────────┴────────────┐
        │                         │
   Classical CV              Deep Learning
        │                         │
   HSV Detection           Person Segmentation
        │                         │
   Mask Generation         Object Detection
        │                         │
        └────────────┬────────────┘
                     │
              Background
               Replacement
                     │
                     ▼
             Invisible Effect
```

This would make the project more robust in different lighting conditions and with different backgrounds.

## 📊 Performance

The application is designed for **real-time webcam processing**, with performance depending on:

* Camera resolution
* Computer hardware
* Image-processing operations
* Lighting conditions

## ⚠️ Limitations

The basic version works best when:

* The cloak has a distinct color.
* The background remains relatively static.
* Lighting is reasonably consistent.
* The cloak color does not appear elsewhere in the scene.

Objects with a similar color to the cloak may also be detected and replaced.

## 📚 Learning Outcomes

Through this project, I learned how to:

* Process live video using OpenCV.
* Work with HSV color spaces.
* Create and manipulate image masks.
* Perform pixel-level image operations.
* Build real-time computer vision applications.
* Understand the fundamentals behind image segmentation.

## 👩‍💻 Author

**Anafa Sadiq**

B.Tech Information Technology

Interested in **Software Engineering, Computer Vision, AI, and Backend Development**.

## 📄 License

This project is created for educational and portfolio purposes.
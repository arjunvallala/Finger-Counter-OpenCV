# Finger Counter using OpenCV & MediaPipe

A real-time finger counting application built with **Python**, **OpenCV**, and **MediaPipe**. The project detects a hand through the webcam, identifies finger landmarks, counts the number of fingers raised, and displays the corresponding image overlay along with the detected count.

## Features

* Real-time hand detection
* Finger landmark detection using MediaPipe
* Counts fingers raised (0–5)
* Displays overlay image corresponding to detected finger count
* Live FPS display
* Modular implementation using a separate `HandTrackingModule.py`

## Project Structure

```
Finger-Counter-OpenCV/
│
├── FingerCounter.py
├── HandTrackingModule.py
├── requirements.txt
├── README.md
└── Fingers/
    ├── 0.png
    ├── 1.png
    ├── 2.png
    ├── 3.png
    ├── 4.png
    └── 5.png
```

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Finger-Counter-OpenCV.git
```

Move into the project folder:

```bash
cd Finger-Counter-OpenCV
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python FingerCounter.py
```

## How It Works

1. Captures video frames using OpenCV.
2. Detects the hand using MediaPipe Hands.
3. Extracts the 21 hand landmarks.
4. Determines whether each finger is open or closed.
5. Counts the total number of raised fingers.
6. Displays the corresponding overlay image and finger count on the webcam feed.

## Notes

* Ensure the `Fingers` folder contains images named:

  * `0.png`
  * `1.png`
  * `2.png`
  * `3.png`
  * `4.png`
  * `5.png`
* Good lighting improves detection accuracy.
* Press **Q** to exit the application.

## Future Improvements

* Support multiple hands simultaneously
* Recognize additional hand gestures
* Volume and brightness control using gestures
* Virtual drawing application
* Gesture-based presentation controller

## Acknowledgements

* OpenCV
* MediaPipe

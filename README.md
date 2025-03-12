# ✋ Mouse control with hand gestures!

A Python program that lets you control your computer's mouse using simple hand gestures captured from your webcam. The application leverages computer vision and hand tracking with MediaPipe, along with PyAutoGUI for mouse control.

## ⭐ Introduction

This project uses your webcam to capture real-time video, detects hand landmarks with MediaPipe, and uses these landmarks to move the mouse pointer and perform click actions via PyAutoGUI. This program tracks the users thumb and a pinch action will result in a mouse click.

## 🔧 Installation

### Prerequisites
- Python 3.x installed on your system.
- A working webcam.
- Basic knowledge of command-line operations.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DhirenGitHub/hand-gesture-mouse-control.git
   cd hand-gesture-mouse-control
2. **Install Required Packages**

   Install the necessary Python libraries using pip:
   
   ```bash
   pip install opencv-python mediapipe pyautogui

## 💡 Use Cases
- Accessibility Enhancements: Provide alternative mouse control for users with mobility challenges.
- Interactive Presentations: Control slide navigation and multimedia playback using hand gestures.
- Smart Environments: Integrate gesture control for smart home or robotics applications, creating hands-free interfaces.

## 🤔 Code Overview
- This program utilizes the MediaPipe library's Hand Landmark Model to get all landmarks of the hand visible on the webcam as shown below
  
  ![image](https://github.com/user-attachments/assets/b280ca8b-51af-4a28-9ae2-d469b0afc94b)

- OpenCV is used to access the user's webcam to get live input and is fed into the Hand Landmark model

  ```bash
  success, img = webcam.read()
  if not success:
      break

  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(img_rgb)
  
- If a hand is detected by the program it will draw lines connecting the hand landmarks as annotation.

  ```bash
  mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

  ...

  cv2.putText(img, f"Index Finger: ({indexfin_x}, {indexfin_y})", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

  cv2.circle(img, (indexfin_x, indexfin_y), 10, (255, 0, 0), -1) #draws a circle on index finger
  cv2.circle(img, (thumb_x, thumb_y), 10, (255, 0, 0), -1)  #draws a circle on thumb

- Then PyAutoGUI to move the mouse depending on the location of the thumb captured by the webcam. It will make an x, y calculation to make accurate mouse movements throughout the user's display. It also tracks the index finger and checks if the distance between the thumb and index finger is less than 35 pixels (basically means the index finger and thumb are in contact and the user is pinching), if so the program will perform a click operation.

  ```bash
  pyautogui.moveTo(1920 - ((1920 / 600) * thumb_x), (1080 / 300) * thumb_y)
  
  distance_for_click = math.sqrt((indexfin_x - thumb_x)**2 + (indexfin_y - thumb_y)**2)
  
  if distance_for_click < 35:
   pyautogui.leftClick()

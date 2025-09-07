# Face Recognition Attendance System

A Face Recognition based attendance system using Python, OpenCV, and Tkinter.

## Description

This project is a desktop application that uses face recognition to automate the process of marking attendance. It captures images, trains a model, and then recognizes faces to mark attendance in a CSV file. The user interface is built with Tkinter.

## Features

- **User-friendly Interface:** Simple and intuitive GUI built with Tkinter.
- **Register New Students:** Easily enroll new students by capturing their images.
- **Train Model:** Train the face recognition model with the captured images.
- **Automatic Attendance:** Mark attendance automatically by recognizing faces in real-time.
- **View Attendance:** View the attendance records in a tabular format.
- **CSV Reports:** Attendance is stored in a CSV file for each subject.

## Technologies Used

- **Python:** The core programming language.
- **OpenCV:** For image processing and face detection.
- **Tkinter:** For the graphical user interface.
- **Pandas:** For data manipulation and CSV handling.
- **Numpy:** For numerical operations.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Tejascodex001/face_recognize_attendance_system.git](https://github.com/Tejascodex001/face_recognize_attendance_system.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd face_recognize_attendance_system
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    ```bash
    python attendance.py
    ```

2.  **Register a new student:**
    - Click on the "Register New Student" button.
    - Enter the student's ID and name.
    - Click on "Take Image" to capture 50 images of the student's face.

3.  **Train the model:**
    - Click on the "Train Image" button to train the face recognition model.

4.  **Mark attendance:**
    - Click on the "Automatic Attendance" button.
    - Enter the subject name.
    - The system will open the camera and mark attendance when a registered face is detected.

5.  **View attendance:**
    - Click on the "View Attendance" button to see the attendance records.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

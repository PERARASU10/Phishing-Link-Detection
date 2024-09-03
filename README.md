# Brainwave-intern-tasks

# Phishing URL Detection Tool

This project is a machine learning-based tool designed to detect phishing URLs. It employs a RandomForestClassifier to predict whether a given URL is phishing or legitimate. The tool is equipped with a user-friendly graphical interface (GUI) built using tkinter, making it easy for users to input URLs and receive predictions in real-time.

## Features

    Machine Learning Model: Trained using a Random Forest classifier on a dataset of phishing and legitimate URLs.
    
    GUI Interface: Provides a clean and intuitive interface to input URLs and get predictions.
    
    Basic Animation: Adds a simple animation effect to enhance the user experience when displaying the prediction results.

## Installation
 ## Clone the Repository
```
git clone https://github.com/PERARASU10/Brainwave_matrix_intern.git
cd phishing-url-detection
```

## Install Dependencies

Ensure you have Python 3.6+ installed on your machine.

Install the required Python packages using pip:

```
pip install pandas scikit-learn tkinter

```

## Dataset

Ensure that your dataset file (in CSV format) is located in the project directory. Update the file_path variable in the scanner.py script to point to your dataset file.

## Running the Tool

You can start the phishing detection tool by executing the following command:
```
python scanner.py
```
This will launch the GUI, allowing you to enter a URL and receive a prediction on whether the URL is likely phishing or legitimate.

## Usage

    Launch the Tool: Run python scanner.py.
    Enter URL: Type the URL you want to check in the text field.
    Get Prediction: Click "Predict" to see if the URL is classified as phishing or legitimate.

## Screenshots

Here’s what the interface looks like:


## Troubleshooting

    File Not Found Error: Ensure that the file_path in scanner.py correctly points to your dataset file.
    
    Missing Dependencies: Run pip install -r requirements.txt to ensure all dependencies are installed.
    
    GUI Not Displaying Properly: Check if you have tkinter installed, as it is required for the GUI.

## Contact

If you have any questions or suggestions, feel free to contact me at mperarasu3116@gmail.com

## Acknowledgments

    The dataset used for training the model.
    The Python community for providing the necessary libraries and resources.
    PERARASU M - Author and maintainer of the project.

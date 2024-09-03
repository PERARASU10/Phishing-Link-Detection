import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from urllib.parse import urlparse
import re
import tkinter as tk
from tkinter import ttk, messagebox

# Load dataset
file_path = 'dataset_link_phishing.csv'  # Update with your correct file path
data = pd.read_csv(file_path, low_memory=False)

# Drop irrelevant columns
data = data.drop(columns=['Unnamed: 0', 'url'])

# Convert 'status' to numerical
data['status'] = data['status'].map({'phishing': 1, 'legitimate': 0})

# Handle non-numeric columns (convert or drop)
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = pd.to_numeric(data[col], errors='coerce')
        
# Drop columns with NaN values after conversion or fill NaNs with a value
data = data.dropna()

# Define features and target
X = data.drop(columns=['status'])
y = data['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Function to extract features from URL
def extract_features_from_url(url):
    features = {}
    parsed_url = urlparse(url)
    
    features['url_length'] = len(url)
    features['hostname_length'] = len(parsed_url.netloc)
    features['ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0
    features['total_of.'] = url.count('.')
    features['total_of-'] = url.count('-')
    features['total_of@'] = url.count('@')
    features['total_of?'] = url.count('?')
    features['total_of&'] = url.count('&')
    features['total_of='] = url.count('=')
    features['total_of_'] = url.count('_')
    features['total_of~'] = url.count('~')
    features['total_of%'] = url.count('%')
    features['total_of/'] = url.count('/')
    features['total_of*'] = url.count('*')
    features['total_of:'] = url.count(':')
    features['total_of,'] = url.count(',')
    features['total_of;'] = url.count(';')
    features['total_of$'] = url.count('$')
    features['total_of_www'] = url.count('www')
    features['total_of_com'] = url.count('.com')
    features['total_of_http_in_path'] = url.count('http')
    features['https_token'] = 1 if 'https' in parsed_url.scheme else 0
    
    # Add other feature extraction as needed
    # Defaulting missing features to 0
    for col in X.columns:
        if col not in features:
            features[col] = 0
            
    return pd.DataFrame([features])

# Predict URL
def predict_url(url):
    features = extract_features_from_url(url)
    
    # Predict using the trained model
    prediction = model.predict(features)
    
    # Output the result
    if prediction[0] == 1:
        return "The URL is likely PHISHING. Don't touch it."
    else:
        return "The URL is likely LEGITIMATE."

# GUI Implementation
def on_predict_button_click():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL.")
        return
    
    result = predict_url(url)
    result_label.config(text=result, foreground="green" if "LEGITIMATE" in result else "red")
    animate_result()

def animate_result():
    for i in range(0, 11):
        result_label.place_configure(relx=0.5, rely=(0.6 + i/100))
        root.update()
        root.after(30)

# Create the main application window
root = tk.Tk()
root.title("Phishing URL Detection")

# Set the window size and center it on the screen
window_width, window_height = 400, 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Set the background color
root.configure(bg="#f0f0f0")

# Create and place the URL input label and entry field with styles
url_label = ttk.Label(root, text="Enter URL:", font=("Arial", 12))
url_label.pack(pady=10)
url_entry = ttk.Entry(root, width=50, font=("Arial", 10))
url_entry.pack(pady=10)

# Create and place the Predict button with styles
predict_button = ttk.Button(root, text="Detect", command=on_predict_button_click)
predict_button.pack(pady=20)

# Create and place a label to display the result
result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()

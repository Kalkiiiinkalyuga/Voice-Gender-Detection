import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk

class VoiceGenderRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Gender Recognition App")

        self.label = tk.Label(root, text="Voice Gender Recognition", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.record_button = tk.Button(root, text="Record Voice", command=self.record_voice)
        self.record_button.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse Audio File", command=self.browse_audio_file)
        self.browse_button.pack(pady=10)

        self.predict_button = tk.Button(root, text="Predict Gender", command=self.predict_gender)
        self.predict_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        # Initialize model attribute
        self.model = self.create_model()

    def record_voice(self):
        file = "recorded_voice.wav"
        # Replace this line with your actual record_to_file logic
        print(f"Recording voice to {file}")

    def browse_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.audio_file_path = file_path
            self.result_label.config(text=f"Selected Audio File: {file_path}")

    def preprocess_audio(self, file_path):
        # Replace this line with your actual extract_feature logic
        features = np.random.rand(1, 10)  # Placeholder for features
        return features

    def create_model(self):
        # Replace this with your actual model creation logic
        model = tf.keras.Sequential([
            # Your model layers go here
            # Example: tf.keras.layers.Dense(64, activation='relu', input_shape=(input_size,))
        ])
        return model

    def predict_gender(self):
        if hasattr(self, 'audio_file_path') or os.path.isfile("recorded_voice.wav"):
            if hasattr(self, 'audio_file_path'):
                file_path = self.audio_file_path
            else:
                file_path = "recorded_voice.wav"

            # Preprocess the audio
            features = self.preprocess_audio(file_path)

            # Predict the gender
            male_prob = self.model.predict(features)[0][0]
            female_prob = 1 - male_prob
            gender = "male" if male_prob > female_prob else "female"

            # Show the result
            self.result_label.config(text=f"Result: {gender}\n"
                                          f"Probabilities: Male: {male_prob*100:.2f}% Female: {female_prob*100:.2f}%")
        else:
            self.result_label.config(text="Please record voice or select an audio file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceGenderRecognitionApp(root)
    root.mainloop()

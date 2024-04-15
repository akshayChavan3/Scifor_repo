import tkinter as tk
from tkinter import PhotoImage

# Create the main window
root = tk.Tk()
root.title("Image Display")

# Load the image file (replace 'your_image_file.png' with your actual image file)

# image_path = r"C:\Users\sures\OneDrive\Desktop\istockphoto-1420676204-612x612.jpg"

background_image = PhotoImage(file= r"C:\Users\sures\OneDrive\Desktop\istockphoto-1420676204-612x612.jpg")


image_path = "C:\\Users\\sures\\OneDrive\\Desktop\\Asiatic-lion-Indias-conservation-success-story-scaled.webp"

background_image = PhotoImage(file="C:\\Users\\sures\\OneDrive\\Desktop\\Asiatic-lion-Indias-conservation-success-story-scaled.webp")

image_path = "C:\\Users\\sures\\OneDrive\\Desktop\\360_F_318477235_qtvHD7hAYa8V4Z7cIejqhqIhWlS9hQ6N.jpg"

background_image = PhotoImage(file="C:\\Users\\sures\\OneDrive\\Desktop\\360_F_318477235_qtvHD7hAYa8V4Z7cIejqhqIhWlS9hQ6N.jpg")

image_path = "C:\\Users\\sures\\OneDrive\\Desktop\\download (1).jpg"

background_image = PhotoImage(file="C:\\Users\\sures\\OneDrive\\Desktop\\download (1).jpg")

# Create a label to display the image
image_label = tk.Label(root, image=background_image)
image_label.pack()

# Start the Tkinter event loop
root.mainloop()

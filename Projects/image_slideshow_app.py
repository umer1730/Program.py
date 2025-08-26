from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Image Slideshow Viewer")

# Image paths
image_paths = [
    r"d:\abc\game\New folder\facebook.png",
    r"d:\abc\game\New folder\insatagram.png",
    r"d:\abc\game\New folder\787330c2-1582-48c9-a927-6f8310c33e05-cover.png",
]

# Resize and load images
image_size = (500, 500)  # smaller size for performance and fitting
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Cycle through images
slideshow = cycle(photo_images)

# Label to display image
label = tk.Label(root)
label.pack()

# Slideshow function using .after()
def update_image():
    next_image = next(slideshow)
    label.config(image=next_image)
    root.after(3000, update_image)  # call again after 3 seconds

# Button to start slideshow
play_button = tk.Button(root, text="Play Slideshow", command=update_image)
play_button.pack()

root.mainloop()

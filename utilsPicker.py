import cv2
import numpy as np
import tkinter as tk
from tkinter import Label, Button, Frame, Canvas
from PIL import Image, ImageTk

"""
Library for loading an image from path, creating gui for color picker
"""

def load_image(image_path):
    """Loads an image using OpenCV."""
    return cv2.imread(image_path)

def get_color(event):
    """Callback function to get the color of a pixel on mouse click."""
    # Convert display coordinates to original image coordinates
    x = int(event.x * original_img_cv.shape[1] / img_tk.width())
    y = int(event.y * original_img_cv.shape[0] / img_tk.height())
    
    if 0 <= x < original_img_cv.shape[1] and 0 <= y < original_img_cv.shape[0]:
        # Get color from the original image, store in RGB format
        pixel = original_img_cv[y, x]  
        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])  

        # write color rgb code
        color = f"RGB: ({r}, {g}, {b})"     

        # display color to gui
        gui_label.config(text=color)        
        gui_color_box.config(bg=f'#{r:02x}{g:02x}{b:02x}')

def zoom(event):
    """Handles zooming in and out with the mouse wheel."""
    global img_tk, zoom_factor, canvas_image

    # Zoom step --> zoom in/out
    if event.delta > 0:
        zoom_factor *= 1.1  # Zoom in
    else:
        zoom_factor /= 1.1  # Zoom out
    
    # Calculate new size of the image
    new_size = (int(original_img_pil.width * zoom_factor), int(original_img_pil.height * zoom_factor))
    resized_img = original_img_pil.resize(new_size, Image.Resampling.LANCZOS)

    # Resize the image
    img_tk = ImageTk.PhotoImage(resized_img)
    canvas.itemconfig(canvas_image, image=img_tk)
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

def show_image_with_picker(image_path):
    """Creates a GUI to display an image with zoom and color picking."""
    global gui_label, gui_color_box, img_tk, original_img_cv, original_img_pil, zoom_factor, canvas, canvas_image
    
    root = tk.Tk()
    root.title("Color Picker")
    
    # Load image
    original_img_cv = load_image(image_path)

    # Check if the image exists
    if original_img_cv is None:
        print("Error: Could not load image.")
        return
    
    # Ensure RGB color order (cv2 is loading the color code in the BRG format)
    original_img_cv = cv2.cvtColor(original_img_cv, cv2.COLOR_BGR2RGB)

    # Load the image
    original_img_pil = Image.fromarray(original_img_cv)
    img_tk = ImageTk.PhotoImage(original_img_pil)
    zoom_factor = 1.0
    
    # some GUI properties -- frame, buttons,...
    control_frame = Frame(root)
    control_frame.pack()
    
    gui_label = Label(control_frame, text="Click on the image to get RGB values")
    gui_label.pack()
    
    gui_color_box = Label(control_frame, width=10, height=2, bg="white")
    gui_color_box.pack()
    
    cancel_button = Button(control_frame, text="Cancel", command=root.destroy)
    cancel_button.pack()
    
    # Canvas to display the image
    canvas = Canvas(root, width=img_tk.width(), height=img_tk.height(), cursor="cross")
    canvas.pack()
    canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.bind("<Button-1>", get_color)
    canvas.bind("<MouseWheel>", zoom)
    
    root.mainloop()
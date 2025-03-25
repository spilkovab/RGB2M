import cv2
import numpy as np
# import tkinter as tk
# from tkinter import Label, Button, Frame, Canvas
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *

"""
Library for loading an image from path, creating gui for color picker
"""
def init_app():
    global app, color_frame

    app = CTk()
    app.geometry("1300x750")
    buttons()
    customtkinter.set_appearance_mode("dark")
    appearance_mode()

    color_frame = CTkFrame(app, width=100, height=50, 
                           fg_color="white", corner_radius=5)
    color_frame.place(relx=0.5, y=50, anchor="center")
    return app

def appearance_mode():
    mode = customtkinter.get_appearance_mode()
    # buttons()

    if mode == 'Light':
        customtkinter.set_appearance_mode("dark")
        btnAppearance.configure(text="Light mode")

    else:
        customtkinter.set_appearance_mode("light")
        btnAppearance.configure(text="Dark mode")

    # return app

def load_image(image_path,app):
    """Loads an image using OpenCV."""

    global image, pil_image, image_label

    # return cv2.imread(image_path)
    pil_image = Image.open(image_path)
    im_w = pil_image.width/2.5
    im_h = pil_image.height/2.5

    image = CTkImage(pil_image, size=(im_w, im_h))

    frame = CTkFrame(app, width=im_w, height=im_h,
                      fg_color='gray', corner_radius=5)
    frame.place(x = 20, y=20, anchor="nw")
    
    image_label = CTkLabel(frame, image=image, text="", cursor="cross")
    image_label.pack(padx=5, pady=5)

    image_label.bind("<Button-1>", get_color)
    # image_label.bind("<MouseWheel>", zoom)

    # canvas = CTkCanvas(app, width=im_w, height=im_h,
    #                     cursor="cross",)
    # canvas.place(x = 20, y=20, anchor="nw")
    # canvas.bind("<MouseWheel>", zoom)

    return image, pil_image, frame, image_label

def buttons():
    """ Helper function to create buttons in the app."""
    global btnAppearance, cancel_button, rgb_code

    # Button to change the appearance mode
    btnAppearance = CTkButton(master=app, text="Light mode", font=('Arial', 15),
                               command=appearance_mode, width=55, height=20, hover=True)
    btnAppearance.place(relx=0.99, y=20,anchor="ne")

    # Button to close the app
    cancel_button = CTkButton(app, text="Cancel", font=('Arial', 15),
                               command=app.destroy, width=55, height=20, hover=True)
    cancel_button.place(relx=0.99, rely=0.99, anchor="se")

    # Label to display the RGB code
    rgb_code = CTkLabel(app, text=f"RGB: ", font=('Arial', 15))
    rgb_code.place(relx=0.5, y=100, anchor="center")
    

def get_color(event):
    """Callback function to get the color of a pixel on mouse click."""
    # global rgb_color

    # TODO: fix rgb values!!!!!
    x, y = event.x, event.y
    rgb_color = []
    rgb_color = pil_image.getpixel((x, y))

    # change the color of the frame
    color_frame.configure(fg_color=f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}")
    # write the rgb code
    rgb_code.configure(text=f"RGB: {rgb_color}")

    
def zoom(event):
    """Handles zooming in and out with the mouse wheel."""

    # global image, pil_image#, image_label
    w, h = int(pil_image.width/2.5), int(pil_image.height/2.5)

    # Determine the zoom direction
    if event.delta > 0:
        scale = 1.1  # Zoom in
    else:
        scale = 0.9  # Zoom out

    # Calculate the size of the crop box.
    # For zooming in, we want a smaller region; for zooming out, a larger region.
    # Adjust by dividing the original dimensions by the scale.
    crop_width = int(w / scale)
    crop_height = int(h / scale)

    # Calculate coordinates for a centered crop box.
    left = (w - crop_width) // 2
    upper = (h - crop_height) // 2
    right = left + crop_width
    lower = upper + crop_height

    # Crop the image to the calculated box
    cropped_image = pil_image.crop((left, upper, right, lower))
    
    # Resize the cropped image back to the original dimensions
    resized_image = cropped_image.resize((w, h), resample=Image.LANCZOS)
    resized_ctk_image = CTkImage(resized_image, size=(w, h))

    # Update the image label (make sure to keep a reference to the image)
    image_label.configure(image=resized_ctk_image)
    # image_label.image = resized_image  # Prevent garbage collection






    # # Calculate new size
    # new_width = int(w * scale)
    # new_height = int(h * scale)

    # # Resize the image
    # resized_image = pil_image.crop((new_width, new_height))
    # resized_image = resized_image.resize((pil_image.width, pil_image.height))

    # # Update the image label
    # image_label.configure(image=resized_image)
    # image_label.image = image

# def show_image_with_picker(image_path):
#     """Creates a GUI to display an image with zoom and color picking."""
#     # global gui_label, gui_color_box, img_tk, original_img_cv, original_img_pil, zoom_factor, canvas, canvas_image
    
#     app = init_app()
#     orig_img, _, _ = load_image()
    
#     # Load image
#     # original_img_cv = load_image(image_path)

#     # Check if the image exists
#     if orig_img is None:
#         print("Error: Could not load image.")
#         return
    
#     # Ensure RGB color order (cv2 is loading the color code in the BRG format)
#     orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)

#     # Load the image
#     # original_img_pil = Image.fromarray(original_img_cv)
#     # img_tk = ImageCTk.PhotoImage(original_img_pil)
#     zoom_factor = 1.0
    
#     # some GUI properties -- frame, buttons,...
#     control_frame = Frame(app)
#     control_frame.pack()
    
#     gui_label = Label(control_frame, text="Click on the image to get RGB values")
#     gui_label.pack()
    
#     gui_color_box = Label(control_frame, width=10, height=2, bg="white")
#     gui_color_box.pack()
    
#     cancel_button = Button(control_frame, text="Cancel", command=root.destroy)
#     cancel_button.pack()
    
#     # Canvas to display the image
#     canvas = Canvas(root, width=img_tk.width(), height=img_tk.height(), cursor="cross")
#     canvas.pack()
#     canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.bind("<Button-1>", get_color)
#     canvas.bind("<MouseWheel>", zoom)
    
#     root.mainloop()
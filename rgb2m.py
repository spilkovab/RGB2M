import utilsPicker
from utilsPicker import *
import customtkinter
from customtkinter import *

# load image path
image_path = "testImages/im01.jpg" 


"""Creates a GUI to display an image with zoom and color picking."""
# global gui_label, gui_color_box, img_tk, original_img_cv, original_img_pil, zoom_factor, canvas, canvas_image

app = init_app()
img, pil_image, frame, image_label = load_image(image_path,app)

# Load image
# original_img_cv = load_image(image_path)

# Check if the image exists
if img is None:
    print("Error: Could not load image.")
    

# Ensure RGB color order (cv2 is loading the color code in the BRG format)
# img = cv2.cvtColor(pil_image, cv2.COLOR_BGR2RGB)

zoom_factor = 1.0


# gui_color_box = CTkLabel(control_frame, width=10, height=2)
# gui_color_box.pack()

# Canvas to display the image
# canvas = CTkCanvas(app, width=img.width(), height=img.height(), cursor="cross")
# canvas.pack()
# canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
# canvas.bind("<Button-1>", get_color)
# canvas.bind("<MouseWheel>", zoom)

app.mainloop()

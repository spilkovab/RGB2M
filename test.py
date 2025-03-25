import customtkinter
from customtkinter import *
from PIL import Image  

# Init app
app = CTk()

# Default settings
app.geometry("1300x750")
customtkinter.set_appearance_mode("dark")

def appearance_mode():
    # set appearence mode to dark
    mode = customtkinter.get_appearance_mode()
    
    if mode=='Light':
        customtkinter.set_appearance_mode("dark")
        btnAppearance.configure(text="Set to Light mode")

    else:
        customtkinter.set_appearance_mode("light")
        btnAppearance.configure(text="Set to Dark mode")

def get_color(event):
    """Callback function to get the color of a pixel on mouse click."""
    # Convert display coordinates to original image coordinates
    x = int(event.x * pil_image.shape[1] / img_tk.width())
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

def load_image(image_path):

    global pil_image

    pil_image = Image.open(image_path)
    im_w = pil_image.width/2.5
    im_h = pil_image.height/2.5

    image = CTkImage(pil_image, size=(im_w, im_h))

    frame = CTkFrame(app, width=im_w, height=im_h, fg_color="gray", corner_radius=5)
    frame.place(x=20, y=20, anchor="nw")

    # Display image inside a CTkLabel
    image_label = CTkLabel(frame, image=image, text="")  # `text=""` hides the default text
    image_label.pack(padx=5, pady=5)


btnAppearance = CTkButton(master=app, text="Set to Light mode", font=('Arial', 15), command=appearance_mode, width=55, height=20, hover=True)
btnAppearance.place(relx=0.99, y=20, anchor="ne")


image_path = "testImages/im01.jpg"  # Change this to your image path
load_image(image_path)

app.mainloop()




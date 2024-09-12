# rounded_button.py

import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=120, height=40, radius=20, bg_color="#4CAF50", fg_color="#FFFFFF", hover_bg_color="#45A049", click_bg_color="#3E8E41", *args, **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0, *args, **kwargs)
        self.command = command
        self.bg_color = bg_color
        self.hover_bg_color = hover_bg_color
        self.click_bg_color = click_bg_color
        self.default_bg_color = bg_color
        self.width = width
        self.height = height
        self.radius = radius

        self.button_image = self.create_rounded_rectangle_image(width, height, radius, bg_color)
        self.button_image_hover = self.create_rounded_rectangle_image(width, height, radius, hover_bg_color)
        self.button_image_click = self.create_rounded_rectangle_image(width, height, radius, click_bg_color)

        self.button_photo = ImageTk.PhotoImage(self.button_image)
        self.button_photo_hover = ImageTk.PhotoImage(self.button_image_hover)
        self.button_photo_click = ImageTk.PhotoImage(self.button_image_click)

        self.image_id = self.create_image(0, 0, anchor="nw", image=self.button_photo)
        self.text = self.create_text(width // 2, height // 2, text=text, fill=fg_color, font=('Helvetica', 12))

       
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def create_rounded_rectangle_image(self, width, height, radius, color):
        """Helper function to create a rounded rectangle image"""
        image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle([(0, 0), (width, height)], radius, fill=color)
        return image

    def on_enter(self, event):
        """Hover effect"""
        self.itemconfig(self.image_id, image=self.button_photo_hover)

    def on_leave(self, event):
        """Remove hover effect"""
        self.itemconfig(self.image_id, image=self.button_photo)

    def on_click(self, event):
        """Click effect"""
        self.itemconfig(self.image_id, image=self.button_photo_click)
        self.after(100, lambda: self.itemconfig(self.image_id, image=self.button_photo)) 
        if self.command:
            self.command()

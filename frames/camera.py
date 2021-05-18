import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from model.cnn import analize


class CameraFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.isSnapPressed = False
        self.image = None
        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.cameraPanel = tk.Label(parent)
        self.cameraPanel.grid(row=0, padx=5, pady=5)

        self.label = tk.Label(parent, text="")
        self.label.grid(row=1, padx=5, pady=5)
        self.label.config(text="", font=("Helvetica", 18), fg="Red")

        self.btnContainer = tk.Frame(parent)
        self.btnContainer.grid(row=2, padx=5, pady=5)

        filebtn = tk.Button(
            self.btnContainer,
            text="Take Snapshot",
            image=self.pixel,
            width=100,
            height=25,
            compound="center",
            command=self.snapshot,
        )
        filebtn.grid(column=0, row=0, padx=5, pady=5)

        camerabtn = tk.Button(
            self.btnContainer,
            text="Reset",
            image=self.pixel,
            width=100,
            height=25,
            compound="center",
            command=self.reset,
        )
        camerabtn.grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.show()

    def show(self):
        ret, frame = self.cap.read()
        if ret == True and not self.isSnapPressed:
            frame = imutils.resize(frame, width=400)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            self.image = img
            img = ImageTk.PhotoImage(image=img)

            self.cameraPanel.configure(image=img)
            self.cameraPanel.image = img
            self.cameraPanel.after(10, self.show)
        if ret != True:
            self.cap.release()

    def snapshot(self):
        self.isSnapPressed = True
        self.image = self.image.resize((150, 150))
        result = analize(self.image).upper()
        color = "Red" if result == "ROTTEN" else "Green"
        self.label.config(text=result, font=("Helvetica", 18), fg=color)

    def reset(self):
        self.isSnapPressed = False
        self.label.config(text="")
        self.show()

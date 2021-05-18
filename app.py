from tkinter import *
from frames.main import MainFrame
from frames.camera import CameraFrame

root = MainFrame(className="Prototype")

CameraFrame(root.container)

root.mainloop()

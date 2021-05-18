# CNN Fresh Rotten
A Prototype of a Convolutional Neural Network for rotten and fresh fruit detection

# Setup

## Prerequisites

Create a Virtual Environment
```
  python -m venv venv
```

Activate the Virtual Environment on **`Windows`**
```
  venv/Scripts/Activate.ps1
```

Activate the Virtual Environment on **`Mac/Linux`**
```bash
  source venv/bin/activate
```

Install project dependencies
```
  pip install pillow tensorflow scipy numpy opencv-contrib-python imutils 
```

## Run
To run the program just run the code below:
```
  python app.py
```

## Tips
* `Take Snapshot` button take a snapshot and freeze the webcam and pass to the CNN to classify it
* `Reset` button unfreeze the camera so that you can take another snapshot
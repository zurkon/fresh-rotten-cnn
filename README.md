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

## Dataset
The dataset that you need to train the model is available on Kaggle: [Fruits fresh and rotten for classification](https://www.kaggle.com/sriramr/fruits-fresh-and-rotten-for-classification)

**Download the dataset, UnZip it and place the `dataset` folder inside `temp` folder.**

After that, just run the `utils.py` file:
```
  python utils.py
```

It will split that fruit images into `Train`, `Test` and `Val` folders, each one contain 2 folder:
* `fresh`   - containing fresh fruit images
* `rotten`  - containing rotten fruit images

## Install project dependencies
If you have the CNN model ready to use:
```
  pip install pillow tensorflow scipy numpy opencv-contrib-python imutils 
```

If you need to train the model using the `CNN_model.ipynb` file on this repo:
```
  pip install tensorflow scipy numpy pandas matplotlib opencv-contrib-python imutils 
```

## Run
To run the program just run the code below:
```
  python app.py
```

## Tips
* `Take Snapshot` button take a snapshot and freeze the webcam and pass to the CNN to classify it
* `Reset` button unfreeze the camera so that you can take another snapshot
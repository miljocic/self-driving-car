# Behavioral Cloning - Self Driving Car

End-to-end deep learning project that predicts steering angles directly from camera images using a Convolutional Neural Network (CNN).

## Tech Stack
- Flask (real-time server)
- Keras + TensorFlow (model training)
- OpenCV (image preprocessing)
- SocketIO (simulator communication)

## Features
- NVIDIA-style CNN architecture
- Image preprocessing (crop, resize, YUV conversion)
- Data augmentation (flip, brightness, translation, shadows)
- Real-time autonomous driving in simulator

## Training

python model.py -d data -n 10 -b 128

## Run Autonomous Driving

python drive.py -m model/model-001.h5

## Concept

The model learns steering behavior from recorded driving data (behavioral cloning) and performs real-time inference to control the vehicle.

## Authors

Jovana Lazic

Nada Trajkovic

Milica Jocic

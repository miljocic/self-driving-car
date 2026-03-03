import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten, Input
from utils import INPUT_SHAPE, batch_generator
import argparse
import os

np.random.seed(0)

MODEL_SAVE_PATH = 'model/model-{epoch:03d}.h5'


def load_data(args):
    """
    Load training data and split it into training and validation set
    """
    data_df = pd.read_csv(os.path.join(os.getcwd(), args.data_dir, 'driving_log.csv'), names=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed'])
    X = data_df[['center', 'left', 'right']].values
    y = data_df['steering'].values
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=args.test_size, random_state=0)

    return X_train, X_valid, y_train, y_valid


def build_model():
    """
    Build the model
    """
    model = None

    return model


def train_model(model, args, X_train, X_valid, y_train, y_valid):
    """
    Train the model

    Primer upotrebe batch_generator funkcije:
        batch_generator(args.data_dir, X_train, y_train, args.batch_size, True)
    
    Moze se koristiti i za trening i za validacione podatke.
    """
    pass


def main():
    """
    Load train/validation data set and train the model
    """
    parser = argparse.ArgumentParser(description='Behavioral Cloning Training Program')
    parser.add_argument('-d', help='data directory',              dest='data_dir',          type=str,   default='data')
    parser.add_argument('-n', help='number of epochs',            dest='nb_epoch',          type=int,   default=10)
    parser.add_argument('-s', help='number of batches per epoch', dest='steps_per_epoch',   type=int,   default=100)
    parser.add_argument('-b', help='batch size',                  dest='batch_size',        type=int,   default=128)
    parser.add_argument('-l', help='learning rate',               dest='learning_rate',     type=float, default=1.0e-3)
    args = parser.parse_args()

    data = load_data(args)
    model = build_model(args)
    train_model(model, args, *data)


if __name__ == '__main__':
    main()


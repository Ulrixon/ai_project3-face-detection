#%%
from pandas import array
import sklearn
import tensorflow as tf
import pandas as pd
from keras.models import Model
from keras.layers import Input, Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2 as cv
from PIL import Image
from keras.utils import np_utils
from keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau
# %%
import torch
torch.cuda.is_available()
# %%

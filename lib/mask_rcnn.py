'''res network applications''' 

import sys
import os
from mrcnn import utils  
from mrcnn.config import Config
import mrcnn.model as modellib
from mrcnn import visualize

Mask_RCNN = 'Mask_RCNN/'
MODEL_DIR = os.path.join(Mask_RCNN, "mrcnn/logs")


class CocoSynthConfig(Config):
    """Configuration for training on the box_synthetic dataset.
    Derives from the base Config class and overrides specific values.
    """
    NAME = "cocosynth_dataset"

    # Train on 1 GPU and 1 image per GPU. Batch size is 1 (GPUs * images/GPU).
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    # Number of classes (including background)
    NUM_CLASSES = 2  # background + cigarette butt

    # All of our training images are 512x512
    IMAGE_MIN_DIM = 512
    IMAGE_MAX_DIM = 512

    # Found out best barametrs for tune
    STEPS_PER_EPOCH = 1000  # that param is unchanged for real
    DETECTION_MIN_CONFIDENCE = 0.7
    LEARNING_RATE = 0.001
    DETECTION_NMS_THRESHOLD = 0.3
    WEIGHT_DECAY  = 0.0001

    VALIDATION_STEPS = 5
    
    # Gives better result than resn50
    BACKBONE = 'resnet101'

    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)
    TRAIN_ROIS_PER_IMAGE = 32
    MAX_GT_INSTANCES = 50 
    POST_NMS_ROIS_INFERENCE = 500 
    POST_NMS_ROIS_TRAINING = 1000 
    

def load_best_model():
    config = CocoSynthConfig()
    config.display()


def recreate_model(inference_config):
    model = modellib.MaskRCNN(mode="inference", 
            config=inference_config,
            model_dir=MODEL_DIR)
            
    return  model
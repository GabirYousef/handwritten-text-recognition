#!/bin/bash

### ---------------------------------------- ###
### define dataset name and data environment ###
### ---------------------------------------- ###
# DATASET="bentham"
# DATASET="iam"
DATASET="saintgall"
# DATASET="rimes"

DATASET_DIR="./data/$DATASET"
OUTPUT_DIR="./output"


### ----------------------------------------------- ###
### structure the raw dataset to the design pattern ###
### ----------------------------------------------- ###
# python src/normalize.py --dataset_dir $DATASET_DIR


### ---------------------- ###
### preprocess the dataset ###
### ---------------------- ###
# python src/preprocess.py --dataset_dir $DATASET_DIR


### ----------- ###
### train model ###
### ----------- ###
python src/train.py --dataset_dir $DATASET_DIR --output_dir $OUTPUT_DIR


### ---------- ###
### test model ###
### ---------- ###
# python src/test.py --dataset_dir $DATASET_DIR --output_dir $OUTPUT_DIR
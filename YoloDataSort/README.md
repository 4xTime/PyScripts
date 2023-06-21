# YOLO Data Preparation Script

This script helps in preparing data for training a YOLO (You Only Look Once) object detection model. It organizes the dataset into train, test, and validation sets, and moves the image files accordingly.

## Prerequisites

- Python 3.x

## Usage

1. Place your dataset in the desired directory.
2. Run the script with the following command:

python data_preparation_script.py <dataset_directory_path>


3. Select the desired image distribution for the train, test, and validation sets.
- Option 0: 50% train, 25% test, 25% validation (default)
- Option 1: 25% train, 25% test, 50% validation
- Option 2: Custom distribution (enter the number of images for each set)

4. The script will create the necessary folders and move the images accordingly.

## Folder Structure

After running the script, the folder structure will be as follows:

YoloReadyToTrain
├── train
│ ├── images
│ └── labels
├── test
│ ├── images
│ └── labels
└── valid
├── images
└── labels

- The `train/images` folder contains images for training.
- The `test/images` folder contains images for testing.
- The `valid/images` folder contains images for validation.
- The `labels` folders are currently empty and can be used for storing annotation files if needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
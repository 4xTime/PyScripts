
# YOLO Data Preparation Script

This Python script is designed to help you organize and split your image data for training a YOLO (You Only Look Once) object detection model. The script creates the necessary folder structure, splits the data into train, test, and validation sets, and generates a custom YAML file for YOLO configuration.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- A directory containing your image dataset.

## Getting Started

1. Clone this repository or download the script `YoloDataSort.py` to your local machine.

2. Place your image dataset in a separate directory.

## Usage

To use the script, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the `YoloDataSort.py` script is located.

3. Run the script with the path to your image dataset as a command-line argument:

   ```bash
   python YoloDataSort.py /path/to/your/image/dataset

    The script will prompt you to choose between preset data splits or provide custom values for train, test, and validation sets. Select an option based on your requirements.

    The script will create the required folder structure inside a folder called YoloReadyToTrain in the current working directory.

    The images will be randomly moved to their respective train, test, and validation folders according to the chosen data split.

    A custom YAML file named custom.yaml will be generated inside the YoloReadyToTrain folder. This file contains the paths to the train, validation, and test folders, as well as the number of classes and class names. You should edit this file to match your specific class names and number of classes.

Data Split Options

    Option 0: I: 50% / T: 25% / V: 25%
    Option 1: I: 25% / T: 25% / V: 50%
    Option 2: Custom - You can specify the number of images for each category (train, test, and validation).

Note

    The script assumes that your image files have extensions .jpg, .jpeg, or .png. Ensure your images are properly formatted with these extensions.

    If the number of images specified in custom input exceeds the available images in the dataset, the script will automatically adjust the splits to fit the available data.

    Make sure to review the generated custom.yaml file and update the class names according to your dataset.

Contributing

If you find any issues with the script or have suggestions for improvement, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.
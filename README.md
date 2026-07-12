# Image Recognition Model

## Project Overview

This project is an image recognition model that classifies images into two categories: **Anime Characters** and **Real Human Characters**.

The model was created using **Google Teachable Machine** and exported in **TensorFlow/Keras format**. The Python program loads the trained model, processes an input image, and predicts the class with a confidence score.

## Author

**Adel Abdulaziz Bin Atiq**

## Classes

The model can recognize:

- Anime Character
- Real Human Character

## Technologies Used

- Python
- TensorFlow / Keras
- tf_keras
- NumPy
- Pillow (PIL)
- Google Teachable Machine

## Project Files

```
Image-Recognition-Model/
│
├── keras_model.h5        # Trained AI model
├── labels.txt            # Class labels
├── main.py               # Image prediction code
├── Eren jaeger.jpg       # Test image
└── README.md             # Project documentation
```

## Installation

Install the required libraries:

```bash
pip install tensorflow tf_keras numpy pillow
```

## How to Run

1. Download or clone the repository.

2. Make sure these files are in the same folder:

- `keras_model.h5`
- `labels.txt`
- `main.py`
- Image file

3. Run the program:

```bash
python main.py
```

## How the Model Works

1. The program loads the trained Keras model.
2. The input image is converted to RGB format.
3. The image is resized to **224 × 224 pixels**.
4. The image is normalized before prediction.
5. The model predicts the image category.
6. The program displays:
   - Predicted class
   - Confidence score

## Example Output

```
Class: Anime Character
Confidence Score: 0.98
```

## Model Details

- Model Type: Image Classification
- Input Size: 224 × 224 pixels
- Framework: TensorFlow / Keras
- Model Format: `.h5`

## Conclusion

This project demonstrates how artificial intelligence can be used for image recognition and classification by distinguishing between anime characters and real human characters.

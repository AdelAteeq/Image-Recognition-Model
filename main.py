{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXSwrFvm8GrvHUJZ8ilX09",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdelAteeq/Image-Recognition-Model/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "JFgxZniYZH8p",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d6f9a552-bc28-4964-881e-f4a57e4797bd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 1s 975ms/step\n",
            "Class: anime\n",
            "Confidence Score: 0.9999944\n"
          ]
        }
      ],
      "source": [
        "from keras.models import load_model  # TensorFlow is required for Keras to work\n",
        "from PIL import Image, ImageOps  # Install pillow instead of PIL\n",
        "import numpy as np\n",
        "import tf_keras as tk\n",
        "\n",
        "# Disable scientific notation for clarity\n",
        "np.set_printoptions(suppress=True)\n",
        "\n",
        "# Load the model\n",
        "model = tk.models.load_model(\"keras_model.h5\", compile=False)\n",
        "# Load the labels\n",
        "class_names = open(\"labels.txt\", \"r\").readlines()\n",
        "\n",
        "# Create the array of the right shape to feed into the keras model\n",
        "# The 'length' or number of images you can put into the array is\n",
        "# determined by the first position in the shape tuple, in this case 1\n",
        "data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)\n",
        "\n",
        "# Replace this with the path to your image\n",
        "image = Image.open(\"Eren jaeger.jpg\").convert(\"RGB\")\n",
        "\n",
        "# resizing the image to be at least 224x224 and then cropping from the center\n",
        "size = (224, 224)\n",
        "image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)\n",
        "\n",
        "# turn the image into a numpy array\n",
        "image_array = np.asarray(image)\n",
        "\n",
        "# Normalize the image\n",
        "normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1\n",
        "\n",
        "# Load the image into the array\n",
        "data[0] = normalized_image_array\n",
        "\n",
        "# Predicts the model\n",
        "prediction = model.predict(data)\n",
        "index = np.argmax(prediction)\n",
        "class_name = class_names[index]\n",
        "confidence_score = prediction[0][index]\n",
        "\n",
        "# Print prediction and confidence score\n",
        "print(\"Class:\", class_name[2:], end=\"\")\n",
        "print(\"Confidence Score:\", confidence_score)\n"
      ]
    }
  ]
}
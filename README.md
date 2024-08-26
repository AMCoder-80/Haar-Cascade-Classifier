## Object Detection using Haar Cascade Classifier method

**Running code**

To run this project you only need to create a virtualenv and activate it using following commands:

Windows:

``.\venv\Scripts\activate``

Linux, Mac

``sourve venv/bin/activate``

Then you should install required packages into your virtualenv using the following command

``pip install -r requirements.txt``

Now you have everything ready to run the code.

*detect_webcam.py*: This code opens your webcam and starts detecting every ducks that appears into your frams

``python3 detect_webcam.py``

*detect_image.py*: This code reads an image and tries to detect all ducks inside the image.

``python3 detect_image.py``

**The process of training Haar cascade classifier algorithm is available in this medium publication**

[Training tutorial](https://medium.com/@alirezamortezaei/building-an-object-detection-system-with-opencvs-haar-cascade-classifier-and-docker-using-python-7b8cc03c719d)
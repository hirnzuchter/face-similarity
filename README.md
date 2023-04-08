# Face Similarity
## Introduction
This Face Similarity model uses Tensorflow to determine whether or not
two inputs are of the same person, returning a value of 0 if the two are the 
same and returning a value of 1 if the two are different. Because of the way
the "reduction" network was designed, it is noncommutative. Thus, in applications,
I recommend that you apply a AND(NOT(b1, b2)) to the operation applied to the stacked
image img1, img2 and img2, img1 respectively. For clarification, the model has as input
two images of the same size stacked on top of each other. In the "validation" cell of
Jupyter notebook, there is an example of cleaning and transforming image data such that
it may be input to the model. Included also in the notebook are my image processing
functions, which greatly simplify this. This model was trained on google images of
celebrities, and google images of searches of less-known names. My thoughts are that
searches of less-known names are more likely to produce images of different people. 
The google images are produced using my RIG("Retrieve Images on Google") module.
## Usage
### Engineering
If you want to play around with the model construction, you will have to:
  1. Download Tensorflow
  2. Download pillow
  3. Download OpenCV
  4. (optional--you may use your own data if you want)Download the dataset 
    for the names at https://pypi.org/project/names-dataset/ into the project folder. 
    In particular, the "curate" folder should be listed directly under the project 
    folder so that it may be referenced from the Jupyter notebook through:
    ```"./curate"```.
### Utility
On the other hand, if you just want to use the model, you will have to:
  1. Download Tensorflow
  2. Load the weight weight set(make
    sure to check the model architecture as listed in the Jupyter notebook)
  3. Use model.predict() as it fits your needs.

If you have any questions or would like to collaborate, contact me at sactoa@gmail.com.

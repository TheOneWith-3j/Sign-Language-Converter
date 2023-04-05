# Sign_language-converter
This project has 3 major features. 
1. Sign language to Text and speech
2. Speech to Sign Language
3. Conversion from Youtube transcript

Additionally, there is a feature to display the transcript of a youtube video in sign language to help aid the specially abled people


**ABSTRACT:** 

We have developed a real-time method using neural networks to recognize finger-spelling based American Sign Language, which is one of the oldest and most natural forms of communication. Recognizing human hand gestures from camera images is an intriguing topic in computer vision. To achieve this, we propose a convolutional neural network (CNN) method that can recognize human hand gestures from camera images. Our aim is to recognize hand gestures of human task activities from a camera image by using the hand position and orientation to train and test the CNN. We first filter the hand and then pass it through a classifier to predict the class of the hand gestures. The calibrated images are then used to train the CNN.


**Introduction:**

As spoken language is not an option for individuals with communication-related disabilities, American Sign Language has become the predominant sign language. Communication is the act of exchanging thoughts and messages, which can be done in various ways such as through speech, signals, behavior, and visuals. Deaf and mute individuals communicate using hand gestures to express their ideas, which are understood through visual perception. This nonverbal communication is commonly referred to as sign language.

Our project focuses on developing a model that can recognize finger-spelling-based hand gestures to form complete words by combining each gesture. The gestures we aim to train the model on are depicted in the image below.


**Scope:**
This System will be Beneficial for Both Dumb/Deaf People and the People Who do not understands the Sign Language. They just need to do that with sign Language gestures and this system will identify what he/she is trying to say after identification it gives the output in the form of Text as well as Speech format. This makes the communication with them much easier as they can now communicate twith people who do not know the sign language.

We have also added a functionality of youtube so that the person can even watch youtube videos with the ease of their own language rather than just reasing the subtitles. In futuren we can colab with youtube and google to provide an avatar that converts the captions into live gestures.


**Data Acquisition:**

When using vision-based methods, the computer's webcam serves as the input device for observing hand and/or finger movements. Vision-based methods require only a camera, enabling a natural interaction between humans and computers without the need for additional devices, which reduces costs. However, the main challenge of vision-based hand detection is coping with the wide range of appearances of the human hand due to numerous movements, variations in skin color, and differences in viewpoints, scales, and camera speed during scene capture.


**Gesture classification:**

Convolutional Neural Network (CNN)
Convolutional Layer
Pooling Layer
Fully Connected Layer


**Text To Speech Translation:**

This model translates the text into speech by using modules such as pyttsx3 library to convert the words provided by the user using the sign language.

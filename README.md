# Design of real-time continuous EEG acquisition system with feedback based error correction for P300 task paradigms.

This project aims to design a real-time continuous EEG acquisition system with feedback-based error correction for P300 task paradigms. The project encompasses both hardware and software components, providing a comprehensive solution for reliable EEG-based Brain-Computer Interfaces (BCIs).

## Objectives :

#### Hardware
Design an EEG cap based on the standard 10-20 electrode system.
Select suitable components for the acquisition system.
Design a compact EEG acquisition circuit.
Fabricate a PCB for the EEG acquisition system.

#### Software
Choose a suitable P300 task paradigm for EEG data acquisition.
Develop an error detection algorithm using Deep Learning to enhance BCI performance.
Create a software design flowchart outlining the steps involved in acquiring, processing, and analyzing EEG signals.

## Software Design Flowchart

#### Acquire EEG Signals:
Use an open-source dataset that satisfies user requirements.
Utilize the KAGGLE - BCI Challenge @ NER 2015 dataset recorded with 56 passive Ag/AgCl EEG sensors following the extended 10-20 system.

#### Pre-processing:
Implement bandpass filtering to prepare EEG signals for analysis.

#### Deep Learning Model:
Design a 15-layer Convolutional Neural Network model for feature extraction and classification.
The model is influenced by EEGNET, employing depthwise and separable convolutions.
Input consists of batches of 100 samples, each with T timepoints and C channels.

#### Evaluation and Analysis:
Train the model using the provided dataset.
Evaluate the results and analyze the model's outputs for error detection in P300 task paradigms.

## Dataset Description
KAGGLE - BCI Challenge @ NER 2015:
EEG recorded with 56 passive Ag/AgCl EEG sensors.
Subjects underwent five copy spelling sessions, each consisting of twelve 5-letter words (except the fifth session, which had twenty 5-letter words).

## Deep Learning Model Details

#### Architecture:

15-layer Convolutional Neural Network.
Inspired by EEGNET with depthwise and separable convolutions.
Convolution Operations:

Temporal filters of size (1,56) followed by batch normalization.
Depthwise convolution layer of (56,1) for every channel.
Separable layer with a kernel size of (1,8) to learn individual summaries and combine outputs.
Fully connected layer with a sigmoid activation for binary classification.
Training Details:

Loss Function: Binary Cross-Entropy.

Optimizer: Adam with weight decay (learning rate: 0.001, beta values: 0.9, 0.999, weight decay: 0.01).

This project presents an integrated solution for real-time EEG acquisition and error correction, bridging the gap between hardware design, data acquisition, and advanced Deep Learning techniques for improved Brain-Computer Interface performance.

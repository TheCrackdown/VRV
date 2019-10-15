# THE CRACKDOWN

## Introduction
The Crackdown is basically a repository on GitHub which hosts tool VRV, our very own created tool to detect whether a given site is a phishing site or not. VRV integrates two models. The first model follows the approach of using open source tools followed  by a second model which incorporates Machine Learning.

## VRV
VRV is a tool that will be used to tell whether the URL under consideration is a Phishing or a Non- Phishing one.
The tool will be working two models.
The first model follows the approach of using open source tools followed  by a second model which incorporates Machine Learning.
Machine learning model incorporates various classifiers that will be later used to enhance the probability and accuracy of the tool.
Later, both the models will be combined to generate the final output to tell whether the URL under consideration is a Phishing URL or a Genuine one.

## Overall System Architecture
<img width="718" alt="architecture" src="https://user-images.githubusercontent.com/54947999/66801089-7662c380-ef35-11e9-8e26-cfbcfe3fdc23.png">

## Working Of Tool
![flowchart](https://user-images.githubusercontent.com/54947999/66801143-ad38d980-ef35-11e9-9a61-79cdce3655b6.png)

## Welcome to VRV!

VRV is part of The CrackDown project to detect general phishing pages.

VRV is a tool that will be used to tell whether the URL under consideration is a Phishing or a Non- Phishing one.

The tool will be working two models.

The first model follows the approach of using open source tools followed  by a second model which incorporates Machine Learning.

Machine learning model incorporates various classifiers that will be later used to enhance the probability and accuracy of the tool.

Later, both the models will be combined to generate the final output to tell whether the URL under consideration is a Phishing URL or a Genuine one.

## Machine Learning Model
A machine learning model to identify phishing pages by looking at:

* HTML text - searching for brand name and signin keywords in HTML source code
* HTML structure - searching for submission forms and their attributes
* IMAGE text - searching for texts directly from image

We apply tesseract (a Deep learning based OCR engine) to extract texts from images.

We also NLP analysis to filter and clean nonsense words.

It supports:

- [x] Directly detection of potential phishing pages
- [x] A behavior-based model to investigate general phishing behaviors
- [x] A machine-learning-based (RandomForest) to combine all the properties to make a final decision


### Install OCR, NLTK and ML dependences
```
bash install.sh
```

### Demo

Run the demo to get predictions of testing samples under test folder.

1 is predicted as a phsihing page and 0 is predicted as a benign page.

```
python3 demo.py

Prediction result:	 googlw.lt----1.0----[0.28993355726427317, 0.7100664427357269]

Prediction result:	 googlw.cl----1.0----[0.09047988302948216, 0.9095201169705178]

Prediction result:	 googlw.co.il----1.0----[0.24020989615461588, 0.7597901038453841]

Prediction result:	 goofgle.se----1.0----[0.31088049798443707, 0.6891195020155627]

Prediction result:	 facebook-c.com----1.0----[0.22163562365428768, 0.7783643763457124]

Prediction result:	 faceb00k.bid----1.0----[0.17656695383979332, 0.8234330461602067]

Prediction result:	 sewauk.org----1.0----[0.25669347640761164, 0.7433065235923882]

Prediction result:	 100022538-facebook.com----0.0----[0.9193098619543378, 0.08069013804566202]

```

Get feature vectors.

```
python3 feature_extract.py
```

## Disclaimer and Reference

This is a research prototype, use at your own risk.

# Eye Disease Detection using Deep Learning

![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12cbe8a4-f55c-4b40-85bb-d8e1405e7b84/dfffuxf-dd7dbabc-ce26-46a1-be51-e98ba43094d8.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyY2JlOGE0LWY1NWMtNGI0MC04NWJiLWQ4ZTE0MDVlN2I4NFwvZGZmZnV4Zi1kZDdkYmFiYy1jZTI2LTQ2YTEtYmU1MS1lOThiYTQzMDk0ZDguZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.o6dWe-IFyyKk4Cw2QiriZC_aoZ5rsPvK0eZbSP9zTWk" />


A deep learning project to detect and classify eye diseases from images using computer vision.

---

## Project Description

This project leverages a convolutional neural network to classify eye diseases from retinal or eye image datasets.  
The model aims to assist medical diagnostics by providing fast, automated, and accurate predictions of common eye conditions.

---

## Author

**Ali Akbar Khan**

---

## Technologies Used

- Python  
- Fastai  
- PyTorch  
- Jupyter Notebook  
- Gradio (optional for deployment)  

---

## Model Details

- **Architecture**: `resnet18` pretrained CNN  
- **Training**: Fine-tuned for 10 epochs using Fastai's `vision_learner`  
- **Metric**: Achieved ~92% accuracy on validation set

---

## Dataset

A labeled dataset of eye images was used, possibly sourced from Kaggle or medical image repositories.  
The images represent different categories of eye diseases, such as:

- Cataract  
- Glaucoma  
- Retina disease  
- Normal

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aliiakbarkhan/eye-disease-detection-DL.git
cd eye-disease-detection-DL
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the notebook

Use Jupyter or VSCode to open waste-segregation.ipynb and run all cells.

### 4. Or launch Gradio app (if available)
```bash
python eye_app.py
```
### Sample Predictions
The model can take any image of retina and classify it into one of the predefined categories with high accuracy.
Here's a snapshot of predictions from the Gradio interface.

<img src="https://github.com/aliiakbarkhan/eye-disease-detection-DL/blob/main/output.png" />

### File Structure
```bash
waste-segregation/
├── eye_disease.ipynb     # Main notebook
├── eye_disease_model.pkl                   # Trained model (optional)
├── eye_app.py                      # Gradio app (if created)
├── README.md                   # Project documentation
```




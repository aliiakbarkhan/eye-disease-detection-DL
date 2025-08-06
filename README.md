# Eye Disease Detection using Deep Learning

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




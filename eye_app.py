from fastai.vision.all import *
import gradio as gr

learn = load_learner('eye_disease_model.pkl')

def predict_eye_disease(img):
    pred, pred_idx, probs = learn.predict(img)
    return {str(pred): float(probs[pred_idx])}

interface = gr.Interface(
    fn=predict_eye_disease,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=1),
    title="Eye Disease Detection - By Ali Akbar Khan",
    description="Upload an eye image to detect eye diseases like Cataract, Glaucoma, Diabetic Retinopathy, etc."
)

interface.launch()

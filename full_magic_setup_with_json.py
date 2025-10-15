import os
import json

# Project name
project_name = "Cattle_Health_Prototype"

# Create main folder
os.makedirs(project_name, exist_ok=True)

# Files and starter content
files_content = {
    f"{project_name}/app.py": '''\
# ===== Cattle Health Score Prototype =====
# Streamlit app: Upload image, detect cattle using YOLOv8, calculate health score, save BPA-style JSON

import streamlit as st
from ultralytics import YOLO
import json

st.title("Cattle Health Score Prototype")

# Upload image
uploaded = st.file_uploader("Upload side-view image of cattle", type=["jpg","jpeg","png"])
breed = st.selectbox("Select Breed", ["Murrah","Surti","Nili-Ravi","Gir","Jersey","HF_cross"])
tag_id = st.text_input("Animal Tag ID (optional)")

# Load YOLO model
@st.cache_resource
def load_model():
    return YOLO("best.pt")  # Make sure best.pt is in the same folder

model = load_model()

# Load breed reference JSON
with open("breed_reference.json") as f:
    breed_data = json.load(f)

if uploaded:
    with open("temp.jpg","wb") as f:
        f.write(uploaded.getbuffer())
    
    results = model.predict(source="temp.jpg", save=False, conf=0.25)[0]
    
    if len(results.boxes) == 0:
        st.error("No animal detected. Try another image.")
    else:
        x1, y1, x2, y2 = map(float, results.boxes.xyxy[0])
        st.success("Animal detected!")
        
        # Calculate measurements
        length_px = x2 - x1
        height_px = y2 - y1
        ratio = length_px / height_px
        
        # Reference ratio for selected breed
        ref_ratio = breed_data.get(breed, {}).get("length_to_height_ratio", 2.2)
        
        # Compute health score
        score = max(0, 100 * (1 - abs(ratio - ref_ratio)/ref_ratio))
        st.metric("Health Score", f"{score:.1f}/100")
        
        # BPA-style JSON
        payload = {
            "animal_id": tag_id or "NA",
            "breed": breed,
            "measurements": {"length_px":length_px,"height_px":height_px,"ratio":ratio},
            "health_score":{"score_value":round(score,2)}
        }
        
        if st.button("Save JSON"):
            with open("output.json","w") as f:
                json.dump(payload,f,indent=2)
            st.success("Saved to output.json")
            st.code(json.dumps(payload,indent=2))
''',

    f"{project_name}/train_yolo_colab.ipynb": '''\
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# YOLOv8 Training Notebook\\n",
              "Upload your YOLO-labeled dataset and train the model here."]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["!pip install -q ultralytics roboflow"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["from ultralytics import YOLO\\n",
              "# Replace 'dataset/data.yaml' with your Roboflow dataset path\\n",
              "model = YOLO('yolov8n.pt')  # nano model for fast prototyping\\n",
              "model.train(data='dataset/data.yaml', epochs=30, imgsz=640, batch=16)"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Download trained weights\\n",
              "model_path = 'runs/detect/train/weights/best.pt'\\n",
              "from google.colab import files\\n",
              "files.download(model_path)"]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
''',

    f"{project_name}/requirements.txt": "streamlit\nultralytics\nopencv-python\n",
    f"{project_name}/output.json": "{}\n",
    f"{project_name}/breed_reference.json": json.dumps({
        "Murrah": {"length_to_height_ratio":2.3,"notes":"Popular Indian dairy buffalo"},
        "Surti": {"length_to_height_ratio":2.2,"notes":"Smaller buffalo, Western India"},
        "Nili-Ravi": {"length_to_height_ratio":2.25,"notes":"Punjab/Pakistan buffalo"},
        "Gir": {"length_to_height_ratio":2.1,"notes":"Indian Gir cattle"},
        "Jersey": {"length_to_height_ratio":2.0,"notes":"Small-medium international dairy breed"},
        "HF_cross": {"length_to_height_ratio":2.0,"notes":"Holstein-Friesian crossbreed"}
    }, indent=2)
}

# Create files and write content
for filepath, content in files_content.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filepath}")

print("\n✅ Full project skeleton with starter code and breed_reference.json created!")
print(f"Next steps:\n1. Open {project_name} in VS Code/HappyFace.\n2. Add your YOLO dataset.\n3. Train model in Colab or use existing best.pt.\n4. Run 'streamlit run app.py'.")
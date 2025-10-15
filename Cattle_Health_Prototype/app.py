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
    # Using pre-trained YOLOv8 model (will auto-download if not present)
    return YOLO("yolov8n.pt")  # You can also use yolov8s.pt, yolov8m.pt, etc.

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

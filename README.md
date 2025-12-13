# GPR B-Scan Visualization & Analysis Toolkit

A Python-based toolkit for visualizing and exploring **Ground Penetrating Radar (GPR) B-scan images**.  
This repository is intended for **subsurface perception research**, **robotic sensing pipelines**, and **pre–machine learning data inspection**.

The toolkit enables fast qualitative analysis of GPR datasets, validation of augmented data, and basic feature highlighting useful for downstream perception and Physical AI systems.

---

## 🚀 Features

- **Class-wise visualization**
  - Displays representative GPR samples from multiple subsurface categories.

- **Sequential B-scan playback**
  - Plays ordered radar frames like a video to simulate spatial scanning.

- **Original vs Augmented comparison**
  - Side-by-side inspection to verify augmentation quality and realism.

- **Heatmap visualization**
  - Enhances radar signal intensity to highlight strong reflectors and anomalies.

- **Edge detection demo**
  - Uses classical image processing to emphasize utilities and structural patterns.

---

## 📁 Dataset Directory Structure
GPR_data/
│
├── intact/
│ ├── image_001.jpg
│ ├── image_002.jpg
│
├── Utilities/
│ ├── image_001.jpg
│ ├── image_002.jpg
│
├── cavities/
│ ├── image_001.jpg
│ ├── image_002.jpg
│
├── augmented_intact/
├── augmented_utilities/
└── augmented_cavities/

---

## 🧪 Visualizations Included

| Visualization | Description |
|---------------|-------------|
| Class Summary | Quick qualitative overview of subsurface classes |
| Sequence Playback | Simulated radar scanning across spatial frames |
| Original vs Augmented | Validation of synthetic or augmented data |
| Heatmap Mode | Signal strength enhancement for clearer interpretation |
| Edge Detection | Utility and anomaly highlighting |

---

## ⚙️ Requirements

Install required Python dependencies:
```bash
pip install numpy matplotlib opencv-python

📜 License

This project is provided for research and educational use.



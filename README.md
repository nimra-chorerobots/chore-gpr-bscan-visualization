# GPR B-Scan Dataset: Visualization and Qualitative Analysis

This repository provides a **Ground Penetrating Radar (GPR) B-scan dataset and visualization toolkit** for qualitative analysis of subsurface structures, including **intact ground**, **buried utilities**, and **cavity-like anomalies**.

The dataset consists of **pre-rendered 2D GPR B-scan images**, accompanied by a Python-based visualization pipeline designed to inspect data quality, validate augmentation, and highlight physically meaningful radar features prior to machine learning or robotic perception tasks.

---

## 📌 Dataset Overview

Ground Penetrating Radar (GPR) is widely used for subsurface inspection due to its ability to detect buried objects and material discontinuities.  
This dataset focuses on **visual separability and interpretability of GPR signatures**, rather than raw signal reconstruction.

The provided data supports:
- Subsurface perception research
- Robotics and autonomous inspection
- Pre-ML data validation and augmentation verification
- Teaching and demonstration of GPR phenomenology

---

## 📂 Dataset Structure

The dataset is organized into semantic subsurface classes, with both original and augmented Ground Penetrating Radar (GPR) B-scan images.

```text
GPR_data/
├── intact/
│   ├── image_001.jpg
│   ├── image_002.jpg
│   └── ...
├── utilities/
│   ├── image_001.jpg
│   ├── image_002.jpg
│   └── ...
├── cavities/
│   ├── image_001.jpg
│   ├── image_002.jpg
│   └── ...
├── augmented_intact/
│   ├── image_001.jpg
│   ├── image_002.jpg
│   └── ...
├── augmented_utilities/
│   ├── image_001.jpg
│   ├── image_002.jpg
│   └── ...
└── augmented_cavities/
    ├── image_001.jpg
    ├── image_002.jpg
    └── ...
 
---
### Class Descriptions

- **Intact**  
  Uniform, horizontally layered radar responses with no dominant hyperbolic reflections.

- **Utilities**  
  Strong, localized hyperbolic signatures corresponding to buried pipes, cables, or similar structures.

- **Cavities**  
  Irregular, high-frequency and chaotic radar patterns indicative of voids or subsurface discontinuities.

Augmented folders contain synthetically modified samples generated to increase data diversity while preserving physical realism.

---

## 🧪 Visualization Pipeline

The repository includes a Python script (`GPR_view.py`) that provides the following qualitative analysis tools:

### 1. Class Summary Visualization
Displays one representative sample from each subsurface class to verify visual separability and labeling correctness.
<img width="1500" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/b67f582b-c191-473e-9f96-74cf0eb19ad7" />

### 2. Sequential B-scan Playback
Plays ordered B-scan frames sequentially to simulate spatial radar scanning and verify continuity across frames.
<img width="1000" height="400" alt="Figure_2" src="https://github.com/user-attachments/assets/d615c60f-fe74-44f4-8df4-12c25f3ef384" />

### 3. Original vs Augmented Comparison
Side-by-side visualization to ensure augmentation preserves physically meaningful GPR features.
<img width="1200" height="400" alt="Figure_3" src="https://github.com/user-attachments/assets/7a023e17-b292-4723-8b0f-dfb4a4174959" />

### 4. Heatmap Visualization
Enhances signal intensity using color mapping to emphasize strong reflectors and subtle subsurface structures.
<img width="1000" height="400" alt="Figure_4" src="https://github.com/user-attachments/assets/930572de-6e2e-4382-bf68-d2b83cc26870" />

### 5. Edge-based Feature Extraction
Applies classical edge detection to highlight hyperbolic boundaries and structural features associated with buried utilities.
<img width="1200" height="400" alt="Figure_5" src="https://github.com/user-attachments/assets/5c173bf1-45e5-4221-a1f4-dce797868113" />

---

## 📊 Qualitative Results

Visual inspection of the dataset reveals:

- Clear visual distinction between intact ground, utilities, and cavities
- Consistent hyperbolic signatures for buried utilities
- Spatial continuity across consecutive B-scan frames
- Physically plausible augmented samples
- Extractable geometric features using classical image processing

These results confirm that the dataset is **suitable for downstream learning-based or hybrid physics–ML approaches**.

---
## 🎯 Intended Applications

GPR-based subsurface classification

Robotic perception and autonomy

Preprocessing and validation for deep learning

Dataset quality assurance

Academic teaching and demonstrations

## Project Status

🟢 Prototype

### Current Features

- GPR B-Scan visualization
- Sequential playback
- Heatmap generation
- Edge-based feature extraction
- Dataset inspection

### Planned

- ROS 2 integration
- Isaac Sim visualization
- Real-time GPR processing
- Underground object classification
- AI-based anomaly detection
  

## 📦 Dataset Access

The GPR B-scan dataset used in this repository is publicly available on **Mendeley Data**:

🔗 **Dataset link:**  
https://data.mendeley.com/datasets/ww7fd9t325/1

The dataset contains labeled GPR B-scan images categorized into intact ground, buried utilities, and cavities, along with augmented samples for data diversity.



## ⚙️ Requirements

Install the required Python dependencies:

```bash
pip install numpy matplotlib opencv-python


<br>
<div align="center">
  <h1>🧠 Efficient CT-Based Segmentation for LCLNM</h1>
  <p>
    <strong>YOLOv8 + Deformable Self-Attention (DSA) for Accurate Lateral Cervical Lymph Node Metastasis Detection</strong>
  </p>
</div>

<div align="center">
  <a href="https://github.com/yourusername/LCLNM-Segmentation">
    <img src="https://img.shields.io/badge/PyTorch-2.0%2B-red?logo=pytorch&logoColor=white" alt="PyTorch">
  </a>
  <a href="https://github.com/yourusername/LCLNM-Segmentation">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  </a>
</div>

---

## 📌 Overview

This repository provides the implementation of our paper:  
**"Efficient CT-Based Image Segmentation for Predicting Lateral Cervical Lymph Node Metastasis in Papillary Thyroid Carcinoma"**.

We propose a **YOLOv8-based medical image segmentation framework** enhanced with a **Deformable Self-Attention (DSA)** module to improve detection and delineation of metastatic lymph nodes from contrast-enhanced CT scans.  
The method achieves **spatially adaptive feature aggregation** while maintaining **real-time inference efficiency**, making it suitable for clinical applications.

---

## ✨ Key Features

- ⚡ **High Efficiency**: Lightweight YOLOv8 backbone optimized for medical CT segmentation.
- 🧩 **Deformable Self-Attention**: Dynamically adjusts receptive fields to handle structural variations.
- 🧠 **Clinical Applicability**: Targets lateral cervical lymph node metastasis (LCLNM) in papillary thyroid carcinoma.
- 📊 **Scalable Design**: Provides a foundation for future volumetric reconstruction and immersive 3D visualization.

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/binbin1021/Predicting-Lateral-Cervical-Lymph-Node-Metastasis.git
cd ultralytics
pip install -e '.[dev]'

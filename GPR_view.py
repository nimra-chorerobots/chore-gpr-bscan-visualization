# ============================================================
# GPR DATA VISUALIZATION & EXPLORATION SCRIPT
# Author: Nimra
# Purpose:
# - Visualize Ground Penetrating Radar (GPR) B-scan images
# - Inspect different subsurface classes (intact, utilities, cavities)
# - Compare original vs augmented data
# - Demonstrate basic feature extraction
# ============================================================

# ----------------------------
# IMPORT REQUIRED LIBRARIES
# ----------------------------

import os                  # For directory and file handling
import glob                # For matching file patterns (e.g., *.jpg)
import random              # For random image selection
import numpy as np         # Numerical operations
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2                 # OpenCV for image processing

# ============================================================
# CONFIGURATION SECTION
# ============================================================

# Root directory where all GPR image folders exist
# IMPORTANT: Change this path according to your system
BASE_DIR = r"D:\Chorerobotics\codes\GPR_data"

# Original GPR data classes
CLASSES = ["intact", "Utilities", "cavities"]

# Corresponding augmented data folders
AUG_CLASSES = [
    "augmented_intact",
    "augmented_utilities",
    "augmented_cavities"
]

# ============================================================
# 1️⃣ CLASS SUMMARY VISUALIZATION
# ============================================================
# Displays ONE random image from each class side-by-side
# This gives a quick overview of how different subsurface
# categories visually look in GPR scans
# ============================================================

def show_class_summary():

    # Create a figure with one subplot per class
    fig, axes = plt.subplots(1, len(CLASSES), figsize=(15, 5))

    # Loop through each class and its corresponding axis
    for ax, cls in zip(axes, CLASSES):

        # Build full folder path for the class
        folder = os.path.join(BASE_DIR, cls)

        # Get all JPG images in that folder
        img_files = glob.glob(os.path.join(folder, "*.jpg"))

        # If no images are found, show warning text
        if not img_files:
            ax.set_title(f"No images in {cls}")
            ax.axis("off")
            continue

        # Randomly select one image
        img_path = random.choice(img_files)

        # Read the image
        img = mpimg.imread(img_path)

        # Display image
        ax.imshow(img, cmap="gray")
        ax.set_title(
            f"{cls}\n({os.path.basename(img_path)})",
            fontsize=10
        )
        ax.axis("off")

    plt.suptitle(
        "GPR CATEGORY SUMMARY (Intact / Utilities / Cavities)",
        fontsize=14
    )
    plt.tight_layout()
    plt.show()

# ============================================================
# 2️⃣ VIDEO-LIKE PLAYBACK OF B-SCAN SEQUENCES
# ============================================================
# Plays all images in a folder sequentially
# Simulates how GPR scans evolve spatially (like a radar sweep)
# ============================================================

def play_sequence(class_name="Utilities", speed=0.05):

    folder = os.path.join(BASE_DIR, class_name)

    # Sort images to maintain spatial order
    img_files = sorted(glob.glob(os.path.join(folder, "*.jpg")))

    print(f"[INFO] {class_name}: {len(img_files)} frames found")

    # Turn interactive mode ON for animation
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 4))

    for i, img_path in enumerate(img_files):

        img = mpimg.imread(img_path)

        ax.clear()
        ax.imshow(img, cmap="gray", aspect="auto")
        ax.set_title(
            f"{class_name} – frame {i+1}/{len(img_files)}",
            fontsize=12
        )
        ax.axis("off")

        # Pause controls playback speed
        plt.pause(speed)

    # Turn interactive mode OFF
    plt.ioff()
    plt.show()

# ============================================================
# 3️⃣ ORIGINAL VS AUGMENTED IMAGE COMPARISON
# ============================================================
# Shows side-by-side comparison to verify:
# - Data augmentation realism
# - Structural feature preservation
# ============================================================

def compare_original_augmented(cls="Utilities"):

    orig_folder = os.path.join(BASE_DIR, cls)
    aug_folder = os.path.join(BASE_DIR, "augmented_" + cls.lower())

    orig_files = glob.glob(os.path.join(orig_folder, "*.jpg"))
    aug_files = glob.glob(os.path.join(aug_folder, "*.jpg"))

    if not orig_files or not aug_files:
        print("Original or augmented files missing.")
        return

    # Random sample from both sets
    orig = mpimg.imread(random.choice(orig_files))
    aug = mpimg.imread(random.choice(aug_files))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].imshow(orig, cmap="gray")
    axes[0].set_title("Original " + cls)
    axes[0].axis("off")

    axes[1].imshow(aug, cmap="gray")
    axes[1].set_title("Augmented " + cls)
    axes[1].axis("off")

    plt.suptitle(
        f"Original vs Augmented Image – {cls}",
        fontsize=14
    )
    plt.show()

# ============================================================
# 4️⃣ HEATMAP VISUALIZATION
# ============================================================
# Converts grayscale GPR scan into heatmap
# Useful for highlighting strong reflectors
# ============================================================

def show_heatmap(class_name="Utilities"):

    folder = os.path.join(BASE_DIR, class_name)
    img_path = random.choice(glob.glob(os.path.join(folder, "*.jpg")))

    img = mpimg.imread(img_path)

    plt.figure(figsize=(10, 4))
    plt.imshow(img, cmap="inferno", aspect="auto")
    plt.title(
        f"HEATMAP MODE – {class_name}\n({os.path.basename(img_path)})"
    )
    plt.axis("off")
    plt.colorbar(label="Signal strength")
    plt.show()

# ============================================================
# 5️⃣ EDGE DETECTION DEMO (UTILITY HIGHLIGHTING)
# ============================================================
# Uses Canny edge detection to:
# - Emphasize hyperbolas
# - Highlight buried utilities
# - Demonstrate basic feature extraction
# ============================================================

def edge_detection_demo(class_name="Utilities"):

    folder = os.path.join(BASE_DIR, class_name)
    img_path = random.choice(glob.glob(os.path.join(folder, "*.jpg")))

    # Load image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Apply Canny Edge Detector
    edges = cv2.Canny(img, 50, 150)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].imshow(img, cmap="gray")
    axes[0].set_title("Original B-scan")
    axes[0].axis("off")

    axes[1].imshow(edges, cmap="gray")
    axes[1].set_title("Edge Detection (Utility Highlight)")
    axes[1].axis("off")

    plt.suptitle("Utility Feature Extraction Demo", fontsize=14)
    plt.show()

# ============================================================
# MAIN EXECUTION BLOCK
# ============================================================
# This ensures functions run only when script is executed
# directly (not when imported as a module)
# ============================================================

if __name__ == "__main__":

    print("Showing class summary...")
    show_class_summary()

    print("\nPlaying Utilities scan sequence...")
    play_sequence("Utilities")

    print("\nComparing original vs augmented...")
    compare_original_augmented("Utilities")

    print("\nHeatmap visualization...")
    show_heatmap("Utilities")

    print("\nEdge detection demo...")
    edge_detection_demo("Utilities")

# 🖼️ Image Resizer & Converter Tool

A simple *Python + Pillow* script to batch resize, upscale, and/or convert images in a folder.  
Supports multiple image formats and preserves aspect ratio during resizing.

---

## 📌 Features
- *Resize* images to your desired size (downscale or upscale).
- *Preserve aspect ratio* so images don't look stretched.
- *Convert image format* (JPEG, PNG, BMP, TIFF, GIF, etc.).
- *Batch process* all images in a folder at once.
- *Choose mode*:
  1. Resize & Convert
  2. Resize Only
  3. Convert Only (no resize)

---

## 📂 Folder Structure
Image-Resizer-Tool/                                                                                                                                                          
│                                                                                                                                                                           
├── image_tool.py # The Python script                                                                                                                                      
├── input_images/ # Folder containing original images                                                                                                                   
└── output_images/ # Folder for processed images (auto-created)                                                                                                        

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
Make sure Python is installed, then install Pillow:
```bash
pip install pillow
```
### 2️⃣ Add Your Images
Place all the images you want to process inside:

input_images/

### 3️⃣ Run the Script
```bash
python image_tool.py
```

### 4️⃣ Follow the Prompts
Example:

```pgsql
=== Image Resizer & Converter Tool ===
1 - Resize & Convert
2 - Resize Only
3 - Convert Only (no resize)
Choose mode (1/2/3): 1

Enter new width (px): 800
Enter new height (px): 600
Enter output format (JPEG, PNG, etc.): JPEG
```

## 📝 Example Usage
#### Example 1: Resize & Convert
- Input: photo.png (1600×1200)
- Mode: 1
- Size: 800×600
- Format: JPEG
- Output: photo.jpeg (800×600) in output_images/

#### Example 2: Resize Only
- Input: photo.png (1600×1200)
- Mode: 2
- Size: 800×600
- Output: photo.png (800×600) in output_images/

#### Example 3: Convert Only
- Input: photo.png
- Mode: 3
- Format: JPEG
- Output: photo.jpeg in output_images/


## ⚠️ Notes
- Upscaling works, but quality may decrease for small images enlarged too much.                                                                                     
- For better upscaling quality, consider AI upscalers like Real-ESRGAN.                                                                                                  
- Supported formats: .jpg, .jpeg, .png, .bmp, .tiff, .gif.                                                                                                               

## 📜 License
This script is free to use and modify for personal or commercial projects.


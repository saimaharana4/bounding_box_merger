---

# Bounding Box Merger Project

## Overview
The Bounding Box Merger Project aims to streamline the process of merging closely related bounding boxes in images of spreadsheets. Utilizing Optical Character Recognition (OCR) and data science algorithms, this project reads bounding box coordinates from images, identifies pairs of coordinates that are closely related, and merges them into a single bounding box.

## Getting Started

### Prerequisites
- Python 3.8+
- Tesseract OCR
- Libraries: pandas, OpenCV, pytesseract, scikit-learn

### Installation
1. **Install Tesseract OCR:**
   - Windows: Download and install from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
   - macOS/Linux: Use Homebrew or apt-get.
     ```
     brew install tesseract # macOS
     sudo apt-get install tesseract-ocr # Ubuntu/Linux
     ```
2. **Install Python Libraries:**
   ```
   pip install pandas opencv-python pytesseract scikit-learn
   ```

### Directory Structure
```
Bounding_Box_Merger_Project/
│
├── data/
│   ├── raw/
│   │   └── screening_data_csv.zip
│   │
│   ├── processed/
│   │   ├── images/
│   │   ├── bounding_boxes.csv
│   │   └── merged_bounding_boxes.csv
│
├── notebooks/
│   ├── 01_Data_Extraction_and_Preprocessing.ipynb
│   └── 02_Bounding_Box_Merging.ipynb
│
└── README.md
```

## Usage

1. **Prepare Your Data:** Place the `screening_data_csv.zip` file containing images inside the `data/raw/` directory.

2. **Data Extraction and Preprocessing:**
   - Navigate to the `notebooks/` directory.
   - Open and run `01_Data_Extraction_and_Preprocessing.ipynb` to extract bounding box data from images and save it as `bounding_boxes.csv` in the `data/processed/` directory.

3. **Bounding Box Merging:**
   - Continue in the `notebooks/` directory.
   - Open and execute `02_Bounding_Box_Merging.ipynb` to read the `bounding_boxes.csv`, merge related bounding boxes, and save the merged coordinates to `merged_bounding_boxes.csv`.

## Contributing
We welcome contributions! Please feel free to fork this project, make your changes, and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE).

---

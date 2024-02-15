# Bounding Box Merging Project

## Overview
This project automates the process of identifying and merging closely related bounding boxes extracted from images of Excel sheets using Optical Character Recognition (OCR) and clustering algorithms. It streamlines data extraction from structured documents, enhancing data processing efficiency.

## Project Structure
```
bounding_box_merger/
│
├── data/
│   ├── processed/
│   │   ├── csv/
│   │   │   ├── list_a.csv                                      # Extracted bounding boxes from List A
│   │   │   ├── list_b.csv                                      # Extracted bounding boxes from List B
│   │   │   └── merged_boxes.csv                                # Merged bounding boxes
│   │   └── images/
│   │       ├── List_A/                                         # Images for List A
│   │       └── List_B/                                         # Images for List B
│   └── raw/
│       └── screening_data_csv.zip                              # ZIP file containing original images
│
├── notebooks/
│        ├── 01_Data_Extraction_and_Preprocessing.ipynb         # Created the pipeline  to extract and preprocess the data
│        └── 02_Bounding_Box_Merging.ipynb                       # Data Science model implemented
│                      
├── src/
│   ├── data_extraction.py                                      # Script for OCR-based data extraction
│   ├── clustering_and_merging.py                               # Script for clustering and merging bounding boxes
│   └── visualization.py                                        # Script for visualizing bounding boxes
│
├── Documentation.docx                                          # Project Objective and implementation method
├── README.md                                                   # Project documentation
└── requirements.txt                                            # Python dependencies
```

## Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/saimaharana4/bounding_box_merger.git
   cd bounding_box_merger
   ```

2. **Create and activate a virtual environment**

   - For Windows:

     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```sh
     python3 -m venv venv
     source venv/bin/activate

3. **Ensure Python 3.x is installed. Install necessary Python libraries:**

      ```sh
      pip install -r requirements.txt
      ```

## Usage

### Data Extraction

1. **Prepare Your ZIP File**: Place the ZIP file containing images in the `data/raw` directory.
2. **Run OCR Script**: Extract and save bounding box coordinates to CSV files.

```sh
python src/data_extraction.py
```

### Clustering and Merging

1. **Adjust Paths**: Ensure CSV paths in `clustering_and_merging.py` point to your extracted data.
2. **Run Clustering and Merging Script**: Process the extracted bounding boxes.

```sh
python src/clustering_and_merging.py
```

### Visualization

1. **Set Image and CSV Paths**: In `visualization.py`, adjust `image_path` and `boxes_csv_path` to your files.
2. **Visualize**: Overlay bounding boxes on images.

```sh
python src/visualization.py
```

### Evaluation

1. **Run Evaluation Metrics**: Compute performance metrics against DBSCAN inial model with tuned model.

## Algorithms Used

- **OCR**: Tesseract OCR for text and bounding box extraction.
- **Clustering**: DBSCAN for identifying groups of closely related bounding boxes.
- **Standardization**: StandardScaler from scikit-learn for feature scaling.

## Evaluation Metrics

- **Calinski-Harabasz Index**: Ratio of between-clusters to within-cluster dispersion.
- **Davies-Bouldin Index**: Average similarity of each cluster with its most similar cluster.


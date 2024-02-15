import os
import cv2
import zipfile
import pandas as pd
import pytesseract
from pathlib import Path
import re

def process_images(zip_file_path, destination_path, tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)
    print(f"Files extracted to {destination_path}")

    source_dir = Path(destination_path, "screening_data_csv_1")
    list_a_dir = Path(destination_path, "List_A")
    list_b_dir = Path(destination_path, "List_B")

    list_a_dir.mkdir(parents=True, exist_ok=True)
    list_b_dir.mkdir(parents=True, exist_ok=True)

    for image_path in source_dir.glob('*.png'):
        image = cv2.imread(str(image_path))
        if image is None:
            print(f"Error: Unable to load image at {image_path}")
            continue

        split_col_index = int(image.shape[1] * 0.3)
        list_a_image = image[:, :split_col_index]
        list_b_image = image[:, split_col_index:]
        list_a_image_path = list_a_dir / f'{image_path.stem}_list_a.png'
        list_b_image_path = list_b_dir / f'{image_path.stem}_list_b.png'
        cv2.imwrite(str(list_a_image_path), list_a_image)
        cv2.imwrite(str(list_b_image_path), list_b_image)

    def ocr_to_dataframe(image_path, pattern):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_image)
        matches = re.findall(pattern, text)
        return pd.DataFrame(matches, columns=['x1', 'y1', 'x2', 'y2']).astype(int)

    pattern = r'\[?\(?(\d+), (\d+), (\d+), (\d+)\)?\]?'
    df_list_a = pd.DataFrame()
    df_list_b = pd.DataFrame()

    for image_path in list_a_dir.glob('*.png'):
        df_list_a = pd.concat([df_list_a, ocr_to_dataframe(str(image_path), pattern)], ignore_index=True)

    for image_path in list_b_dir.glob('*.png'):
        df_list_b = pd.concat([df_list_b, ocr_to_dataframe(str(image_path), pattern)], ignore_index=True)

    print(f"List A DataFrame shape: {df_list_a.shape}")
    print(f"List B DataFrame shape: {df_list_b.shape}")

    list_a_csv_path = "data/processed/csv/list_a.csv"
    list_b_csv_path = "data/processed/csv/list_b.csv"

    df_list_a.to_csv(list_a_csv_path, index=False)
    df_list_b.to_csv(list_b_csv_path, index=False)

    print(f"List A DataFrame saved to {list_a_csv_path}")
    print(f"List B DataFrame saved to {list_b_csv_path}")

if __name__ == "__main__":
    zip_file_path = r"D:\bounding_box_merger\data\raw\screening_data_csv.zip"
    destination_path = r"D:\bounding_box_merger\data\processed\images"
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    process_images(zip_file_path, destination_path, tesseract_path)
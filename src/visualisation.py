import cv2
import pandas as pd
from pathlib import Path

def draw_bounding_boxes(image_path, boxes, color=(255, 0, 0), thickness=2):
    """
    Draws bounding boxes on an image and displays it.
    
    Parameters:
    - image_path: Path to the original image.
    - boxes: DataFrame or list of bounding boxes with columns/elements [x1, y1, x2, y2].
    - color: Box color.
    - thickness: Line thickness.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return

    # Draw each bounding box on the image
    for _, box in boxes.iterrows():
        start_point = (int(box['x1']), int(box['y1']))
        end_point = (int(box['x2']), int(box['y2']))
        cv2.rectangle(image, start_point, end_point, color, thickness)

    # Display the image
    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(0)  # Wait for a key press to close
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage
    image_path = r"D:\bounding_box_merger\data\test\screening_data_csv_1_page_1.png"
    boxes_csv_path = r"D:\bounding_box_merger\data\processed\csv\merged_boxes.csv"  # Path to the CSV file containing bounding boxes

    # Load bounding boxes from CSV
    boxes_df = pd.read_csv(boxes_csv_path)

    # Draw bounding boxes on the image
    draw_bounding_boxes(image_path, boxes_df)

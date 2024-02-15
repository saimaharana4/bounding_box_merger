import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

def load_data(csv_path):
    return pd.read_csv(csv_path)

def cluster_bounding_boxes(df):
    # Calculate the center of each bounding box to use for clustering
    df['center_x'] = (df['x1'] + df['x2']) / 2.0
    df['center_y'] = (df['y1'] + df['y2']) / 2.0
    
    # Use only the center points for clustering
    X = df[['center_x', 'center_y']].values
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=0.6, min_samples=3)
    clusters = dbscan.fit_predict(X_scaled)
    
    return clusters

def merge_bounding_boxes(df, clusters):
    df['cluster'] = clusters
    
    # Initialize an empty list to hold the merged bounding boxes
    merged_boxes = []
    
    for cluster in set(clusters):
        if cluster == -1:  # Skip noise points
            continue
        cluster_df = df[df['cluster'] == cluster]
        
        # Calculate the minimum enclosing bounding box
        min_x = cluster_df['x1'].min()
        min_y = cluster_df['y1'].min()
        max_x = cluster_df['x2'].max()
        max_y = cluster_df['y2'].max()
        
        merged_boxes.append([min_x, min_y, max_x, max_y])
    
    # Convert the merged bounding boxes into a DataFrame
    merged_df = pd.DataFrame(merged_boxes, columns=['x1', 'y1', 'x2', 'y2'])
    return merged_df

if __name__ == "__main__":
    list_a_csv_path = r"D:\bounding_box_merger\data\processed\csv\list_a.csv"
    list_b_csv_path = r"D:\bounding_box_merger\data\processed\csv\list_b.csv"
    
    # Load data
    df_list_a = load_data(list_a_csv_path)
    df_list_b = load_data(list_b_csv_path)
    
    # Concatenate List A and List B data for clustering
    df_combined = pd.concat([df_list_a, df_list_b], ignore_index=True)
    
    # Cluster bounding boxes
    clusters = cluster_bounding_boxes(df_combined)
    
    # Merge bounding boxes within each cluster
    merged_df = merge_bounding_boxes(df_combined, clusters)
    
    # Save merged bounding boxes to CSV
    merged_csv_path = r"D:\bounding_box_merger\data\processed\csv\merged_boxes.csv"
    merged_df.to_csv(merged_csv_path, index=False)
    print(f"Merged bounding boxes saved to {merged_csv_path}")

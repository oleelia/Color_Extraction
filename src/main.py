#pip install Pillow
#pip install scikit-learn
#pip install matplotlib
#pip install -U pyinstaller

from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import os
import matplotlib.pyplot as plt

def extract_colors(image_path, num_colors=5):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Reshape the array to a list of pixels
    pixels = image_array.reshape((-1, 3))

    # Use k-means clustering to find dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors_rgb = kmeans.cluster_centers_.astype(int)

    # Convert RGB to hex
    colors_hex = ['#%02x%02x%02x' % (r, g, b) for r, g, b in colors_rgb]

    # Get the labels for each pixel (which cluster it belongs to)
    labels = kmeans.labels_

    # Count the occurrence of each label
    label_counts = np.bincount(labels)

    # Calculate percentages
    total_pixels = np.prod(image_array.shape[:2])
    percentages = label_counts / total_pixels

    return colors_hex, percentages

def main():
    # get image path and save to variable
    os.system("cls")
    image = input("What image do you want to scan?\n")
    image_path = "images/" + image

    os.system("cls")
    num_colors = (int)(input("How many hex codes do you want?\n"))

    colors, percentages = extract_colors(image_path, num_colors)
    os.system("cls")
    print("Dominant colors in hex codes:", colors)
    
    # Create a pie chart
    plt.figure(figsize=(5, 5))
    plt.pie(percentages, labels=colors, colors=colors, startangle=90, autopct='%1.1f%%')
    plt.axis("equal")
    plt.title("Dominant Colors")
    plt.show()
    
    # keeps window open
    input("Press enter to exit...")

if __name__ == "__main__":
    main()
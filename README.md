#Content-Based-Image-Retrieval-Using-Radon-Barcode

This project demonstrates the use of **Radon barcodes** for content-based image retrieval on a dataset of handwritten digits (0–9), with ten images per digit (total of 100 images). Each image is converted into a 162-bit “barcode,” which can then be compared via **Hamming distance** to find the most similar image. By running multiple searches, you can measure the retrieval accuracy and explore methods to increase it.

---

## How to Run

1. **Clone or Download** this repository into a local directory.  
2. **Install Dependencies** (Python 3.x, NumPy, Pillow):
   ```bash
   pip install numpy pillow
## Generate Barcodes

Run the `Barcode_Generator.py` file (edit the code to switch between generating barcodes for one image or for all):

```bash
python Barcode_Generator.py

Barcodes will be saved in your chosen file format (JSON or TXT).

## Search for Matches

Run the `Search_Algorithm.py` file to compare a chosen image’s barcode with the rest of the dataset:

```bash
python Search_Algorithm.py

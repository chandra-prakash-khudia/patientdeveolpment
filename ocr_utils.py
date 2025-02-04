import cv2
from paddleocr import PaddleOCR

def sort_text_row_col(image_path: str) -> list:
    """Extracts and sorts text from image using PaddleOCR."""
    ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)
    results = ocr.ocr(image_path)
    
    extracted_data = []
    for line in results[0]:
        box = line[0]
        text = line[1][0]
        y_center = (box[0][1] + box[2][1]) / 2
        x_center = (box[0][0] + box[2][0]) / 2
        extracted_data.append((y_center, x_center, text))
    
    extracted_data.sort(key=lambda item: (item[0], item[1]))
    
    row_tolerance = 15
    rows = []
    current_row = []
    
    for i, data in enumerate(extracted_data):
        if i == 0 or abs(data[0] - extracted_data[i-1][0]) < row_tolerance:
            current_row.append(data)
        else:
            rows.append(current_row)
            current_row = [data]
    if current_row:
        rows.append(current_row)
    
    return [[item[2] for item in sorted(row, key=lambda x: x[1])] for row in rows]

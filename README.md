# Plant Leaf Identification and Peppermint Classification

## Overview:
This repository contains the implementation of a deep learning-based model for plant leaf identification and peppermint classification. The project aims to accurately identify various plant leaves and classify peppermint samples into 'Dried', 'Fresh', and 'Spoiled' categories. The model utilizes transfer learning with the VGG16 architecture and extensive data preprocessing techniques to achieve high accuracy and robust performance.

## Methodology:
1. **Identification Model:** 
   - Dataset Preparation: Diverse dataset collection, preprocessing, and augmentation.
   - Model Architecture: Transfer learning with VGG16, custom classification layers.
   - Training Procedure: Adam optimizer, evaluation metrics monitoring.

2. **Classification Model:** 
   - Dataset Description: Peppermint-specific dataset curation and preprocessing.
   - Model Architecture: Transfer learning with VGG16, customization for peppermint classification.
   - Training Process: Similar to the identification model.

3. **Evaluation and Testing:**
   - Evaluation Metrics: Accuracy, precision, recall, F1-score.
   - Confusion Matrix: Visual representation of model predictions.
   - Testing: Evaluation on separate test datasets.

4. **Model Deployment:**
   - Models saved in HDF5 format for future use.
   - Detailed documentation for model loading and integration.

## Experimental Setup:
- **Identification Results:** High accuracy (99.65%) and robust performance across classes.
- **Classification Results:** Testing accuracy (97.74%) and F1-score (97.73%) indicating accurate categorization of peppermint samples.

## Conclusion:
The implemented models demonstrate exceptional performance in plant leaf identification and peppermint classification tasks. The high accuracy rates and balanced F1-scores validate their effectiveness for real-world applications in industries such as agriculture, food processing, and pharmaceuticals.

## Contributors:
- Yashashree Sagar Bedmutha 

## License:
This project is licensed under the MIT License.

## Contact:
For any inquiries or support, please contact [yashashree.bedmutha@gmail.com].

## Acknowledgements:
We acknowledge the support and guidance from Prof Kailas Patil and Yogesh Suryawanshi.

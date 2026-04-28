# Customer Churn Prediction using Telco Customer Churn Dataset

This project analyzes the Telco Customer Churn dataset and develops machine learning classification models to predict whether a customer is likely to leave the service.

## Dataset
- Original rows: 7043
- Original columns: 21
- Missing TotalCharges rows removed: 11
- Target variable: Churn

## Models
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors Classifier

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

## Best Model
Best model by F1-score in this run: **Random Forest**

## Results

| Model               |   Accuracy |   Precision |   Recall |   F1 Score |   ROC-AUC |
|:--------------------|-----------:|------------:|---------:|-----------:|----------:|
| Random Forest       |   0.75764  |    0.530055 | 0.778075 |   0.630553 |  0.83607  |
| Logistic Regression |   0.729922 |    0.494966 | 0.78877  |   0.608247 |  0.837125 |
| Decision Tree       |   0.711443 |    0.474684 | 0.802139 |   0.596421 |  0.811352 |
| KNN                 |   0.791756 |    0.615385 | 0.57754  |   0.595862 |  0.818938 |

## Files
- `MIS308_Customer_Churn_Project.ipynb`: Main analysis notebook
- `MIS308_Customer_Churn_Project_Report.docx`: Project report
- `WA_Fn-UseC_-Telco-Customer-Churn.csv`: Dataset
- `best_churn_model.pkl`: Saved best model pipeline

## Local Run Instructions

To run the Streamlit application locally, the following files should be in the same folder:

- streamlit_app.py
- best_churn_model.pkl
- requirements.txt

Then, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
- 

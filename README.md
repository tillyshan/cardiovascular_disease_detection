# Project: cardiovascular diseases detection

**Description:**
Developed a machine learning model to predict the presence of cardiovascular disease in patients based on a comprehensive dataset. 

 Business Requirement 1:
- Consider our client in a private hospital; their requirement is to identify all patients with the disease as accurately as possible. They are okay with some misidentifications regarding positive patients, as it does not pose a threat to the patients' lives.

 Business Requirement 2:
- Consider our client, an online medicine shop. They wish to offer a 50 percent discount on specific medicines to customers who have a disease. Their requirement is to send the discount offer via email only to customers with a disease.
 
**Technologies and Libraries:**
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Streamlit

**Key Steps:**
1. **Understand the Data:** Thoroughly analyzed the dataset to understand its structure and characteristics.
2. **Exploratory Data Analysis:** Further analyzed data set using different charts, summaries. 
3. **Data cleaning:** Performed data cleaning to handle missing values, duplicate entries, and inconsistent data. Identified and removed outliers that could impact model performance.
4. **Data Preprocessing:** Applied feature scaling techniques to standardize feature values.Encoded categorical features for compatibility with machine learning algorithms.
6. **Model Evaluation:** Implemented logistic regression, linear SVM, random forest, and GaussianNB models.
7. **Ensemble Methods:** Utilized a hard voting classifier to combine the strengths of multiple models.
8. **Performance Comparison:** Compared the performance of different models based on various metrics.
9. **Model Selection:** Chose the best performing model.
10. **Hyper Parameter Tuning:** Further improve model performances by tuning hyper parameters.
11. **Test the model on unseen Data** Model was tested on test set
12. **Build eb Application** Build interactive web application using streamlit

Please visit the [repository](https://github.com/tillyshan/Heart-Disease-detection/blob/main/heart%20disease%20detection.ipynb) for the Code.

### Model Selection and Web Application

After evaluating multiple machine learning models, the final model was selected based on its performance, with a focus on recall for the positive class, ensuring accurate identification of heart disease patients.

#### Best Model: [Logistic Regression]

To make the model accessible and user-friendly, a basic web application was created using the Streamlit library. The application allows users to input relevant data and get predictions regarding the likelihood of heart disease. It provides a basic user-friendly interface.

Please visit the [repository](https://github.com/tillyshan/Heart-Disease-detection/blob/main/web%20application.py) for the model.

![App interface](https://github.com/tillyshan/Heart-Disease-detection/blob/main/image.png)


### Usage
To run the Heart Disease Detection application, follow these steps:

1. **Clone the Repository:** Clone the GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/tillyshan/Heart-Disease-detection.git
    ```

2.**Run the Application:** Start the application by running the following command in your Anaconda Prompt, Command Prompt, or PyCharm Terminal:

   ```bash
   streamlit run web application.py
   ```

3. **Access the Application:** Open a web browser and navigate to the URL provided in the terminal (usually, it will be something like http://localhost:8501). You will see the user-friendly interface where you can enter your details.

Please note that the application is for demonstration and educational purposes.

### Future Enhancements
"The model achieves a 70% accuracy rate. Various models and model combinations can be employed to enhance performance."

This README provides an overview of the "Heart Disease Detection" project, highlighting its key components and the development of a user-friendly web application for predicting heart disease. For more detailed information and access to the code, please visit the [repository] (https://github.com/tillyshan/Heart-Disease-detection)).

This project showcased the significance of prioritizing recall for the positive class in the context of heart disease detection, emphasizing the accurate identification of patients at risk. It demonstrated the effective use of machine learning and data preprocessing techniques to build a robust predictive model for healthcare applications.


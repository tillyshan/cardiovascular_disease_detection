# Project: cardiovascular diseases detection

## Description:
Developed a machine learning model to predict the presence of cardiovascular disease in patients based on a comprehensive dataset. 

 Business Requirement 1:
- Consider our client in a private hospital; their requirement is to identify all patients with the disease as accurately as possible. They are okay with some misidentifications regarding positive patients, as it does not pose a threat to the patients' lives.

 Business Requirement 2:
- Consider our client, an online medicine shop. They wish to offer a 50 percent discount on specific medicines to customers who have a disease. Their requirement is to send the discount offer via email only to customers with a disease.

 **Interactive APP:**
- Built an interactive web application using sreamlit framework.
  
![APP Interface](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/gif.gif)


## Technologies and Libraries:
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Streamlit

## Key Steps:

### Understand the Data:
Data set has 70,000 data points and 12 features.
<h4><font color='purple'>There are 3 types of input features:</font></h4>
<ul>
    <li>Objective: factual information;</li>
    <li>Examination: results of medical examination;</li>
    <li>Subjective: information given by the patient.</li>
</ul>

<h4><font color = 'purple'>Features:</font></h4>
<ul>
    <li>Age | Objective Feature | age | int (days)|</li>
    <li>Height | Objective Feature | height | int (cm) |</li>
    <li>Weight | Objective Feature | weight | float (kg) |</li>
    <li>Gender | Objective Feature | gender | categorical code |</li>
    <li>Systolic blood pressure | Examination Feature | ap_hi | int |</li>
    <li>Diastolic blood pressure | Examination Feature | ap_lo | int |</li>
    <li>Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |</li>
    <li>Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |</li>
    <li>Smoking | Subjective Feature | smoke | binary |</li>
    <li>Alcohol intake | Subjective Feature | alco | binary |</li>
    <li>Physical activity | Subjective Feature | active | binary |</li>
    <li>Presence or absence of cardiovascular disease | Target Variable | cardio | binary |</li>
</ul>

- **Systolic blood pressurepressure:** pressure during the heart's contraction or systole.
- **Diastolic blood pressure:** pressure when the heart is at rest or between beats during diastole.
  
<font color='purple'>**All of the dataset values were collected at the moment of medical examination.**</font>

### Exploratory Data Analysis:
Further analyzed data set using different charts, summaries.

![](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/images/image1.png)

### Data cleaning:
Performed data cleaning to handle missing values, duplicate entries, and inconsistent data. Identified and removed outliers that could impact model performance. When removing outliers for blood pressure values, consider the standards rather than a specific method for detecting outliers.

**Standards for Minimum and Maximum Values for Detecting Outliers in Diastolic Blood Pressure:**
**For Adults (18 and Older):**
- *Lower Limit:* 40 mmHg or lower
- *Upper Limit:* 110 mmHg or higher

**For Older Adults (65 and Older):**
- *Lower Limit:* 30 mmHg or lower
- *Upper Limit:* 100 mmHg or higher
or higher

**Standards for Minimum and Maximum Values for Detecting Outliers in Systolic Blood Pressure:**

**For Adults (18 Years and Older):**
- *Lower Limit:* 60 mmHg or lower
- *Upper Limit:* 220 mmHg or higher

**For Older Adults (65 Years and Older):**
- *Lower Limit:* 50 mmHg or lower
- *Upper Limit:* 200 mmHg or higher
or higheror higher

![](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/images/image2.png)

## Data Preprocessing:
Applied feature scaling techniques to standardize feature values.Encoded categorical features for compatibility with machine learning algorithms.

## Model Evaluationon Base line Scores:
Implemented logistic regression, linear SVM, random forest, and GaussianNB models.

![](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/images/image4.png)

## Try Ensemble Methods:
Utilized a hard voting classifier to combine the strengths of multiple models.

## Performance Comparison and model selection
Compared the performance of different models based on various metrics and Chose the best performing model.

## Hyper Parameter Tuning:
Further improve model performances by tuning hyper parameters. 

## Test the model on unseen Data
The model was tested on the test set. Check whether the model generalized well and evaluate its performance using various metrics.

Please visit the [repository](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/cardiovascular_disease_detection.ipynb)) for the Code.

## Completed model adjustments for two different business scenarios.

**Scenario 1:**

![](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/images/image5.png)

**Scenario 2:**

![](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/images/image6.png)

## Build Web Application
Build interactive web application using streamlit.

Please visit the [repository](https://github.com/tillyshan/Heart-Disease-detection/blob/main/heart%20disease%20detection.ipynb) for the Code.

### Model Selection and Web Application

After evaluating multiple machine learning models, the final model was selected based on its performance, with a focus on recall for the positive class, ensuring accurate identification of heart disease patients.

#### Best Model: [Logistic Regression]

To make the model accessible and user-friendly, a basic web application was created using the Streamlit library. The application allows users to input relevant data and get predictions regarding the likelihood of heart disease. It provides a basic user-friendly interface.

Please visit the [repository](https://github.com/tillyshan/cardiovascular_disease_detection/blob/main/app.py) for the app.

### Usage
To run the Cardiovascular Disease Detection app, follow these steps:

1. **Clone the Repository:** Clone the GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/tillyshan/cardiovascular_disease_detection.git
    ```

2.**Run the Application:** Start the application by running the following command in your Anaconda Prompt, Command Prompt, or PyCharm Terminal:

   ```bash
   streamlit run web app.py
   ```

3. **Access the Application:** Open a web browser and navigate to the URL provided in the terminal (usually, it will be something like http://localhost:8501). You will see the user-friendly interface where you can enter your details.

Please note that the application is for demonstration and educational purposes.

### Future Enhancements
"The model achieves a 70% accuracy rate. Various models and model combinations can be employed to enhance performance."

This README provides an overview of the " Cardiovascular Disease Detection" project, highlighting its key components and the development of a user-friendly web application for predicting heart disease. For more detailed information and access to the code, please visit the ![repository](https://github.com/tillyshan/cardiovascular_disease_detection).

This project showcased the significance of prioritizing recall for the positive class in the context of heart disease detection, emphasizing the accurate identification of patients at risk. It demonstrated the effective use of machine learning and data preprocessing techniques to build a robust predictive model for healthcare applications.


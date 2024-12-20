# Building-Machine-Learning-Pipeline-on-Startups-Acquisition-Status
This Project Focuses on understand the financial conditions of company fundraising goals.

## <br>**➲ The Objective** :
The objective of the project is to predict whether a startup which is currently Operating, IPO, Acquired, or closed.This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed.

## <br>**➲ Dataset**:

### Link to raw data(Huge JSON and Excel fiel):
           https://drive.google.com/file/d/1tWYkHYHm2HoiCajZ49Cs1K7sklWTdAbV/view?usp=sharing

## <br>**➲ Summary**:

The data contains industry trends, investment insights and individual company information. Since the data was acquired on a trial basis, it only contains information about companies. After training the model, we predict whether startups still operating, IPO, acquired, or closed.

## <br>**➲ Data types**:

The dataset includes the following key columns for model training:
* Entity Information: name, entity_type, category_code, etc.
* Status Information: status, founded_at, closed_at
* Company Financial Information: funding_total_usd, funding_rounds, first_investment_at, etc.
* Geographical Information: country_code, state_code, city, region
* Milestones and Relationships: milestones, relationships

-- The dataset also contains columns that provide additional context but are not directly useful for model training (such as created_at, updated_at, logo_url, etc).


## <br>**➲ Data Cleaning**:
In data cleaning we are will remove the inappropriate & unncessary information from raw data(main data).Hence, after which we’ll perform data cleaning involving following steps:
* Checking the percentage of NaN(null values) values present in each feature
* Removing duplicates
* Dropping columns which have NaN values.
* Remove unnecessary and corrupted data.
* Data Labelling.


  ## <br>**➲ Exploratory Data Analysis (EDA)**
<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Target Class for Binary Classification
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/cls_dis1.png' style='width: 50%; height:250px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Text Length in Ham Messages
       </summary>
                     <p align='center'>
                            <img src='' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Text Length in Spam Messages
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/project_branch/images/spam_distribution.png' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Ham & Spam Messages in the Dataset
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/project_branch/images/Ham_spam_dis.png' style='width: 50%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> WordCloud of Ham Message
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/project_branch/images/ham_wordcloud.png' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> WordCloud of Spam Message
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/project_branch/images/spam_wordcloud.png' style='width: 70%;' />
                     </p>
</details>

**Classification Report for Testing**
<p align='center'>
      <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/main/images/Report1.png' style='width: 58%;' />
</p>


**Confusion Matrix for Testing**
<p align='center'>
      <img src='https://github.com/Shuhaib73/NLP_Message_Spam-Ham_Classification/blob/main/images/testing_cls1.png' style='width: 58%;' />
</p>

## <br>**➲ Machine Learning Pipeline**:

-- The data preprocessing steps include:

           * Feature Selection: Identifying the relevant features from the raw data that will be used for model training.
           * Handling Missing Data: Imputing or removing missing values to ensure clean training data.
           * Normalization/Standardization: Scaling features to bring them to a similar range and avoid model bias.
           * Categorical Encoding: Encoding categorical variables (e.g., company industry, status) into numerical formats using techniques like one-hot encoding or label encoding.

## <br>**➲ Building and Training Model**:
-- The pipeline includes both binary and multiclass classification models, as the startup statuses need to be classified into one of several categories. The steps include:

           * Model Selection: Using suitable classifiers (e.g.Random Forest, XGBoost, etc.).
           * Model Training: Splitting the dataset into training and testing sets and training models on the training data.
           * Model Evaluation: Evaluating models using metrics like accuracy, precision, recall, and F1-score, among others.

## <br>**➲ Dockerization**:
-- The entire machine learning pipeline is dockerized, making it portable and easier to deploy in various environments. This involves:

           * Containerizing the model and pipeline using Docker to ensure consistency across different stages of development, testing, and production.

## <br>**➲ CI/CD Automation**:
           * Continuous Integration and Continuous Deployment (CI/CD) pipelines are implemented to automate the testing, building, and deployment of the model. This ensures that updates to the model or pipeline are smoothly integrated and deployed without manual intervention.

## <br>**➲ Website Development with Flask**:
-- In addition to model deployment, a Flask-based web application has been developed to interact with the trained model. This web application provides a user-friendly interface to input data, make predictions, and display the results. It communicates with the deployed model through RESTful APIs, ensuring that users can interact with the model in real-time.

## <br>**➲ Database Integration and Model Deployment**:
           * Once the models is trained and evaluated, I deployed the model using Amazon ECS (Elastic Container Service), ensuring scalability and easy access for real-time predictions. This setup allows the model to be accessed via APIs for making predictions in real-time, such as determining the status of new startups.

           * To manage and store company and user credentials securely, Amazon RDS (Relational Database Service) has been used. RDS provides scalable, managed storage for user data and startup-related information. It ensures that sensitive information is stored securely and can be easily accessed by the deployed application for real-time predictions.

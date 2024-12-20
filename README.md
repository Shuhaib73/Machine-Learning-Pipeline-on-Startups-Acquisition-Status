# Building-Machine-Learning-Pipeline-on-Startups-Acquisition-Status 🚀📊
**This Project Focuses on understand the financial conditions of company fundraising goals.**

## <br>**➲ The Objective** :
The objective of the project is to predict whether a startup which is currently Operating, IPO, Acquired, or closed.This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed.

#### *** Note: To access the Web Application Kindly visit my portfolio website or you can contact me through LinkedIn/Mail.***

## <br>**➲ 📂 Dataset**:

### Link to raw data(Huge JSON and Excel fiel):
           https://drive.google.com/file/d/1tWYkHYHm2HoiCajZ49Cs1K7sklWTdAbV/view?usp=sharing

## <br>**➲ 📑 Data types**:

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


## 🛠️ **Technologies Used**

- **Python** 🐍: The core programming language that powers the app.  
- **Flask**: A Backend web framework for building web applications.  
- **HTML/CSS**: Used for structuring and styling the frontend of the app, ensuring an intuitive user interface for interacting with the sentiment analysis model.
- **Scikit-learn**: Applied for machine learning tasks, such as preprocessing, feature engineering, and model evaluation, in the startup status classification pipeline.
- **XGBoost**: Utilized as an ensemble method for classification, offering high performance and accuracy in predicting startup acquisition status.
- **Stacking Ensemble**: Implemented to combine multiple models in a layered fashion, enhancing the predictive performance by leveraging the strengths of individual models.
- **Random Forest**: Used as a robust classifier for the startup acquisition status, providing high accuracy and generalization by aggregating predictions from multiple decision trees.
- **SMOTE**: (Synthetic Minority Over-sampling Technique): Applied to address class imbalance, generating synthetic data points for the underrepresented class to improve model performance.
- **MySQL**: Used as the relational database management system (RDBMS) for storing and managing the Startups details and User Credentials, ensuring reliable data retrieval and storage for the project.
- **AWS RDS**: Utilized to host and manage the MySQL database in a scalable and reliable cloud environment, providing automatic backups, scaling, and high availability.
- **AWS ECS**: (Elastic Container Service): Deployed for running Docker containers on AWS, allowing for seamless scaling and management of the app’s containerized services in a cloud environment.
- **Docker**: Utilized in this project to create a containerized environment for the app, ensuring consistent development and deployment across different environments.
- **Docker Container Images**: Employed to package all necessary code, libraries, and dependencies, allowing for the easy deployment and scaling of the sentiment analysis app.
- **CI/CD (Continuous Integration/Continuous Deployment)**: Integrated into the development workflow to automatically test and deploy new changes to the app, ensuring higher quality and faster release cycles for updates.
- **GitHub Actions**: Implemented for automating the CI/CD pipeline, allowing for seamless building, testing, and deployment of the sentiment analysis model directly from GitHub.
- **Pandas**: A robust library for dataset management and processing.    
- **Matplotlib/Seaborn**: Used for creating impactful visualizations that simplify data insights.  

## 🌟 **Usage Examples**

1. **Targeted Advertising:** Generate personalized faces for advertisements tailored to specific demographics. For example, "A young woman with curly hair wearing trendy sunglasses" for promoting fashion accessories.

2. **Virtual Influencers:** Create realistic celebrity-like virtual personalities for brands to engage audiences on social media platforms, such as "A smiling man with a neat beard and stylish glasses."

3. **Facial Attribute Illustration:** Generating images of faces based on text descriptions of specific attributes (e.g., "A smiling woman with blond hair and glasses").

4. **Personalized Avatar Creation:** Create custom avatars by specifying attributes such as "A young man with a mustache and curly hair."

5. **E-commerce and Product Visualization:** Display how accessories like glasses, hats, or earrings look on different faces. For example, "A man with a square jawline wearing a fedora."

6. **Entertainment Marketing:** Design promotional materials by generating faces of fictional characters for movies, games, or TV shows. For instance, "A mysterious man with a scar across his cheek and intense eyes."

7. **Event Promotions:** Create promotional imagery with realistic faces for events like fashion shows or conferences. Example: "A group of diverse people smiling at a conference."

8. **Education and Training:** Generate faces for use in training materials, such as "A teacher-like figure with glasses and a welcoming smile."


  ## <br>**➲ Exploratory Data Analysis (EDA)**
<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Target Class for Binary Classification
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/cls_dis1.png' style='width: 50%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Startups by Country
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/dis2.png' style='width: 50%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Startups by Region
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/dis3.png' style='width: 50%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Distribution of Acquired Companies by Category
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/dis4.png' style='width: 50%; height:300px' />       
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Number of Startups founded in different year
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/dis6.png' style='width: 80%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Classification Report For Testing
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/rep1.png' style='width: 50%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Machine Learning Pipeline for Binary Classification
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/pip1.png' style='width: 50%; height:300px' />
                     </p>
</details>


<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Machine Learning Pipeline for Stacking Classifier [Ensemble Method]
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/pip2.png' style='width: 50%; height:300px' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Machine Learning Pipeline for Multiclass Classification
       </summary>
                     <p align='center'>
                                <img src='https://github.com/Shuhaib73/Machine-Learning-Pipeline-on-Startups-Acquisition-Status/blob/prj_branch/website/__pycache__/pip3.png' style='width: 50%; height:300px' />
                     </p>
</details>


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


---


## 📧 **Contact**

For questions, feedback, or contributions, please contact:  
**Shuhaib**  
**Email**: mohamed.shuhaib73@gmail.com
**LinkedIn**: https://www.linkedin.com/in/mohamedshuhaib/

---


# Building-Machine-Learning-Pipeline-on-Startups-Acquisition-Status
Our aim to understand the financial conditions of company fundraising goals.

# Objective:
The objective of the project is to predict whether a startup which is currently Operating, IPO, Acquired, or closed.This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed.

## Data:

### Link to raw data(Huge JSON and Excel fiel):
           https://drive.google.com/file/d/1tWYkHYHm2HoiCajZ49Cs1K7sklWTdAbV/view?usp=sharing

### Summary:

The data contains industry trends, investment insights and individual company information. Since the data was acquired on a trial basis, it only contains information about companies. After training the model, we predict whether startups still operating, IPO, acquired, or closed.

### Data types:

The dataset includes the following key columns for model training:
* Entity Information: name, entity_type, category_code, etc.
* Status Information: status, founded_at, closed_at
* Company Financial Information: funding_total_usd, funding_rounds, first_investment_at, etc.
* Geographical Information: country_code, state_code, city, region
* Milestones and Relationships: milestones, relationships

-- The dataset also contains columns that provide additional context but are not directly useful for model training (such as created_at, updated_at, logo_url, etc).


## Data Cleaning:
In data cleaning we are will remove the inappropriate & unncessary information from raw data(main data).Hence, after which we’ll perform data cleaning involving following steps:
* Checking the percentage of NaN(null values) values present in each feature
* Removing duplicates
* Dropping columns which have NaN values.
* Remove unnecessary and corrupted data.
* Data Labelling.

## Machine Learning Pipeline:

-- The data preprocessing steps include:
-- Feature Selection: Identifying the relevant features from the raw data that will be used for model training.
-- Handling Missing Data: Imputing or removing missing values to ensure clean training data.
-- Normalization/Standardization: Scaling features to bring them to a similar range and avoid model bias.
-- Categorical Encoding: Encoding categorical variables (e.g., company industry, status) into numerical formats using techniques like one-hot encoding or label encoding.

## Building and Training Model:
           * The pipeline includes both binary and multiclass classification models, as the startup statuses need to be classified into one of several categories. The steps include:
           * Model Selection: Using suitable classifiers (e.g.Random Forest, XGBoost, etc.).
           * Model Training: Splitting the dataset into training and testing sets and training models on the training data.
           * Model Evaluation: Evaluating models using metrics like accuracy, precision, recall, and F1-score, among others.

## Dockerization::
           * The entire machine learning pipeline is dockerized, making it portable and easier to deploy in various environments. This involves:
           * Containerizing the model and pipeline using Docker to ensure consistency across different stages of development, testing, and production.

## CI/CD Automation:
           * Continuous Integration and Continuous Deployment (CI/CD) pipelines are implemented to automate the testing, building, and deployment of the model. This ensures that updates to the model or pipeline are smoothly integrated and deployed without manual intervention.

## Model Deployment and Database Integration:
           * Once the models are trained and evaluated, they will be deployed using Amazon ECS (Elastic Container Service), ensuring scalability and easy access for real-time predictions. This setup allows the model to be accessed via APIs for making predictions in real-time, such as determining the status of new startups.

           * To manage and store company and user credentials securely, Amazon RDS (Relational Database Service) will be used. RDS will allow for scalable, managed storage of user data and startup-related information. This ensures that sensitive information is stored securely and can be easily accessed by the deployed application.

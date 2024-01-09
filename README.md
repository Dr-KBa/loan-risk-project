# Capstone Project 3 overview
You and your friend came up with a brilliant startup idea - provide risk evaluation as a service for retail banks. As with most successful startup teams, both of you have your specialty. Your friend is responsible for sales and operations, while you are responsible for everything product-related, from planning to data analysis to building the solution. You have quickly identified that machine learning will be an essential part of your offering because you believe that the models can capture statistical patterns in the defaults on bank loans. You decide to start your investigation by downloading this dataset from Home Credit Group. You are not yet sure, what is the most crucial problem for your potential clients, so you had a meeting with your friend to discuss how your proof-of-concept (POC) product should look like. After a lot of arguing, you both agreed to create a number of different models so that you have a robust and diversified offering when you get your first meeting with the potential clients. You are eager to investigate the dataset and see what you can predict, so you propose that you come up with interesting features to analyze and predict - this way, you'll focus on building a solid offering, and she can work on getting meetings with the banks.

Plan:

1. Analyze the raw data and inform the potential clients about accessible features that can be used for predictions. Result: data structured and presented.
2. Explore some of the features that would inform the clients about the likely portrait of a normal and problematic costumers. Result: data structured and presented.
3. Create a model (Model 1) that would help bank quickly (having limited data) evaluate customers' creditworthiness. Result: model that is better than random guessing.
4. Deploy the model (Model 1) to the cloud. Result: model that is accessible via HTTP requests.
5. Make model practical to use and capable of live demo. Result: Model is accessible via simple user interface so that bank employees can quickly evaluate weather client is worth further considerations for the loan.
6. Create a more complex model (Model 2) that may be used after initial filtering (Model 1), or instead of it. This model should be further developed if the bank is interested in my services. Result: model encompassing more data then Model 1 and utilizing at least one bonus challenge.

# Data acquisition
The dataset should be downloaded from Turing College relevant assignment webpage. Original data source appears to be based on Home Credit Default Risk Kaggle Competition.

# Project structure

This project mainly consists of three distinct parts:
1. Exploratory data analysis
```
/ProjectRoot
    EDA.ipynb
    Introduction.ipynb
```

3. First model training and deployment
```
/ProjectRoot
    /Model 1 deployment
        Dockerfile
        README.md
        app_Model_1.py
        optimized_model_1_CatB.pkl
        requirements.txt
    /Model 1 local access
        README.MD
        Unique values.txt
        app.py
    ML1-CB (4).ipynb
    ML1-LR (1).ipynb
    ML1-RF (2).ipynb
    ML1-XGB (3).ipynb
```

5. Second model training
```
/ProjectRoot
    EDA2.ipynb
    ML2-NN.ipynb
```
    
Two folders for deployment and testing have associated README.md files to help navigate through the contents. 

# Project aim
The real aim of this project is to demonstrate the material learned and the abilities gained in Module 3.
The imaginary aim is to create an offer for bank that would help it classify loans to normal and risky using data
from the previous applications of the clients. The bank should also be interested in the ability to analyze the data and provide insights. The presentation to the bank should include a live demo.

# Project tasks
To achieve real and imaginary goals following steps were taken:
1. Analyze the raw data and inform the potential clients about accessible features that can be used for predictions. Result: data structured and presented.
2. Explore some of the features that would inform the clients about the likely portrait of a normal and problematic costumers. Result: data structured and presented.
3. Create a model (Model 1) that would help bank quickly (having limited data) evaluate customers' creditworthiness. Result: model that is better than random guessing.
4. Deploy the model (Model 1) to the cloud. Result: model that is accessible via HTTP requests.
5. Make model practical to use and capable of live demo. Result: Model is accessible via simple user interface so that bank employees can quickly evaluate weather client is worth further considerations for the loan.
6. Create a more complex model (Model 2) that may be used after initial filtering (Model 1), or instead of it. This model should be further developed if the bank is interested in my services. Result: model encompassing more data then Model 1 and utilizing at least one bonus challenge.

# Tests
Model access tests were performed. Detailed information can be found in Model 1 README.md files.

# List of requirements and how they were followed

1. Download the data from here and the data description from here.
Result: fully completed.
2. Create a plan for your investigation, analysis, and POC building. This should include your assumptions, overall objectives, and objectives for each step in your plan. You are not expected to have a plan for the whole project but instead have a clear understanding of what you'll try to achieve in the next step and build the plan one step at a time.
Result: fully completed, assuming having limited domain knowledge.
3. Perform exploratory data analysis. This should include creating statistical summaries and charts, testing for anomalies, checking for correlations and other relations between variables, and other EDA elements.
Result: Fully completed as various types of charts created, correlations extensively checked, outliers spotted. Possible improvement: more features and the value distributions visualized, if more time is given.
4. Perform statistical inference. This should include defining the target population, forming multiple statistical hypotheses and constructing confidence intervals, setting the significance levels, conducting z or t-tests for these hypotheses.
Result: Fully completed as few statistical tests were conducted after checking suitability of the data for them.
5. Use machine learning models to predict the target variables based on your proposed plan. You should use hyperparameter tuning, model ensembling, the analysis of model selection, and other methods. The decision of where to use and not to use these techniques is up to you; however, they should be aligned with your team's objectives.
Result: completed, as different models were used; hyperparameters tuned; regarding model ensembling  XGBoost is an ensemble learning technique. Possible improvement: more models can be tested, i.e. lightGBM with all model hyperparameter-tuned, if no performance restrictions.
6. Deploy these machine learning models to Google Cloud Platform. You are free to choose any deployment option you wish as long as it can be called an HTTP request.
Result: completed. Possible improvement: second model also in the Google Cloud if cost is not important. Also, given significantly more features the live demo using "streamlit" or similar interface approach would not be possible.
7. Provide clear explanations in your notebook. Your explanations should inform the reader what you are trying to achieve, what results you got, and what these results mean.
Result: Fully completed.
8. Provide suggestions about how your analysis and models can be improved.
Result: Fully completed.


# Contribution
The analysis and most of the coding was done by Kazimieras Badokas.

ChatGPT was prompted to generate initial "streamlit" template for web interface and some parts of code; also to find errors in the code or replace some code with more efficient one. nb_black extension was used to correctly format the code. DALL-E was prompted to generate illustration for the project in the Intro notebook. Some parts of the code especially in the EDA part were reused from previous projects (like Stroke prediction dataset, Lending club...). Deployment was done mostly following this guide: https://towardsdatascience.com/introduction-to-ml-deployment-flask-docker-locust-b87b5bd78a17


# License for dataset
Exact license for this particular dataset is unknow. However, it is likely this one: https://www.kaggle.com/competitions/home-credit-default-risk/rules#7-competition-data



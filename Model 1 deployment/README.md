# Model deployment to Google Cloud (via Container Registry)

1. Create Dockerfile (no extension)
2. Create requirements.txt with packages to be used listed (pip freeze to reveal system package versions)
3. Docker build (ensure Docker engine is running):
    docker build -t app_name_lowercase .
4. (optional) Run Docker container locally with:
    docker run -p 8000:80 app_name_lowercase
5. Tag docker image:
    docker tag app_name_lowercase gcr.io/gc-project-id/app_name_lowercase
6. (may be optional) Authenticate gcloud:
    gcloud auth configure-docker
7. Push to GC Registry:
    docker push gcr.io/gc-project-id/app_name_lowercase
8. Deploy to Cloud Run via dashboard or terminal
    
# Model deployment to Google Cloud (via Artifact Registry) - PREFERED
Note: when building containers using Apple Silicon "linux/amd64" specification is mandatory, otherwise the container will fail to run on Google Cloud!

1. 1-2 steps as in "Model deployment to Google Cloud (via Container Registry)"
2. Build Docker container:
    buildx build --platform linux/amd64 -t europe-central2-docker.pkg.dev/gc-project-id/repo-id/app_name_lowercase .    
3. Prepare for container push:
    gcloud auth configure-docker europe-central2-docker.pkg.dev
4. Push to GC Artifact registry:
    docker push europe-central2-docker.pkg.dev/gc-project-id/repo-id/app_name_lowercase
5. 8. Deploy to Cloud Run via dashboard or terminal

#Tests
## The model can be tested locally, when Docker container is running, with the following script (adjust test values, if necessary; also port adjustment to 8080 may be necessary):
    
    curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
        "NAME_CONTRACT_TYPE": "Cash loans",
        "CODE_GENDER": "M",
        "FLAG_OWN_CAR": 1,
        "FLAG_OWN_REALTY": 1,
        "CNT_CHILDREN": 0,
        "AMT_INCOME_TOTAL": 150000,
        "AMT_CREDIT": 500000,
        "AMT_ANNUITY": 25000,
        "AMT_GOODS_PRICE": 450000,
        "NAME_TYPE_SUITE": "Unaccompanied",
        "NAME_INCOME_TYPE": "Working",
        "NAME_EDUCATION_TYPE": "Secondary / secondary special",
        "NAME_FAMILY_STATUS": "Single / not married",
        "NAME_HOUSING_TYPE": "House / apartment",
        "REGION_POPULATION_RELATIVE": 0,
        "DAYS_BIRTH": 0,
        "DAYS_EMPLOYED": 0,
        "DAYS_REGISTRATION": 0,
        "DAYS_ID_PUBLISH": 0,
        "OWN_CAR_AGE": 0,
        "FLAG_MOBIL": 0,
        "FLAG_EMP_PHONE": 0,
        "FLAG_WORK_PHONE": 0,
        "FLAG_CONT_MOBILE": 0,
        "FLAG_PHONE": 0,
        "FLAG_EMAIL": 0,
        "OCCUPATION_TYPE": "Core staff",
        "CNT_FAM_MEMBERS": 0,
        "REGION_RATING_CLIENT": 0,
        "REGION_RATING_CLIENT_W_CITY": 0,
        "WEEKDAY_APPR_PROCESS_START": "MONDAY",
        "HOUR_APPR_PROCESS_START": 0,
        "REG_REGION_NOT_LIVE_REGION": 0,
        "REG_REGION_NOT_WORK_REGION": 0,
        "LIVE_REGION_NOT_WORK_REGION": 0,
        "REG_CITY_NOT_LIVE_CITY": 0,
        "REG_CITY_NOT_WORK_CITY": 0,
        "LIVE_CITY_NOT_WORK_CITY": 0,
        "ORGANIZATION_TYPE": "Business Entity Type 3",
        "Income_Class": "Upper middle income",
        "DTI_PROC": 10
      }'

## The model can be tested on Cloud Run using Postman API platform.
1. Open Postman app.
2. Create a New Request with the following details:
    HTTP Method: POST;
    Request URL: https://cloud-run-url/predict. (it is important to include /predict endpoint, cloud-run-url could be found in Cloud Run dashboard).
3. Set Request Headers:
    Click on the Headers tab and add two headers:
    "Content-Type" value application/json;
    "accept value" application/json.
4. Configure the Request Body:
    Select raw;
    Select JSON;
    Enter json data with test values as follows:
    
{
    "NAME_CONTRACT_TYPE": "Cash loans",
    "CODE_GENDER": "M",
    "FLAG_OWN_CAR": 1,
    "FLAG_OWN_REALTY": 1,
    "CNT_CHILDREN": 0,
    "AMT_INCOME_TOTAL": 150000,
    "AMT_CREDIT": 500000,
    "AMT_ANNUITY": 25000,
    "AMT_GOODS_PRICE": 450000,
    "NAME_TYPE_SUITE": "Unaccompanied",
    "NAME_INCOME_TYPE": "Working",
    "NAME_EDUCATION_TYPE": "Secondary / secondary special",
    "NAME_FAMILY_STATUS": "Single / not married",
    "NAME_HOUSING_TYPE": "House / apartment",
    "REGION_POPULATION_RELATIVE": 0,
    "DAYS_BIRTH": 0,
    "DAYS_EMPLOYED": 0,
    "DAYS_REGISTRATION": 0,
    "DAYS_ID_PUBLISH": 0,
    "OWN_CAR_AGE": 0,
    "FLAG_MOBIL": 0,
    "FLAG_EMP_PHONE": 0,
    "FLAG_WORK_PHONE": 0,
    "FLAG_CONT_MOBILE": 0,
    "FLAG_PHONE": 0,
    "FLAG_EMAIL": 0,
    "OCCUPATION_TYPE": "Core staff",
    "CNT_FAM_MEMBERS": 0,
    "REGION_RATING_CLIENT": 0,
    "REGION_RATING_CLIENT_W_CITY": 0,
    "WEEKDAY_APPR_PROCESS_START": "MONDAY",
    "HOUR_APPR_PROCESS_START": 0,
    "REG_REGION_NOT_LIVE_REGION": 0,
    "REG_REGION_NOT_WORK_REGION": 0,
    "LIVE_REGION_NOT_WORK_REGION": 0,
    "REG_CITY_NOT_LIVE_CITY": 0,
    "REG_CITY_NOT_WORK_CITY": 0,
    "LIVE_CITY_NOT_WORK_CITY": 0,
    "ORGANIZATION_TYPE": "Business Entity Type 3",
    "Income_Class": "Upper middle income",
    "DTI_PROC": 10
}

5. Click send and read the server response.

## Other tests
Other tests may be as well possible as long as POST request is sent to the /predict endpoint with the appropriate json format (as outlined above.)


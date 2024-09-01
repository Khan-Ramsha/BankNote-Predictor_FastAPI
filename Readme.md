## Machine Learning Prediction API with FastAPI

#### This repository contains a machine learning prediction API built using FastAPI. The API allows users to send input data and receive predictions based on a trained machine learning model.

## Features

FastAPI: Provides a robust and efficient backend framework for handling API requests.

Swagger UI/OpenAPI: Integrated with FastAPI for easy testing and interaction with the API.

Model Prediction: The API loads a pre-trained machine learning model (saved as a pickle file) to generate predictions based on input data.

Installation
Clone the repository:

```
git clone https://github.com/yourusername/your-repo-name.git 
cd BankNote-Predictor_FastAPI
```

Install dependencies:

``` pip install -r app/requirements.txt ```

Running the Application

Start the FastAPI server:
``` uvicorn app.main:app --reload ```

Access the API:

Open your browser and navigate to http://127.0.0.1:8000/docs to interact with the API using Swagger UI.
In the Swagger UI, you can select the POST /predict endpoint, provide the necessary input parameters, and execute the request to observe the output.
Alternatively, you can access the OpenAPI schema at http://127.0.0.1:8000/openapi.json.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

# Enterprise Marketing Mix Modeling

## Project Overview

This project is about Marketing Mix Modeling (MMM) using Bayesian techniques.

The main goal is to understand how different marketing channels affect sales and how the marketing budget can be allocated better.

The project also includes a Power BI dashboard and a deployed API for getting sales predictions.

## Business Problem

Businesses spend money on different marketing channels such as TV, Radio, Search, Facebook, YouTube, Email, etc.

The objective of this project is to:

- Understand the impact of different marketing channels on sales
- Estimate the contribution of each channel
- Understand marketing performance
- Support better budget allocation decisions
- Predict sales for different marketing scenarios

## Dataset

The dataset contains weekly marketing and sales data, including:

- Sales
- TV Spend
- Radio Spend
- Search Spend
- Facebook Spend
- Instagram Spend
- YouTube Spend
- Display Spend
- Email Spend
- Affiliate Spend
- Price
- Promotion
- Holiday
- Competitor Spend
- Other business variables

## Project Workflow

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Adstock Transformation
5. Hill Saturation Transformation
6. Bayesian Marketing Mix Modeling
7. Model Evaluation
8. Channel Contribution Analysis
9. Budget Optimization
10. Power BI Dashboard Development
11. API Development
12. Docker Containerization
13. Cloud Deployment

## Marketing Transformations

### Adstock Transformation

Adstock is used to capture the carryover effect of marketing.

For example, if a company spends money on TV advertising this week, its effect may continue in the following weeks.

### Hill Saturation

Hill saturation is used to represent the idea of diminishing returns.

When marketing spend increases, sales impact may increase initially, but after some point the additional impact becomes smaller.

## Bayesian Marketing Mix Model

The model is built using PyMC.

The model estimates the relationship between marketing channels, business variables, and sales.

The main features used in the model include:

- TV
- Radio
- Search
- Facebook
- Instagram
- YouTube
- Display
- Email
- Affiliate
- Price
- Promotion
- Holiday
- Competitor Spend

## Dashboard

The Power BI dashboard includes four main pages:

- Executive Dashboard
- Marketing Performance
- Bayesian MMM Insights
- Budget Optimization & Recommendations

The dashboard helps to understand marketing performance and channel-level insights.

## API

A FastAPI application was created to serve the trained MMM model.

The API provides a `/predict` endpoint that takes marketing and business inputs and returns predicted sales.

Example response: {"predicted_sales": 13512.27}

The API documentation is available through Swagger UI using the `/docs` endpoint.

## Docker

The API is packaged into a Docker container.

Docker is used so that the application and its required Python dependencies can run in a consistent environment.

## CI/CD

GitHub Actions is used for the CI/CD pipeline.

The deployment workflow performs these steps:

1. Install Python dependencies
2. Check the project files
3. Build the Docker image
4. Push the Docker image to Docker Hub
5. Authenticate with Google Cloud
6. Deploy the application to Google Cloud Run

## Cloud Deployment

The FastAPI application is deployed on Google Cloud Run.

The application is publicly accessible through the Cloud Run URL.

The deployment uses GitHub Actions and Google Cloud Workload Identity Federation for authentication.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- PyMC
- ArviZ
- Scikit-learn
- SciPy
- FastAPI
- Docker
- Docker Hub
- Git
- GitHub
- GitHub Actions
- Google Cloud Run
- Power BI

## Project Outcome

The project helps estimate the contribution of different marketing channels and understand their effect on sales.

It also provides budget allocation insights and a prediction API that can be used for different marketing scenarios.

## Author

Khushi Gupta

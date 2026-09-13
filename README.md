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

Example response:

```json
{
  "predicted_sales": 13512.27
}

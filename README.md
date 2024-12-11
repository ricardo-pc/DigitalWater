# Digital Water

Our solution, **Digital Water**, was created and presented for the Atos IT Challenge 2020, an international competition themed **Cooperative Artificial Intelligence**. Participants were challenged to "devise an innovative use case and build a prototype demonstrating Cooperative AI, including plans for further development and market potential." After eight months of dedicated work, my team and I earned **second place** among thousands of competitors worldwide, becoming the **first Mexican team** to achieve this distinction in the competition's 10-year history. [Atos website](https://www.atositchallenge.net/edition-2020/).

## Table of Contents
1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Usage](#usage)
5. [Data](#data)


## About the Project

This project explores the application of machine learning to improve water resource management. Its goal is to forecast water demand, which refers to the amount a city needs within a given period, alongside the available water capacity from its sources. While this analysis represents a mass balance and does not account for losses from the source to the final point, we recognize these losses as a significant factor.

Being a native of Monterrey, Nuevo León, México, I focused this project on my home state, using real data provided by the official utility, **Agua y Drenaje de Monterrey**. At the time, we were unaware that Monterrey was on the brink of a severe water crisis, which began just two years after the project’s completion. Our model hinted at this possibility, but we either did not believe it or did not want to.

The water crisis in Monterrey was devastating. Only after experiencing the constant anxiety of opening a faucet, unsure if water would flow, do you truly value something that always seemed guaranteed. Ironically, in one of Latin America’s wealthiest cities, where gleaming skyscrapers and high per capita income symbolize progress, all five million residents were reduced to just a few liters of water daily for nearly two years. Read more about Monterrey's Water Crisis: [Harvard University GSD](https://www.gsd.harvard.edu/2024/02/from-drought-to-flood-solutions-for-extreme-climate-events-in-monterrey-mexico/), [AquaTech](https://www.aquatechtrade.com/news/urban-water/mexico-water-conservation-pressure-regulation)



## Features

For the Atos IT Challenge 2020, the following was included:
### ☁️ **Google Colab Notebooks**
  - LSTM model to predict daily water demand
  - LSTM model to predict daily water capacity

### 📊 **Interactive Front-end Platform (no longer available after 01/2021)**
  - Hosted on Heroku

### 📂 **Well-Documented Datasets**
- datasets with real data, from the official source (SADM)

### 🔗 **Research of Monterrey's Water Network**
- reported in summary reports to understand the data's context

### 🎥 **Promotional Video**
- brief explanation of solution and front-end platform

## Project Structure

your-repo-name/ ├── data/ # Datasets and raw data used in the project │ ├── sample_data.csv # Example dataset for testing and demonstration │ └── README.md # Information about the datasets ├── notebooks/ # Jupyter Notebooks for analysis and modeling │ ├── data_analysis.ipynb # Notebook for data exploration │ ├── model_training.ipynb # Notebook for training the model │ └── README.md # Details about the notebooks ├── docs/ # Documentation for project context and methodology │ ├── project_overview.md # Detailed project overview │ └── methodology.md # Description of the approach and methods used ├── scripts/ # Python scripts for preprocessing and automation │ ├── preprocess_data.py # Script for data preprocessing │ ├── train_model.py # Script for model training │ └── utils.py # Utility functions ├── requirements.txt # Dependencies required for the project ├── LICENSE # License information ├── README.md # Project README └── .gitignore # Files and folders to be ignored by Git


# python-dataset-scripts
A collection of Python scripts for generating realistic simulated datasets based on real-world topics. Designed for data analysts and engineers to practice SQL, dashboarding, and machine learning workflows. Each dataset includes custom logic, column relationships, and domain-specific structure.

#  Simulated Dataset Creation Projects

This repository showcases my custom Python scripts for generating realistic simulated datasets based on real-world topics and use cases. These datasets are published on Kaggle(https://www.kaggle.com/rivalytics) and are designed for practice with SQL, data visualization, machine learning, and exploratory data analysis.

Each dataset follows a structured creation process to ensure the values are realistic, logically consistent, and ready for analysis.

---

##  Dataset Creation Framework

I use the following step-by-step process when creating simulation datasets:

### 1. Define the Simulation Universe
Start with a clear **context or scenario**. Choose a theme like hospital visits, relationship diaries, or job burnout.

- Identify core **entities** (e.g., patients, visits, transactions)
- Define the **purpose** of the dataset (e.g., regression, dashboarding, anomaly detection)

### 2. Conduct Domain Research
Study how the scenario works in real life:
- What KPIs or metrics are commonly used?
- What problems are analysts trying to solve?
- Use real dashboards, articles, and use cases for inspiration.

### 3. Design Columns & Data Types
Based on research:
- Choose relevant and meaningful columns
- Assign appropriate data types (e.g., float, string, datetime)
- Plan realistic value ranges or categories

### 4. Map Column Relationships
Ensure fields relate to each other logically:
- `age` may influence `readmission_risk`
- `department` may affect `visit_duration`
- Define realistic dependencies or hierarchies

### 5. Apply Conditional Logic
Use Python to implement logic like:
- `if/else` conditions
- `random.choices()` with weights
- Probability curves for realistic variance

This avoids random, noisy data and creates believable outcomes.

### 6. Validate Output
- Check distributions, ranges, and nulls
- Ensure primary/foreign keys are respected if needed
- Format output as CSV, JSON, or ZIP bundles

### 7. Visualize Relationships
(Optional but recommended):
- Plot distributions or heatmaps to confirm relationships
- Use ChatGPT to generate the visuals

### 8. Package and Document
- Include a data dictionary for each dataset
- Write a brief usage guide or README
- Publish to Kaggle or include in this repo for portfolio review

---

##  What's in This Repo

Each folder contains:
- Python script used to generate the dataset
- Generated sample dataset(s)
- Data dictionary (when applicable)
- Notes or references for domain logic

---

##  Why Simulated Datasets Matter

Creating high-quality simulated datasets allows data analysts and engineers to:
- Practice realistic analysis without violating privacy laws
- Build public portfolios and GitHub projects
- Train models or build dashboards on domain-specific data

This repo reflects my skillset in data modeling, logic design, and dataset engineering — with an emphasis on quality, not just quantity.

---

##  Want to Learn More?

I'm currently building a cloud-based app that lets users generate structured datasets through a vending-machine-style interface using AWS Lambda, S3, and config-driven logic. Follow my Medium blog (https://medium.com/rivalytics) to read about my build journey.



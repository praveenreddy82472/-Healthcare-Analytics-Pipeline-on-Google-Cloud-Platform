# 🏥 Healthcare Analytics Pipeline on Google Cloud

This project demonstrates how to build a complete data pipeline on **Google Cloud Platform (GCP)** for healthcare data. The solution involves ingesting raw data into **Google Cloud Storage**, processing it using **Apache Beam with Dataflow**, loading into **BigQuery**, and performing **data visualization and machine learning** using **BigQuery ML** and **Vertex AI Studio**.

---

## 📊 Project Flow & Architecture

### 🔁 End-to-End Steps:
1. **Load data to GCS**
2. **Create BigQuery dataset & table**
3. **Run Apache Beam (Dataflow) Python pipeline**
4. **Store processed data in BigQuery**
5. **Explore data with Data Canvas & Vertex AI Insights**
6. **Build ML model using BigQuery ML**
7. **Explore AutoML in Vertex AI Studio**

---

## 📌 Pipeline Architecture

![Pipeline]([https://your-image-link.com/pipeline-diagram.png](https://github.com/praveenreddy82472/tutorial_test/blob/main/DaflwPip.jpg))  
*(Upload an architecture diagram or draw using draw.io and host it)*

---

## ⚙️ Step-by-Step Implementation

### 1️⃣ Upload CSV to Google Cloud Storage (GCS)
Upload the healthcare dataset to a GCS bucket:
```bash
gsutil cp healthcare_dataset.csv gs://your-bucket-name/
---

### 2️⃣ Create BigQuery Dataset and Table
In the BigQuery console:

Create a dataset (e.g., healthdatapro)

You can either let the pipeline create the table or create it manually based on your schema.
---

---
### 3️⃣ Dataflow Pipeline using Apache Beam (Python)
Create and run a Dataflow job using a Python script:

bash
Copy
Edit
python load_to_bigquery.py \
  --project=your-gcp-project \
  --region=your-region \
  --stagingLocation=gs://your-bucket/staging \
  --tempLocation=gs://your-bucket/temp \
  --runner=DataflowRunner
This script:

Reads the CSV from GCS

Parses and transforms records

Loads them into BigQuery with a predefined schema

---

---
### 4️⃣ Verify Data in BigQuery
After the pipeline runs:

Go to BigQuery > Your Dataset > Preview the table

You should see all records loaded successfully

---
---
### 5️⃣ Visualize Using Data Canvas & Vertex AI Insights
Use Table Explorer in BigQuery for visual data profiling

Use Vertex AI > Data Insights to:

Check correlations

Detect missing values

View label distribution
---

---
### 6️⃣ Machine Learning with BigQuery ML
Train a model (e.g., Decision Tree) using SQL:

sql
Copy
Edit
CREATE OR REPLACE MODEL `your-dataset.test_results_model`
OPTIONS(model_type='DECISION_TREE_CLASSIFIER', input_label_cols=['Test_Results']) AS
SELECT * FROM `your-dataset.health_records`;
Evaluate the model:

sql
Copy
Edit
SELECT * FROM ML.EVALUATE(MODEL `your-dataset.test_results_model`);
Predict outcomes:

sql
Copy
Edit
SELECT * FROM ML.PREDICT(MODEL `your-dataset.test_results_model`, 
  (SELECT * FROM `your-dataset.health_records`));

---

---
### 7️⃣ Explore Vertex AI Studio
(Optional) Use Vertex AI Studio for:

Drag-and-drop AutoML model training

Automatic feature preprocessing

Model performance analysis

Steps:

Import data from BigQuery

Select label column (e.g., Test_Results)

Train AutoML model

Review evaluation metrics
---

---
### 🚀 Tools Used
Google Cloud Storage (GCS) – Data ingestion

Apache Beam / Dataflow – ETL pipeline

BigQuery – Data warehouse & analytics

BigQuery ML – SQL-based ML modeling

Vertex AI Studio – AutoML and data insights

Data Canvas – Interactive data exploration
---

---
### 📈 Outcomes
** Data ingested, transformed, and loaded into BigQuery

Visualized using BigQuery Insights & Canvas

ML model trained and evaluated

Explored AutoML using Vertex AI Studio

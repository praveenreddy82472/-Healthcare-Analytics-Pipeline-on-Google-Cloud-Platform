# 🏥 Healthcare Analytics Pipeline on Google Cloud

This project demonstrates how to build a complete data pipeline on **Google Cloud Platform (GCP)** for healthcare data. The solution involves ingesting raw data into **Google Cloud Storage**, processing it using **Apache Beam with Dataflow**, loading into **BigQuery**, and performing data visualization and machine learning using **BigQuery ML** and **Vertex AI Studio**.

---

## 📊 Project Flow & Architecture

### 🔁 End-to-End Steps:
- Load data to GCS
- Create BigQuery dataset & table
- Run Apache Beam (Dataflow) Python pipeline
- Store processed data in BigQuery
- Explore data with Data Canvas & Vertex AI Insights
- Build ML model using BigQuery ML
- Explore AutoML in Vertex AI Studio

---

## 📌 Pipeline Architecture

![Pipeline Architecture](https://raw.githubusercontent.com/praveenreddy82472/tutorial_test/main/DaflwPip.jpg)


---

## ⚙️ Step-by-Step Implementation

### 1️⃣ Upload CSV to Google Cloud Storage (GCS)

Upload the healthcare dataset to a GCS bucket:

```bash
gsutil cp healthcare_dataset.csv gs://your-bucket-name/


2️⃣ Create BigQuery Dataset and Table
In the BigQuery console:

Create a dataset (e.g., healthdatapro)

You can either create the table manually based on your schema or let the Dataflow pipeline create it automatically.

3️⃣ Dataflow Pipeline using Apache Beam (Python)
Run the Dataflow job with the following command:

bash
Copy
Edit
python load_to_bigquery.py \
  --project=your-project-id \
  --region=your-region \
  --stagingLocation=gs://your-bucket-name/staging \
  --tempLocation=gs://your-bucket-name/temp \
  --runner=DataflowRunner
This script will:

Read the CSV file from GCS

Parse and transform records according to the BigQuery schema

Load the data into BigQuery

4️⃣ Verify Data in BigQuery
After the pipeline completes successfully:

Navigate to BigQuery Console

Open your dataset (e.g., healthdatapro)

Preview the table to verify all records are loaded correctly

5️⃣ Visualize Using Data Canvas & Vertex AI Insights
Use the BigQuery Table Explorer and Vertex AI to explore and profile the data:

Use Table Explorer for quick data profiling

Use Vertex AI Data Insights to:

Check feature correlations

Detect missing or anomalous values

Analyze label distribution for your target column (Test_Results)

6️⃣ Machine Learning with BigQuery ML
Train a Decision Tree classifier directly in BigQuery using SQL

7️⃣ Explore Vertex AI Studio
Optionally, use Vertex AI Studio for automated ML (AutoML) workflows:

Import your dataset directly from BigQuery

Select the target label column (Test_Results)

Train AutoML models with drag-and-drop interface

Automatically apply feature preprocessing (e.g., encoding, normalization)

Analyze model performance using built-in dashboards

🚀 Tools Used
Tool	Purpose
Google Cloud Storage	Data ingestion and storage
Apache Beam / Dataflow	Scalable ETL pipeline
BigQuery	Data warehousing and analytics
BigQuery ML	SQL-based machine learning
Vertex AI Studio	AutoML and interactive model building
Data Canvas	Interactive data visualization

📈 Project Outcomes
Data successfully ingested, transformed, and loaded into BigQuery

Visualized data insights and explored data distributions

Built, evaluated, and predicted using BigQuery ML models

Experimented with AutoML capabilities in Vertex AI Studio

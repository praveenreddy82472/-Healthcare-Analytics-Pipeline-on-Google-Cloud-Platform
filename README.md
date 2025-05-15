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

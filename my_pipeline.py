import argparse
import time
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from datetime import datetime

# Main pipeline function
def run():
    # Command line arguments
    parser = argparse.ArgumentParser(description='Load from CSV into BigQuery')
    parser.add_argument('--project', required=True, help='Specify Google Cloud project')
    parser.add_argument('--region', required=True, help='Specify Google Cloud region')
    parser.add_argument('--stagingLocation', required=True, help='Specify Cloud Storage bucket for staging')
    parser.add_argument('--tempLocation', required=True, help='Specify Cloud Storage bucket for temp')
    parser.add_argument('--runner', required=True, help='Specify Apache Beam Runner')
    opts = parser.parse_args()

    # Setting up the Beam pipeline options
    options = PipelineOptions()
    options.view_as(GoogleCloudOptions).project = opts.project
    options.view_as(GoogleCloudOptions).region = opts.region
    options.view_as(GoogleCloudOptions).staging_location = opts.stagingLocation
    options.view_as(GoogleCloudOptions).temp_location = opts.tempLocation
    options.view_as(GoogleCloudOptions).job_name = f'my-pipeline-{int(time.time())}'
    options.view_as(StandardOptions).runner = opts.runner

    # Static input and output (replace with your GCS input and BigQuery output table)
    input = 'gs://pra18project1/healthcare_dataset.csv'
    output = f'{opts.project}:healthdatapro.health_records'

    # Table schema for BigQuery
    table_schema = {
        "fields": [
            {"name": "Name", "type": "STRING"},
            {"name": "Age", "type": "INTEGER"},
            {"name": "Gender", "type": "STRING"},
            {"name": "Blood Type", "type": "STRING"},
            {"name": "Medical Condition", "type": "STRING"},
            {"name": "Date of Admission", "type": "DATE"},
            {"name": "Doctor", "type": "STRING"},
            {"name": "Hospital", "type": "STRING"},
            {"name": "Insurance Provider", "type": "STRING"},
            {"name": "Billing Amount", "type": "FLOAT"},
            {"name": "Room Number", "type": "INTEGER"},
            {"name": "Admission Type", "type": "STRING"},
            {"name": "Discharge Date", "type": "DATE"},
            {"name": "Medication", "type": "STRING"},
            {"name": "Test Results", "type": "STRING"}
        ]
    }

    # Function to parse each CSV line
    def parse_csv(line):
        values = line.split(',')
        if len(values) != 15:
            logging.warning(f"Skipping row with incorrect number of values: {line}")
            return None
        try:
            return {
                "Name": values[0],
                "Age": int(values[1]),
                "Gender": values[2],
                "Blood Type": values[3],
                "Medical Condition": values[4],
                "Date of Admission": datetime.strptime(values[5], '%Y-%m-%d').strftime('%Y-%m-%d'),
                "Doctor": values[6],
                "Hospital": values[7],
                "Insurance Provider": values[8],
                "Billing Amount": float(values[9]),
                "Room Number": int(values[10]),
                "Admission Type": values[11],
                "Discharge Date": datetime.strptime(values[12], '%Y-%m-%d').strftime('%Y-%m-%d'),
                "Medication": values[13],
                "Test Results": values[14]
            }
        except Exception as e:
            logging.error(f"Error parsing row: {line}, Error: {e}")
            return None

    # Create the pipeline
    with beam.Pipeline(options=options) as p:
        (p
         | 'ReadFromGCS' >> beam.io.ReadFromText(input, skip_header_lines=1)
         | 'ParseCSV' >> beam.Map(parse_csv)
         | 'FilterValidRows' >> beam.Filter(lambda row: row is not None)
         | 'WriteToBQ' >> beam.io.WriteToBigQuery(
                output,
                schema=table_schema,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
            )
        )

    logging.getLogger().setLevel(logging.INFO)
    logging.info("Pipeline submitted.")

if __name__ == '__main__':
    run()



python my_pipeline.py \
  --project=project1-459615 \
  --region=us-central1 \
  --stagingLocation=gs://project1-459615-staging/ \
  --tempLocation=gs://project1-459615-temp/ \
  --runner=DataflowRunner

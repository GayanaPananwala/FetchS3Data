import os
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def process_sales_data(file_path):
    
    data = pd.read_csv(file_path)
    total_sales = data['Sales'].sum()
    print(f"Total Sales: {total_sales}")

def main():
    data_path = 'data/sales_data.csv'

    # Checking if USE_S3 is set
    if os.getenv('USE_S3', '0') == '1':
        try:
            s3 = boto3.client('s3')
            bucket_name = os.environ['S3_BUCKET_NAME']
            s3_key = os.environ['S3_KEY']
            s3.download_file(bucket_name, s3_key, '/tmp/sales_data.csv')
            data_path = '/tmp/sales_data.csv'
        except NoCredentialsError:
            print("Error: No AWS credentials found. Please ensure that your credentials are set.")
            return
        except PartialCredentialsError:
            print("Error: Incomplete AWS credentials. Please check credentials.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    process_sales_data(data_path)

if __name__ == "__main__":
    main()

import boto3
import botocore

class S3Client:
    def __init__(self):
        self.s3 = None

    def get_s3_client(self):
        if(self.s3 is None):
            self.s3 = boto3.resource('s3')

        return self.s3

    def download_file(self, bucket_name, file_name, target_file_name):
        try:
            s3 = self.get_s3_client()
            s3.Bucket(bucket_name).download_file(file_name, target_file_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise
        print("File downloaded to ", target_file_name)
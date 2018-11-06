import boto3
import os
import argparse

def upload(bucket_name, direction):
	s3 = boto3.client('s3')
	bucket_name = bucket_name
	os.chdir(direction)
	for i in os.listdir():
		try:
			filename = i
			s3.upload_file(filename, bucket_name, 'photo/'+filename)
			print('Done!')
		except Exception as e:
			print(e)
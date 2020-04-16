#
# clara_setup.py
# ~~~~~~~~~~~~~~
#
#  Expected environmental variables are:
#     AIAA: DNS name of AIAA server that will download MMAR, e.g. 'blahblah.us-west-2.elb.amazonaws.com/'
#     MODEL: THE NVIDIA MMAR name, e.g. clara_mri_seg_brain_tumors_br16_t1c2tc_no_amp
#     DATABUCKET: S3 bucket containing model training data
#     DATA: Training data corresponding to the specified MODEL MMAR
#     EFS: Path to write data.  This should be where container mounted EFS, e.g. '/workspace/'
#     HTTPS: Flag for TLS, should be either 'true' or 'false'    
# 
import os
import json
import logging
import requests
import boto3

if __name__ == "__main__":
    
   s3 = boto3.client('s3')

   # Use Clara Train API to download example model   
   if os.getenv('HTTPS') == 'true':
      aiaa_uri = 'http://' + os.getenv('AIAA')
   else:
      aiaa_uri = 'http://' + os.getenv('AIAA')
   payload = {'path':'nvidia/med/' + os.getenv('MODEL'), 'version':'1'}
   headers = {'accept':'application/json', 'Content-Type':'application/json'}
   r = requests.put(aiaa_uri + 'admin/model/' + os.getenv('MODEL'), 
                    data=json.dumps(payload), 
                    headers=headers)

   logging.info('Clara setup completed model download') 

   # Pull training data from S3 bucket
   data_bucket = os.getenv('DATABUCKET')
   data = os.getenv('DATA')
   # Path to efs where clara expects data
   local_data_path = os.path.join(os.getenv('EFS'), data)
   s3.download_file(data_bucket, data, local_data_path)
   logging.info('Clara setup completed data download')

   # Setup complete. I'm out!

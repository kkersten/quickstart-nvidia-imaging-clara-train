#!/bin/bash

# Set environmental variables
export CLOUD9SG=sg-<insert ID>
export EFSSG=sg-<insert ID>
export AIAA=<insert DNS>/ # Include trailing slash
export EFSDNS=<insert DNS>
export DATABUCKET=<S3 containing data>
export DATA=Task09_Spleen.tar 
export MODEL=clara_ct_annotation_spleen_amp
export EFS='/mnt/efs/data/'
export HTTPS=false

# Allow inboud EFS packets
aws ec2 authorize-security-group-ingress --group-id $CLOUD9SG --protocol tcp --port 2049 --source-group $EFSSG 

# Mount EFS
sudo mkdir /mnt/efs/

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $EFSDNS:/ /mnt/efs

sudo mkdir $EFS
sudo chown -R ec2-user $EFS

# Pull data
python3 ./clara_setup.py




# Create a bucket for CloudTrail logs

```sh
aws s3 mb s3://my-cloudtrail-ab-1212
```

# Create bucket policy to allow CloudTrail to put to bucket

```sh
aws s3api put-bucket-policy \
--bucket my-cloudtrail-ab-1212 \
--policy file://bucket-policy.json
```
> Necessário adicionar uma policy permitindo a escrita do CloudTrail no S3

[Policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html)

# Create Trail

```sh
aws cloudtrail create-trail \
--name MyTrail \
--s3-bucket-name my-cloudtrail-ab-1212 \
--region ca-central-1
```
[create-trail](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/create-trail.html)

# Start Logging

```sh
aws cloudtrail start-logging \
--name MyTrail
```
[start-logging](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/start-logging.html)
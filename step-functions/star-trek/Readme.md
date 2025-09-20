## Create Bucket

```sh
aws s3 mb s3://sf-star-trek-131241 \
--region us-east-1
```

## Enable EventBridge Communication

```sh
aws s3api put-bucket-notification-configuration \
--region us-east-1 \
--bucket sf-star-trek-131241 \
--notification-configuration '
{
    "EventBridgeConfiguration": {
    }
}'
```

## Upload files

```sh
aws s3 cp picard.jpg s3://sf-star-trek-131241/picard.jpg \
--region us-east-1
```

## Cleanup

```sh
aws s3 rm s3://sf-star-trek-131241/picard.jpg \
--region us-east-1

aws s3 rb s3://sf-star-trek-131241 \
--region us-east-1
```

## References

https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html
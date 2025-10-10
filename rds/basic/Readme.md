# Create Secret via Secrets Manager

```sh
aws secretsmanager create-secret \
--name MyRdsPassword \
--description "My RDS Password" \
--secret-string "{\"password\":\"mypassword\"}"
``` 

> https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/create-secret.html
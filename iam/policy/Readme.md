## Convert to JSON

The command

```sh
yq -o json policy.yml > policy.json
```

The bash script

```sh
./update
```

## Create IAM Policy

```sh
aws iam create-policy \
--policy-name my-fun-policy \
--policy-document file://policy.json

# aws iam create-policy - chama a funcao de criacao de policy no IAM
# --policy-name my-fun-policy - define o nome da policy
# --policy-document file://policy.json - busca a policy no local informado
```

## Attach Policy to user

```sh
aws iam attach-user-policy \
--policy-arn arn:aws:iam::982383527471:policy/my-fun-policy  \
--user-name aws-examples

# aws iam attach-user-policy - chama a funcao de atrelar a policy a um usuario no IAM
# --policy-arn arn:aws:iam::982383527471:policy/my-fun-policy - o ARN da policy que sera atribuida
# --user-name aws-examples - nome do usuario em que a policy sera atribuida
```
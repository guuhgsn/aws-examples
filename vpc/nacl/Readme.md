## Create NACL

```sh
aws ec2 create-network-acl --vpc-id vpc-03181823a2da0addd

# https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-acl.html
# aws ec2 create-network-acl - chama a opcao de criacao de NACL
# --vpc-id - define a VPC onde a NACL sera criada
```

## Add entry

```sh
aws ec2 create-network-acl-entry \
--network-acl-id acl-02def3052778d5ce2 \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=0,To=65535 \
--cidr-block 174.5.108.3/32 \
--rule-action deny

# https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-acl-entry.html
# aws ec2 create-network-acl-entry - chama a opcao de configuracao de propriedades da NACL
# --network-acl-id - define a NACL que sera configurada
# --ingress - especifica que sera uma regra para o trafego de entrada
# --rule-number - ordem de prioridade da regra
# --protocol - define os protocolos que serao afetados 
# --port-range - define o range de portas afetadas
# --cidr-block - define o CIDR da NACL
# --rule-action - especifica se sera uma regra de deny ou allow
```


## Get AMI for Amazon Linux 2

Grab the latest AML2 AMI

```sh
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name, 'amzn2')]|sort_by(@, &CreationDate)[-1].ImageId" \
--region ca-central-1 \
--output text

# https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html
# aws ec2 describe-images - chama a opcao de listagem de imagens
# --owners amazon - busca apenas as imagens da Amazon
# --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" - retorna todas as imagens que contenham o nome amzn2-ami-hvm-*-x86_64-gp2 e que estejam disponiveis
# --query "Images[?starts_with(Name, 'amzn2')]|sort_by(@, &CreationDate)[-1].ImageId" - retorna a versao mais recente da imagem que tem o nome iniciando em amzn2
# --region - imagens disponiveis na regiao informada
# --output text - formata a saida do comando em texto simples
```

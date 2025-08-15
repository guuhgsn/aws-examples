# Build Image

```sh
docker build -t  app .

# docker build - comando para construir uma imagem docker
# -t app - define o nome da imagem como app
# . - indica o diretorio atual como o contexto para o dockerfile
```

# Register Job

```sh
aws batch register-job-definition \
--job-definition-name square-job \
--type container \
--container-properties '{
    "image": "982383527471.dkr.ecr.ca-central-1.amazonaws.com/square",
    "vcpus": 1, 
    "memory": 128
}'

# aws batch register-job-definition - comando para criar uma definicao de job no AWS Batch
# --job-definition-name square-job - define o nome da definicao do job
# --type container - especifica que o job sera executado em um container
# --container-properties - define as propriedades do container como imagem, vCPU e memoria
```

https://docs.aws.amazon.com/cli/latest/reference/batch/register-job-definition.html#examples

# Create Compute Env

```sh
aws batch create-compute-environment \
--compute-environment-name my-compute-env \
--type MANAGED \
--compute-resources minvCpus=0,desiredvCpus=1,maxvCpus=1,instanceTypes=m4.16xlarge,subnets=subnet-12345678,securityGroupIds=sg-12345678 \
--service-role arn:aws:iam::123456789012:role/service-role/AWSBatchServiceRole

# aws batch create-compute-environment - comando para criar um ambiente de computacao
# --compute-environment-name my-compute-env - define o nome do ambiente de computacao
# --type managed - indica que o ambiente sera gerenciado pela AWS
# --compute-resources - especifica os detalhes dos recursos como vCPU, tipo de instancia e subnets
# --service-role - define a role do iam para o aws batch gerenciar os recursos
```

# Create Queue

```sh
aws batch create-job-queue \
--job-queue-name my-job-queue \
--state ENABLED \
--priority 1 \
--compute-environment-order '[
  {
    "order": 1,
    "computeEnvironment": "arn:aws:batch:ca-central-1:982383527471:compute-environment/ComputeEnv"
  }
]'

# aws batch create-job-queue - comando para criar uma fila de jobs
# --job-queue-name my-job-queue - define o nome da fila
# --state enabled - habilita a fila de jobs
# --priority 1 - define a prioridade da fila
# --compute-environment-order - associa o ambiente de computacao a fila
```

# Submit Job

```sh
aws batch submit-job \
--job-name my-job \
--job-definition square-job \
--job-queue my-job-queue

# aws batch submit-job - comando para enviar um job para a fila
# --job-name my-job - define o nome do job
# --job-definition square-job - especifica a definicao do job a ser usada
# --job-queue my-job-queue - indica a fila para a qual o job sera enviado
```
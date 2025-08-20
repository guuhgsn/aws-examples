## Create Content Buckets upload test video

```sh
aws s3 mb s3://srcvideos.example1254124.com --region us-east-1

# aws s3 mb - comando para criar um bucket no S3 (mb significa make bucket)
# s3://srcvideos.example1254124.com - o nome e o caminho do bucket (no caso o source)
# --region us-east-1 - a regiao onde o bucket sera criado

aws s3 mb s3://videos.example1254124.com --region us-east-1

# aws s3 mb - comando para criar um bucket no S3 (mb significa make bucket)
# s3://videos.example1254124.com - o nome e o caminho do bucket (no caso o destination)
# --region us-east-1 - a regiao onde o bucket sera criado

aws s3 cp App2Container.mp4 s3://srcvideos.example1254124.com/video.mp4 --region us-east-1

# aws s3 cp - comando para copiar um arquivo para o S3 (cp significa copy)
# App2Container.mp4 - o arquivo local que sera copiado
# s3://srcvideos.example1254124.com/video.mp4 - o bucket de destino (primeiro envia pro source) e o nome do arquivo no S3
# --region us-east-1 - a regiao do bucket de destino
```

## Create Pipeline

```sh
aws elastictranscoder create-pipeline \
--name my-transcoder-pipeline \
--input-bucket srcvideos.example1254124.com \
--role arn:aws:iam::982383527471:role/Elastic_Transcoder_Default_Role \
--content-config file://content-config.json \
--thumbnail-config file://thumbnail-config.json \
--region us-east-1

# aws elastictranscoder create-pipeline - comando para criar um pipeline no Elastic Transcoder
# --name my-transcoder-pipeline - o nome do pipeline
# --input-bucket srcvideos.example1254124.com - o bucket de entrada onde os arquivos de video estao
# --role - a role do iam que o elastic transcoder usara para acessar os buckets
# --content-config file://content-config.json - o arquivo de configuracao para as saidas de video
# --thumbnail-config file://thumbnail-config.json - o arquivo de configuracao para as miniaturas
# --region us-east-1 - a regiao onde o pipeline sera criado
```

## Create Job

```sh
aws elastictranscoder create-job \
--pipeline-id 1713880324699-qws2vn \
--inputs file://inputs.json \
--outputs file://outputs.json \
--output-key-prefix "videos/" \
--user-metadata file://user-metadata.json \
--region us-east-1 \
--query Job.Id

# aws elastictranscoder create-job - comando para criar um job de transcricao
# --pipeline-id 1713880324699-qws2vn - o id do pipeline a ser usado
# --inputs file://inputs.json - o arquivo de entrada contendo o nome do arquivo a ser transcodificado
# --outputs file://outputs.json - o arquivo de configuracao para as saidas do job
# --output-key-prefix "videos/" - o prefixo para o nome dos arquivos de saida no bucket
# --user-metadata file://user-metadata.json - metadados opcionais do usuario
# --region us-east-1 - a regiao do servico
# --query job.id - uma query para exibir apenas o id do job na saida
```

## Job Details

```sh
aws elastictranscoder read-job --id 1713880946080-cezshj --region us-east-1

# aws elastictranscoder read-job - comando para ler os detalhes de um job de transcricao
# --id 1713880946080-cezshj - o id do job que sera consultado
# --region us-east-1 - a regiao do servico
```
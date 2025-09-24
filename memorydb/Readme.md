# Create Subnet Group

```sh
aws memorydb create-subnet-group \
--subnet-group-name mysubnetgroup \
--description "my subnet group" \
--subnet-ids subnet-0e0fd31733061237d subnet-0c96245f8e4d94ed6 \
--query SubnetGroup.ARN \
--output text
```

> dont use the default VPC! create a VPC with subnets

# Create User

```sh
aws memorydb create-user \
--user-name gustavogoncalves \
--access-string "on ~* &* +@all" \
--authentication-mode Passwords="Testing12345678901234567890!",Type=password
```

# Create ACL

```sh
aws memorydb create-acl \
--acl-name "new-acl-1" \
--user-names "gustavogoncalves"
```

# Create Cluster

```sh
aws memorydb create-cluster \
--cluster-name my-new-cluster \
--node-type db.t4g.small \
--acl-name new-acl-1 \
--subnet-group mysubnetgroup
```
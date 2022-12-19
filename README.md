# estudo-acloudguru
Estudo sobre Cloud na plataforma  A cloud Guru

## AWS Certified Developer - Associate (DVA-C01)

### 5.5 - Introduction to Serverless Computing

#### Building a Serverless Website - Demo
Arquivos: [https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Serverless_Webite_Demo](https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Serverless_Webite_Demo)

### 5.6 - Version Control With Lambda - Demo
Arquivos: [https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Version_Control_With_Lambda](https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Version_Control_With_Lambda)

- `$LATEST` is always the lastversion of code you uploaded to lambda
- `Versionong and Aliases`: Use Lambda versioning and aliases to point your applications to specific version if you don't want to use $LATEST
- `Examples ARNs`: 
  - arn:aws:lambda:us-east-1:123456789012: function:mylambda:Prod
  - arn:aws:lambda:us-east-1:123456789012: function:mylambda:$LATEST
- `Update your Aliases`: If your application uses an alias instead of $LATEST, remember that it will not automatically use the new code when you upload it.

### 5.7 Lambda Concurrent Executions Limit
Know that a limit exits - 1,000 concurrent executions per second
- If you are running a serverless website like ACG, it’s likely you will hit the limit at some point
- If you hit the limit you will start to see invocations being rejected - 429 HTTP status code
- The remedy is to get the limit raised by AWS support
- Reserved concurrency guarantees a set number of concurrent executions are always available to a critical
function

### 5.8 Lambda and VPC Access

Enabling Lambda to Access VPC Resources
• To enable this, you need to allow the function to connect to the private subnet.
• Lambda needs the following VPC Configuration information so that it can connect to the VPC:
• Private subnet ID
• Security group ID (with required access)
• Lambda uses this information to set up ENIs using an available IP address from your private
subnet

Enabling Lambda to Access VPC Resources
• You add VPC information to your Lambda function config using the vpc-config parameter.
```bash
aws lambda update-function-configuration \
--function-name my-function \
--vpcconfig SubnetIds=subnet-1122aabb,SecurityGroupIds=sg-51530134
```

Lambda and VPCs
• It is possible to enable Lambda to access resources which are inside a private VPC.
• Provide VPC config to the function – private subnet ID, security group ID.
• Lambda uses the VPC information to set up ENIs using an IP from the private subnet CIDR range.
• The security group then allows your function to access resources in VPC.

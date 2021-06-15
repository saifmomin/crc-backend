#Create an S3 bucket
aws2 s3 mb s3://rc-back

#package sam
sam package --s3-bucket rc-back --template-file template.yaml --output-template-file out/packaged.yaml

#deploy sam
sam deploy --template-file out/packaged.yaml --stack-name visits --capabilities CAPABILITY_IAM

#On-Demand billing mode [BillingMode: PAY_PER_REQUEST]. This is not working with SAM template.
aws2 dynamodb update-table --table-name visits-Table-HNOR8TNB71ZY --billing-mode PAY_PER_REQUEST
#Create an S3 bucket
aws2 s3 mb s3://rc-back

#package sam
sam package --s3-bucket rc-back --template-file template.yaml --output-template-file out/packaged.yaml

#deploy sam
sam deploy --template-file out/packaged.yaml --stack-name website --capabilities CAPABILITY_IAM

sam deploy --template-file /home/runner/work/rc-backend/rc-backend/out/packaged.yaml --stack-name website --capabilities CAPABILITY_IAM

#On-Demand billing mode [BillingMode: PAY_PER_REQUEST]. This is not working with SAM template.
aws2 dynamodb update-table --table-name website-Table-Y7HZHCOX6DY --billing-mode PAY_PER_REQUEST


#Git
git status
git add .
git commit -m ""
git push
git pull --rebase

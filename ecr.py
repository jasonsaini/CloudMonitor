import boto3

ecr_client = boto3.client("ecr")

repo_name = 'my-cloud-native-repo'
response = ecr_client.create_repository(repositoryName=repo_name)

repo_uri = response['repository']['repositoryUri']
print(repo_uri)

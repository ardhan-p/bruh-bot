import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('BruhBotUsers')

print(table.creation_date_time)
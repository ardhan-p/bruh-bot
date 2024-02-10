import boto3
import env

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(env.DYNAMODB_TABLE_NAME)

def checkUser(message):
    username = message.author.name
    
    response = table.get_item(
        Key={
            'discord_id': username
        }
    )
    
    return response

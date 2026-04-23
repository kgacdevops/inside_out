import json, boto3, random, urllib.request
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('verses_table')

def get_verse(selected_verse):
    format_verse = selected_verse.replace(" ", "+").lower()
    verse_content = ""
    with urllib.request.urlopen("https://bible-api.com/" + format_verse) as res:
        verse_content = json.loads(res.read().decode())['text']
    return verse_content.replace("\n", " ").replace("\"", "").strip()

def lambda_handler(event, context):
    get_items = table.scan(
        FilterExpression=Attr('mood').eq(event['queryStringParameters']['mood'])
    )
    vref_list = []
    for vref in get_items['Items']:
        vref_list.append(vref['verse_reference'])
    selected_verse = random.choice(vref_list)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'body': json.dumps({
            'reference': selected_verse,
            'content': get_verse(selected_verse)
        })
    }
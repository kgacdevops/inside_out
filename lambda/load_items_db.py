import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('verses_table')

def lambda_handler(event, context):
    items = [
        { "verse_reference": "Matthew 11:28", "mood": "happy" },
        { "verse_reference": "Proverbs 17:22", "mood": "happy" },
        { "verse_reference": "Psalm 56:8", "mood": "sad" },
        { "verse_reference": "Romans 8:38-39", "mood": "sad" },
        { "verse_reference": "Psalm 34:18", "mood": "sad" },
        { "verse_reference": "Psalm 42:11", "mood": "sad" },
        { "verse_reference": "Proverbs 29:22", "mood": "angry" },
        { "verse_reference": "Psalm 37:8", "mood": "angry" },
        { "verse_reference": "Proverbs 10:12", "mood": "angry" },
        { "verse_reference": "Proverbs 14:29", "mood": "angry" },
        { "verse_reference": "Philippians 4:6", "mood": "anxious" },
        { "verse_reference": "1 Peter 5:7", "mood": "anxious" },
        { "verse_reference": "Matthew 6:31", "mood": "anxious" },
        { "verse_reference": "Psalm 55:22", "mood": "anxious" }
    ]

    with table.batch_writer() as batch:
        for item in items:
            print("Saving: ", item)
            batch.put_item(Item=item)
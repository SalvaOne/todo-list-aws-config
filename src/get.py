import json
import decimalencoder
import todoList


def get(event, context):
    # create a response
    item_id = event.get('pathParameters', {}).get('id')
    item = todoList.get_item(item_id)
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response

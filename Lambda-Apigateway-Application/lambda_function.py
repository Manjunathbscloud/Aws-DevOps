import json

def lambda_handler(event, context):
    # Check if the request method is GET
    if event['httpMethod'] == 'GET':
        # Check if the request path is "/path1"
        if event['path'] == '/path1':
            # Return response for path1 along with event details
            return {
                'statusCode': 200,
                'body': json.dumps({'response': 'This is response from path1', 'event_details': event})
            }
        # Check if the request path is "/path2"
        elif event['path'] == '/path2':
            # Return response for path2 along with event details
            return {
                'statusCode': 200,
                'body': json.dumps({'response': 'This is response from path2', 'event_details': event})
            }
        else:
            # Return 404 error if the requested path is not "/path1" or "/path2"
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'This method or path is not available'})
            }
    else:
        # Return 405 error if the request method is not GET
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method not allowed'})
        }

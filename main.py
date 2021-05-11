import boto3
def check_tables(region='eu-west-2'):
    dynamodb = boto3.resource('dynamodb',region_name=region)
    list(dynamodb.tables.all())
def create_table(region='eu-west-2'):
    dynamodb = boto3.resource('dynamodb',region_name=region)
    table = dynamodb.create_table(
        TableName = 'pringle_prices',
        KeySchema = [
            {
                'AttributeName': 'date',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'shop',
                'KeyType': 'RANGE'
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'shop',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

def add_iteam():
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamodb.Table('pringle_prices')
    table.put_item(
    Item= {
        'date': '2020/12/10',
        'shop': 'tesco',
        'price': '1.50'
    })
if __name__ == '__main__':
    #create_table()
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamodb.Table('pringle_prices')
    print(table.scan())
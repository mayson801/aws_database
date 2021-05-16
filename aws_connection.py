import boto3
from boto3.dynamodb.conditions import Key

def check_tables(region='eu-west-2'):
    dynamodb = boto3.resource('dynamodb',region_name=region)
    list(dynamodb.tables.all())
def create_table(region='eu-west-2'):
    dynamodb = boto3.resource('dynamodb',region_name=region)
    table = dynamodb.create_table(
        TableName = 'pringle_prices',
        KeySchema = [
            {
                'AttributeName': 'shop',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'date',
                'KeyType': 'RANGE'
            }

        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'shop',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

def add_iteam(shop,date,price):
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamodb.Table('pringle_prices')
    table.put_item(
    Item= {
        'shop': shop,
        'date': date,
        'price': price
    })
def get_table():
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamodb.Table('pringle_prices')
    whole_table = (table.scan())
    return whole_table['Items']
def query(shop):
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamodb.Table('pringle_prices')
    response = table.query(
        KeyConditionExpression=Key('shop').eq(shop)
    )
    return response
def restore_back_up():
    data = [{'price': '£1.50', 'shop': 'asda', 'date': '11/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '11/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '11/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '11/05/2021'},
     {'price': '£2.50', 'shop': 'tesco', 'date': '11/05/2021'},
     {'price': '£1.50', 'shop': 'asda', 'date': '13/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '13/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '13/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '13/05/2021'},
     {'price': '£2.50', 'shop': 'tesco', 'date': '13/05/2021'},
     {'price': '£1.50', 'shop': 'asda', 'date': '14/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '14/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '14/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '14/05/2021'},
     {'price': '£2.50', 'shop': 'tesco', 'date': '14/05/2021'},
     {'price': '£1.50', 'shop': 'asda', 'date': '16/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '16/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '16/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '16/05/2021'},
     {'price': '2.50', 'shop': 'tesco', 'date': '16/05/2021'},
     {'price': '£1.50', 'shop': 'asda', 'date': '12/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '12/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '12/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '12/05/2021'},
     {'price': '£2.50', 'shop': 'tesco', 'date': '12/05/2021'},
     {'price': '£1.50', 'shop': 'asda', 'date': '15/05/2021'},
     {'price': '£3', 'shop': 'coop', 'date': '15/05/2021'},
     {'price': '£3', 'shop': 'morrisons', 'date': '15/05/2021'},
     {'price': '£2.50', 'shop': 'sainsburys', 'date': '15/05/2021'},
     {'price': '£2.50', 'shop': 'tesco', 'date': '15/05/2021'}]
    print(len(data))
    for i in data:
        add_iteam(i['shop'],i['date'],i['price'])
if __name__ == '__main__':
    #create_table()
    #print(get_table())
    jo = query('tesco')
    print(jo['Items'])

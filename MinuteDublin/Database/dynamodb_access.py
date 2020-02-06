###############
# Stop items
###############
import boto3
from decimal import Decimal
import datetime as datetime

dynamodb = boto3.resource('dynamodb')

# Database object creation classes/methods
## Stops
def create_stop_item(stop_id, name, type, latitude, longitude,\
                     routes, arrivals, is_open):
    stop_hash = {'id':stop_id, 'name':name, 'type':type, 'latitude':str(latitude),\
                 'longitude':str(longitude), 'routes':routes, 'arrivals':arrivals,\
                 'is_open':bool(is_open),'timestamp':datetime.datetime.now().isoformat()}
    return stop_hash

# Transportation item creation
def create_transport_item(transport_id, name, type, route, latitude,\
                          longitude, last_stop_time):
    transport_hash = {'id':transport_id, 'name':name, 'type':type,\
                      'route':route, 'latitude':str(latitude),\
                      'longitude':str(longitude), 'last_stop_time':last_stop_time,\
                      'timestamp':datetime.datetime.now().isoformat()}
    return transport_hash

# Transportation item creation
def create_route_item(route_id, name, type, segments, stops):
    transport_hash = {'id':route_id, 'name':name, 'type':type,\
                      'segments': segments, 'stops':stops,\
                      'timestamp':datetime.datetime.now().isoformat()}
    return transport_hash

# Database access classes/methods
def read_table_item(table_name, key_name, key_value):
    """
    Return item read by primary key.
    """
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={key_name: key_value})
    return response

def add_item(table_name, table_item):
    """
    Add one item (row) to table. table_item is a dictionary {col_name: value}.
    """
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=table_item)
    return response

def delete_item(table_name, key_name, key_value):
    """
    Delete an item (row) in table from its primary key.
    """
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={key_name: key_value})
    return
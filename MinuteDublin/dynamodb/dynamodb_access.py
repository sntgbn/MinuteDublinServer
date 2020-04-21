###############
# Stop items
###############
import boto3
from decimal import Decimal
import datetime as datetime

dynamodb = boto3.resource('dynamodb')

# Database object creation classes/methods
## Stops
def __create_stop_item__(stop_id, name, type, latitude, longitude):
    stop_hash = {'id':stop_id, 'name':name, 'type':type, 'latitude':str(latitude),\
                 'longitude':str(longitude), 'timestamp':datetime.datetime.now().isoformat()}
    return stop_hash

# Transportation item creation
def __create_transport_item__(transport_id, name, type, route, latitude,\
                              longitude, last_stop_time):
    transport_hash = {'id':transport_id, 'name':name, 'type':type,\
                      'route':route, 'latitude':str(latitude),\
                      'longitude':str(longitude), 'last_stop_time':last_stop_time,\
                      'timestamp':datetime.datetime.now().isoformat()}
    return transport_hash

# Route item creation
def __create_route_item__(route_id, name, type, segments, stops):
    transport_hash = {'id':route_id, 'name':name, 'type':type,\
                      'segments': segments, 'stops':stops,\
                      'timestamp':datetime.datetime.now().isoformat()}
    return transport_hash

# Database access classes/methods
def __read_table_item__(table_name, key_name, key_value):
    """
    Return item read by primary key.
    """
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={key_name: key_value})
    return response

def __read_all_table_items__(table_name):
    """
    Return item read by primary key.
    """
    table = dynamodb.Table(table_name)
    return table.scan()['Items']

def __add_item__(table_name, table_item):
    """
    Add one item (row) to table. table_item is a dictionary {col_name: value}.
    """
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=table_item)
    return response

def __delete_item__(table_name, key_name, key_value):
    """
    Delete an item (row) in table from its primary key.
    """
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={key_name: key_value})
    return response

#################################
##             BUS             ##
#################################
def create_bus_stop(stop_id, name, latitude, longitude):
    stop_hash = __create_stop_item__(stop_id=stop_id, name=name, type='bus',
                                     latitude=latitude, longitude=longitude)
    db_return = __add_item__(table_name='BusStops', table_item=stop_hash)
    return db_return

def get_bus_stop(key_name, key_value):
    response = __read_table_item__(table_name='BusStops', key_name=key_name,\
                                   key_value=key_value)
    return response

def get_all_bus_stops():
    return __read_all_table_items__('BusStops')


def delete_bus_stop(key_name, key_value):
    response = __delete_item__(table_name='BusStops', key_name=key_name,\
                               key_value=key_value)
    return response

#################################
##             TRAINS          ##
#################################
def create_train_stop(stop_id, name, latitude, longitude):
    stop_hash = __create_stop_item__(stop_id=stop_id, name=name, type='train',
                                     latitude=latitude, longitude=longitude)
    db_return = __add_item__(table_name='TrainStops', table_item=stop_hash)
    return db_return

def get_train_stop(key_name, key_value):
    response = __read_table_item__(table_name='TrainStops', key_name=key_name,\
                                   key_value=key_value)
    return response

def get_all_train_stops():
    return __read_all_table_items__('TrainStops')

def get_all_trains():
    return __read_all_table_items__('TrainTransports')

def get_all_reports():
    return __read_all_table_items__('reports')


def delete_train_stop(key_name, key_value):
    response = __delete_item__(table_name='TrainStops', key_name=key_name,\
                               key_value=key_value)
    return response

#################################
##          HOSPITALS          ##
#################################
def create_hospital(name, latitude, longitude):
    hospital = {'name':name, 'latitude':str(latitude), 'longitude':str(longitude)}
    db_return = __add_item__(table_name='Hospitals', table_item=hospital)
    return db_return

def get_all_hospitals():
    return __read_all_table_items__('Hospitals')

def delete_hospital(name):
    response = __delete_item__(table_name='Hospitals', key_name='name',\
                               key_value=name)
    return response

#################################
##        FIRE STATIONS        ##
#################################
def create_firestation(name, latitude, longitude):
    fire_station = {'name':name, 'latitude':str(latitude), 'longitude':str(longitude)}
    db_return = __add_item__(table_name='FireStations', table_item=fire_station)
    return db_return

def get_all_firestations():
    return __read_all_table_items__('FireStations')

def delete_firestation(name):
    response = __delete_item__(table_name='FireStations', key_name='name',\
                               key_value=name)
    return response

#################################
##       GARDA STATIONS        ##
#################################
def create_gardastation(name, latitude, longitude):
    garda_station = {'name':name, 'latitude':str(latitude), 'longitude':str(longitude)}
    db_return = __add_item__(table_name='GardaStations', table_item=garda_station)
    return db_return

def get_all_gardastations():
    return __read_all_table_items__('GardaStations')

def delete_gardastation(name):
    response = __delete_item__(table_name='GardaStations', key_name='name',\
                               key_value=name)
    return response

#################################
##             EVENT           ##
#################################
def create_event(event_id, name, latitude, longitude):
    event = {'event_id':event_id, 'name':name, 'latitude':str(latitude), 'longitude':str(longitude)}
    db_return = __add_item__(table_name='Events', table_item=event)
    return db_return

def get_all_events():
    return __read_all_table_items__('Events')

def delete_event(event_id):
    response = __delete_item__(table_name='Events', key_name='event_id',\
                               key_value=event_id)
    return response


#################################
##              LUAS           ##
#################################
def create_lua_stop(stop_id, name, latitude, longitude):
    stop_hash = __create_stop_item__(stop_id=stop_id, name=name, type='lua',
                                     latitude=latitude, longitude=longitude)
    db_return = __add_item__(table_name='LuaStops', table_item=stop_hash)
    return db_return

def get_lua_stop(key_name, key_value):
    response = __read_table_item__(table_name='LuaStops', key_name=key_name,\
                                   key_value=key_value)
    return response

def delete_lua_stop(key_name, key_value):
    response = __delete_item__(table_name='LuaStops', key_name=key_name,\
                               key_value=key_value)
    return response

#################################
##            POLYGON          ##
#################################
def is_inside_polygon(latitude, longitude, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l-1:
        i += 1
        #printi,poly[i], j,poly[j]
        if ((poly[i]["lat"] <= latitude and latitude < poly[j]["lat"]) or (poly[j]["lat"] <= latitude and latitude < poly[i]["lat"])):
            if (longitude < (poly[j]["lng"] - poly[i]["lng"]) * (latitude - poly[i]["lat"]) / (poly[j]["lat"] - poly[i]["lat"]) + poly[i]["lng"]):
                c = not c
        j = i
    return c

dublin_coordinates = [{'lat':53.2099936251, 'lng':-6.2568709764},{'lat':53.2383995869, 'lng':-6.404197593},
                      {'lat':53.2966406056, 'lng':-6.4678633444},{'lat':53.3756575371, 'lng':-6.4741118017},
                      {'lat':53.4151111465, 'lng':-6.4016981933},{'lat':53.4240400411, 'lng':-6.2456373822},
                      {'lat':53.3987380065, 'lng':-6.02341142},  {'lat':53.2510960153, 'lng':-6.0471419289},
                      {'lat':53.2234549302, 'lng':-6.1220412746},{'lat':53.2099936251, 'lng':-6.2568709764}]
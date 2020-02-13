import boto3
import dynamodb_access as ddba
import json
import unittest 
  
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Stops')

class minuteDublinStops(unittest.TestCase):   
    # Returns True or False.  
    def test_a_1_put_dummy_stop_bus(self):
        print('Test A 1 - Creating dummy bus stop object for DB')
        dummy_stop = ddba.create_bus_stop(stop_id="9057323590", name='Generic Bus',\
                                          latitude= 53.3498, longitude= -6.2603)
        print('Test A 1 - Successfully created dummy BUS stop object for DB')
        self.assertTrue(True)
    
    def test_a_2_get_dummy_stop_bus(self):
        print('Test A 2 - Reading dummy bus stop object for DB')
        response = ddba.get_bus_stop(key_name='id', key_value="9057323590")
        self.assertNotEqual(first=response.get('Item'), second=None, msg='Test A 2 - Dummy BUS stop object NOT FOUND in DB')
        print('Test A 2 - Dummy BUS stop object FOUND in DB')

    def test_a_3_put_dummy_stop_lua(self):
        print('Test A 3 - Creating dummy stop object for DB')
        dummy_stop = ddba.create_lua_stop(stop_id="100411", name='LuLua',\
                                          latitude= 53.3498, longitude= -6.2603)
        print('Test A 3 - Successfully created dummy LUA stop object for DB')
        self.assertTrue(True)

    def test_a_4_get_dummy_stop_lua(self):
        print('Test A 4 - Reading dummy bus stop object for DB')
        response = ddba.get_lua_stop(key_name='id', key_value="100411")
        self.assertNotEqual(first=response.get('Item'), second=None, msg='Test A 4 - Dummy LUA stop object NOT FOUND in DB')
        print('Test A 4 - Dummy LUA stop object FOUND in DB')

    def test_a_5_put_dummy_stop_train(self):
        print('Test A 5 - Creating dummy stop object for DB')
        dummy_stop = ddba.create_train_stop(stop_id="71411", name='Snowpiercer',\
                                            latitude= 53.3498, longitude= -6.2603)
        print('Test A 5 - Successfully created dummy TRAIN stop object for DB')
        self.assertTrue(True)

    # def test_a_6_get_dummy_stop_lua(self):
    #     print('Test A 6 - Reading dummy TRAIN stop object for DB')
    #     response = ddba.get_train_stop(key_name='id', key_value=71411)
    #     self.assertNotEqual(first=response.get('Item'), second=None, msg='Test A 6 - Dummy TRAIN stop object NOT FOUND in DB')
    #     print('Test A 6 - Dummy TRAIN stop object FOUND in DB')

    # def test_b_1_put_dummy_transport_bus(self):
    #     print('Test B 1 - Creating dummy BUS transport object for DB')
    #     dummy_transport = ddba.create_transport_item(transport_id=1993, name='Ottos Bus',\
    #                                             type= 'bus', route='Green', latitude= 53.3498,\
    #                                             longitude= -6.2603, last_stop_time='00:30')
    #     response = ddba.add_item(table_name='BusTransports', table_item=dummy_transport)
    #     print('Test B 1 - Successfully created dummy BUS stop object for DB')
    #     self.assertTrue(True)

    # def test_b_2_get_dummy_transport_bus(self):
    #     print('Test B 2 - Reading dummy BUS transport object for DB')
    #     response = ddba.read_table_item(table_name='BusTransports', key_name='id', key_value=1993)
    #     self.assertNotEqual(first=response.get('Item'), second=None, msg='Test B 2 - Dummy BUS transport object NOT FOUND in DB')
    #     print('Test B 2 - Dummy BUS transport object FOUND in DB')

    # def test_b_3_put_dummy_transport_lua(self):
    #     print('Test B 1 - Creating dummy transport object for DB')
    #     dummy_transport = ddba.create_transport_item(transport_id=121, name='PARNELLLUA',\
    #                                             type= 'lua', route='Green', latitude= 53.3498,\
    #                                             longitude= -6.2603, last_stop_time='00:30')
    #     response = ddba.add_item(table_name='LuaTransports', table_item=dummy_transport)
    #     print('Test B 1 - Successfully created dummy LUA stop object for DB')
    #     self.assertTrue(True)

    # def test_b_4_get_dummy_transport_lua(self):
    #     print('Test B 2 - Reading dummy LUA transport object for DB')
    #     response = ddba.read_table_item(table_name='LuaTransports', key_name='id', key_value=121)
    #     self.assertNotEqual(first=response.get('Item'), second=None, msg='Test B 2 - Dummy LUA transport object NOT FOUND in DB')
    #     print('Test B 2 - Dummy LUA transport object FOUND in DB')

    # def test_b_5_put_dummy_transport_lua(self):
    #     print('Test B 5 - Creating dummy TRAIN transport object for DB')
    #     dummy_transport = ddba.create_transport_item(transport_id=121, name='PARNELLLUA',\
    #                                             type= 'train', route='Green', latitude= 53.3498,\
    #                                             longitude= -6.2603, last_stop_time='00:30')
    #     response = ddba.add_item(table_name='TrainTransports', table_item=dummy_transport)
    #     print('Test B 5 - Successfully created dummy TRAIN stop object for DB')
    #     self.assertTrue(True)

    # def test_b_6_get_dummy_transport_train(self):
    #     print('Test B 6 - Reading dummy TRAIN transport object for DB')
    #     response = ddba.read_table_item(table_name='TrainTransports', key_name='id', key_value=121)
    #     self.assertNotEqual(first=response.get('Item'), second=None, msg='Test B 6 - Dummy TRAIN transport object NOT FOUND in DB')
    #     print('Test B 6 - Dummy TRAIN transport object FOUND in DB')

if __name__ == '__main__': 
    unittest.main() 
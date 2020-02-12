import boto3
import dynamodb_access as ddba
import json
import unittest 
  
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Stops')

class minuteDublinStops(unittest.TestCase):   
    # Returns True or False.  
    def test_a_1_put_dummy_stop(self):
        print('Test A 1 - Creating dummy stop object for DB')
        dummy_stop = ddba.create_stop_item(stop_id=9057323590, name='LuLua',\
            type= 'Lua', latitude= 53.3498, longitude= -6.2603,\
            routes= ['Route66', 'El Camino'], arrivals= ['Everything', 'Nothing'], is_open= True)
        response = ddba.add_item(table_name='Stops', table_item=dummy_stop)
        print('Test A 1 - Successfully created dummy stop object for DB')
        self.assertTrue(True)
    
    def test_a_2_get_dummy_stop(self):
        print('Test A 2 - Reading dummy stop object for DB')
        response = ddba.read_table_item(table_name='Stops', key_name='id', key_value=9057323590)
        self.assertNotEqual(first=response.get('Item'), second=None, msg='Test A 2 - Dummy stop object NOT FOUND in DB')
        print('Test A 2 - Dummy stop object FOUND in DB')

    # def test_a_3_delete_dummy_stop(self):
    #     ddba.delete_item(table_name='Stops', key_name='id', key_value=9057323590)
    #     response = ddba.read_table_item(table_name='Stops', key_name='id', key_value=9057323590)
    #     self.assertEqual(first=response.get('Item'), second=None, msg='Test A 3 - Dummy stop object UNSUCCESSFULLY deleted from DB')
    #     print('Test A 3 - Dummy stop object successfully deleted from DB')

    def test_b_1_put_dummy_stop(self):
        print('Test B 1 - Creating dummy transport object for DB')
        dummy_transport = ddba.create_transport_item(transport_id=100411, name='Green LuLua',\
                                                type= 'Lua', route='Green', latitude= 53.3498,\
                                                longitude= -6.2603, last_stop_time='00:30')
        response = ddba.add_item(table_name='Transports', table_item=dummy_transport)
        print('Test B 1 - Successfully created dummy stop object for DB')
        self.assertTrue(True)

    def test_b_2_get_dummy_stop(self):
        print('Test B 2 - Reading dummy transport object for DB')
        response = ddba.read_table_item(table_name='Transports', key_name='id', key_value=100411)
        self.assertNotEqual(first=response.get('Item'), second=None, msg='Test B 2 - Dummy transport object NOT FOUND in DB')
        print('Test B 2 - Dummy transport object FOUND in DB')

    # def test_b_3_delete_dummy_stop(self):
    #     ddba.delete_item(table_name='Transports', key_name='id', key_value=100411)
    #     response = ddba.read_table_item(table_name='Stops', key_name='id', key_value=100411)
    #     self.assertEqual(first=response.get('Item'), second=None, msg='Test A 3 - Dummy transport object UNSUCCESSFULLY deleted from DB')
    #     print('Test A 3 - Dummy transport object successfully deleted from DB')

    def test_c_1_put_dummy_route(self):
        # create_route_item(route_id, name, type, segments, stops)
        print('Test C 1 - Creating dummy route object for DB')
        dummy_transport = ddba.create_route_item(route_id=71408, name='Green',\
                                                 type= 'Lua', segments=['SegmentA', 'SegmentB'],
                                                 stops=['StopA', 'StopB'])
        response = ddba.add_item(table_name='Routes', table_item=dummy_transport)
        print('Test C 1 - Successfully created dummy route object for DB')
        self.assertTrue(True)

    def test_c_2_get_dummy_route(self):
        print('Test C 2 - Reading dummy route object for DB')
        response = ddba.read_table_item(table_name='Routes', key_name='id', key_value=71408)
        self.assertNotEqual(first=response.get('Item'), second=None, msg='Test C 2 - Dummy route object NOT FOUND in DB')
        print('Test C 2 - Dummy route object FOUND in DB')

if __name__ == '__main__': 
    unittest.main() 
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

    def test_a_6_put_dummy_hospital(self):
        print('Test A 6 - Putting dummy hospital on DB')
        dummy_hospital = ddba.create_hospital('hospi', 15, 15)
        print('Test A 6 - Successfully created dummy hospital object for DB')

    def test_a_7_put_dummy_hospital(self):
        print('Test A 7 - Deleting dummy hospital from DB')
        dummy_hospital = ddba.delete_hospital('hospi')
        print('Test A 7 - Successfully deleted dummy hospital from DB')

    def test_a_8_put_dummy_firestation(self):
        print('Test A 8 - Putting dummy fire station on DB')
        dummy_hospital = ddba.create_firestation('fire', 15, 15)
        print('Test A 8 - Successfully created dummy fire station object on DB')

    def test_a_9_put_dummy_firestation(self):
        print('Test A 9 - Deleting dummy fire station from DB')
        dummy_hospital = ddba.delete_firestation('fire')
        print('Test A 9 - Successfully deleted dummy fire station from DB')

    def test_a_8_put_dummy_gardastation(self):
        print('Test A 8 - Putting dummy fire station on DB')
        dummy_hospital = ddba.create_gardastation('garda', 15, 15)
        print('Test A 8 - Successfully created dummy garda station object for DB')

    def test_a_9_put_dummy_gardastation(self):
        print('Test A 9 - Deleting dummy fire station from DB')
        dummy_hospital = ddba.delete_gardastation('garda')
        print('Test A 9 - Successfully deleted dummy garda station from DB')

    def test_a_10_put_dummy_event(self):
        print('Test A 8 - Putting dummy event on DB')
        dummy_hospital = ddba.create_event(0, 'emergency', 15, 15)
        print('Test A 8 - Successfully created dummy event on DB')

    def test_a_9_put_dummy_gardastation(self):
        print('Test A 9 - Deleting dummy event from DB')
        dummy_hospital = ddba.delete_event(0)
        print('Test A 9 - Successfully deleted dummy event from DB')


if __name__ == '__main__': 
    unittest.main() 
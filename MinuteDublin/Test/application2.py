from flask import Flask


redis_host = "minutedublin-001.ivfkmx.0001.use1.cache.amazonaws.com"
redis_port = 6379

def get_all_bus_stops_from_redis():

    with open('bus_stops.json') as json_file:
        data = json.load(json_file)
        filtered_data = {"type": "FeatureCollection","features":[]}
        for feature in data['features']:

            latitude = feature['geometry']['coordinates'][0]
            longitude = feature['geometry']['coordinates'][1]

            distance_to_center = np.sqrt(( -6.254572 - latitude)**2 + ( 53.343792- longitude)**2)

            if distance_to_center < 0.08:
                filtered_data["features"].append(feature)

    return filtered_data


def get_all_bus_stops():
    r = redis.StrictRedis(host=redis_host, port=redis_port, charset="utf-8", decode_responses=True)
    bus_stops = r.get("bus_stops")

    return json.loads(bus_stops)



# print a nice greeting.
def say_hello(username = "General Kenobi!"):
    return '<p>Hello %s!</p>\n' % username

# get something from the DB
def get_db(key = "a"):
    r = redis.StrictRedis(host=redis_host, port=redis_port)
    r.get(key)
    return '<p>%s</p>\n' % r.get(key)

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    get_db("a") + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

application.add_url_rule('/get_all_bus_stops', 'get_all_bus_stops', get_all_bus_stops)

application.add_url_rule('/get_all_bus_stops_from_redis', 'get_all_bus_stops_from_redis', get_all_bus_stops_from_redis)




# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="0.0.0.0", port=80)

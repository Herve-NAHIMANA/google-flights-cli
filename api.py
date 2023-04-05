from flask import Flask, render_template
from flask_restful import Resource, Api
from flight_finder import FlightFinder


app = Flask(__name__)
api = Api(app)
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/contacts')
def contacts():
    return render_template("contact.html")
@app.route('/flights/<from_>/<to_>/<start_>')
def find_flights_oneway(from_, to_, start_):
    ff = FlightFinder(from_, to_, start_)
    
    return ff.find_flights()

@app.route('/flights/<from_>/<to_>/<start_>/<end_>')
def find_flights(from_, to_, start_, end_):
    ff = FlightFinder(from_, to_, start_, end_)
    
    return ff.find_flights()

@app.route('/flights/<from_>/<to_>/<start_>/<end_>/<passengers_>')
def find_flights_passengers(from_, to_, start_, end_, passengers_):
    ff = FlightFinder(from_, to_, start_, end_, passengers_)
    
    return ff.find_flights()

@app.route('/flights/<from_>/<to_>/<start_>/<end_>/<stops_>')
def find_flights_stops(from_, to_, start_, end_, stops_):
    ff = FlightFinder(from_, to_, start_, end_, None, stops_)
    
    return ff.find_flights()

@app.route('/flights/<from_>/<to_>/<start_>/<end_>/<passengers_>/<stops_>')
def find_flights_passengers_stops(from_, to_, start_, end_, stops_):
    ff = FlightFinder(from_, to_, start_, end_, passengers_, stops_)
    
    return ff.find_flights()

@app.route('/cheapest/<from_>/<to_>/<start_>')
def find_cheapest_oneway(from_, to_, start_):
    ff = FlightFinder(from_, to_, start_)
    
    return ff.find_flight()

@app.route('/cheapest/<from_>/<to_>/<start_>/<end_>')
def find_cheapest(from_, to_, start_, end_):
    ff = FlightFinder(from_, to_, start_, end_)
    
    return ff.find_flight()

@app.route('/cheapest/<from_>/<to_>/<start_>/<end_>/<passengers_>')
def find_cheapest_passengers(from_, to_, start_, end_, passengers_):
    ff = FlightFinder(from_, to_, start_, end_, passengers_)
    
    return ff.find_flight()

@app.route('/cheapest/<from_>/<to_>/<start_>/<end_>/<stops_>')
def find_cheapest_stops(from_, to_, start_, end_, stops_):
    ff = FlightFinder(from_, to_, start_, end_, None, stops_)
    
    return ff.find_flight()

@app.route('/cheapest/<from_>/<to_>/<start_>/<end_>/<passengers_>/<stops_>')
def find_cheapest_passengers_stops(from_, to_, start_, end_, stops_):
    ff = FlightFinder(from_, to_, start_, end_, passengers_, stops_)
    
    return ff.find_flight()

if __name__ == '__main__':
    app.run(debug=True)

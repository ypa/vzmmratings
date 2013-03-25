from flask import Response
from flask import request
from models import Hotel
from models import Review
import datetime
import time
import jsonutil
import random



def home():
  return redirect(url_for('list_hotels'))

def warmup():
  """App Engine warmup handler
  See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
  """
  return ''

def list_hotels():
  hotels = Hotel.all().fetch(None)
  return jsonutil.encode(hotels)

def hotel_reviews(hotel_id):
  hotel = Hotel.get_by_id(hotel_id)
  reviews = hotel.reviews
  return jsonutil.encode(reviews)

def create_hotel():
  if request.headers['Content-Type'] != 'application/json; charset=UTF-8':
    raise Exception("415 Unsupported Media Type")
  data = request.json
  hotel = Hotel(**data)
  hotel.put()
  return jsonutil.encode(hotel.key().id())

def show_hotel_by_id(hotel_id):
  hotel = Hotel.get_by_id(hotel_id)
  return jsonutil.encode(hotel)

def show_hotel_by_name(name):
  q = Hotel.all()
  hotel_list = q.filter("name = ", name)
  return jsonutil.encode(hotel_list)

def show_hotel_by_number(number):
  q = Hotel.all()
  hotel_list = q.filter("number = ", number)
  return jsonutil.encode(hotel_list)

def edit_hotel_review(hotel_id):
  if request.method == 'POST':
    hotel = Hotel.get_by_id(hotel_id)
    data = request.json
    review = Review(**data)
    review.hotel = hotel
    review.put()
    return hotel_reviews(hotel_id)




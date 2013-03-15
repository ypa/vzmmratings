from google.appengine.ext import db

class ExampleModel(db.Model):
  """Example Model"""
  example_id = db.StringProperty(required=True)
  example_title = db.StringProperty(required=True)
  added_by = db.UserProperty()
  timestamp = db.DateTimeProperty(auto_now_add=True)


class Hotel(db.Model):
  """Hotel Model"""
  number = db.IntegerProperty(required=True)
  name = db.StringProperty(required=True)
  description = db.TextProperty()
  #implicitly created property'reviews' from Review ReferenceProperty


class Review(db.Model):
  """Review model"""
  #hotel ReferenceProperty
  hotel = db.ReferenceProperty(Hotel, collection_name='reviews')
  rating = db.RatingProperty(required=True, choices=set([1, 2, 3, 4, 5]))
  rater = db.StringProperty(required=True)
  comment = db.TextProperty()
  rater_city = db.StringProperty()
  rater_country = db.StringProperty()
  timestamp = db.DateTimeProperty(auto_now_add=True)

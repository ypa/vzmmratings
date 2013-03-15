from flask import render_template

from application import app
from application import views


app.add_url_rule('/api/', view_func=views.home, methods=['GET',]) # Main page


#hotel reviews endpoint
app.add_url_rule('/api/hotels/<int:hotel_id>/reviews', view_func=views.hotel_reviews, methods=['GET'])

#add hotel review endpoint
app.add_url_rule('/api/hotels/<int:hotel_id>/reviews/edit', view_func=views.edit_hotel_review, methods=['PUT', 'POST'] )

#hotels list endpoint
app.add_url_rule('/api/hotels', view_func=views.list_hotels, methods=['GET'])

#endpoint for creating a new hotel
app.add_url_rule('/api/hotels/create', view_func=views.create_hotel, methods=['POST'])

#endpoint for getting a specific hotel
app.add_url_rule("/api/hotels/<int:hotel_id>", view_func=views.show_hotel_by_id, methods=['GET'])

#ednpoint for filtering hotels by name
app.add_url_rule("/api/hotels/name/<string:name>", view_func=views.show_hotel_by_name, methods=['GET'])

#ednpoint for filtering hotels by number
app.add_url_rule("/api/hotels/number/<int:number>", view_func=views.show_hotel_by_number, methods=['GET'])

## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
  return render_template('500.html'), 500


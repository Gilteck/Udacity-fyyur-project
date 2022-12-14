#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from sqlalchemy import func
from flask import Flask, render_template, request, Response, flash, redirect, url_for
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
# local import
from init import moment, db, migrate
from controllers import venue, show, artist
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
def register_init(app):
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)



app = Flask(__name__)
app.config.from_object('config')
register_init(app)

# TODO: connect to a local postgresql database(COMPLETED)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

    # TODO: (COMPLETED) implement any missing fields, as a database migration using Flask-Migrate


    # TODO: (COMPLETED) implement any missing fields, as a database migration using Flask-Migrate

# TODO (COMPLETED) Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: (COMPLETED) replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
    return venue.get_venues()


@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: (COMPLETED) implement search on venues with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
    return venue.search_venues()


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: (COMPLETED) replace with real venue data from the venues table, using venue_id
    return venue.show_venue(venue_id)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  return venue.create_venue_form()


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: (COMPLETED) insert form data as a new Venue record in the db, instead
  # TODO: (COMPLETED) modify data to be the data object returned from db insertion
    return venue.create_venue_submission()

  # on successful db insert, flash success
  # TODO: (COMPLETED) on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  

@app.route('/venues/<venue_id>/delete', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: (COMPLETED) Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
    return venue.delete_venue(venue_id)


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: (COMPLETED) replace with real data returned from querying the database
    return artist.artists()


@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: (COMPLETED) implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
    return artist.search_artists()


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: (COMPLETED) replace with real artist data from the artist table, using artist_id
    return artist.show_artist(artist_id)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  # TODO: (COMPLETED) populate form with fields from artist with ID <artist_id>
     return artist.edit_artist(artist_id)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: (COMPLETED) take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
    return artist.edit_artist_submission(artist_id)


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  # TODO: (COMPLETED) populate form with values from venue with ID <venue_id>
      return venue.edit_venue(venue_id)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: (COMPLETED) take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
     return venue.edit_venue_submission(venue_id)


#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    return artist.create_artist_form()


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: (COMPLETED) insert form data as a new Venue record in the db, instead
  # TODO: (COMPLETED) modify data to be the data object returned from db insertion
  # on successful db insert, flash success
  # TODO: (COMPLETED) on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
    return artist.create_artist_submission()


@app.route('/artists/<int:artist_id>/delete', methods=['DELETE'])
def delete_artist(artist_id):
    return artist.delete_artist(artist_id)


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: (COMPLETED) replace with real venues data.
    return show.shows()


@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
    return show.create_shows()


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: (COMPLETED) insert form data as a new Show record in the db, instead
  # on successful db insert, flash success
  # TODO: (COMPLETED) on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return show.create_show_submission()


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
#if __name__ == '__main__':
#    app.run()

# Or specify port manually:

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000)


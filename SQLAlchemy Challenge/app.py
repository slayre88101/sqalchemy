# Import the dependencies.
import numpy as np
from pathlib import Path
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine('C:\Anaconda\python\sql\sqalchemy_challenge\surfsup\Starter_Code\Resources\hawaii.sqlite')

# reflect an existing database into a new model
start = automap_base()
# reflect the tables
start.prepare(autoload_with = engine, reflect = True)

# Save references to each table
measurements = start.classes.measurement
stations = start.classes.station
# Create our session (link) from Python to the DB
Session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(_name_)



#################################################
# Flask Routes
#################################################

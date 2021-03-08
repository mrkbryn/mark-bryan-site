from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('research', __name__, url_prefix='/research')

# Temporary mock-data
research_data = [
    {
        "name": "Data Vocalization: Optimizing Voice Output of Relational Data",
        "date": "August 2017",
        "publication": "Proceedings of the VLDB Endowment, Volume 10",
        "url": "http://www.vldb.org/pvldb/vol10/p1574-trummer.pdf",
        "description": "Research on data visualization aims at finding the best way to present data "
                       "via visual interfaces. We introduce the complementary problem of 'data vocalization.' "
                       "Our goal is to present relational data in the most efficient way via voice output. "
                       "This problem setting is motivated by emerging tools and devices (e.g., Google Home, "
                       "Amazon Echo, Apple’s Siri, or voice-based SQL interfaces) that communicate data primarily "
                       "via audio output to their users...",
    },
    {
        "name": "Vocalizing Large Time Series Efficiently",
        "date": "July 2018",
        "publication": "Proceedings of the VLDB Endowment, Volume 11",
        "url": "http://www.vldb.org/pvldb/vol11/p1563-trummer.pdf",
        "description": "We vocalize query results for time series data. We describe a holistic approach "
                       "that integrates query evaluation and vocalization. In particular, we generate only "
                       "those parts of the query result that are relevant for voice output..."
    },
]


@bp.route('/')
def index():
    return render_template('research/index.html', research=research_data)

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_simple_geoip import SimpleGeoIP
from utils import *
import os

app = Flask(__name__)
os.environ['GEOIPIFY_API_KEY']="at_1nz6LP168j2nkHEkBP3M2CZXqw3ZX"
CORS(app)
simple_geoip = SimpleGeoIP(app)

##################
# Web app routes #
##################

@app.route("/api/", methods=["GET"])
def index_api():

    data=get_world_data()
    return json.dumps(data)

@app.route("/api/continent/<iso2>")
def continent_api(iso2):
    
    data=get_continent_data(iso2, True)
    return data


@app.route("/api/country/<iso2>")
def country_api(iso2):
    data=get_country_data(iso2, True)
    return data


##################
# Web app routes #
##################

    
@app.route("/", methods=["GET"])
def index():

    data=get_world_data()
    if not data:
        return "Donnees indisponible"
    
    html=render_template('index.html', title="World",
                        data=data)
    return html

@app.route("/continent/<iso2>/")
def continent(iso2):
    
    data=get_continent_data(iso2, True)
    if not data:
        return "Donnees indisponible"


    html=render_template('cont_page.html', data=data)
    return html


@app.route("/country/", methods=['GET', 'POST'])
def country():
    
    if request.method == "POST":
        
        iso2=request.form['iso2']

        if not iso2:
            return "Donnees indisponible"

        
        data=get_country_data(iso2, True)

        if not data:
            return "Donnees indisponible"


        html=render_template('pays_page.html', data=data)

    else:
        geoip_data = simple_geoip.get_geoip_data()
        
        iso2="CM"
        try:
            iso2=geoip_data['location']["country"]
        except:
            iso2="CM"
            
        data=get_country_data(iso2, True)

        if not data:
            return "Donnees indisponible"

        html=render_template('pays_page.html', data=data)
    return html

@app.route("/about/", methods=["GET"])
def about():
    
    html=render_template('about_page.html')
    return html


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port)

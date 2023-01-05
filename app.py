""" Random banner app
"""

from glob import glob
import os
from random import choice

from flask import Flask, render_template, send_file

# app instance
app = Flask(__name__)

@app.route("/")
def root_text():
    "Root page"
    return ("No contents in this page. §^ム^§")

@app.route("/banner.png", methods=['GET'])
def get_banner():
    "Returns random banner"
    banners = glob("./static/banners/*.png")
    banner = choice(banners)
    return send_file(os.path.abspath(banner), mimetype="image/png")

@app.route("/gallery", methods=['GET'])
def gallery():
    "return gallery"
    banners = glob("./static/banners/*.png")
    return render_template("gallery.html", banners=banners)

@app.route("/gallery/<int:number>", methods=['GET'])
def gallery_specific(number):
    "Returns selected banner"
    banners = glob(f"{os.path.dirname(__file__)}/banners/*.png")
    if number >= len(banners):
        return f"§^ム^§ < Sorry, but requested banner #{number} does not exist."
    return send_file(os.path.abspath(banners[number]), mimetype="image/png")
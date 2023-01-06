""" Random banner app
"""

from glob import glob
import os
from random import choice

from flask import Flask, render_template, send_file, url_for
from flask.views import View

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

# favicon: favicon.ico, favicon.png, site.webmanifest etc.
class Favicon(View):
    "dinamic dispatch class for favicon"
    methods = ['GET']
    def __init__(self, material, mime):
        self.material = material
        self.material_abspath = os.path.abspath(f"./static/{material}")
        self.mime = mime

    def dispatch_request(self):
        return send_file(self.material_abspath, self.mime)

# favicons in this site
favicon_materials = {
    "android-chrome-192x192.png": "image/png",
    "android-chrome-512x512.png": "image/png",
    "apple-touch-icon.png": "image/png",
    "favicon-16x16.png": "image/png",
    "favicon-32x32.png": "image/png",
    "favicon.ico": "image/vnd.microsoft.icon",
    "favicon.png": "image/png",
    "site.webmanifest": "application/manifest+json"
}

# add url rule for favicons
for material, mime in favicon_materials.items():
    app.add_url_rule(
        f"/{material}",
        view_func=Favicon.as_view(material, material, mime)
    )

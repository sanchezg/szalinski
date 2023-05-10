from flask import Blueprint, redirect, render_template, request

from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.domain.services.urls import UrlLookup, UrlStore

main = Blueprint("main", __name__, template_folder="templates")

@main.route("/", methods=["GET", "POST"])
@main.route("/<code>")
@inject
async def index(code=None, url_lookup: UrlLookup = Provide[Container.url_lookup], url_store: UrlStore = Provide[Container.url_store]):
    if request.method == "GET":
        if code is None or code == "favicon.ico":
            return render_template("index.html")
        # else: get url and redirect to hashed code
        url = await url_lookup(url_hash=code)
        if url:
            return redirect(url)
        return "Not found", 404
    url = request.form.get("url")
    url_hash = await url_store(url=url)
    return render_template("index.html", url_hash=url_hash)

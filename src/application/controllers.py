from flask import Blueprint, render_template, request


main = Blueprint("main", __name__, template_folder="templates")

@main.route("/", methods=["GET", "POST"])
@main.route("/<code>")
def index(code=None):
    if request.method == "GET":
        if code is None:
            return render_template("index.html")
        # else: redirect to hashed code
        render_template("index.html")
    url = request.form.get("url")
    return render_template("index.html", url_hash=url)

from app import app
from flask import url_for, redirect, render_template, flash, g, session
from plugin_manager import PluginManager


@app.route("/")
def root():
    return redirect("/dashboard", 302)


@app.route("/sources/<source_id>")
def source_details(source_id):
    plugin = PluginManager().get_plugins()[source_id]
    return render_template("source.html.j2", plugin=plugin)


@app.route("/dashboard")
def dashboard():
    plugins = PluginManager().get_plugins()
    return render_template("dashboard.html.j2", plugins=plugins)

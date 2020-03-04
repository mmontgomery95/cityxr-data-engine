from app import app
from flask import url_for, redirect, render_template, flash, g, session
from plugin_manager import PluginManager


@app.route("/")
def root():
    return redirect("/dashboard", 302)


@app.route("/dashboard")
def dashboard():
    plugins = PluginManager().get_plugins()
    return render_template("dashboard.html", plugins=plugins)

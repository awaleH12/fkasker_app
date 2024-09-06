from flask import Flask, redirect, render_template, request

def create_app():
  app = Flask(__name__, template_folder="templates")

  @app.route("/")
  def index():
    return render_template("index.html")
  
  @app.route("/test")
  def test():
    return "yeb our app is working"
  
  # error pages
  @app.errorhandler(404)
  def error404(e):
    return render_template("404.html"), 404
  
  @app.errorhandler(500)
  def error500(e):
    return render_template("500.html"), 500
  
  return app 
from flask import Blueprint, request,render_template,current_app


portfolio_blurprint=Blueprint("welcome",__name__, template_folder="templates")
@portfolio_blurprint.route("/",methods=["GET"])
def PortfolioView():
    return  render_template("my_protfolio/index.html")
# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, url_for
#from passlib.apps import custom_app_context as pwd_context
# from tempfile import mkdtemp

# from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
# if app.config["DEBUG"]:
#     @app.after_request
#     def after_request(response):
#         response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#         response.headers["Expires"] = 0
#         response.headers["Pragma"] = "no-cache"
#         return response

# # custom filter
# app.jinja_env.filters["usd"] = usd

# # configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    # rows=db.execute("SElect * from users Where id=:id",id=session["user_id"] )
    # bal=rows[0]["cash"]
    # rows=db.execute("SELECT * from purchase where userid=:id",id =session["user_id"])
    # x=set()
    # for user in rows:
    #     x.add(user["symbol"])
    # sharel={}
    # for a in x:
    #     share=0
    #     for user in rows:
    #         if user["symbol"]==a:
    #             share+=user["share"]
    #     sharel.update({a:share})
    # pricel={}
    # namel={}
    # for a in x:
    #     dic=lookup(a)
    #     pricel.update({a:dic["price"]})
    #     namel.update({a:dic["name"]})
    # total=0
    # for key in pricel:
    #     total+=pricel[key]*sharel[key]

    return render_template('lol.html')
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock."""
#     if request.method=="POST":
#         if not request.form.get("symbo"):
#             return apology("enter a symbol")
#         elif not request.form.get("shares"):
#             return apology("plz enter shares / symbol")
#         dic=lookup(request.form.get("symbo"))
#         if dic==None:
#             return apology("Not found")
#         try:
#             int(request.form.get("shares"))
#         except:
#             return apology("Enter Integer SHARES")
#         price=int(dic["price"])
#         name=dic["symbol"]
#         share=int(request.form.get("shares"))
#         cost=price*share
#         i=int(session["user_id"])
#         rows=db.execute("SELECT * FROM users WHERE id =:id",id=i )
#         cashh=int(rows[0]["cash"])
#
#         if cashh <cost:
#             return apology("cannot be purchased.Add Cash")
#         bal=cashh-cost
#         db.execute("UPDATE users SET cash=:cash WHERE id=:id",id=i,cash=bal)
#         db.execute("INSERT INTO purchase (userid,symbol,share,price) VALUES (:id,:symbol,:number,:price)",id=i,symbol=name,number=share,price=price)
#         rows=db.execute("SELECT * from purchase where userid=:id",id =session["user_id"])
#         x=set()
#         for user in rows:
#             x.add(user["symbol"])
#         sharel={}
#         for a in x:
#             share=0
#             for user in rows:
#                 if user["symbol"]==a:
#                     share+=user["share"]
#             sharel.update({a:share})
#         pricel={}
#         namel={}
#         for a in x:
#             dic=lookup(a)
#             pricel.update({a:dic["price"]})
#             namel.update({a:dic["name"]})
#         total=0
#         for key in pricel:
#             total+=pricel[key]*sharel[key]
#
#
#         return render_template("bought.html",namel=namel,pricel=pricel,bal=bal,usd=usd,x=x,sharel=sharel,inshare=total)
#
#     else:
#         return render_template("buy.html")
#
# @app.route("/history")
# @login_required
# def history():
#     """Show history of transactions."""
#     rows=db.execute("SELECT * from purchase where userid=:id",id =session["user_id"])
#
#     return render_template("history.html",rows=rows,usd=usd)
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Log user in."""
#
#     # forget any user_id
#     session.clear()
#
#     # if user reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":
#
#         # ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username")
#
#         # ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password")
#
#         # query database for username
#         rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
#
#         # ensure username exists and password is correct
#         if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
#             return apology("invalid username and/or password")
#
#         # remember which user has logged in
#         session["user_id"] = rows[0]["id"]
#
#         # redirect user to home page
#         return redirect(url_for("index"))
#
#     # else if user reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")
#
# @app.route("/logout")
# def logout():
#     """Log user out."""
#
#     # forget any user_id
#     session.clear()
#
#     # redirect user to login form
#     return redirect(url_for("login"))
#
# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     """Get stock quote."""
#     if request.method=="POST":
#         symbol=request.form.get("symbo")
#         dic=lookup(symbol)
#         if dic==None:
#             return apology("Not found")
#
#         return render_template("quoted.html",dici=dic,s=usd(dic["price"]))
#
#     return render_template("quote.html")
#
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     """Register user."""
#     if request.method == "POST":
#
#         # ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username")
#
#         # ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password")
#         elif request.form.get("password") != request.form.get("verify"):
#             return apology("passwords do not match")
#         # query database for username
#         ha=pwd_context.hash(request.form.get("password"))
#         uname=request.form.get("username")
#         rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
#         if len(rows)==1:
#             return apology("user alredy exist")
#
#         db.execute("INSERT INTO users (username,hash) VALUES (:username,:hashed)",username=request.form.get("username"),hashed=ha)
#
#
#         # redirect user to home page
#         return redirect(url_for("login"))
#
#     # else if user reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("register.html")
#
#
# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell shares of stock."""
#     if request.method=="POST":
#         if not request.form.get("symbo"):
#             return apology("enter a symbol")
#         elif not request.form.get("shares"):
#             return apology("plz enter shares / symbol")
#         try:
#             int(request.form.get("shares"))
#         except:
#             return apology("Enter integers SHARES")
#         rows=db.execute("SELECT * from purchase where userid=:id",id =session["user_id"])
#         x=set()
#         use=db.execute("SELECT * from users where id=:id",id =session["user_id"])
#         dic=lookup(request.form.get("symbo"))
#         price=int(dic["price"])
#         name=dic["symbol"]
#         share=int(request.form.get("shares"))
#         for user in rows:
#             x.add(user["symbol"])
#         if not name in x:
#             return apology("not bought")
#         sharea=0
#         for user in rows:
#             if user["symbol"]==name:
#                 sharea+=user["share"]
#         if share>sharea:
#             return apology("dont have enough shares")
#         bal=int(use[0]["cash"])+share*price
#         i=session["user_id"]
#         share=-1*share
#         db.execute("UPDATE users SET cash=:cash WHERE id=:id",id=i,cash=bal)
#         db.execute("INSERT INTO purchase (userid,symbol,share,price) VALUES (:id,:symbol,:number,:price)",id=i,symbol=name,number=share,price=price)
#         rows=db.execute("SELECT * from purchase where userid=:id",id =session["user_id"])
#         sharel={}
#         for a in x:
#             share=0
#             for user in rows:
#                 if user["symbol"]==a:
#                     share+=user["share"]
#             sharel.update({a:share})
#         pricel={}
#         namel={}
#         for a in x:
#             dic=lookup(a)
#             pricel.update({a:dic["price"]})
#             namel.update({a:dic["name"]})
#         total=0
#         for key in pricel:
#             total+=pricel[key]*sharel[key]
#
#
#         return render_template("sold.html",namel=namel,pricel=pricel,bal=bal,usd=usd,x=x,sharel=sharel,inshare=total)
#
#     else:
#         return render_template("sell.html")
# @app.route("/settings", methods=["GET", "POST"])
# @login_required
# def settings():
#     if request.method=="POST":
#         return render_template("changep.html")
#     else:
#         return render_template("settings.html")
# @app.route("/changep",methods=["GET","POST"])
# @login_required
# def changep():
#     if request.method=="POST":
#         if not (request.form.get("opass") or request.form.get("npass") or request.form.get("vpass")):
#             return apology("Enter details")
#         rows=db.execute("Select * from users Where id=:id",id=session["user_id"])
#         opass=request.form.get("opass")
#         npass=request.form.get("npass")
#         vpass=request.form.get("vpass")
#         if npass!=vpass:
#             return("new passowrd don't match")
#         if not pwd_context.verify(request.form.get("opass"), rows[0]["hash"]):
#             return apology("invalid username and/or password")
#         ha=pwd_context.hash(npass)
#         db.execute("Update users SET hash=:hash Where id=:id",id=session["user_id"],hash=ha)
#         session.clear()
#         return redirect(url_for("login"))
#     else:
#         return render_template("changep.html")
#
# @app.route("/addc", methods =["GET","POST"])
# @login_required
# def addc():
#     if request.method=="POST":
#         try:
#             int(request.form.get("money"))
#         except:
#             return apology("enter integer")
#         money=int(request.form.get("money"))
#         rows=db.execute("Select * from users WHERE id=:id",id=session["user_id"])
#         money+=(rows[0]["cash"])
#         db.execute("Update users SET cash=:money where id=:id",id=session["user_id"],money=money)
#         return redirect(url_for("index"))
#     else:
#         return render_template("addc.html")

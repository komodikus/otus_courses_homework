from database import query, Wares
from flask import Flask, render_template, request


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route("/")
def main_page():
    return render_template('mainpage.html', wares=query)

@app.route('/product/<int:pid>')
def show_product(pid=None):
    ware = Wares.get(Wares.id_ware==pid)
    if ware:
        return render_template('product_cart.html', ware=ware)
    return page_not_found



if __name__ == '__main__':
    app.run()

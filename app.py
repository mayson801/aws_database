from flask import Flask,render_template
import json
from aws_connection import *
app = Flask(__name__)

@app.route("/")
def load_home():
    #table_data = get_table()
    #print(table_data['Items'])
    shop_name=['asda','coop','morrisons','sainsburys','tesco']
    shop_data=[]
    for i in shop_name:
        query_shop = query(i)
        shop_data.append(query_shop['Items'])
    print(shop_data)
    return render_template('home.html', shop_data = shop_data)

if __name__ == "__main__":
    app.run(debug=True)
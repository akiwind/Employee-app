from flask import Blueprint, request, render_template, redirect
from app.db.werehouse_repo import (
    add_item, get_all_items, get_item_by_id, update_item, delete_item,
)

werehouse_bp = Blueprint("werehouse", __name__)

@werehouse_bp.route("/werehouse", methods=["GET","POST"])
def home():
      
    if request.method == "GET":
        html = render_template("werehouse/list.html",list_items=get_all_items())
        return html
    else:
        value = request.form["item_value"]
        ilosc = request.form["item_quantity"]
        category = request.form["item_category"]
        name = request.form["item_name"]

        if value is None or name is None or ilosc is None or category is None:
            return render_template("werehouse/list.html", 
                                    list_employees=get_all_items(),
                                    error="Wszystkie pola muszą być wypełnione!")
        
        try:
            value = int(value)
            ilosc = int(ilosc)
        except ValueError:
            return render_template("werehouse/list.html", 
                                    list_items=get_all_items(),
                                    error="Value i Quantity muszą być liczbami!")
        

        add_item(name, ilosc, value, category)
        return redirect("/werehouse") 

@werehouse_bp.route("/werehouse/edit/<int:item_id>", methods=["GET","POST"])
def item(item_id):

    if request.method == "GET":
        html = render_template("werehouse/edit.html" ,item_data = get_item_by_id(item_id))
        return html        
    else:
        update_item(request.form["item_name"],
                        request.form["item_quantity"],
                        request.form["item_value"],
                        request.form["item_category"],
                        item_id) 
        return redirect("/werehouse")


@werehouse_bp.route("/werehouse/delete/<int:item_id>", methods=["GET","POST"])
def delete(item_id):
    if request.method == "GET":
        html = render_template("/werehouse/delete.html" ,item_data = get_item_by_id(item_id))
        return html      
    else:
        delete_item(item_id)
        return redirect("/werehouse")


if __name__ == "__main__":
    app.run(debug=True)
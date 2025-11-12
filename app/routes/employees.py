from flask import Blueprint, request, render_template, redirect
from app.db.employees_repo import (
    get_all_employees, add_employees, get_employee_by_id, update_employee, delete_employee, phone_exists)

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/employees", methods=["GET","POST"])
def home():
      
    if request.method == "GET":
        html = render_template("employees/list.html",list_employees=get_all_employees())
        return html
    else:
        phone =request.form["phone"]
        name = request.form["first_name"]
        surname = request.form["last_name"]
        adres = request.form["address"]
        country = request.form["country"]

        if phone is None or name is None or surname is None or adres is None or country is None:
            return render_template("employees/list.html", 
                                    list_employees=get_all_employees(),
                                    error="Wszystkie pola muszą być wypełnione!")

        try:
            phone = int(phone)
        except ValueError:
            return render_template("employees/list.html", 
                                    list_employees=get_all_employees(),
                                    error="Numer telefonu musi mieć tylko cyfy!")

        if phone_exists(phone):
            return render_template("employees/list.html", 
                                    list_employees=get_all_employees(),
                                    error="Taki numer telefonu już istnieje!")

        add_employees(name, surname, adres, country, phone)
        return redirect("/employees") 

@employees_bp.route("/employees/edit/<int:emp_id>", methods=["GET","POST"])
def employee(emp_id):

    if request.method == "GET":
        html = render_template("employees/edit.html" ,employee_data = get_employee_by_id(emp_id))
        return html        
    else:
        update_employee(request.form["first_name"],
                        request.form["last_name"],
                        request.form["address"],
                        request.form["country"],
                        request.form["phone"],
                        emp_id)
        return redirect("/employees")


@employees_bp.route("/employees/delete/<int:emp_id>", methods=["GET","POST"])
def delete(emp_id):
    if request.method == "GET":
        html = render_template("employees/delete.html" ,employee_data = get_employee_by_id(emp_id))
        return html      
    else:
        delete_employee(emp_id)
        return redirect("/employees")


if __name__ == "__main__":
    app.run(debug=True)


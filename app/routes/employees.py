from flask import Blueprint, request, render_template
from app.db.employees_repo import (
    get_all_employees, add_employees, get_employee_by_id, update_employee, delete_employee)

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/", methods=["GET","POST"])
def home():
      
    if request.method == "GET":
        html = render_template("employees/list.html",list_employees=get_all_employees())
        return html
    else:
        add_employees(request.form["first_name"],
                      request.form["last_name"],
                      request.form["address"],
                      request.form["country"],
                      request.form["phone"])
        return redirect("/") 

@employees_bp.route("/edit/<int:emp_id>", methods=["GET","POST"])
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
        return redirect("/")


@employees_bp.route("/delete/<int:emp_id>", methods=["GET","POST"])
def delete(emp_id):
    if request.method == "GET":
        html = render_template("employees/delete.html" ,employee_data = get_employee_by_id(emp_id))
        return html      
    else:
        delete_employee(emp_id)
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


from flask import Blueprint, request, render_template
from app.db.connection import (
    get_all_employees, add_employees, get_employee_by_id, update_employee, delete_employee
)


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
    if request.method == "POST":
        delete_employee(emp_id)
        return "<h1>Usunieto pracownika</h1><a href='/'>Zobacz listę pracowników</a>"
    else:
        employee_data = get_employee_by_id(emp_id)
        return (f"<br><h1>Czy na pewno chcesz usunąć pracownika z listy?</h1><br><form method='POST'>" \
            f"<p>Obecne dane: {employee_data}</p>"
            f"<input type='submit' >TAK</form>"\
            f"<a href='/'>Wróc do listy pracowników</a>")


if __name__ == "__main__":
    app.run(debug=True)


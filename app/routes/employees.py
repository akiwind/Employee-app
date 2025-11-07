from flask import Blueprint, request
from app.db.connection import (
    get_all_employees, add_employees, get_employee_by_id, update_employee, delete_employee
)

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/", methods=["GET","POST"])
def home():
    list_employees = get_all_employees()
    html = "<h1>Lista pracowników</h1><ul>"
    for emp in list_employees:
        html += f"<li>{emp}<a href='/edit/{emp[0]}'><button type='button'>Edytuj</button></a><a href='/delete/{emp[0]}'><button type='button'>Usuń</button></a></li>"
    html += "</ul>"
    if request.method == "POST":
        add_employees(request.form["first_name"],request.form["last_name"],request.form["address"],request.form["country"],request.form["phone"])
        return "<h1>Wysłano formularz</h1><br><a href='/'>Zobacz listę pracowników</a>" 
    else:
        return html + "<br><h1>Wypełnij formularz</h1><br><form method='POST'>" \
        "<label>First name:</label><br><input type='text' name='first_name'><br>" \
        "<label>Last name:</label><br><input type='text' name='last_name'><br>" \
        "<label>Adres:</label><br><input type='text' name='address'><br>" \
        "<label>Country:</label><br><input type='text' name='country'><br>" \
        "<label>Phone number:</label><br><input type='text' name='phone'><br>" \
        "<input type='submit'></form>"


@employees_bp.route("/edit/<int:emp_id>", methods=["GET","POST"])
def employee(emp_id):
    if request.method == "POST":
        update_employee(request.form["first_name"],request.form["last_name"],request.form["address"],request.form["country"],request.form["phone"],emp_id)
        return "<h1>Edytowano dane</h1><a href='/'>Zobacz listę pracowników</a>"
    else:
        employee_data = get_employee_by_id(emp_id)
        return (f"<br><h1>Wypełnij formularz edycji danych</h1><br><form method='POST'>" \
            f"<p>Obecne dane: {employee_data}</p>"
            f"<label>First name:</label><br><input type='text' name='first_name'><br>" \
            f"<label>Last name:</label><br><input type='text' name='last_name'><br>" \
            f"<label>Adres:</label><br><input type='text' name='address'><br>" \
            f"<label>Country:</label><br><input type='text' name='country'><br>" \
            f"<label>Phone number:</label><br><input type='text' name='phone'><br>" \
            f"<input type='submit' >Zapisz</form>"\
            f"<a href='/'>Zobacz listę pracowników</a>")


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


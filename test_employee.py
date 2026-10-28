
from employee import employee_details

def test_employee_details():
    result = employee_details("Rahul", "EMP101", "IT", 50000)

    expected = (
        "Employee Name: Rahul\n"
        "Employee ID: EMP101\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    assert result == expected

#   Problem No 01
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def area(self):
        return self.side_length ** 2

    @property
    def perimeter(self):
        return 4 * self.side_length

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.side_length})"

    def __str__(self) -> str:
        return f"Square with side length: {self.side_length}"


class Cube(Square):
    def __init__(self, side_length):
        super().__init__(side_length)
    
    def volume(self):
        return  self.side_length ** 3
        
    def surface_area(self):
        return 6 * self.side_length ** 2

# -------------------------------------------------------------------------


# Problem No 02

import math

class Point:
    """
    A class to represent a point in a 2D coordinate system.
    """
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Initializes a new point at the given coordinates.
        
        x: x-coordinate (default is 0.0)
        y: y-coordinate (default is 0.0)
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        """Gets the x-coordinate."""
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """Sets the x-coordinate."""
        self._x = value

    @property
    def y(self) -> float:
        """Gets the y-coordinate."""
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """Sets the y-coordinate."""
        self._y = value

    def distance_to(self, other: 'Point') -> float:
        """
        Calculates the distance between this point and another point.
        
        :param other: Another point in the 2D coordinate system.
        :return: The distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_from_origin(self) -> float:
        """
        Calculates the distance from the origin (0, 0) to this point.
        
        :return: The distance from the origin to this point.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        """Return a string representation of the Point instance."""
        return f'{type(self).__name__} ({self.x},{self.y})'


class Point3D(Point):
    """
    A class to represent a point in a 3D coordinate system, inheriting from Point.
    """
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        """
        Initializes a new point in a 3D coordinate system.
        
        x: x-coordinate (default is 0.0)
        y: y-coordinate (default is 0.0)
        z: z-coordinate (default is 0.0)
        """
        super().__init__(x, y)
        self._z = z

    @property
    def z(self) -> float:
        """Gets the z-coordinate."""
        return self._z

    @z.setter
    def z(self, value: float) -> None:
        """Sets the z-coordinate."""
        self._z = value

    def distance_from_origin(self) -> float:
        """
        Calculates the distance from the origin (0, 0, 0) to this point.
        
        :return: The distance from the origin to this point.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def distance_to(self, other: 'Point3D') -> float:
        """
        Calculates the distance between this point and another 3D point.
        
        :param other: Another point in the 3D coordinate system.
        :return: The distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + 
                         (self.y - other.y) ** 2 + 
                         (self.z - other.z) ** 2)

    def __repr__(self):
        """Return a string representation of the Point3D instance."""
        return f'{type(self).__name__} ({self.x}, {self.y}, {self.z})'


# -------------------------------------------------------------------------------------------------

# Problem No 03

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side
    def __repr__(self) -> str:
        return f'Square(side={self.side})'

# -----------------------------------------------------------------------------------------

# Problem No 04

import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @property
    def circumference(self) -> float:
        return 2 * math.pi * self._radius

    @property
    def diameter(self) -> float:
        return self._radius * 2


class Sphere(Circle):
    def __init__(self, radius: float):
        super().__init__(radius)

    @property
    def surface_area(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self) -> float:
        return (4/3) * math.pi * (self.radius ** 3)

    def __repr__(self) -> str:
        return f"Sphere(radius={self.radius})"


# -----------------------------------------------------------------------------------------

# Problem No 05

class Payroll_system:
    def calculate_payroll(self, employees):
        print("Calculate Payroll")
        print("===========================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print()

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Salary_employee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class Hourly_employee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class Commission_employee(Salary_employee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

# --------------------------------------------------------------------------------------

# Problem No 06

class ElectricalEmployee:
    def __init__(self, fName, lName, pay, department="Electrical Department"):
        self.fName = fName
        self.lName = lName
        self.email = f"{self.fName.lower()}{self.lName.lower()}@uet.edu.pk"
        self.pay = pay
        self.department = department

    def raisePay(self, percentage):
        self.pay += self.pay * (percentage / 100)

    def __str__(self):
        return (
            f"Name: {self.fName} {self.lName}\n"
            f"Email: {self.email}\n"
            f"Pay: Rs{self.pay:.2f}\n"
            f"Department: {self.department}")

class ElectricalAdminStaff(ElectricalEmployee):
    def __init__(self, fName, lName, pay, team=None):
        super().__init__(fName, lName, pay)
        self.team = team
        self.tasks = []

    def assignTask(self, task):
        self.tasks.append(task)

    def __str__(self):
        base_info = super().__str__()
        team_info = f"Team: {self.team}" if self.team else "Team: None"
        tasks_info = f"Tasks Assigned: {', '.join(self.tasks) if self.tasks else 'No tasks assigned'}"
        return f"{base_info}\n{team_info}\n{tasks_info}"

class ElectricalInstructor(ElectricalEmployee):
    def __init__(self, fName, lName, pay, designation):
        super().__init__(fName, lName, pay)
        self.designation = designation
        self.courses = []

    def assignCourse(self, course):
        self.courses.append(course)

    def __str__(self):
        base_info = super().__str__()
        designation_info = f"Designation: {self.designation}"
        courses_info = f"Courses Assigned: {', '.join(self.courses) if self.courses else 'No courses assigned'}"
        return f"{base_info}\n{designation_info}\n{courses_info}"

# --------------------------------------------------------------------------------------------------------------------------------------


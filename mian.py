from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from typing import Dict, Optional, List
import hashlib


# ==================================================
# Utilities
# ==================================================

class PasswordHasher:

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    @staticmethod
    def verify(
        password: str,
        hashed: str
    ) -> bool:
        return (
            PasswordHasher
            .hash_password(password)
            == hashed
        )


# ==================================================
# Domain
# ==================================================

@dataclass(frozen=True)
class Employee:
    id: int
    name: str
    age: int
    salary: float


@dataclass(frozen=True)
class User:
    username: str
    password: str


# ==================================================
# Exceptions
# ==================================================

class EmployeeError(Exception):
    pass


class EmployeeExists(EmployeeError):
    pass


class EmployeeNotFound(EmployeeError):
    pass


class AuthenticationError(Exception):
    pass


# ==================================================
# Repository Contracts
# ==================================================

class EmployeeRepository(ABC):

    @abstractmethod
    def save(self, employee):
        pass

    @abstractmethod
    def get_by_id(self, emp_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def remove(self, emp_id):
        pass


class UserRepository(ABC):

    @abstractmethod
    def login(
        self,
        username,
        password
    ):
        pass


# ==================================================
# Infrastructure
# ==================================================

class InMemoryEmployeeRepository(
    EmployeeRepository
):

    def __init__(self):
        self.storage: Dict[
            int,
            Employee
        ] = {}

    def save(
        self,
        employee
    ):
        self.storage[
            employee.id
        ] = employee

    def get_by_id(
        self,
        emp_id
    ):
        return self.storage.get(
            emp_id
        )

    def get_all(
        self
    ):
        return list(
            self.storage.values()
        )

    def remove(
        self,
        emp_id
    ):
        self.storage.pop(
            emp_id,
            None
        )


class InMemoryUserRepository(
    UserRepository
):

    def __init__(self):

        self.users = {

            "admin":
            User(
                "admin",
                PasswordHasher
                .hash_password(
                    "admin123"
                )
            )

        }

    def login(
        self,
        username,
        password
    ):

        user = self.users.get(
            username
        )

        if not user:
            raise AuthenticationError(
                "User not found"
            )

        if not (
            PasswordHasher
            .verify(
                password,
                user.password
            )
        ):
            raise AuthenticationError(
                "Wrong password"
            )

        return True


# ==================================================
# Services
# ==================================================

class EmployeeService:

    def __init__(
        self,
        repo
    ):
        self.repo = repo

    def add_employee(
        self,
        id,
        name,
        age,
        salary
    ):

        if (
            self.repo
            .get_by_id(
                id
            )
        ):
            raise EmployeeExists()

        if age < 18:
            raise ValueError(
                "Invalid age"
            )

        if salary <= 0:
            raise ValueError(
                "Invalid salary"
            )

        emp = Employee(
            id,
            name.title(),
            age,
            salary
        )

        self.repo.save(
            emp
        )

    def update_salary(
        self,
        id,
        salary
    ):

        emp = (
            self.repo
            .get_by_id(
                id
            )
        )

        if not emp:
            raise EmployeeNotFound()

        updated = replace(
            emp,
            salary=salary
        )

        self.repo.save(
            updated
        )

    def remove(
        self,
        id
    ):

        if not (
            self.repo
            .get_by_id(
                id
            )
        ):
            raise EmployeeNotFound()

        self.repo.remove(
            id
        )

    def show(self):

        for emp in (
            self.repo
            .get_all()
        ):
            print(emp)


# ==================================================
# Login Service
# ==================================================

class AuthService:

    def __init__(
        self,
        repo
    ):
        self.repo = repo

    def login(
        self
    ):

        username = input(
            "Username: "
        )

        password = input(
            "Password: "
        )

        return (
            self.repo
            .login(
                username,
                password
            )
        )


# ==================================================
# UI
# ==================================================

def menu():

    print("""
1 Add Employee
2 Show Employees
3 Update Salary
4 Remove Employee
5 Exit
""")


def main():

    auth = AuthService(
        InMemoryUserRepository()
    )

    try:

        auth.login()

        print(
            "\nLogin Success\n"
        )

    except Exception as e:

        print(
            e
        )

        return

    service = EmployeeService(
        InMemoryEmployeeRepository()
    )

    while True:

        menu()

        choice = input(
            "Choose: "
        )

        try:

            if choice == "1":

                service.add_employee(
                    int(
                        input(
                            "ID:"
                        )
                    ),

                    input(
                        "Name:"
                    ),

                    int(
                        input(
                            "Age:"
                        )
                    ),

                    float(
                        input(
                            "Salary:"
                        )
                    )

                )

            elif choice == "2":

                service.show()

            elif choice == "3":

                service.update_salary(

                    int(
                        input(
                            "ID:"
                        )
                    ),

                    float(
                        input(
                            "Salary:"
                        )
                    )

                )

            elif choice == "4":

                service.remove(

                    int(
                        input(
                            "ID:"
                        )
                    )

                )

            elif choice == "5":

                break

        except Exception as e:

            print(
                f"\nError: {e}"
            )


if __name__ == "__main__":
    main()
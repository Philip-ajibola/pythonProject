from decimal import Decimal

from commission_employee import CommissionEmployee


class SalaryEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, nin, sales, rate, base_pay):
        super().__init__(first_name, last_name, nin, sales, rate)
        self.base_pay = base_pay


    @property
    def base_pay(self):
        return self._base_pay

    @base_pay.setter
    def base_pay(self,pay):
        if pay<Decimal(0.0): raise ValueError("Invalid pay")
        self._base_pay = pay

    def earning(self):
        return self.base_pay + super().earning()

    def __repr__(self):
        return f"{super().__repr__()}\n"\
                f"Salary: {self.base_pay}\n"\
                f"Monthly Earning: {self.earning()}"

izu =SalaryEmployee("Izu","Miraim",420,10000,15,500000)
#print(izu)
print(issubclass(SalaryEmployee,object))
print(isinstance(izu,SalaryEmployee))
print(issubclass(CommissionEmployee,SalaryEmployee))
print(issubclass(SalaryEmployee,CommissionEmployee))


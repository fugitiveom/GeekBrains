# - Начальный баланс равен нулю
# - Доступные действия: пополнить, снять, выйти
# - Сумма пополнения и снятия кратны 50 уе
# - Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 уе
# - После каждой третей операции пополнения или снятия начислаяются проценты - 3%
# - Нельзя снять больше чем на счете
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой орпецией,
# даже ошибочной
# - любое действие выводит сумму денег

import sys
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class BankSettings:
    withdraw_comission_ratio = 0.015
    withdraw_comission_min_ue = 30
    withdraw_comission_max_ue = 600
    withdraw_devided_by = 50
    operations_for_profit = 3
    profit_ratio = 0.03
    min_balance = 0
    rich_tax_ratio = 0.1
    rich_tax_threshold = 5_000_000

@dataclass
class CMD:
    withdraw = 'withdraw'
    deposit = 'deposit'
    stop = 'stop'

class Account:
    def __init__(self) -> None:
        self.__balance = 0
        self.__operations = 1

    def get_balance(self) -> int:
        return self.__balance

    def get_operations(self) -> int:
        return self.__operations

    def increase_operations(self) -> None:
        self.__operations += 1

    def withdraw(self, amount: int) -> None:
        self.__balance -= amount

    def deposit(self, amount: int) -> None:
        self.__balance += amount

class OperationCharge(ABC):
    def __init__(self, account: Account, amount: int) -> None:
        self._account = account
        self._amount = amount

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def get_charge(self):
        pass

class OperationComission(OperationCharge):
    def __init__(self, account: Account, amount: int) -> None:
        super().__init__(account, amount)
        self.__comission = self.calculate()

    def calculate(self):
        comission = \
            min(\
                 max(\
                     BankSettings.withdraw_comission_ratio * self._amount,\
                        BankSettings.withdraw_comission_min_ue\
                    ),
                 BankSettings.withdraw_comission_max_ue\
            )
        return comission

    def get_charge(self):
        return self.__comission

class OperationTax(OperationCharge):
    def __init__(self, account: Account, amount: int) -> None:
        super().__init__(account, amount)
        self.__tax = self.calculate()

    def calculate(self) -> int:
        return self._amount * BankSettings.rich_tax_ratio\
             if self._account.get_balance() >= BankSettings.rich_tax_threshold else 0

    def get_charge(self) -> int:
        return self.__tax

class OperationProfit(OperationCharge):
    def __init__(self, account: Account, amount: int) -> None:
        super().__init__(account, amount)
        self.__profit = self.calculate()

    def calculate(self) -> int:
        return self._amount * BankSettings.profit_ratio

    def get_charge(self) -> int:
        return self.__profit

class OperationPrep:
    def __init__(self, account: Account, amount: int, tax: OperationTax = None,\
                 comission: OperationComission = None, profit: OperationProfit = None,\
                     operation_type: str = '') -> None:
        self.account = account
        self.__amount = amount
        self.tax = tax
        self.comission = comission
        self.profit = profit
        self.__operation_type = operation_type
        self.__total_amount = self.calc_total_amount()

    def calc_total_amount(self):
        if self.__operation_type == CMD.withdraw:
            total_amount = self.__amount + self.comission.get_charge()\
                                + self.tax.get_charge()
        elif self.__operation_type == CMD.deposit:
            total_amount = self.__amount + (self.profit.get_charge()\
                 if self.check_profit_needed() else 0)
        return total_amount

    def check_withdraw_possible(self) -> bool:
        return self._check_devided_by() and self._check_funds_enough()

    def check_profit_needed(self) -> bool:
        return True if self.account.get_operations() % \
            BankSettings.operations_for_profit == 0 and\
                 self.account.get_operations() > 0 else False

    def get_total_amount(self) -> int:
        return self.__total_amount

    def _check_devided_by(self) -> bool:
        return self.__amount % BankSettings.withdraw_devided_by == 0

    def _check_funds_enough(self) -> bool:
        is_enough = self.account.get_balance() - self.__total_amount > 0
        return is_enough

class Operation:
    def __init__(self, operation_type: str, operation_data: OperationPrep) -> None:
        self.__operation_type = operation_type
        self.operation_data = operation_data
        self.__account = operation_data.account

    def process(self) -> None:
        if self.__operation_type == 'withdraw':
            self.__account.withdraw(self.operation_data.get_total_amount())
        if self.__operation_type == 'deposit':
            self.__account.deposit(self.operation_data.get_total_amount())
        self.__account.increase_operations()

class UserCli:
    account = Account()

    def __init__(self) -> None:
        self.main()

    def main(self) -> None:
        while True:
            print(f'\nТекущий баланс: {self.account.get_balance()}')
            print('Доступные команды:\n',
                  'withdraw - для снятия\n',
                  'deposit - для пополнения\n',
                  'stop - для выхода\n')
            cmd = input('Введите команду: ')
            if cmd.lower() == CMD.stop:
                sys.exit()
            if cmd.lower() == CMD.withdraw:
                amount = input('Введите сумму для снятия: ')
                try:
                    amount = int(amount)
                    comission = OperationComission(self.account, amount)
                    tax = OperationTax(self.account, amount)
                    checked_data = OperationPrep(self.account, amount, tax, comission,\
                                                  operation_type=cmd)
                    is_possible = checked_data.check_withdraw_possible()
                    if not is_possible:
                        raise ValueError
                    operation = Operation(cmd, checked_data)
                    operation.process()
                except ValueError:
                    print('Неправильная сумма')

            if cmd.lower() == CMD.deposit:
                amount = input('Введите сумму для внесения: ')
                try:
                    amount = int(amount)
                    tax = OperationTax(self.account, amount)
                    profit = OperationProfit(self.account, amount)
                    checked_data = OperationPrep(self.account, amount, profit = profit,\
                                                  operation_type=cmd)
                    operation = Operation(cmd, checked_data)
                    operation.process()
                except ValueError:
                    print('\nНеправильная сумма!')

if __name__ == '__main__':
    usercli = UserCli()
    usercli.main()

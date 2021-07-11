from client import ClientBinance , Agent
import datetime
from xlwt import Workbook
import pandas as pd
import numpy as np
def get_detect(data: pd.DataFrame, start_time: str):
    correct_data = pd.DataFrame(data.loc[(data['date'] >= start_time)].detect)
    correct_data = np.array(correct_data)  # array for ml
    return correct_data


class Account(ClientBinance):
    __balance = 0
    __name = ""
    __transaction = []
    __coins = {'btc' : 0.0}
    def __init__(self , balance:float , name:str , api_key:str , api_secret:str):
        super(Account, self).__init__(api_key , api_secret )
        self.__balance = balance
        self.__name = name
    def get_balance(self):
        return self.__balance
    def details_toString(self):
        print("name:" + self.__name + "\n"+ "balance:" + str(self.__balance) + "$")
    def transaction(self , value:float):
        op = '+' if  value > 0 else '-'
        if op=='-' and abs(value) > self.__balance :
            print("not enough money")
        else:
            self.__balance = value + self.__balance
            temp = {'timeStamp':datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") ,'value':value , 'operation': op ,
                    'balance':self.__balance , 'coin':self.__coins['btc']}
            self.__transaction.append(temp)
    def coin_exchange(self , symbol:str='btc' , amount:float=0 ,price:float=0, buy:bool=True ):
        if not buy and self.__coins[symbol]>=amount:
            self.__coins[symbol] = self.__coins[symbol] - amount
            self.transaction(value=amount*price)
            print(self.__coins[symbol])
        elif buy and self.get_balance() >= amount*price:
            self.__coins[symbol] = self.__coins[symbol] + amount
            self.transaction(value=-amount*price)
            print(self.__coins[symbol])

    def get_transaction(self):
        return self.__transaction
    def get_coins_amount(self,name:str='btc'):
        return self.__coins[name]
    def export_to_excel(self , filename:str):
        wb = Workbook()
        sheet1 = wb.add_sheet('Demo transaction')
        sheet1.write(0, 0, 'Transaction Time')
        sheet1.write(0, 1, 'Balance')
        sheet1.write(0, 2, 'Value')
        sheet1.write(0, 3, 'Operation')
        sheet1.write(0, 4, 'Coin Amount')

        for index , item in enumerate(self.__transaction , start=1):
            sheet1.write(index, 0, item['timeStamp'] )
            sheet1.write(index, 1, item['balance'])
            sheet1.write(index, 2, abs(item['value']))
            sheet1.write(index, 3, 'Deposit' if item['operation']== '+' else 'Withdraw')
            sheet1.write(index, 4, item['coin'])

        wb.save(filename+'.xls')
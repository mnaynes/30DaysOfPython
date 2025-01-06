from math import sqrt
import pandas as pd

class MyStatistics:
    def __init__(self, sample_size=[]):
        self.sample_size = sorted(sample_size)
    
    def count(self):
        return len(self.sample_size)
    
    def sum(self):
        sum = 0
        for item in self.sample_size:
            sum += item

        return sum
    
    def min(self):
        return self.sample_size[0]
    
    def max(self):
        return self.sample_size[len(self.sample_size)-1]
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        if self.count() % 2 == 0:
            return (self.sample_size[self.count()//2] + self.sample_size[self.count()//2 - 1]) / 2
        else:
            return self.sample_size[self.count()//2]
    
    def freq_dist(self):
        D = {} 
        for item in self.sample_size: 
            if item in D: 
                D[item] = D[item] + 1
            else: 
                D[item] = 1
                
        return sorted(D.items(), key=lambda x:x[1], reverse=True)
        
    def mode(self):
        freq_dist = self.freq_dist()
        return freq_dist[0]
    
    def var(self):
        variance = 0
        mean = self.mean()
        for item in self.sample_size:
            variance += (item - mean)**2
        
        return variance / self.count()
    
    def std(self):
        return sqrt(self.var())
    
    def describe(self):
        print(f'Count: {self.count()}')
        print(f'Sum: {self.sum()}')
        print(f'Min: {self.min()}')
        print(f'Max: {self.max()}')
        print(f'Range: {self.range()}')
        print(f'Mean: {self.mean():.0f}')
        print(f'Median: {self.median()}')
        print(f'Mode: {self.mode()}')
        print(f'Standard Deviation: {self.std():.1f}')
        print(f'Variance: {self.var():.1f}')
        print(f'Frequency Distribution: {self.freq_dist()}')
        

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]  
data = MyStatistics(ages)
data.describe()

#####################################################################################################################################

class PersonAccount:
    def __init__(self, firstname, lastname, income=[], expenses=[], properties=[]):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expenses = expenses
        self.properties = properties

    def total_income(self):
        return sum(self.income['Value'] + self.properties['Value'])

    def add_expenses(self):
        return sum(self.expenses['Value'])

    def account_balance(self):
        return self.total_income() - self.add_expenses()
    
    def print_data(self, data):
        return pd.DataFrame.from_dict(data).to_string(index=False)
    
    def print_fullname(self):
        return self.firstname + ' ' + self.lastname
    
    def describe(self):
        print(f'\nStatement Balance of {self.print_fullname()}')
        print(f'\n{self.print_data(self.income)}')
        print(f'\n{self.print_data(self.expenses)}')
        print(f'\n{self.print_data(self.properties)}')
        print(f'\nTotal Income: {self.total_income():,.2f}')
        print(f'\nTotal Expenses: {self.add_expenses():,.2f}')
        print(f'\nAccount Balance: {self.account_balance():,.2f}')


income = {
    'Income' : ['Merchandise Sale', 'Revenue from Training', 'Income from sale of van'],
    'Value' : [25800, 5000, 2000]
}
expenses = {
    'Expense' : ['Procurement Costs', 'Wages', 'Rent', 'Interest Paid', 'Transportation', 'Utilities'],
    'Value': [8000, 700, 1000, 500, 300, 150,]
}

properties = {
    'Property' : ['Real Estate', 'Town House'],
    'Value' : [50200, 30000]
}
user = PersonAccount('Mike', 'Smith', income, expenses, properties)
user.describe()
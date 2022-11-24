import pandas as pd
import types
op = pd.read_csv('../data/series_dataframe.csv')
op_not = op.loc[(op['Series'] != op['DataFrame'])]
op_ser = op_not['Series'].dropna()
op_ser_list = op_ser.tolist()

count = 0
for i in op_ser_list:
    try:

        if type(pd.Series.__dict__[i]) == types.FunctionType:
            print(i, end=',  ')
            count += 1
            if count % 5 == 0:
                print()
    except Exception as e:
        pass
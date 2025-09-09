from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv('/home/kng/kng/MOUNTAIN2/LANDSLIDE_5yrs.csv')
new_df = pd.DataFrame(columns=df.columns)

for index, rows in df.iterrows():
    data = df.loc[index, :].values.tolist()
    early_str = data[0].split('~')[0]
    later = data[0].split('~')[1]
    date = datetime.strptime(early_str, '%Y-%m-%d') #산사태 시작날
    later_str = datetime.strptime(later, '%m-%d') 
    to_date = later_str.replace(year=date.year) #산사태 끝날

    date = date - timedelta(days=1)
    to_date = to_date - timedelta(days=1)
    
    while date <= to_date:
        date_str = date.strftime('%Y-%m-%d')
        new_row = [date_str] + data[1:]
        new_df = pd.concat([new_df, pd.DataFrame([new_row], columns=df.columns)], ignore_index=True)
        date += timedelta(days=1)
    print('Progressing...',index, '/', len(df))

new_df.to_csv('landslide_splited.csv', index=False)
print(new_df)

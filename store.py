import pandas as pd

polling_unit = 'New Polling Unit'

def create_initial_dataframe(parties):
    df = pd.DataFrame(columns=['Polling Unit'] + parties + ['Total Votes'])
    return df

def update_results(df, polling_unit, results):
    if df[df['Polling Unit'] == polling_unit].empty:
        new_row = {'Polling Unit': polling_unit}
        new_row.update(results)
        new_row['Total Votes'] = sum(results.values())
        df = df._append(new_row, ignore_index=True)
    else:
        df.loc[df['Polling Unit'] == polling_unit, list(results.keys())] = pd.Series(results)
        df.loc[df['Polling Unit'] == polling_unit, 'Total Votes'] = sum(results.values())
    
    return df

def save_to_csv(df, filename='polling_results.csv'):
    df.to_csv(filename, index=False)

def load_from_csv(filename='polling_results.csv'):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame()


def main():
    parties = ['ACN', 'ANPP', 'CDC', 'CPP', 'DPP', 'JP', 'LABO', 'PDP', 'PPA']
    df = load_from_csv()
    
    if df.empty:
        df = create_initial_dataframe(parties)
    
    print("Current DataFrame:")
    print(df)
    
    new_results = {'ACN': 120, 'ANPP': 150, 'CDC': 80}
    df = update_results(df, polling_unit, new_results)
    
    print("\nUpdated DataFrame:")
    print(df)
    
    save_to_csv(df)

if __name__ == '__main__':
    main()

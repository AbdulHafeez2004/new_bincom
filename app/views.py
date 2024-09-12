from django.shortcuts import render
from django.contrib import messages
import pandas as pd


# data = pd.read_csv('C:/Users/abdul/OneDrive/Desktop/bincom project/bincom/announced_lga_results.csv')
# Create your views here.

pu_data = pd.read_csv('C:/Users/abdul/OneDrive/Desktop/bincom project/bincom/announced_pu_results.csv')




def index(request):
    data = pd.read_csv('C:/Users/abdul/OneDrive/Desktop/bincom project/bincom/announced_lga_results.csv')
    df = data.head(9)
    geeks_object = df.to_html(classes='data', header="true")
    params={'geek': geeks_object}
    

    return render(request, 'index.html', params) 


def sum(request):
    pu_data = pd.read_csv('C:/Users/abdul/OneDrive/Desktop/bincom project/bincom/announced_pu_results.csv')

    if 'party_abbreviation' not in pu_data.columns or 'party_score' not in pu_data.columns:
        raise ValueError("CSV file must contain 'party_abbreviation' and 'party_score' columns")

    pu_data['party_score'] = pd.to_numeric(pu_data['party_score'], errors='coerce')

    pu_data.dropna(subset=['party_score'], inplace=True)

    party_totals = pu_data.groupby('party_abbreviation')['party_score'].sum().reset_index()

    party_totals.columns = ['Party', 'Total Score']

    party_totals.to_csv('party_totals.csv', index=False)


    total_object = party_totals.to_html(classes='data', header="true")
    params2={'sum': total_object}

    return render(request, 'sum.html', params2)    




from django.shortcuts import render
import pandas as pd 

def index(request):
    x=pd.read_csv(
        'teste.csv',
        sep=",",
        names=['cat', 'item', 'preço'])

    a=[[x.item[i], x.preço[i], x.cat[i]] for i in range(len(x))]
    context={'tabela':a}

    return render(request, 'gesso2.html', context)

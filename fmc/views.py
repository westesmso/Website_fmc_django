from django.shortcuts import render

def home(request):
    return render(request,'fmc/home.html')

def sobre(request):
    return render(request,'fmc/sobre.html')

def servicos(request):
    return render(request,'fmc/servicos.html')

def contato(request):
    return render(request,'fmc/contato.html')    

def trabalhe(request):    
    return render(request,'fmc/trabalhe.html')

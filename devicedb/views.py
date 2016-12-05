from django.shortcuts import render

def devicedb_list(request):
    return render(request, 'devicedb/devicedb_list.html', {})
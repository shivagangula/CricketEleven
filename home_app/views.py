from django.shortcuts import render
from cricbuzz import Cricbuzz
import json
import requests
c = Cricbuzz()




def new_home(request):
    matches = c.matches()
    send = {'matches' : matches}
    list_mathes = []
    for i in range(len(matches)):
        list_mathes.append(matches[i]['id'])
    live_match = []
    complt_match = []
    preview_match =[]
    for i in list_mathes:
        check = c.matchinfo(i)
        if check['mchstate'] == 'inprogress':
            live_match.append(check)
        elif check['mchstate'] ==  'innings break':
            live_match.append(check)
        elif check['mchstate'] == 'preview':
            preview_match.append(check)
        else:
            complt_match.append(check)
    send['live'] = live_match
    send['complited'] = complt_match
    send['preview'] = preview_match
    return render(request, 'home_app/new_home.html', send)

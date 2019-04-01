from django.shortcuts import render,HttpResponse
from home_app.views import c
import json

def score(request, id):
   score = c.scorecard(id)
   info = c.matchinfo(id)
   commentary = c.commentary(id)
   print(type(score))
   send = {      'matchinfo': info,
                 'commentary':commentary['commentary'],
                 }
   try:
               send['stat']     = info['mchstate']
               send['team1']      = score['scorecard'][0]
               send['bowlcard_1'] = score['scorecard'][0]['bowlcard']
               send['team2']      = score['scorecard'][1]
               send['bowlcard_2'] = score['scorecard'][1]['bowlcard']
   except:
        try:
              send['stat']     = info['mchstate']
              send['team1']      = score['scorecard'][0]
              send['bowlcard_1'] = score['scorecard'][0]['bowlcard']

        except:
             send['stat']  = info['mchstate']
   return render(request, 'score/score.html', send)

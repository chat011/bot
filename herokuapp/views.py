from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.views.generic import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer

ip = "192.168.10.12"

bot = ChatBot('MyChatBot')

# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
conversation = open('herokuapp/static/data/data.txt','r').readlines()
 
trainer.train(conversation)
@csrf_exempt
def hello(request):
    waiting_list=[]
    if request.method == 'POST':
        s=request.body
        a=json.loads(s)
        inputs=a['value']
        puts=a['data']
        if puts=="Daily":
            if inputs=="continue":
                print("1")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Daily"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        elif puts=="Bi-weekly":
            if inputs=="continue":
                print("2")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Bi-weekly"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")

        elif puts=="Monthly":
            if inputs=="continue":
                print("3")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Monthly"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        elif puts=="Extended_Wear":
            if inputs=="continue":
                print("4")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Extended_Wear"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        elif puts=="Toric_Astigmatism":
            if inputs=="continue":
                print("5")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Toric_Astigmatism"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        elif puts=="Multifocal_Presbyopia":
            if inputs=="continue":
                print("6")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Multifocal_Presbyopia"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        else:
            if inputs=="continue":
                print("7")
                waiting_list={"url":"https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python","image":"http://"+ip+":8000/static/image/adsasd.png","descripion":"Colored"}
                return HttpResponse(json.dumps(waiting_list), content_type="application/json")
            else:
                print("no")
        while True:
            message = inputs
            if message.strip()!= 'Bye':
                reply = bot.get_response(message)
                dats="'"+str(reply)+"'"
                x=dats.replace("'","")
                # print(x)
                dads={'message':x}
                print(dads)
                
                # print('ChatBot:',reply)
                waiting_list={'bot':"\""+str(reply)+"\""}
                return HttpResponse(json.dumps(dads), content_type="application/json")

            if message.strip()=='Bye':
                print('ChatBot:Bye')
                break

        waiting_list=[{'bot':"thanks"}]
        return HttpResponse(json.dumps(waiting_list), content_type="application/json")
    
    else:
        waiting_list=[{'bot':"thanks"}]
        print("*******************")
        return HttpResponse(json.dumps(waiting_list), content_type="application/json")
        
def index(request):
    return render(request,'index.html')


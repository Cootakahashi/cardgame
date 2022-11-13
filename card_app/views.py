from django.shortcuts import render
from .models import CardModel, CardInfo
from django.views.generic import ListView
import csv

class Decklistview(ListView):
    template_name = 'deck.html'
    model = CardModel
    def get(self, request):
        cardimg = CardInfo.objects.all()
        print(type(cardimg))
        print(len(cardimg))
        
        img = cardimg[0]
        img = img.image
        print(img)
        params = {'img': img}
        return render(request, 'deck.html', params)



class Cardlistview(ListView):
    template_name = 'card.html'
    model = CardModel




def logcsv(comment):
    with open('/root/cardgamelog.csv', 'a') as f:
        writer = csv.write(f)
        writer.writerow(comment)



def cardsave(request):
    print("HERE1")
    if request.method == 'POST':
        try:
            logcsv("here")
            number = request.POST['number']
            name = request.POST['name']
            atk = request.POST['atk']
            hp = request.POST['hp']
            stk = request.POST['stk']
            text = request.POST['text']
            level_limit = request.POST['level_limit']
            cnt_limit = request.POST['cnt_limit']
            party_num = request.POST['party_num']
            number_sheet_limit = request.POST['number_sheet_limit']
            print("HERWE2")
            

            obj = CardModel(number=number, name=name, atk=atk, hp=hp,stk=stk, text=text, level_limit=level_limit, cnt_limit=cnt_limit, party_num=party_num, number_sheet_limit=number_sheet_limit)
            obj.save()
            return render(request, 'post.html', {'result': '正常にカード情報を登録しました'})
        except:
            return render(request, 'post.html', {'result': '保存できませんでした、情報を正しく入力して再度登録してください'})
    else:
        return render(request, 'post.html', {'hi': 'hi'})



from django.shortcuts import render
from .models import CardModel, CardInfo
from django.views.generic import ListView
import csv
import os
from django.views.generic.detail import DetailView
from django.http import HttpResponse


def top(request):
    return render(request, 'top.html', {'items': 'hi'})

def ifrafunc(request):
    items = CardInfo.objects.all()
    return render(request, 'ifra.html', {'items': items})


class Decklistview(ListView):
    template_name = 'deck.html'
    model = CardModel
    def get(self, request):
        items = CardInfo.objects.all()

        params = {'items': items}
        return render(request, 'deck.html', params)

def tessave(request):
    import csv
    path = "/Users/takahashiko/crowdworks/takasan/needfile/1弾カード画像"
    files = os.listdir(path)
    pics = [f for f in files if os.path.isfile(os.path.join(path, f))]
    pics = sorted(pics)
    path_medi = "card_pics1/"


    # return render(request, 'deck.html', {'a': 'a'})
    # CardInfo.objects.all().delete()

    with open('/Users/takahashiko/crowdworks/takasan/needfile/card1-4-starter/1.csv', 'r') as f:
        reader = csv.reader(f)
        for num,lists in enumerate(reader):
            if num >= 1:

                lists.insert(0, '1')
                lv = lists[12]
                atk = lists[13]
                hp = lists[14]
                stk = lists[15]
                if lv == '':
                    lv = None
                
                elif atk == '':
                    atk = None
                    

                elif hp != None:
                    hp = 1
                    print("!!====")

                elif stk == '':
                    stk = None
                try:
                    obj = CardInfo(series=lists[0],
                    image=path_medi+pics[num],
                    number=lists[1],
                    rarelity=lists[2],
                    name_japan=lists[3],
                    kana=lists[4],
                    rubi=lists[5],
                    party=lists[7],
                    attribute=lists[8],
                    attribute2=lists[9],
                    attribute3=lists[10],
                    attribute4=lists[11],
                    lv=lists[12],
                    atk=lists[13],
                    hp=lists[14],
                    stk=lists[15],
                    leftup=lists[16],
                    leftdown=lists[17],
                    text =lists[18],
                    cnt=lists[19],
                    flaver_text=lists[20],
                    in_limit=lists[21],
                    )
                    obj.save()
                except Exception as e:
                    print(e)
                    print(num)
                    print("AAAAAAAAAA")
                    try:
                        obj = CardInfo(series=lists[0],
                        number=lists[1],
                        image=path_medi+pics[num],
                        rarelity=lists[2],
                        name_japan=lists[3],
                        kana=lists[4],
                        rubi=lists[5],
                        party=lists[7],
                        attribute=lists[8],
                        attribute2=lists[9],
                        attribute3=lists[10],
                        attribute4=lists[11],
                        lv=0,
                        atk=0,
                        hp=0,
                        stk=0,
                        leftup=lists[16],
                        leftdown=lists[17],
                        text =lists[18],
                        cnt=lists[19],
                        flaver_text=lists[20],
                        in_limit=lists[21],
                        )
                        obj.save()
                        print("!!!!!!!!!!!!!!!!!")
                    except Exception as e:
                        print(e)
                        print("=======================SECOND=====")
                    pass
        return render(request, 'deck.html', {'hi': 'hi'})



def saveinfo(request):
    import csv
    # CardInfo.objects.all().delete()

    with open('/Users/takahashiko/crowdworks/takasan/needfile/card1-4-starter/starter.csv', 'r') as f:
        reader = csv.reader(f)
        for num,lists in enumerate(reader):
            if num >= 1:

                lists.insert(0, '6')
                lv = lists[12]
                atk = lists[13]

                hp = lists[14]
                stk = lists[15]
                
                # if lv == '':
                #     lv = None
                
                # elif atk == '':
                #     atk = None
                    

                # elif hp != None:
                #     hp = 1
                #     print("!!====")


                # elif stk == '':
                #     stk = None
                try:
                    obj = CardInfo(series=lists[0],
                    number=lists[1],
                    rarelity=lists[2],
                    name_japan=lists[3],
                    kana=lists[4],
                    rubi=lists[5],
                    party=lists[7],
                    attribute=lists[8],
                    attribute2=lists[9],
                    attribute3=lists[10],
                    attribute4=lists[11],
                    lv=lists[12],
                    atk=lists[13],
                    hp=lists[14],
                    stk=lists[15],
                    leftup=lists[16],
                    leftdown=lists[17],
                    text =lists[18],
                    cnt=lists[19],
                    flaver_text=lists[20],
                    in_limit=lists[21],
                    )
                    obj.save()
                except Exception as e:
                    print(e)
                    print(num)
                    print("AAAAAAAAAA")
                    try:
                        obj = CardInfo(series=lists[0],
                        number=lists[1],
                        rarelity=lists[2],
                        name_japan=lists[3],
                        kana=lists[4],
                        rubi=lists[5],
                        party=lists[7],
                        attribute=lists[8],
                        attribute2=lists[9],
                        attribute3=lists[10],
                        attribute4=lists[11],
                        lv=0,
                        atk=0,
                        hp=0,
                        stk=0,
                        leftup=lists[16],
                        leftdown=lists[17],
                        text =lists[18],
                        cnt=lists[19],
                        flaver_text=lists[20],
                        in_limit=lists[21],
                        )
                        obj.save()
                        print("!!!!!!!!!!!!!!!!!")
                    except Exception as e:
                        print(e)
                        print("SECOND=====")
                    pass
        return render(request, 'deck.html', {'hi': 'hi'})
        
        
        
            
        

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









class card_detail(DetailView):
    model = CardInfo
    template_name = 'card_detail.html'


   
from django.shortcuts import render
from .models import CardModel
# Create your views here.

def cardsave(request):
    if request.method == 'POST':
        try:
            number = request.POST['number']
            name = request.POST['name']
            atk = request.POST['atk']
            hp = request.POST['hp']
            if int(hp) > 1:
                return 0
            stk = request.POST['stk']
            text = request.POST['text']
            level_limit = request.POST['level_limit']
            cnt_limit = request.POST['cnt_limit']
            party_num = request.POST['party_num']
            number_sheet_limit = request.POST['number_sheet_limit']

            obj = CardModel(number=number, name=name, atk=atk, hp=hp,stk=stk, text=text, level_limit=level_limit, cnt_limit=cnt_limit, party_num=party_num, number_sheet_limit=number_sheet_limit)
            obj.save()
            return render(request, 'post.html', {'result': '正常にカード情報を登録しました'})
        except:
            return render(request, 'post.html', {'result': '保存できませんでした、情報を正しく入力して再度登録してください'})
    else:
        return render(request, 'post.html', {'hi': 'hi'})

from django.shortcuts import render, get_object_or_404, redirect
from community.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse

def index(request):
    response_data = {}
    if request.method == "GET":
        return render(request,'community/index.html')

    elif request.method == "POST":
        login_userid = request.POST.get('userid', None)
        login_password = request.POST.get('password', None)

        if not ( login_userid and login_password):
            response_data['error'] = '아이디와 비밀번호를 모두 입력하세요.'
        else:
            myuser = User.objects.get(userid = login_userid)
            if check_password(login_password, myuser.password):
                return redirect('/home')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'community/index.html', response_data)

def home(request):
    return render(request,'community/home.html')

#######################

def detail2002(request):
    question = Question2002.objects.all()
    choice = Choice2002.objects.all()
    return render(request,'community/korea_japan.html',{'question':question, 'choice':choice})

def vote2002(request):
    question = Question2002.objects.all()
    choice = Choice2002.objects.all()
    try:
        selected_choice = choice.get(pk=request.POST['choice'])
    except(KeyError, Choice2002.DoesNotExist):
        return render(request,'community/korea_japan.html',{'question':question, 'error_message':"선택된 것이 없습니다."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('community:results2002',args=()))

def results2002(request):
    question = Question2002.objects.all()
    choice = Choice2002.objects.all()
    return render(request, 'community/korea_japan_results.html', {'question': question,'choice':choice})

#######################

def detail2010(request):
    question = Question2010.objects.all()
    choice = Choice2010.objects.all()
    return render(request,'community/namagog.html',{'question':question, 'choice':choice})

def vote2010(request):
    question = Question2010.objects.all()
    choice = Choice2010.objects.all()
    try:
        selected_choice = choice.get(pk=request.POST['choice'])
    except(KeyError, Choice2010.DoesNotExist):
        return render(request,'community/namagog.html',{'question':question, 'error_message':"선택된 것이 없습니다."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('community:results2010',args=()))

def results2010(request):
    question = Question2010.objects.all()
    choice = Choice2010.objects.all()
    return render(request, 'community/namagog_results.html', {'question': question,'choice':choice})

#######################

def detailnow(request):
    question = QuestionNow.objects.all()
    choice = ChoiceNow.objects.all()
    return render(request,'community/korea.html',{'question':question, 'choice':choice})

def votenow(request):
    choice = ChoiceNow.objects.all()
    try:
        selected_choice = choice.get(pk=request.POST['choice'])
    except(KeyError, ChoiceNow.DoesNotExist):
        return render(request,'community/korea.html',{'question':choice, 'error_message':"선택된 것이 없습니다."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('community:resultsnow',args=()))

def resultsnow(request):
    question = QuestionNow.objects.all()
    choice = ChoiceNow.objects.all()
    return render(request, 'community/korea_results.html', {'question': question,'choice':choice})

#######################

def indexbest(request):
    latest_question_list = QuestionBest.objects.all()
    context = {'latest_question_list': latest_question_list}

    return render(request,'community/korea_best_player.html',context)

def detailbest(request, question_id):
    question = get_object_or_404(QuestionBest, pk=question_id)
    return render(request,'community/korea_best_player_detail.html',{'question':question})

def votebest(request,question_id):
    question = get_object_or_404(QuestionBest, pk=question_id)
    try:
        selected_choice = question.choicebest_set.get(pk=request.POST['choice'])
    except(KeyError, ChoiceBest.DoesNotExist):
        return render(request,'community/korea_best_player_detail.html',{'question':question, 'error_message':"선택된 것이 없습니다."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('community:resultsbest', args=(question_id,)))

def resultsbest(request, question_id):
    question = get_object_or_404(QuestionBest, pk=question_id)
    return render(request, 'community/korea_best_player_results.html', {'question': question})

######################################################

def mebership(request):
    if request.method == 'GET':
        return render(request, 'community/Membership_Form.html')

    elif request.method == "POST":
        h_username = request.POST.get('username', None)
        h_userid = request.POST.get('userid', None)
        h_password = request.POST.get('password', None)
        h_re_password = request.POST.get('re_password', None)
        res_data = {}

        if not (h_username and h_userid and h_password and h_re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'community/Membership_Form.html', res_data)
        if h_password != h_re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'community/Membership_Form.html', res_data)
        else:
            res_data['error'] = '회원가입이 완료되었습니다.'
            user = User(username = h_username, userid = h_userid , password = make_password(h_password))
            user.save()
        return render(request , 'community/Membership_Form.html', res_data)

##########################################################


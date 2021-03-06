from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from teams.models import Team, Comment
from teams.models import Recruit
from django.contrib.auth.decorators import login_required


#############################팀소개 게시판##########################################
def regTeam(request):
    return render(request, 'teams/board_create.html')


def regConTeam(request):
    name = request.POST['name']
    major = request.POST['major']
    memo = request.POST['memo']
    captain = request.POST['captain']
    memCount = request.POST['memCount']

    qs = Team(t_name=name, t_major=major, t_memo=memo, t_captain=captain, t_memCount=memCount)
    qs.save()

    return HttpResponseRedirect(reverse('teams:teamAll'))


@login_required(login_url='user:login')
def reaTeamAll(request):
    qs = Team.objects.all()  # 팀 정보 가져오기
    context = {'team_list': qs}
    return render(request, 'teams/board_main_ver2.html', context)


def detTeam(request, id):
    qs = Team.objects.get(id=id)
    context = {'team_info': qs}
    return render(request, 'teams/board_detail.html', context)


def reaTeamOne(request, id):
    qs = Team.objects.get(id=id)
    context = {'team_info': qs}
    return render(request, 'teams/board_update.html', context)


def modConTeam(request):
    name = request.POST['name']
    major = request.POST['major']
    memo = request.POST['memo']
    captain = request.POST['captain']
    memCount = request.POST['memCount']
    id = request.POST['id']

    t_qs = Team.objects.get(id=id)  # Query String

    t_qs.t_name = name
    t_qs.t_major = major
    t_qs.t_memo = memo
    t_qs.t_captain = captain
    t_qs.t_memCount = memCount

    t_qs.save()

    # templates로 이동
    return HttpResponseRedirect(reverse('teams:teamAll'))


def delConTeam(request, id):
    qs = Team.objects.get(id=id)
    qs.delete()

    return HttpResponseRedirect(reverse('teams:teamAll'))


#############################인원모집게시판##########################################
def recruitAll(request):
    qs = Recruit.objects.all()  # 팀 정보 가져오기
    context = {'recruit_list': qs}
    return render(request, 'teams/board2_main.html', context)


def recruitNew(request):
    return render(request, 'teams/board2_create.html')


def recruitCon(request):
    title = request.POST['title']
    memo = request.POST['memo']
    writer = request.POST['writer']

    qs = Recruit(r_title=title, r_memo=memo, r_writer=writer)
    qs.save()

    return HttpResponseRedirect(reverse('teams:recruitAll'))


def recruitDet(request, id):
    if request.method == 'POST':

        comment = request.POST['comment']
        writer = request.POST['writer']
        recid = request.POST['recid']
        qs = Recruit.objects.get(id=id)

        save = Comment(c_comment=comment, c_writer=writer, c_recid=recid)
        save.save()

        sq = Comment.objects.all()
        context = {
            'recruit_info': qs,
            'comment_info': sq,
        }

        return render(request, 'teams/board2_detail.html', context)
    elif request.method == 'GET':
        qs = Recruit.objects.get(id=id)
        sq = Comment.objects.all()

        context = {
            'recruit_info': qs,
            'comment_info': sq,
        }

        return render(request, 'teams/board2_detail.html', context)


def recruitOne(request, id):
    qs = Recruit.objects.get(id=id)
    context = {'recruit_info': qs}
    return render(request, 'teams/board2_update.html', context)


def modRecruit(request):
    title = request.POST['title']
    memo = request.POST['memo']
    writer = request.POST['writer']
    id = request.POST['id']

    r_qs = Recruit.objects.get(id=id)  # Query String

    r_qs.r_title = title
    r_qs.r_memo = memo
    r_qs.r_writer = writer

    r_qs.save()

    # templates로 이동
    return HttpResponseRedirect(reverse('teams:recruitAll'))


def delConRecruit(request, id):
    qs = Recruit.objects.get(id=id)
    qs.delete()

    return HttpResponseRedirect(reverse('teams:recruitAll'))

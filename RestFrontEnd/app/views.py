from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
import requests, json
from django.contrib.auth.decorators import login_required

# Create your views here.
def boards_list(request):
    backend_url = 'http://127.0.0.1:8000/'
    headers = {'content-type':'application/json'}
    response = requests.get(backend_url,headers=headers)
    boards = response.json()
    return render(request,'home.html',{'boards':boards})

def board_topics(request,board_id):
    backend_url = 'http://127.0.0.1:8000/boards/'+str(board_id)+'/'
    headers = {'content-type':'application/json'}
    response = requests.get(backend_url,headers=headers)
    response_data = response.json()
    
    response_board = requests.get('http://127.0.0.1:8000/board_details/'\
                                  +str(board_id)+'/',headers=headers)
    board_details = response_board.json()
    return render(request,'topics.html',{'board':board_details,
                                         'topics':response_data})

def new_topic(request,board_id):
    headers = {'content-type':'application/json'}
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['messae']
        created_by = request.user
        data = json.dump(data={"subject":subject,"message":message,
                               "created_by":created_by,"board":board_id})
        response_board = requests.post('http://127.0.0.1:8000/boards/'+\
                                    str(board_id)+'/',headers=headers,data=data)
        add_topic_res = response_board.json()
        return redirect('board_topics',board_id=board_id)
    response_board = requests.get('http://127.0.0.1:8000/board_details/'\
                                  +str(board_id)+'/',headers=headers)
    board_details = response_board.json()
    return render(request,'new_topic.html',{'board':board_details})
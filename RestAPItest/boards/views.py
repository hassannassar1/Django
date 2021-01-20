from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status 
from rest_framework.response import Response
from .models import Board, Topic
from .serializers import BoardSerializer, TopicSerializer, PostSerializer


# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    
'''
class BoardsList(generics.ListCreateAPIView ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardDetails(generics.RetrieveUpdateDestroyAPIView ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer 
    lookup_field = 'id'
    '''
'''
class BoardsList(APIView ):
    def get(self,request):
        boards = Board.objects.all()
        data = BoardSerializer(boards,many=True).data
        return Response(data)
    def post(self,request):
        serializer = BoardSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BoardDetails(APIView ):
    def get(self,request,board_id):
        board = get_object_or_404(Board,pk=board_id)
        data = BoardSerializer(board).data
        return Response(data)

'''
class BoardTopics(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
'''    
class BoardTopics(APIView ):
    def get(self,request,board_id):
        board = get_object_or_404(Board,pk=board_id)
        topics = board.topics.order_by('-created_dt').annotate(comments =\
                                                       Count('posts'))
        data = TopicSerializer(topics,many=True).data
        return Response(data)
    def post(self,request,board_id):
        serializer = TopicSerializer(data= request.data)
        topic_details = request.data
        if serializer.is_valid():
            topic = serializer.save()
            post_serializer = PostSerializer(data = {
                                'message':topic_details['message'],
                                'topic':topic.pk,
                                'created_by':topic.created_by,
                                'created_dt':topic.created_dt,
                                'updated_by':topic.updated_by,
                                'updated_dt':topic.updated_dt,
                                
                                                    })
            if post_serializer.is_valid():
                topic = post_serializer.save()
                return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
 ''' 

'''
@login_required
def new_topic(request,board_id):
    board = get_object_or_404(Board,pk=board_id)
    if request.method == "POST":
        form =NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by = request.user,
                topic=topic

            )
            return redirect('board_topics',board_id=board.pk)
    else:
        form = NewTopicForm()

    return render(request,'new_topic.html',{'board':board,'form':form})
def boards_list(request):
    
    data = {'results':list(boards.values('pk','name','description'))}
    return JsonResponse(data)

def board_topics(request,board_id):

    board = get_object_or_404(Board,pk=board_id)
    #topics = board.topics.objects.all()
    topics = board.topics.order_by('-created_dt').annotate(comments = Count('posts'))
    data = {'results':{
            'name':board.name,
            'description':board.description,
            },
            'topics':list(topics.values('pk','subject','board','created_by','created_dt'))
    }
    
    return JsonResponse(data)
'''
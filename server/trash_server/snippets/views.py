from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet,MapField,AllNode,Client_Queue
from snippets.serializers import SnippetSerializer,InitSerializer




@csrf_exempt
def snippet_init(request):#初期化
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        all_node = AllNode.objects.all()
        #print(request.GET.get("node"))
        serializer = InitSerializer(all_node, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) #data変数にデータを入れる
        serializer = InitSerializer(data=data)#データベースに格納するオブジェクトを作成する
        if serializer.is_valid():
            serializer.save()
            """
            #MAPデータに格納
            mapfield = MapField(client= "C1_test",x = 0,y = 0)
            mapfield.save()
            """
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_list(request):#全データ

    if request.method == 'GET':
        #snippets = Snippet.objects.all()
        allnode = list(AllNode.objects.values_list('name',flat='True').distinct())
        init_node = list(Snippet.objects.values_list('client',flat='True').distinct())
        
        if ((set(allnode)) == (set(init_node))):
            #Queu追加
            client_queue= Client_Queue.object.create(client = request.GET.get("client"))
            qlient_queue.save()
            
            #Queueデータベース参照
            queue = list(Client_Queue.objects.values_list('client',flat='True').distinct())

            #アルゴリズム処理

            #アルゴリズムの結果をMapFieldに代入

            #All_Nodeのclient = request.GET.get("client")を更新
            
            if (set(allnode)) == (set(queue)):
                """
                データベース削除
                Client_Queue
                snippet
                """

            return  JsonResponse({"x":1})#進行命令
        
        #serializer = SnippetSerializer(snippets, many=True)
        #print(serializer.data)
        return JsonResponse({"error": "-1"})#JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #data変数にデータを入れる
        serializer = SnippetSerializer(data=data)#データベースに格納するオブジェクトを作成する
        if serializer.is_valid():
            serializer.save()
            """
            #MAPデータに格納
            mapfield = MapField(client= "C1_test",x = 0,y = 0)
            mapfield.save()
            """
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


"""
@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)#ここで処理を入れればよい

    elif request.method == 'PUT':#UPDATE
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    #elif UPDATE
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
"""

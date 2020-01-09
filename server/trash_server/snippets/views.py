from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet,MapField,AllNode,Client_Queue,Culc_bit
from snippets.serializers import SnippetSerializer,InitSerializer
from snippets.algorism import garbage,calc_position




@csrf_exempt
def snippet_init(request):#初期化
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        all_node = AllNode.objects.all()
        serializer = InitSerializer(all_node, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)                  #data変数にデータを入れる
        serializer = InitSerializer(data=data)              #データベースに格納するオブジェクトを作成する       //IniSerializerはAllNodeへ
        if serializer.is_valid():                           #バリデーションチェック
            serializer.save()                               #DB保存
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
        allnode = list(AllNode.objects.values_list('client',flat='True').distinct())           #allnodeの名前一覧
        data_node = list(Snippet.objects.values_list('name',flat='True').distinct())           #data_nodeの名前一覧

        #Queueデータベース参照
        queue = list(Client_Queue.objects.values_list('client',flat='True').distinct())        #queueに入っているデータを参照
        get_node =  request.GET.get("client")#アクセスしてきたクライエントの名前
        
        """
        test = garbage("test",0,0)
        print(test.name)
        obj_list = []
        for i in allnode:
            AllNode.objects.values_list('client',flat='True')
        """
        culc_bit = Culc_bit.objects.get(id = 1)
        if ((set(allnode)) == (set(data_node))):#全clientがデータPOST済みなら
            if get_node in queue:#既に移動先を送信済みなら
                return JsonResponse({"error": "-1"})#待機命令
            else:
                if(culc_bit.client == 1):
                    temp = AllNode.objects.get(client = get_node)
                    x = temp.x
                    y = temp.y
                    return JsonResponse({"x":x,"y":y})
                #まだGETをもらっていなかったら送信済みQueuデータベースに追加
                client_queue = Client_Queue.objects.create(client = get_node)
                client_queue.save()
                testlist = []
            #アルゴリズム処理
                #instance生成
                for i in allnode:
                    x = AllNode.objects.filter(client=i).values_list('x',flat='True')
                    y = AllNode.objects.filter(client = i).values_list('y',flat='True')
                    weight = Snippet.objects.filter(name = i).values_list('people',flat='True').latest("created")
                    tmp_obj = garbage(i,x,y)#名前,x,y
                    tmp_obj.amount = weight
                    testlist.append(tmp_obj)
                calced_pos = calc_position(testlist)#名前,x,y 引数objで未実装calc_position calc_position = [[名前,x,y],[名前,x,y]]二次元リスト
                #AllNodeで位置情報設定
                for i in calced_pos:#[[名前,x,y],[名前,x,y]]二次元リスト
                    temp = AllNode.objects.get(client = i[0])
                    temp.x = str(i[1])
                    temp.y = str(i[2])
                    temp.save()
                temp = Culc_bit.objects.get(id = 1)
                temp.client = 1    
            if(set(allnode)) == (set(queue)):
                Client_Queue.objects.all().delete()
                Snippet.objects.all().delete()
                temp1 = Culc_bit.objects.get(id = 1)
                temp1.client = 0
                temp1.save()
            temp = AllNode.objects.get(client = get_node)
            x = temp.x
            y = temp.y
            return JsonResponse({"x":x,"y":y})
        #serializer = SnippetSerializer(snippets, many=True)
        #print(serializer.data)
        return JsonResponse({"error": "-2"})#JsonResponse(serializer.data, safe=False)#まだそろってない

    elif request.method == 'POST':
        data = JSONParser().parse(request) #data変数にデータを入れる
        serializer = SnippetSerializer(data=data)#データベースに格納するオブジェクトを作成する
        if serializer.is_valid():
            serializer.save()#データベースセーブ
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

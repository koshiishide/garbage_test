import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

from collections import OrderedDict#順序付きdict



# AxesとFigureを設定

fig, ax = plt.subplots(figsize = (5, 5))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("x", fontsize = 15)
ax.set_ylabel("y", fontsize = 15)
ax.grid()

#step_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
#######################グラフ描画設定###############################

#サーバ側

class garbage:
    def __init__(self,name,x,y,obj):
        self.name       = name
        self.x          = x
        self.y          = y
        self.amount     = 0
        self.maximam    = 20
        self.amount_log = OrderedDict()#ゴミ時系列データ
        self.amount_log[0] =0

        self.instance   = obj
        self.flag_clean = 0#ゴミ回収中フラグ
        self.flag_busy  = 0
        
    def change_amount(self,amount,t):#増加量
        
        if(((self.amount+amount)>0) & (self.amount < self.maximam)):
            self.amount_log[t]=amount
            #print(self.amount_log)#デバッグ
            self.amount = self.amount + amount
            self.check_busy()  
        else:
            self.clean()
            print("clean　処理")
    def clean(self):#ゴミ箱がいっぱいの時
        self.amount = 0
        self.amount_log= OrderedDict()

    def change_course(self,delta_xy):
        pass
    
    def check_busy(self):
        dict_count = len(self.amount_log)
        d_amount = list(self.amount_log.items())
        b1 = d_amount[dict_count-1][0]
        b2 = d_amount[dict_count-1][1]

        a1 = d_amount[dict_count-2][0]
        a2 = d_amount[dict_count-2][1]

        

        if( ((b2-a2) / ((b1-a1)/10)) >= 1.5 ):
            print("busy on")
            self.flag_busy = 1


def calc_deltapos(a_x,a_y,b_x,b_y):
    if (a_x>b_x):
        if(a_y>b_y):
            return ((b_x - a_x),(b_y - a_y))
        else:
            return ((b_x - a_x),(-(a_y)+ b_y))
    else:
        if(a_y>b_y):
            return ((b_x - a_x),(a_y- b_y))
        else:
            return ((b_x - a_x),(b_y - a_y))
        
        





dot, = ax.plot([0], [0], 'bo')
dot2, = ax.plot([1],[1],'ko')
dot3, = ax.plot([-1],[-1],'o')



#初期位置静的設定
test_data =  garbage("ゴミ箱A",0,0,dot)
test_data2 = garbage("ゴミ箱B",1,1,dot2)
test_data3 = garbage("ゴミ箱C",-1,-1,dot3)

obj_list = []
obj_list.append(test_data)
obj_list.append(test_data2)
obj_list.append(test_data3)


obj_count = len(obj_list)


#時系列

def dot_circle(t):
    if ((t%10==0) & (t>0)):
        test_data.change_amount(random.randint(1,3),t)#(ゴミ箱側)
        #print(test_data.amount)
    #step_text.set_text('step = {0}'.format(t))

    #増加フラグbitのチェック(サーバサイド)
    
    for i in range(0,obj_count):
        tmp_obj=obj_list[i]
        if(tmp_obj.flag_busy):
            vec = np.arange(obj_count)
            ind = np.ones(obj_count,dtype=bool)
            ind[i] = False

            target_x = tmp_obj.x
            target_y = tmp_obj.y

            for i in vec[ind]:
                """
                dist_x =  ((obj_list[i].x - target_x) **2 ) ** (-2)                dist_y = ((obj_list[i].y - target_y)** (-2))
                """
                #obj_list[i].instance.set_data(calc_deltapos(obj_list[i].x,obj_list[i].y,target_x,target_y))
                tmp_xy=calc_deltapos(obj_list[i].x,obj_list[i].y,target_x,target_y)
                print(tmp_xy)
                obj_list[i].x =obj_list[i].x + tmp_xy[0]
                obj_list[i].y =obj_list[i].x + tmp_xy[1]
                
            tmp_obj.flag_busy = 0
            print(tmp_obj.name,"busy flag off")

    print(obj_list[0].name,"位置xy",obj_list[0].x,obj_list[0].y,"\n",
          obj_list[1].name,"位置xy",obj_list[1].x,obj_list[1].y,"\n",
          obj_list[2].name,"位置xy",obj_list[2].x,obj_list[2].y,"\n"
          )
    
    
    """
    移動例
    xt = 1
    yt = 1+t
    dot2.set_data(xt, yt)
    """
    return dot,



#####################animation#######################################

ani = animation.FuncAnimation(
      fig,  # Figureオブジェクト
      dot_circle,  # グラフ描画関数
      frames = np.arange(0, 300, 1),  # フレームを設定
      interval = 100,  # 更新間隔(ms)
      repeat = True,  # 描画を繰り返す
      blit = True  # blitting による処理の高速化
      )

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

from collections import OrderedDict#順序付きdict

class garbage:
    def __init__(self,name,x,y):
        self.name       = name
        self.x          = x
        self.y          = y
        self.amount     = 0
        self.maximam    = 20
        self.amount_log = OrderedDict()#ゴミ時系列データ
        self.amount_log[0] =0
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


def calc_deltapos(a_x,a_y,b_x,b_y):#距離の絶対値
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


def calc_position(obj_list):
    list = []
    for i in obj_list:
        list.append([i.name,i.x,i.y])
    return list

# coding: utf-8

import random

who = ['お母さん','彼女','親友','お隣さん','一番仲良い異性','バイトの先輩','バイトの後輩']
where = ['近所の川','公園','リビング','トイレ','ベット','ベランダ']
what = ['電話する','恋話する','滑らない話をする','黒歴史を話す','ヘリウムガス吸って一言で笑いをとる']

print('コロナ渦の年末年始どうやって過ごす？')

def who_is():
    print('誰と？: \t' + random.choice(who) + 'と')

def where_is():
    print('どこで？: \t' + random.choice(where) + 'で')

def what_do():
    print('何する？: \t' + random.choice(what) + '。')

who_is()
where_is()
what_do()

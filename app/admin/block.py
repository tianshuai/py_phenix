from flask import render_template
from .base import admin
from ..models import Block
#from bson import ObjectId

@admin.route('/block/list')
def block_list():
    return render_template('block/list.html')

@admin.route('/block/save')
def block_save():
    #block = Block(mark='ff', name='eee')
    #block = Block.objects(mark='mmm')
    #block.name = 'shuai'

    # 重新选择表
    #block.switch_collection('old_users')
    #block.save()


    #update
    block = Block._get_collection()
    #block.update_one({'_id':ObjectId('56dc39b1a78446616a0a1da8')}, {"$set":{'name':'lll'}})
    #block.update({'mark': 'zzz'}, {"$set":{'name':'ff'}})

    # 查询更新(自增ID)
    a = block.find_one_and_update({'mark':'zzz'}, {'$inc':{'count':1}}, upsert=True)
    #block.save()

    return str(a['count'])



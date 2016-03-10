from flask import render_template
from .base import admin
from ..models import Category
from bson import ObjectId

@admin.route('/category/list')
def category_list():
    return render_template('category/list.html')

@admin.route('/category/save')
def category_save():
    category = Category(mark='ffa', name='eeef')
    #category = Category.objects(mark='mmm')
    #category.name = 'shuai'

    # 重新选择表
    #category.switch_collection('old_users')

    #update
    #category = Category._get_collection()
    #category.update_one({'_id':ObjectId('56dc39b1a78446616a0a1da8')}, {"$set":{'name':'lll'}})
    #category.update({'mark': 'zzz'}, {"$set":{'name':'ff'}})

    # 查询更新(自增ID)
    #a = category.find_one_and_update({'mark':'ff'}, {'$inc':{'count':1}})

    category.save()

    return category.name



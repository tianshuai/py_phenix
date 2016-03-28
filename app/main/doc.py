from flask import render_template, jsonify, url_for, request, redirect, flash, g
from .base import main 
from ..models import Category, Catalog, Doc, User
from ..helpers import force_int, require_staff, require_admin
# markdown 格式转换
import mistune


# 项目首页
@main.route('/doc')
def doc():
    app_users = User.objects(role_id=2)
    server_users = User.objects(role_id=5)
    return render_template('doc/index.html', app_users=app_users, server_users=server_users)


# 项目列表
@main.route('/doc/item_list')
@require_staff
def doc_item_list():
    categories = Category.objects(domain=1)

    return render_template('doc/item_list.html', categories=categories)


# 添加项目
@main.route('/doc/item_add')
@require_admin
def doc_item_add():
    return render_template('doc/item_add.html')


# 保存项目
@main.route('/doc/item_save', methods=['POST'])
@require_admin
def doc_item_save():

    #if 'add' in request.form:
    #if 'Like' in request.form.values():
    name = request.form['name']
    domain = force_int(request.form['domain'], 0)
    user_id = g.user._id

    if name=='' or domain==0:
        return jsonify(success=False, message='缺少请求参数!')
    try:
        category = Category(name=name, domain=domain, user_id=user_id)
        category.save()
        return jsonify(success=True, message='success!', redirect_to=url_for('main.doc_item_list'))
    except:
        return jsonify(success=False, message='创建失败!')


# 文档目录
@main.route('/doc/show/<int:category_id>')
def doc_show(category_id):
    category = Category.objects(_id=category_id).first()

    p_docs = Doc.objects(item_id=category_id, cat_id=0)
    catalogs = Catalog.objects(item_id=category_id)
    if catalogs:
        for d in catalogs:
            c_docs = Doc.objects(cat_id=d._id)
            d.docs = c_docs
    return render_template('doc/show.html', category=category, p_docs=p_docs, catalogs=catalogs)


# 目录新建/编辑
@main.route('/doc/catalog/submit/<int:category_id>/<int:catalog_id>')
@require_admin
def doc_catalog_submit(category_id, catalog_id):

    if category_id==0:
        flash('项目ID不存在!', 'error')
        return redirect(url_for('main.doc'))
 
    if catalog_id==0:
        mode = 'create'
        catalog = None
    else:
        mode = 'edit'
        catalog = Catalog.objects(_id=catalog_id).first()

    return render_template('doc/catalog_submit.html', category_id=category_id, catalog=catalog, mode=mode)


# 保存目录
@main.route('/doc/catalog_save', methods=['POST'])
@require_admin
def doc_catalog_save():
    #if 'add' in request.form:
    #if 'Like' in request.form.values():
    id = force_int(request.form['id'], 0)
    name = request.form['name']
    sort = force_int(request.form['sort'], 0)
    item_id = force_int(request.form['item_id'], 0)

    if name=='':
        return jsonify(success=False, message='缺少请求参数!')
    try:
        if id==0:
            user_id = g.user._id
            catalog = Catalog(name=name, item_id=item_id, user_id=user_id, sort=sort)
            catalog.save()
        else:
            catalog = Catalog._get_collection()
            catalog.update_one({'_id':id}, {"$set":{'name':name, 'sort':sort, 'item_id':item_id}})

        return jsonify(success=True, message='success!', redirect_to=url_for('main.doc_item_list'))
    except:
        return jsonify(success=False, message='创建失败!')


# 项目列表
@main.route('/doc/catalog/list/<int:item_id>')
@require_staff
def doc_catalog_list_ajax(item_id):
    catalogs = Catalog.objects(item_id=item_id)

    return jsonify(success=True, data=catalogs)

# 删除目录
@main.route('/doc/catalog/del', methods=['POST'])
@require_admin
def doc_catalog_del():
    id = force_int(request.form['id'], 0)

    try:
        catalog = Catalog._get_collection()
        catalog = catalog.find_one_and_delete({'_id':id})
        return jsonify(success=True, data=catalog)
    except:
        return jsonify(success=False, message='删除失败!')

# 新建/编辑文档
@main.route('/doc/submit/<int:item_id>/<int:doc_id>')
@require_admin
def doc_submit(item_id, doc_id):

    if item_id==0:
        flash('项目ID不存在!', 'error')
        return redirect(url_for('main.doc'))
 
    if doc_id==0:
        mode = 'create'
        doc = None
    else:
        mode = 'edit'
        doc = Doc.objects(_id=doc_id).first()

    #catalogs = Catalog.objects(item_id=item_id)

    return render_template('doc/doc_submit.html', mode=mode, doc=doc, item_id=item_id, doc_id=doc_id)


# 保存文档
@main.route('/doc/save', methods=['POST'])
@require_admin
def doc_save():
    #if 'add' in request.form:
    #if 'Like' in request.form.values():
    id = force_int(request.form['id'], 0)
    title = request.form['title']
    content = request.form['content']
    sort = force_int(request.form['sort'], 0)
    item_id = force_int(request.form['item_id'], 0)
    cat_id = force_int(request.form['cat_id'], 0)

    if title=='':
        return jsonify(success=False, message='缺少请求参数!')
    try:
        if id==0:
            user_id = g.user._id
            doc = Doc(title=title, content=content, item_id=item_id, cat_id=cat_id, user_id=user_id, sort=sort)
            doc.save()
        else:
            doc = Doc._get_collection()
            doc.update_one({'_id':id}, {"$set":{'title':title, 'content':content, 'cat_id':cat_id, 'sort':sort, 'item_id':item_id}})

        return jsonify(success=True, message='success!', redirect_to=url_for('main.doc_show', category_id=item_id))
    except:
        return jsonify(success=False, message='创建失败!')


# 文档详情
@main.route('/doc/sub_show/<int:doc_id>')
@require_staff
def doc_sub_show(doc_id):
    doc = Doc.objects(_id=doc_id).first()
    # markdown 格式转换html
    markdown = mistune.Markdown()
    content = markdown(doc.content)
    return render_template('doc/sub_show.html', content=content)


# 删除文档
@main.route('/doc/delete/<int:id>', methods=['POST','GET'])
@require_admin
def doc_delete(id):
    try:
        doc = Doc._get_collection()
        doc = doc.find_one_and_delete({'_id':id})
        flash('删除成功!', 'success')
    except:
        flash('删除失败!', 'error')
        return redirect(url_for('main.doc'))

    return redirect(url_for('main.doc_show', category_id=doc['item_id']))

{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":39,"position":39,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":98,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","","app.config[\"MONGO_DBNAME\"] = 'mjGoodFood'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_recipes')","def get_recipes():","    return render_template('recipes.html',","    recipes=mongo.db.recipes.find())","    ","    ","@app.route('/add_recipe')","def add_recipe():","    return render_template('addrecipes.html',","    categories=mongo.db.categories.find())","    ","    ","@app.route('/insert_recipe', methods=['POST'])","def insert_recipe():","    recipes = mongo.db.recipes","    recipes.insert_one(request.form.to_dict())","    return redirect(url_for('get_recipes'))","    ","    ","@app.route('/edit_recipe/<recipe_id>')","def edit_recipe(recipe_id):","    the_recipe = mongo.db.recipes.find_one({\"_id\": ObjectId(recipe_id)})","    all_categories = mongo.db.categories.find()","    return render_template('editrecipe.html', recipe=the_recipe, catergories=all_categories)","    ","    ","@app.route('/update_recipe/<recipe_id>', methods=[\"POST\"])","def update_recipe(recipe_id):","    recipes = mongo.db.recipes","    recipes.update( {'_id': ObjectId(recipe_id)},","    {","        'recipe_name':request.form.get('recipe.name'),","        'category_name':request.form.get('category_name'),","        'recipe_description':request.form.get('recipe_description'),","        'recipe_ingredients':request.form.get('recipe_ingredients'),","        'recipe_method':request.form.get('recipe_method')","    })","    return redirect(url_for('get_recipes'))","","    ","@app.route('/delete.recipe/<recipe_id>')","def delete_recipe(recipe_id):","    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})","    return redirect(url_for('get_recipes'))","    ","","@app.route('/get_categories')","def get_categories():","    return render_template('categories.html',","    categories=mongo.db.categories.find())","    ","    ","@app.route('/delete_category/<category_id>')","def delete_category(category_id):","    mongo.db.categories.remove({'_id': ObjectId(category_id)})","    return redirect(url_for('get_categories'))","    ","    ","@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))","    ","    ","@app.route('/update_category/<category_id>', methods=[\"POST\"])","def update_category(category_id):","    mongo.db.categories.update({'_id': ObjectId(category_id)},","    {'category_name': request.form.get['category_name']})","    return redirect(url_for('get_categories'))","    ","    ","@app.route('/insert_category', methods=[\"POST\"])","def insert_category():","    categories = mongo.db.categories","    category_doc = {'category_name': request.form.get('category_name')}","    mongo.db.categories.insert_one(category_doc)","    return redirect(url_for('get_categories'))","    ","    ","@app.route('/add_category')","def add_category():","    return render_template('addcategory.html')","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":3}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["v"],"id":4},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["n"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["e"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["t"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["e"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"remove","lines":["g"]}],[{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["e"],"id":5},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["v"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["i"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":29},"end":{"row":8,"column":34},"action":"remove","lines":["envir"],"id":6},{"start":{"row":8,"column":29},"end":{"row":8,"column":36},"action":"insert","lines":["environ"]}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["."],"id":7},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["g"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["e"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":76},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"remove","lines":["'"],"id":10}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["\""],"id":11}],[{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"remove","lines":["'"],"id":12}],[{"start":{"row":16,"column":27},"end":{"row":16,"column":28},"action":"insert","lines":["\""],"id":13}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["s"],"id":14}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["s"],"id":15}],[{"start":{"row":17,"column":11},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":17},{"start":{"row":17,"column":11},"end":{"row":18,"column":0},"action":"remove","lines":["",""]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"remove","lines":["s"]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["s"],"id":18}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":36},"action":"remove","lines":["recipes=mongo.db.recipes.find())"],"id":19}],[{"start":{"row":15,"column":18},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":36},"action":"insert","lines":["recipes=mongo.db.recipes.find())"],"id":21}],[{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["r"],"id":22},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["e"]},{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"insert","lines":["c"]},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"insert","lines":["i"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["p"]},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"insert","lines":["e"]},{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["+"],"id":23}],[{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"remove","lines":["+"],"id":24}],[{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["="],"id":25},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["r"]},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"insert","lines":["e"]},{"start":{"row":17,"column":52},"end":{"row":17,"column":53},"action":"insert","lines":["c"]},{"start":{"row":17,"column":53},"end":{"row":17,"column":54},"action":"insert","lines":["i"]}],[{"start":{"row":17,"column":54},"end":{"row":17,"column":55},"action":"insert","lines":["p"],"id":26},{"start":{"row":17,"column":55},"end":{"row":17,"column":56},"action":"insert","lines":["e"]},{"start":{"row":17,"column":56},"end":{"row":17,"column":57},"action":"insert","lines":["s"]},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"insert","lines":[")"]}],[{"start":{"row":17,"column":58},"end":{"row":17,"column":60},"action":"insert","lines":["\"\""],"id":27}],[{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"remove","lines":["\""],"id":28}],[{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"remove","lines":["\""],"id":29}],[{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"insert","lines":["\""],"id":30}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"remove","lines":[")"],"id":31}],[{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["("],"id":32}],[{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"remove","lines":["("],"id":33}],[{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":[" "],"id":34},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["\""]}],[{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"remove","lines":["\""],"id":35}],[{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"remove","lines":["\""],"id":36}],[{"start":{"row":15,"column":18},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["r"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["t"],"id":38},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["u"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["r"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":["n"],"id":39},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":["r"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["u"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["t"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"remove","lines":["e"]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":40},{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":120,"scrollleft":0,"selection":{"start":{"row":23,"column":45},"end":{"row":23,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1578755644857,"hash":"6bf550ca44ab5feeba6fd6dd7a076a1270d6f753"}
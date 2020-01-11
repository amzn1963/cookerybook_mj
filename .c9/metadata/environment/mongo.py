{"filter":false,"title":"mongo.py","tooltip":"/mongo.py","undoManager":{"mark":28,"position":28,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":14},"action":"insert","lines":["import pymongo","import os","","MONGODB_URI = os.getenv(\"MONGO_URI\")","DBS_NAME = \"mjMilestoneDB\"","COLLECTION_NAME = \"mjGoodFood\"","","def mongo_connect(url):","    try:","        conn = pymongo.MongoClient(url)","        print(\"Mongo is connected!\")","        return conn","        ","    except pymongo.errors.ConnectionFailure as e:","        print(\"Could not connect to MongoDB: %s\") % e","        ","conn = mongo_connect(MONGODB_URI)","","coll = conn[DBS_NAME][COLLECTION_NAME]","","documents = coll.find()","","for doc in documents:","    print(doc)"],"id":1}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["B"],"id":2},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["D"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["e"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["n"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["o"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"remove","lines":["t"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"remove","lines":["s"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"remove","lines":["e"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"remove","lines":["l"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"remove","lines":["i"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"remove","lines":["M"]}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["G"],"id":3},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["o"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["o"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":18},"action":"remove","lines":["mjGood"],"id":4},{"start":{"row":4,"column":12},"end":{"row":4,"column":22},"action":"insert","lines":["mjGoodFood"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["d"],"id":5},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["o"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["o"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["F"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["d"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["o"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["o"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["G"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["j"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["m"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["c"],"id":6},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["a"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["t"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["e"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["g"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":24},"action":"remove","lines":["categ"],"id":7},{"start":{"row":5,"column":19},"end":{"row":5,"column":29},"action":"insert","lines":["categories"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":29},"action":"remove","lines":["categories"],"id":8},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["m"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["j"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":21},"action":"remove","lines":["mj"],"id":9},{"start":{"row":5,"column":19},"end":{"row":5,"column":29},"action":"insert","lines":["mjGoodFood"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["d"],"id":10},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["o"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["o"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["F"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["d"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["o"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["o"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["G"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["j"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["m"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["c"],"id":11},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["a"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["t"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["e"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["g"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["o"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["r"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["i"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["s"],"id":12}],[{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":[","],"id":13}],[{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":34},"action":"insert","lines":["\"\""],"id":15}],[{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["r"],"id":16},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["e"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["c"]}],[{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["i"],"id":17},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["p"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["e"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["S"],"id":18}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["S"],"id":19}],[{"start":{"row":5,"column":31},"end":{"row":5,"column":42},"action":"remove","lines":[", \"recipes\""],"id":20}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["S"],"id":21}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"remove","lines":["S"],"id":22}],[{"start":{"row":5,"column":30},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":23}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["C"],"id":24},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["O"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["L"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["L"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["E"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":5},"action":"remove","lines":["COLLE"],"id":25},{"start":{"row":6,"column":0},"end":{"row":6,"column":15},"action":"insert","lines":["COLLECTION_NAME"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":[" "],"id":26},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":20},"action":"insert","lines":["\"\""],"id":28}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["r"],"id":29},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["e"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["c"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["i"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["p"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["e"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":27},"end":{"row":6,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1578728019493,"hash":"e01283289eb5727772600365385282c4a7b23ccd"}
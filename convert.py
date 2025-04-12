import os,json
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
dic={}
for c in get_immediate_subdirectories("."):
	dic[c]=os.listdir(c)
with open('data.json', 'w',encoding="utf-8") as f:
    json.dump(dic,f)
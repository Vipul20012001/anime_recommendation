from  flask import Flask,render_template,request
import pandas as pd
file_path = "static\Action Explosive battles and dynami.txt"
usco=["ID","NAME"]
ft=pd.read_csv("static\Anime.csv")
sum_of_anime=pd.read_csv("static\Anime_with_synopsis.csv")
deta_ID=list(sum_of_anime["MAL_ID"])
deta_Name=list(sum_of_anime["Name"])
deta_genr=list(sum_of_anime["Genres"])
deta_summ=list(sum_of_anime["sypnopsis"])
lensum=len(deta_ID)
print(lensum)
print(deta_summ)
ft1=ft["ID"]
ft2=ft["NAME"]
lenft=len(ft1)
htp=[]
for i in range(lenft):
    htp.append([ft1[i],ft2[i]])
def htm(name):
    p=len(name)
    ans=[]
    l1=name.capitalize()
    for i in htp:
        y=i[1].capitalize()
        if l1==y[:p]:
            ans.append(i)
    return ans
with open(file_path, 'r', encoding='utf-8') as file:
    file_data = file.read()
jt=str(file_data).split(";")
fr=dict()
for i in jt:
    p=i.replace("\n","")
    l=p.split(":")
    if len(l)>1:
        fr[l[0]]=l[1]
ft=[]
for i in fr.keys():
    ft.append([i,fr[i]])
fl=[]
i=0
while i<len(ft):
    j=0
    l=[]
    while j<3:
        l.append(ft[i])
        j+=1
        i+=1
    fl.append(l)
def get_name(i):
    for j in htp:
        if j[0]==i:
            return j[1]
def get_summ(i):
    for p in range(lensum):
        if deta_ID[p]==i:
            return [deta_Name[p],deta_genr[p],deta_summ[p]]
    return [i,"Summary not found"]
def getresom(i):
    ans=[]
    for l in range(lenft):
        if ft1[l]==i:
            for q in range(l-5,l+5):
                ans.append([ft1[q],ft2[q]])
    return ans

app= Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',fl=fl[:3]) 
@app.route("/Genere")
def Genere():
    return render_template('genere.html',fl=fl)
@app.route("/recoom",methods=['GET', 'POST'])
def recoom():
    if request.method == 'POST':
        name = request.form['name']
        fl=htm(name)
        return render_template("recoom.html",fl=fl)
    return render_template("recoom.html")
@app.route("/similar/<int:i>",methods=['GET', 'POST'])
def similar(i):
    summary=get_summ(i)
    recom=getresom(i)
    return render_template("similar.html",nm=[summary,recom])
        
if __name__ =='__main__':
    app.run(debug=True)

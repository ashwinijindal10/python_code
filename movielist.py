#%%writefile $filepth
from bs4 import BeautifulSoup
from retrying import retry
from urllib.request import urlopen
from urllib.error import HTTPError
import pandas as pd
import omdb 

omdb.set_default('apikey', "2ed21063")     
prefixurl="http://freemoviewap-movie-may.review/"
filename="D:\data\mlist.csv"
eng_max_count=95
hin_max_count=7

def retry_if_error(ex):
    return ex is HTTPError

@retry(stop_max_attempt_number=3,wrap_exception=True,retry_on_result=retry_if_error)
def urlopen_with_retry(url):
    htmld= urlopen(url) 
    return BeautifulSoup(htmld.read(), 'html.parser')



def get_dlink_details(url):
    try:
        d1=urlopen_with_retry(url)
        l1=d1.find_all('a',attrs={"href":True})
        return [t["href"] for t in l1 if t["href"] if os.path.splitext(t["href"])[1] in [".mp4",".php"] and t.text.lower().find('download')>-1 ]
    except Exception as inst:
        print(inst)
        return []
    
    
def get_imdb_info(obj):
    try:
      
        rs=omdb.get(title=obj['name'].split("(")[0],year=obj['year'])
        if(rs):
             return { 'rating': rs['imdb_rating'],'genres':rs['genre']}
    except Exception as inst:
         print(inst)
            
    return {'rating':None,'genres':None}
    
    
def get_m_details(data):    
    l2=data.find_all('div',class_="w3l-movie-gride-agile")
    r1=[{ 'name' :s.text.strip(),'url': prefixurl+s.find('a')["href"]} for s in l2] 
   
    df=pd.DataFrame(r1)
    df['link'] =[ ', '.join(get_dlink_details(d['url'])) for d in r1]
    df['year'] =[ (d['url'].split('(')[1][:4] if (('(' in d['url']) and (len(d['url'].split('(')[1])>3)) else None) for d in r1 ]
   
    obj1= [get_imdb_info(f) for i,f in df.iterrows()]
    df= pd.concat([df,pd.DataFrame(obj1)],axis=1) 
    df=df[["name","year","rating","url","link"]]
    return df     
   

def get_mdata(page_from,page_count,kind):
    mtype=[ "hollywood_dub_movie","bollywood-movie"]
    
    for i in range(page_from,page_count+page_from): 
        link = prefixurl+mtype[kind]+ ("" if i<2 else "s_{}".format(i))  + ".php"
        yield urlopen_with_retry(link)
    
    
def loadlist():
    df = pd.DataFrame()
    i=1
    for pageData in get_mdata(1,50,0):
        rs=get_m_details(pageData)
        df=df.append(rs)
        print("listing done for ..page{}".format(i))
        i+=1  
    df.to_csv(filename,mode='a',index=False)

    
loadlist()

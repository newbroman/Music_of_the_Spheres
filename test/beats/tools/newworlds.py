# New worlds: the large bodies beyond Neptune designated since 2024 (2026 ED138 and whatever comes after), from JPL's Small-Body
# Database, written to newworlds.json at the site's root. The app reads that file (from its own site, so nothing is asked of any other
# server by the visitor) and adds each world to its sky with a provisional voice until the app is updated with a proper card.
# Run weekly by .github/workflows/newworlds.yml; by hand: python3 tools/newworlds.py
import json, math, re, sys, urllib.parse, urllib.request, datetime
Q={'fields':'full_name,pdes,name,a,e,i,om,w,tp,H,diameter,data_arc,condition_code,first_obs',
   'sb-kind':'a','sb-cdata':json.dumps({'AND':['a|GT|30','H|LT|4.5']})}
url='https://ssd-api.jpl.nasa.gov/sbdb_query.api?'+urllib.parse.urlencode(Q)
req=urllib.request.Request(url,headers={'User-Agent':'music-of-the-spheres/1.0 (newbroman.github.io)'})
d=json.load(urllib.request.urlopen(req,timeout=90))
F=d['fields'];rows=[dict(zip(F,r)) for r in d.get('data',[])]
since=2024;out=[]
for r in rows:
    fn=(r.get('full_name') or '').strip();pd=(r.get('pdes') or '').strip()
    m=re.search(r'\b((?:19|20)\d\d) [A-Z]{2}\d*\b',fn) or re.search(r'\b((?:19|20)\d\d) [A-Z]{2}\d*\b',pd)
    if not m or int(m.group(1))<since:continue
    try:a,e,i,om,w,tp,H=(float(r[k]) for k in ('a','e','i','om','w','tp','H'))
    except (TypeError,ValueError):continue
    if not(0<e<1 and a>30):continue
    cc=r.get('condition_code');cc=int(cc) if str(cc).isdigit() else 9
    if cc>6:continue
    if float(r.get('data_arc') or 0)<365:continue
    diam=r.get('diameter');diam=float(diam) if diam not in (None,'') else round(1329/math.sqrt(.12)*10**(-H/5))   # albedo 0.12 when no measurement
    desig=m.group(0);name=(r.get('name') or '').strip() or desig
    out.append({'id':re.sub(r'[^a-z0-9]','',desig.lower()),'name':name,'desig':desig,'a':round(a,4),'e':round(e,5),'i':round(i,4),'om':round(om,4),'w':round(w,4),'tp':round(tp,3),
                'H':round(H,2),'d':diam,'measured':r.get('diameter') not in (None,''),'arc':int(float(r.get('data_arc') or 0)),'cc':cc,'first':r.get('first_obs')})
out.sort(key=lambda x:x['H']);out=out[:8]
doc={'source':'JPL Small-Body Database (ssd-api.jpl.nasa.gov), bodies with a > 30 au and H < 4.5, condition code 6 or better, observed over a year or more, designated since %d'%since,
     'fetched':datetime.date.today().isoformat(),'w':out}
old=None
try:old=json.load(open('newworlds.json'))
except Exception:pass
if old and old.get('w')==out:print('no change:',[x['name'] for x in out]);sys.exit(0)
json.dump(doc,open('newworlds.json','w'),ensure_ascii=False,indent=1)
print('new worlds:',[(x['name'],x['a'],x['e'],x['i']) for x in out])

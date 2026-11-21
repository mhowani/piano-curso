import re, json, sys
SRC='/mnt/project-files/app/PianoCurso/PianoCurso/'
def strip_comments(s):
    out=[];i=0;ins=False
    while i<len(s):
        c=s[i]
        if ins:
            out.append(c)
            if c=='\\': out.append(s[i+1]); i+=2; continue
            if c=='"': ins=False
            i+=1; continue
        if c=='"': ins=True; out.append(c); i+=1; continue
        if s.startswith('//',i):
            j=s.find('\n',i); i=j if j>=0 else len(s); continue
        out.append(c); i+=1
    return ''.join(out)
TOK=re.compile(r'\s*(?:("(?:[^"\\]|\\.)*")|(-?\d+(?:\.\d+)?)|(\.[A-Za-z_]\w*)|([A-Za-z_]\w*)|(\S))',re.S)
def tokenize(s):
    toks=[];pos=0
    while pos<len(s):
        m=TOK.match(s,pos)
        if not m or m.end()==pos: break
        pos=m.end()
        if m.group(1): toks.append(('str',json.loads(m.group(1))))
        elif m.group(2): toks.append(('num',int(m.group(2))))
        elif m.group(3): toks.append(('enum',m.group(3)[1:]))
        elif m.group(4): toks.append(('id',m.group(4)))
        elif m.group(5): toks.append(('p',m.group(5)))
    return toks
class P:
    def __init__(s,t,env): s.t=t;s.i=0;s.env=env
    def peek(s,k=0): return s.t[s.i+k] if s.i+k<len(s.t) else ('eof',None)
    def take(s): x=s.t[s.i]; s.i+=1; return x
    def expect(s,v): x=s.take(); assert x==('p',v),(x,v,s.t[s.i-5:s.i+5])
    def expr(s):
        v=s.atom()
        while s.peek()==('p','+'):
            s.take(); v=v+s.atom()
        return v
    def atom(s):
        k,v=s.take()
        if k in('str','num'): return v
        if k=='enum': return v
        if k=='p' and v=='[':
            items=[];d=None
            while s.peek()!=('p',']'):
                a=s.expr()
                if s.peek()==('p',':'):
                    s.take(); b=s.expr(); d=d or {}; d[a]=b
                else: items.append(a)
                if s.peek()==('p',','): s.take()
            s.take(); return d if d is not None else items
        if k=='id':
            if s.peek()==('p','('):
                s.take(); pos=[];kw={}
                while s.peek()!=('p',')'):
                    if s.peek()[0]=='id' and s.peek(1)==('p',':'):
                        name=s.take()[1]; s.take(); kw[name]=s.expr()
                    else: pos.append(s.expr())
                    if s.peek()==('p',','): s.take()
                s.take()
                return s.env[v](*pos,**kw)
            return s.env[v]
        raise Exception((k,v))
def block(src,name):
    m=re.search(r'static let '+name+r'[^=]*=\s*',src); i=m.end()
    # find matching bracket
    depth=0;j=i;ins=False
    while True:
        c=src[j]
        if ins:
            if c=='\\': j+=2; continue
            if c=='"': ins=False
        elif c=='"': ins=True
        elif c=='[': depth+=1
        elif c==']':
            depth-=1
            if depth==0: return src[i:j+1]
        j+=1
cur=strip_comments(open(SRC+'Models/Curriculum.swift').read())
def pieceSteps(first): return [first,"Escúchala entera una vez (en MuseScore pulsa reproducir).","Mano derecha sola, muy lento, de 2 en 2 compases.","Mano izquierda sola, igual.","Manos juntas a la mitad del tempo, con metrónomo.","Sube el metrónomo 4 o 5 pulsaciones cada día que te salga sin fallos."]
assert 'Sube el metrónomo 4 o 5' in cur
def Lesson(id,style,level,kind,title,goal,steps,minutes=15,exerciseID=None,scores=[]):
    return dict(id=id,style=style,level=level,kind=kind,title=title,goal=goal,steps=steps,minutes=minutes,exercise=exerciseID,scores=scores)
def piece(id,style,level,title,goal,first,minutes=15,exercise=None,scores=[]):
    return Lesson(id,style,level,'partitura',title,goal,pieceSteps(first),minutes,exercise,scores)
def ScoreLink(title,composer,year,tip,search=None):
    d=dict(title=title,composer=composer,year=year,tip=tip)
    if search: d['search']=search
    return d
env=dict(Lesson=Lesson,piece=piece,ScoreLink=ScoreLink)
lessons=[]
for n in ['fundamentos','clasica','blues','jazz','pop','rock']:
    lessons+=P(tokenize(block(cur,n)),env).expr()
ex=strip_comments(open(SRC+'Music/ExerciseLibrary.swift').read())
def progression(chords,pats): return ' | '.join(pats[c] for c in chords if c in pats)
def Exercise(id,title,detail,clef,notation,keyFifths=0,tempo=70):
    return dict(id=id,title=title,detail=detail,clef=clef,keyFifths=keyFifths,tempo=tempo,notation=notation)
env2=dict(Exercise=Exercise,progression=progression,twelveBar=["I","I","I","I","IV","IV","I","I","V","IV","I","V"])
exs=P(tokenize(block(ex,'all')),env2).expr()
ch=strip_comments(open(SRC+'Music/Chords.swift').read())
byLesson=P(tokenize(block(ch,'byLesson')),{}).expr()
levels={'cero':0,'inicial':1,'intermedio':2,'avanzado':3}
for l in lessons: l['level']=levels[l['level']]
print(len(lessons),len(exs),len(byLesson),file=sys.stderr)
open('data.js','w').write('const LESSONS='+json.dumps(lessons,ensure_ascii=False)+';\nconst EXERCISES='+json.dumps(exs,ensure_ascii=False)+';\nconst CHORDS_BY_LESSON='+json.dumps(byLesson,ensure_ascii=False)+';\n')

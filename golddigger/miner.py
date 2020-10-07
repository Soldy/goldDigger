from html.parser import HTMLParser


class test(HTMLParser):
    def f(t):
        self.feed(str(t))
    def __init__(self):
        HTMLParser.__init__(self)
    def reset(self):
        HTMLParser.reset(self)
        self.active = True
        self.text=""
        self.title=""
        self.metas=[]
        self.styles=""
        self.specialList=[]
        self.words=[]
        self.wordsCount={}
        self.activeTag=""
        self.links=[]
        self.imgs=[]
        self.scripts=[]
        self.classes=[]
        self.ids=[]
        self.special={
            'h1':[],
            'h2':[],
            'h3':[],
            'h4':[]
        }
        self.tagList = []
    def sfw(self,size): # size filter words
        out = []
        for i in self.words:
            if size > len(i):
               out.append(i)
        return out
    def sfwc(self, size): # size filter words cont
        out = {}
        for i in self.wordsCount:
            if int(size) > len(i):
               out[i] = self.wordsCount[i]
        return out
    def attrs_find(self, tag, attrs):
        for attr in attrs:
            if attr[0].lower() == 'class' :
               for i in attr[1].split():
                   self.classes.append(i)
            if attr[0].lower() == 'id' :
               for i in attr[1].split():
                   self.ids.append(i)
    def link_find(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'href' :
               self.links.append(attr[1])
    def meta_find(self, tag, attrs):
        name = ""
        content = ""
        for attr in attrs:
            if attr[0].lower() == 'name':
               name = attr[1]
            if attr[0].lower() == 'content' :
               content = attr[1]
        if not name == "":
            self.metas.append({
                'name':name,
                'content':content
            })
    def img_find(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'src' :
               self.imgs.append(attr[1])
    def script_find(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'src' :
               self.scripts.append(attr[1])
    def special_tag(self, data):
        if len(self.tagList) > 0:
            tag = self.tagList[-1]
            if tag in ['h1','h2','h3','h4'] :
                if data and data.strip():
                    self.special[tag].append(data)
        if len(self.tagList) > 1:
            tag = self.tagList[-2]
            if tag in ['h1','h2','h3','h4'] :
                if data and data.strip():
                    self.special[tag].append(data.strip())
        if len(self.tagList) > 2:
            tag = self.tagList[-3]
            if tag in ['h1','h2','h3','h4'] :
                if data and data.strip():
                    self.special[tag].append(data.strip())
    def tag_check(self):
        if len(self.tagList) > 0:
            if self.tagList[-1] in ['script', 'style'] :
                self.active = False
            else:
                self.active = True
    def handle_starttag(self, tag, attrs):
        self.tagList.append(tag)
        if tag.lower() == 'a' :
           self.link_find(tag, attrs)
        if tag.lower() == 'img' :
           self.img_find(tag, attrs)
        if tag.lower() == 'script' :
           self.script_find(tag, attrs)
        if tag.lower() == 'meta' :
           self.meta_find(tag, attrs)
        self.attrs_find(tag, attrs)
        self.tag_check()
    def handle_endtag(self, tag):
        if self.tagList[-1] == tag : 
           del self.tagList[-1]
        self.tag_check()
    def handle_data(self, data):
        if self.active == False:
            return False
        if len(self.tagList) > 0:
            if self.tagList[-1] == 'title':
                self.title = data
                return False
        data = data.replace('\n', '')
        data = data.replace('\t', '')
        data = data.replace('\r', '')
        self.special_tag(data)
        self.text = self.text+" "+data
        for w in data.split():
            w = w.lower()
            if  w in  self.wordsCount :
                self.wordsCount[w] += 1
            else :
                self.wordsCount[w] = 1
            self.words.append(w)

m = test()


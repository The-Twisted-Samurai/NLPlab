class req_h:
    
    def __init__(self, sources, category, q, language, country , to, sortBy, pageSize):
        self.sources = sources
        self.category = category
        self.q = q
        self.language = language 
        self.country = country 
        self.to = to
        self.sortBy = sortBy
        self.pageSize = pageSize


class req_e:
    def __init__(self, q , sources, domains, category,  language, country, to, sortBy, pageSize):
        self.q = q
        self.sources = sources
        self.domains = domains 
        self.category = category
        self.language = language 
        self.country = country 
        self.to = to
        self.sortBy = sortBy
        self.pageSize = pageSize



class req_NLP: 
    def __init__(self, url,headers, params,data, auth):
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data
        self.auth = auth
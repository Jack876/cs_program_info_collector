import re

'''
Module 4 //all 11 independent aspect classes of application materials
'''
class GRE():
    
    '''
    all attributes of aspect class are set 'Not mentioned' as default
    '''
    def __init__(self):
        self.req = 'Not mentioned'          
        self.ins_code = 'Not mentioned'   # institution code for GRE/TOEFL
        self.dep_code = 'Not mentioned'   # department code for GRE/TOEFL
        self.score = 'Not mentioned'
        self.full_cont = 'Not mentioned'
        self.gist_cont = []
    
    '''
    the get_XXX() functions update the values of relative attributes and return them
    '''
    def get_req(self,tag):
        if self.ins_code != 'Not mentioned' or self.score != 'Not mentioned':self.req='Required' 
        if self.req == 'Not mentioned':
            req_exp = re.compile(r'(?:not\srequire|no|t\srequire)?.*GRE.*(?:not\srequired|not\sneeded)?',re.S|re.I)
            no_req = req_exp.search(str(tag))
            if no_req: self.req = 'Not required'
        return self.req
    
    def get_ins(self,tag):
        if self.ins_code == 'Not mentioned':
            ins_exp = re.compile(r'(?:Institution\scode|School\scode).*?(\d{4})',re.S|re.I)
            has_ins = ins_exp.search(str(tag))
            if has_ins: self.ins_code = has_ins.group(1)
        return self.ins_code   
     
    def get_dep(self,tag):
        if self.dep_code == 'Not mentioned':
            dep_code = re.compile(r'Department\scode.*?(\d+)',re.S|re.I)
            has_dep = dep_code.search(str(tag))
            ndep_code = re.compile(r'(?:not|no)?.*?Department\scode.*(?:not\srequired|not\sneeded)?',re.S|re.I)
            no_dep = ndep_code.search(str(tag))
            if has_dep: self.dep_code = has_dep.group(1)
            elif no_dep: self.dep_code = 'Not required'
        return self.dep_code
    
    def get_score(self,tag):
        if self.score == 'Not mentioned':
            score_exp = re.compile(
                r'''(?:verbal|\bV\b)?.*(\d\d%|1\d{2}).*(?:verbal|\bV\b)?             
                        # group 1 for verbal/V, it could be in percentile or integer
                    (?:quantitative|\bQ\b)?.*(\d\d%|1\d{2}).*(?:quantitative|\bQ\b)? 
                        # group 2 for quantitative/Q, it could be in percentile or integer 
                    (?:AW|Analytical)?.*(\d\d%|\d\.\d).*(?:AW|Analytical)? 
                        # group 3 for AW, it could be in percentile of integer with decimal
                ''',re.S|re.I|re.X)
            has_score = score_exp.search(str(tag))
            if has_score:
                self.score = 'Verbal:\t' + has_score.group(1) + '\tQuantitative:\t' + has_score.group(2) + '\tAW:\t' + has_score.group(3)
        return self.score
    
    def get_gist(self):     # for the convenience of outputting each attribute in for-loop
        self.gist_cont = ['[GRE]','Requirement:' + self.req, 'Institution code:' + self.ins_code, 'Department code:' + self.dep_code,'Score:' + self.score]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

class TOEFL():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.ins_code = 'Not mentioned' 
        self.dep_code = 'Not mentioned'
        self.minimum = 'Not mentioned'
        self.full_cont = 'Not mentioned'
        self.gist_cont = []
        
    def get_req(self,tag):
        if self.ins_code != 'Not mentioned' or self.minimum != 'Not mentioned': self.req = 'Required'
        if self.req == 'Not mentioned':
            req_exp = re.compile(r'(?:not\srequire|no|t\srequire)?.*TOEFL.*(?:not\srequired|not\sneeded)?',re.S|re.I)
            no_req = req_exp.search(str(tag))
            if no_req: self.req = 'Not required'
        return self.req
    
    def get_ins(self,tag):
        if self.ins_code == 'Not mentioned':
            ins_exp = re.compile(r'(?:Institution\scode|School\scode).*?(\d{4})',re.S|re.I)
            has_ins = ins_exp.search(str(tag))
            if has_ins: self.ins_code = has_ins.group(1)
        return self.ins_code    
    
    def get_dep(self,tag):
        if self.dep_code == 'Not mentioned':
            dep_code = re.compile(r'Department\scode.*?(\d+)',re.S|re.I)
            has_dep = dep_code.search(str(tag))
            ndep_code = re.compile(r'(?:not|no)?.*?Department\scode.*(?:not\srequired|not\sneeded)?',re.S|re.I)
            no_dep = ndep_code.search(str(tag))
            if has_dep: self.dep_code = has_dep.group(1)
            elif no_dep: self.dep_code = 'Not required'
        return self.dep_code
    
    def get_minimum(self,tag):
        if self.minimum == 'Not mentioned':
            minimum_exp=re.compile(
                r'''(?:internet-?\s*?based|iBT|TOEFL\sscore).{,25}(?:[56789]\d\b|1\d\d\b)(?:\s*?-\s*?(?:[56789]\d\b|1\d\d\b))?|   # relevant context may be ahead or after, and score can be 90-100
                    (?:[56789]\d\b|1\d\d\b)(?:\s*?-\s*?(?:[56789]\d\b|1\d\d\b))?.{,25}(?:internet-?\s*?based|iBT|TOEFL\sscore)    # here we judge by word-distance
                ''',re.S|re.I|re.X)
            has_minimum = minimum_exp.search(str(tag))
            if has_minimum: self.minimum = re.findall(r'\d+',minimum_exp.findall(str(tag))[0])[0]
        return self.minimum
    
    def get_gist(self):
        self.gist_cont = ['[TOEFL]','Requirement:' + self.req, 'Institution code:' + self.ins_code, 'Department code:' + self.dep_code, 'Minimum:' + self.minimum]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont=text
        return self.full_cont

class IELTS():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.score = 'Not mentioned'
        self.full_cont = 'Not mentioned'
        self.gist_cont = []
        
    def get_req(self,tag):
        if self.req == 'Not mentioned':
            no_exp = re.compile(r'(?:not/not\saccept|\bno\b|t\saccept).*?IELTS.*(?:not\saccepted)?',re.S|re.I)
            no_req = no_exp.search(str(tag))
            if no_req: self.req = 'Not accepted'
            else: self.req = 'Acceptable'
        return self.req
    
    def get_score(self,tag):
        if self.score == 'Not mentioned':    
            score_exp = re.compile(r'(\b\d(?:\.\d)?\b)',re.S)  # the minimum average score
            has_score = score_exp.search(str(tag))
            if has_score: self.score = has_score.group(1)
        return self.score
    
    def get_gist(self):
        self.gist_cont = ['[IELTS]','Requirement:' + self.req, 'Score:' + self.score]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont=text
        return self.full_cont

class DDL():
    
    def __init__(self):
        self.time = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_time(self,tag):
        if self.time == 'Not mentioned':
            not_exp = re.compile(
                r'''(?:TOEFL|GRE|IELTS).*?(?:D|d)eadline|  # exclude the situation where deadline belongs to tests
                    (?:D|d)eadline.*?(?:TOEFL|GRE|IELTS)
                ''',re.S|re.X)
            not_DDL = not_exp.search(str(tag))
            DDL_exp = re.compile(
                r'''\b[a-zA-Z]{3,9}\b\.?\s*\d{1,2}[a-z]{0,2}\b,?\s*\d{0,4}|   # match pattern December(.) 22(nd, 2017)
                    \d{1,2}\/\d{1,2}\/\d{4}           # match pattern 12/22/2017 (MM/DD/YYYYY) or 18/8/2017 (DD/MM/YYYY)
                ''',re.S|re.X)
            has_DDL = DDL_exp.search(str(tag))
            if not_DDL: self.time = 'Not mentioned'
            elif has_DDL: self.time = DDL_exp.findall(str(tag))[0]
        return self.time
    
    def get_gist(self):
        self.gist_cont = ['[Deadline]','Time:' + self.time]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont=text
        return self.full_cont

class GPA():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.grade = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.grade != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_grade(self,tag):
        if self.grade == 'Not mentioned':
            GPA_exp = re.compile(r'\b[ABC]\b|\d\.\d(?:\/\d\.\d)?|\d\.\d\sout\sof\s\d\.\d',re.S)  # like ABC level or 3.0(/4.0)  
            has_GPA = GPA_exp.search(str(tag))
            if has_GPA: self.grade = GPA_exp.findall(str(tag))[0]
        return self.grade
    
    def get_gist(self):
        self.gist_cont = ['[GPA]','Requirement:' + self.req, 'Grade:' + self.grade]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

class TC():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.form ='Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.form != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_form(self,tag):
        if self.form == 'Not mentioned':
            not_exp = re.compile(
                r'''(?:TOEFL|GRE|IELTS).*?(?:T|t)ranscript|  # exclude the situation where transcripts belong to tests
                    (?:T|t)ranscript.*?(?:TOEFL|GRE|IELTS)
                ''',re.S|re.X)
            not_TC = not_exp.search(str(tag))
            TC_exp = re.compile(r'online|upload',re.S|re.I)
            has_TC = TC_exp.search(str(tag))
            if not_TC: self.form = 'Not mentioned'
            elif has_TC: self.form = 'Electronic'
        return self.form
    
    def get_gist(self):
        self.gist_cont = ['[Transcripts]','Requirement:' + self.req,'Form:' + self.form]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

class FEE():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.money = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        return 'Required'
    
    def get_money(self,tag):
        if self.money == 'Not mentioned':
            FEE_exp = re.compile(r'\$\d+|\d+\sdollars',re.S|re.I)
            has_FEE = FEE_exp.search(str(tag))
            if has_FEE: self.money = FEE_exp.findall(str(tag))[0]
        return self.money
    
    def get_gist(self):
        self.gist_cont = ['[Fee]','Requirement:' + self.req,'Money:' + self.money]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont=='Not mentioned': self.full_cont=text
        return self.full_cont   

class RL():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.number = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.number != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_number(self,tag):
        if self.number == 'Not mentioned':
            RL_exp = re.compile(
                r'''((?:one|two|three|four|five|\d)|(?:\d\s*?-\s*?\d))\s*?
                (?:Recommendation\sLetters|Letters\sof\sRecommendation)
                ''',re.S|re.I|re.X)
            has_RL = RL_exp.search(str(tag))
            if has_RL: self.number = has_RL.group(1)
        return self.number
    
    def get_gist(self):
        self.gist_cont = ['[Recommendation Letters]','Requirement:' + self.req,'Number:' + self.number]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont=text
        return self.full_cont

class PS():
    def __init__(self):
        self.req = 'Not mentioned'
        self.type = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.type != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_number(self,tag):
        if self.type == 'Not mentioned':
            one_exp = re.compile(r'(Personal\sStatement|Statement\sof\sPurpose)',re.S|re.I)
            two_exp = re.compile(r'Personal\sStatement.*?Statement\sof\sPurpose',re.S|re.I)
            has_one = one_exp.search(str(tag))
            has_two = two_exp.search(str(tag))
            if has_two: self.type = 'Both Personal Statement and Statement of Purpose required'
            elif has_one: self.type = 'Only\t'+has_one.group(1)+'\trequired'
        return self.type
    
    def get_gist(self):
        self.gist_cont=['[Personal Statement/Statement of Purpose]','Requirement:' + self.req,'Type:' + self.type]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

class WS():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.length = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.length != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_length(self,tag):
        if self.length == 'Not mentioned':
            WS_exp = re.compile(r'(?:\d{1,2}?\s*(?:-\s*\d{1,2})?|one|two|three)-?\s*?page',re.S|re.I)
            has_WS = WS_exp.search(str(tag))
            if has_WS: self.length = WS_exp.findall(str(tag))[0]
        return self.length
    
    def get_gist(self):
        self.gist_cont = ['[Writing Sample]','Requirement:' + self.req,'Length:' + self.length]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

class CV():
    
    def __init__(self):
        self.req = 'Not mentioned'
        self.type = 'Not mentioned'
        self.gist_cont = []
        self.full_cont = 'Not mentioned'
        
    def get_req(self,tag):
        if self.type != 'Not mentioned': self.req = 'Required'
        return self.req
    
    def get_number(self,tag):
        if self.type == 'Not mentioned':
            two_exp = re.compile(
                r'''Resume.*?(?:\/|or|and).*?(?:CV|C\.V\.|Curriculum\sVita)|
                    (?:CV|C\.V\.|Curriculum\sVita).*?(?:\/|or|and).*?Resume
                ''',re.S|re.I|re.X)
            one_exp = re.compile(r'(Resume|CV|C\.V\.|Curriculum Vita)',re.S|re.I)
            has_two = two_exp.search(str(tag))
            has_one = one_exp.search(str(tag))
            if has_two: self.type = two_exp.findall(str(tag))[0]
            elif has_one: self.type = has_one.group(1)
        return self.type
    
    def get_gist(self):
        self.gist_cont = ['[Rsume/CV]','Requirement:' + self.req,'Type:' + self.type]
        return self.gist_cont
    
    def get_full(self,text):
        if self.full_cont == 'Not mentioned': self.full_cont = text
        return self.full_cont

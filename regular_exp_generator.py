import re

'''
Module 2 //this class provides the basic entrance regular expression 
           of each aspect of application materials.
'''
class Reg_Generator():
       
    def __init__(self):
        self.GRE = r'GRE'
        self.TOEFL = r'TOEFL'
        self.IELTS = r'IELTS'
        self.GPA = r'GPA|grade\spoint\saverage'
        self.TC = r'(?:Official\sTranscripts|Transcripts|Transcript)'
        self.PS = r'(?:Personal\sStatement|Statement\sof\sPurpose)'
        self.RL = r'(?:Recommendation\sLetters|Letters\sof\sRecommendation)'
        self.CV = r'(?:CV|Resume|Curriculum\sVita|C\.V\.)'
        self.WS = r'(?:Writing\sSample|Essay)'
        self.DDL = r'(?:Deadlines|Deadline)'
        self.FEE = r'Fee'
        self.ETC = r'Additional|Supplement|Other'
        
    def GREp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.GRE+r'.*'+r'</'+tag+r'>',re.S)
    
    def TOEFLp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.TOEFL+r'.*'+r'</'+tag+r'>',re.S)
    
    def IELTSp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.IELTS+r'.*'+r'</'+tag+r'>',re.S)
    
    def GPAp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.GPA+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def TCp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.TC+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def PSp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.PS+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def RLp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.RL+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def CVp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.CV+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def WSp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.WS+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def DDLp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.DDL+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def FEEp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.FEE+r'.*'+r'</'+tag+r'>',re.S|re.I)
    
    def ETCp(self,tag):
        return re.compile(r'<'+tag+r'>'+r'.*'+self.ETC+r'.*'+r'</'+tag+r'>',re.S)

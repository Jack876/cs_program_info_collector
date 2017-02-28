import re
from bs4 import BeautifulSoup

'''
Module 3 //this class provides a full description of each aspect
'''                  
class Text_Cleaner():

    def __init__(self,li,aspect):
        self.li = li
        self.aspect = aspect
        
    '''
    cut repeated head, like GRE:/GRE-/GRE.
    '''
    def head_cutter(self):
        head_exp = r'(<li>\s*(?:<p>|<ul>|<ol>)*\s*)((?:<b>|<strong>)?'+r'\s*'+self.aspect+r'\s*'+r'(?:</b>|</strong>)?'+r'(?:\s*\.|\s*-|\s*:|\s*\n))'+r'(.*)'
        has_head = re.compile(head_exp,re.S|re.I).search(str(self.li))
        clean_text = ''
        if has_head:
            temp_text = has_head.group(1)+has_head.group(3)
            clean_text = BeautifulSoup(temp_text,"html.parser").get_text()
        else:
            clean_text = self.li.get_text()
        return clean_text
    
    '''
    delete redundant and unnecessary initial marks of the clean_text
    '''
    def mark_cutter(self,text):
        start_exp = re.compile(r'(\W*)(\w*.*)',re.S)
        start_test = start_exp.search(text)
        if start_test: clean_text = start_test.group(2).strip()
        return clean_text
    
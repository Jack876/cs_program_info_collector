import re,urllib.request
import database
import regular_exp_generator
import text_processor
import aspects
from bs4 import BeautifulSoup

'''
Module 5 // the main running program
'''

'''
 this function instantiates all the classes and updates the attribute of each class
 with HTML tags in loops, and returns a list of attribute-updated objects of each class
'''
def data_extractor(name,univ_name,univ_page):
    
    gre,toefl,ielts,gpa,tc,ps = aspects.GRE(),aspects.TOEFL(),aspects.IELTS(),aspects.GPA(),aspects.TC(),aspects.PS()
    rl,ws,fee,ddl,cv,cs = aspects.RL(),aspects.WS(),aspects.FEE(),aspects.DDL(),aspects.CV(),regular_exp_generator.Reg_Generator()
    web_list = univ_page[univ_name[name]]
    
    for tag in[r'li',r'p']:
        for url in web_list:
            data = urllib.request.urlopen(url).read().decode('UTF-8')
            soup = BeautifulSoup(data,"html.parser")
            source = soup.find_all(tag)
            for element in source:
                if re.search(cs.GREp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.GRE)
                    gre.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    gre.get_ins(element)
                    gre.get_dep(element)
                    gre.get_score(element)
                    gre.get_req(element)
                if re.search(cs.TOEFLp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.TOEFL)
                    toefl.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    toefl.get_ins(element)
                    toefl.get_dep(element)
                    toefl.get_minimum(element)
                    toefl.get_req(element)
                if re.search(cs.IELTSp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.IELTS)
                    ielts.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    ielts.get_score(element)
                    ielts.get_req(element)
                if re.search(cs.GPAp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.GPA)
                    gpa.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    gpa.get_grade(element)
                    gpa.get_req(element)
                if re.search(cs.TCp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.TC)
                    tc.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    tc.get_form(element)
                    tc.get_req(element)
                if re.search(cs.PSp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.PS)
                    ps.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    ps.get_number(element)
                    ps.get_req(element)
                if re.search(cs.RLp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.RL)
                    rl.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    rl.get_number(element)
                    rl.get_req(element)
                if re.search(cs.CVp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.CV)
                    cv.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    cv.get_number(element)
                    cv.get_req(element)
                if re.search(cs.WSp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.WS)
                    ws.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    ws.get_length(element)
                    ws.get_req(element)
                if re.search(cs.DDLp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.DDL)
                    ddl.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    ddl.get_time(element)
                if re.search(cs.FEEp(tag),str(element)):
                    cleaner = text_processor.Text_Cleaner(element,cs.FEE)
                    fee.get_full(cleaner.mark_cutter(cleaner.head_cutter()))
                    fee.get_money(element)
                    fee.get_req(element)
    return [ddl,fee,gre,toefl,ielts,gpa,tc,ps,cv,rl,ws]

'''
 this function outputs each attribute of each aspect class
'''
def result_out():
    name=input('please enter your desired university:\n')
    for aspect in data_extractor(name,database.univ_name,database.univ_page):
        for item in aspect.get_gist():
            print(item)
        print('[Full description]:\n'+aspect.full_cont)
        print()
    
if __name__ == "__main__":
    result_out()

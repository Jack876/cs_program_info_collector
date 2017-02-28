
'''
Module 1 //the basic database from which the program opens the urls of web pages and reads info
'''
# these dictionaries are not complete，
# but it is not hard to append more universities and websites to them 
# according to some US master program rankings

'''
the univ_name dictionary allows different kinds of input from users to refer to the same university, 
with different forms of names as keys and the same integer number as common value
'''
univ_name={'Carnegie Mellon University':1,'CMU':1,'cmu':1,
           'Massachusetts Institute of Technology':2,'MIT':2,'mit':2,
           'University of California—San Diego':3,'UCSD':3,'ucsd':3,
           'Georgia Institute of Technology':4,'gatech':4,
           'Brandeis University':5,'brandeis':5,
           'Stanford University':6,'stanford':6,
           'University of Illinois--Urbana-Champaign':7,'UIUC':7,'uiuc':7,
           'Cornell University':8,'cornell':8,
           'University of Washington':9,'UW':9,'uw':9,
           'University of Wisconsin--Madison':10,'wisconsin':10,
           'University of California--Los Angeles':11,'UCLA':11,'ucla':11,
           'University of Michigan--Ann Arbor':12,'UMich':12,'umich':12,
           }

'''
in univ_page the integer is the key and refers to a list of 
relevant cs program description websites of a certain university
'''
univ_page={1:['http://scs.cmu.edu/masters-admissions','http://www.csd.cs.cmu.edu/academics/masters/admissions'],
           2:['http://www.eecs.mit.edu/academics-admissions/graduate-program/admissions/dear-prospective-applicant'],
           3:['http://cse.ucsd.edu/graduate/admissions/application-checklist','http://cse.ucsd.edu/graduate/admissions'],
           4:['http://www.cc.gatech.edu/academics/degree-programs/masters/computer-science/admissionreqs'],
           5:['http://www.brandeis.edu/gsas/programs/computer_science.html'],
           6:['http://www.cs.stanford.edu/admissions/general-information','http://www.cs.stanford.edu/admissions/deadlines','http://www.cs.stanford.edu/admissions/checklist'],
           7:['http://www.cs.uiuc.edu/admissions/graduate/applications-process-requirements','http://www.grad.illinois.edu/admissions/instructions/04c','http://www.cs.uiuc.edu/admissions/graduate/application-deadlines'],
           8:['http://www.cs.cornell.edu/masters/apply/application'],
           9:['http://www.uwb.edu/mscsse/admissions/applying-for-admissions'],
           10:['http://www.cs.wisc.edu/academics/graduate-programs/guidebook/admission','http://www.cs.wisc.edu/academics/graduate-programs/apply-regular-MS-PhD'],
           11:['http://www.cs.ucla.edu/graduate-admission-requirements/'],
           12:['http://www.eecs.umich.edu/eecs/graduate/cse/apply/how.html','http://www.eecs.umich.edu/eecs/graduate/cse/apply/']
           }

# cs_program_info_collector

[Third Party Lib Required]

BeautifulSoup v4.5

[Main Goal]

To gather admission information of required application materials of different CS programs in American universities.

[Function]

1.Display following gist information of a given CS program:

• Deadline: the application deadline;

• Fee: the amount of application fee;

• GRE: the institution code, department code and score requirement;

• TOEFL: the institution code, department code and the minimum requirement of score; 

• IELTS: the acceptance and minimum score requirement;

• GPA: the minimum requirement of GPA;

• Transcripts: the form of transcripts, electronic or not;

• Personal Statement: the type of Personal Statement or Statement of Purpose; 

• CV: the type of CV or resume;

• Recommendation Letters: the required number of recommendation letters;

• Writing Sample: the requirement of the length of writing sample;

2.Display the detailed full description of above aspects.

[Idea]

Since most of target information is included in the HTML \<li> tags and \<p> tags on the university program websites, the basic idea is to extract all the \<li> and \<p> pairs and then perform regular expressions on them to dig out the target info.

Firstly, for the source of info, websites, we manually collect all the websites of CS programs of a number of American universities according to the ranking of U.S.News (http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-science- schools/computer-science-rankings).

Then we extract all necessary HTML tag pairs with BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/), and then perform regular expressions on each aspect of the application materials and their requirements.

[Framework]

The two univ_name and univ_page dictionaries are the basic database from which open the urls of program web pages and read info. The univ_name allows different kinds of input from users to refer to the same university, with different forms of names, complete or abbreviated, capitalized or lowercased, as keys and the same integer number as their common value. In univ_page the integer is the key and refers to a list of relevant cs program description websites of a certain university.

The Reg_generator class provides the basic entrance regular expression of each aspect of application materials. With that, the program can find all target source in which key words like GRE or CV appear.

The Text_cleaner class mainly provides a clean and organized full description of each aspect. Some target tag pairs contain the key words at the beginning of the sentence, but in the output title of each aspect is already given, so the head_cutter() function in this class cuts off all the repeated pattern of key words, and the mark_cutter() function continues to deal with the left unnecessary marks at the beginning, like ‘;’ or ‘:’.

The 11 aspect classes like GRE, TOEFL and WS are all independent classes. They have different independent attributes and functions, but are still in the same pattern. All the attributes of each aspect class are set ‘Not mentioned’ as default. Every time when the new info is given, the program checks if the value of the attribute is in default, if it is, the value will be updated; if not, it means the value has already been updated, it will remain the same. The method to change the value of each attribute is the relative get function in each class. For instance, the get_socre() function updates the value of score of IELTS class and returns it.

The data_extractor() function is the core running part of the program. It instantiates all the 11 aspect classes, and also actives the Reg-generator and Text_cleaner. It firstly reads in a list of target HTML tags, like \<li> and \<p> in this case, and then according to the input of user gets the relative url list of a given university, and run a for-loop of each tag to scour each website to feed new info to every ‘Not mentioned’ attribute of every independent class. At last it returns a list of objects of all 11 classes with attributes updated.

The result_run() function reads in the object list and outputs all the gist content and full content of each object.

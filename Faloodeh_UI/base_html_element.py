"""
hello everyone I am Amir Mohammad Dehghan
this project is html, css and js compiler
and this file is basic class and function
for create elements in this project ...
"""


class Base_Elements_Tag:
    """
    this class is basic class for create html tags well
     as h1, a p and the other tags similar them ...
    """

    def __init__(self):
        self.html_code = ''

    #     html_code is end answer of your progress and is html code if print it

    def __repr__(self):
        return self.html_code

    #   if you print or return your object from this class it will return html code
    def tab_lines(self, code: str):
        inner = ''
        codes = code.split('\n')
        for i in codes:
            inner += '\t' + str(i) + '\n'
        return inner

    # for more beautiful html code this wil add tab to all codes in any hungry tags

    def general_tag(self, tag_name, args: set = None, attribute: dict = None, single=False, add_to_body=True,
                    inner=None, pyclass=None, pyid=None, pytype=None):
        # this function is basic customize html tags creator like p h1 a and other similar them
        # in tag_name you should enter name of your tag ilke p br and ...
        # some tags just are single. they don't have end tag like this <...> your inner </...> and the have inner
        # but when single is True it will create tags like <br>
        # I called the important html attribute in function entry like id as pyid , class as pyclass, and type as pytype
        # but for other attribute I used **kwargs for enter other and your customize attribute you can use like
        # example="attr_value"
        this_tag = ''
        this_tag += f'\n<{tag_name} '
        if pyclass is not None:
            this_tag += f'class=" {pyclass} "'
        if pyid is not None:
            this_tag += f' id="{pyid}"'
        if pytype is not None:
            this_tag += f' id="{pytype}"'
        this_tag += self.args_controler(args=args, attribute=attribute)
        this_tag += '> '
        if inner is not None and single == False:
            this_tag += str(inner) + f'</{tag_name}>'
        if add_to_body:
            self.html_code += this_tag
        return this_tag

    #         and in above they are adding the important args to your html text for create greate html codes
    #         and for creating our customize tags we can change the tag_name and single
    def hungry_tag(self, tag_name, pyclass=None, pyid=None, pytype=None, args: set = None, attribute: dict = None):
        starting_tag = ''
        ending_tag = f'\n</{tag_name}> \n'
        # this function is basic customize html tags creator like class div section a and other similar them
        # in tag_name you should enter name of your tag ilke p br and ...
        # I called the important html attribute in function entry like id as pyid , class as pyclass, and type as pytype
        # but for other attribute I used **kwargs for enter other and your customize attribute you can use like
        # example="attr_value"

        starting_tag += f'\n<{tag_name} '
        if pyclass is not None:
            starting_tag += f'class=" {pyclass} "'
        if pyid is not None:
            starting_tag += f' id="{pyid}"'
        if pytype is not None:
            starting_tag += f' id="{pytype}"'
        starting_tag += self.args_controler(attribute=attribute, args=args)
        starting_tag += '> '

        self.html_code = str(starting_tag) + self.tab_lines(self.html_code) + str(ending_tag)

    # really it will eat element tags before it
    #  like html code =
    #  <example1>...</example1>
    #  <example2>...</example2>
    #  <example3>...</example3>

    # when you call hungry_tag like main.hungry_tag(tag_name , ...)
    # it will eat before him self element like:
    # <tag_name ... >
    # <example1>...</example1>
    # <example2>...</example2>
    # <example3>...</example3>
    # </tag_name>

    def inner_tag(self, tag_name, add_to_body=True, inner=None, src=None, pyclass=None, pyid=None, args: set = None,
                  attribute: dict = None):
        # this function is basic customize html tags creator like script div class a and other similar them
        # in inner_tag you should enter name of your tag ilke script class and ...
        # they have to include end tag like this <...> your inner </...> and the have inner
        # it did not support single tags
        # I called the important html attribute in function entry like id as pyid , class as pyclass, and type as pytype
        # but for other attribute I used **kwargs for enter other and your customize attribute you can use like
        # example="attr_value"
        this_tag = ''
        this_tag += f'\n<{tag_name}'
        if pyclass is not None:
            this_tag += f'class=" {pyclass} "'
        if pyid is not None:
            this_tag += f' id="{pyid}"'
        if src is not None:
            this_tag += f' src="{src}"'
        this_tag += self.args_controler(attribute=attribute, args=args)
        this_tag += '> \n'
        if inner is not None:
            this_tag += str(inner)
        this_tag += f'\n</{tag_name}>'
        if add_to_body:
            self.html_code += this_tag
        return this_tag

    #         and in above they are adding the important args to your html text for create greate html codes
    #         and for creating our customize tags we can change the tag_name and single

    def add_before(self, main):
        self.html_code = str(main) + self.html_code

    # really this function will add everything before all html tags

    def args_controler(self, args: set, attribute: dict):
        this_tag = ''
        if attribute:
            key = list(attribute.keys())
            # when you use **attribute key is name of your attr like style or others ...
            value = list(attribute.values())
            # when you use **attribute key is value of your attr like "value" or True or integer or others ...
            attrs = ''
            arg = ''
            #  attrs variable for create your customize attributes at end processes it will return like key="value" ...
            for i in range(len(attribute)):
                # by this loop you can create any attrs you want one , fifteen ... or one billion attrs
                if key is not None and value is not None:
                    if type(value[i]) != type(str('')):
                        attrs += f'{key[i]}={value[i]} '
                    elif type(value[i]) == type(str('')):
                        attrs += f'{key[i]}="{value[i]}" '
            this_tag += f' {attrs}'
        if args:
            for i in range(len(args)):
                if i is not None:
                    arg += f'{i} '
            this_tag += f'  {arg} '
        return this_tag
# PASSED adding class and method for write javascript code and create javascript compiler by python
# PASSED adding class and method for create some different and important html elements like class ,
#  div section and other like this
# TODO create python test for test project by pytest in this dir/test.py


#  POWERED BY AMIR MOHAMMAD DEHGHAN

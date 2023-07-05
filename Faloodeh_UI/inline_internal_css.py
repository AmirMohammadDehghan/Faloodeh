
def inline_css3(**kwargs):
    if kwargs:
        key = list(kwargs.keys())
        # when you use **kwargs key is name of your style like color or others ...
        value = list(kwargs.values())
        # when you use **kwargs key is value of your style like red or others ...
        styles = ''
        #  attrs variable for create your customize attributes at end processes it will return like key:"value"; ...
        for i in range(len(kwargs)):
            # by this loop you can create any style you want one , fifteen ... or one billion style
            if key is not None and value is not None:
                styles += f'{key[i]}:{value[i]}; '.replace('_', '-').replace('__', '_')
        return f' {styles}'

def external_css3(path:str, **kwargs):
    if kwargs:
        key = list(kwargs.keys())
        # when you use **kwargs key is name of your style like color or others ...
        value = list(kwargs.values())
        # when you use **kwargs key is value of your style like red or others ...
        styles = ''
        #  attrs variable for create your customize attributes at end processes it will return like key:"value"; ...
        for i in range(len(kwargs)):
            # by this loop you can create any style you want one , fifteen ... or one billion style
            if key is not None and value is not None:
                styles += f'{key[i]}:{value[i]};\n '.replace('_', '-').replace('__', '_')
        styles = '{ \n' + styles + '}'
        return f'{path} {styles}' 




#TODO add internal css
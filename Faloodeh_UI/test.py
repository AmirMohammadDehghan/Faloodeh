if __name__ == '__main__':
    from html_elements import Elements_Tag
    import time


    start = time.time()


    main = Elements_Tag()
    main.doctype('HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"')
    main.doctype()
    main.element_tag(tag_name='p', inner='hello world', pyid='hello', pyclass='hello class', style='fdjhg : lfg', a=3, b=True)
    main.element_tag(tag_name='h1', inner='test two')
    main.html_tag(lang='en')


    print(main)
    m = str(main).split('\n')
    for i in m:
        print('\t'+i)

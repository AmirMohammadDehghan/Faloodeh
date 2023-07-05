"""
hello everyone I am Amir Mohammad Dehghan
this project is html, css and js compiler
and this file is basic class and function
for create elements in this project ...
"""
from .base_html_element import Base_Elements_Tag
from .internal_javascript import Faloodeh_Js2Py


class Elements_Tag(Base_Elements_Tag):
    # this class will inheritance from base_element_tag class and use basic methods for create spacial html elements
    def __init__(self):
        super().__init__()
        self.help_en = {

            ############# basic tags ######################
            'doctype': ' Defines the document type.',
            'html': "                        Defines an HTML document",
            'head': "  Contains metadata/information for the document",
            'title': "                Defines a title for the document",
            'body': "                     Defines the document's body",
            'h': "                           Defines HTML headings",
            'p': "                             Defines a paragraph",
            'br': "                     Inserts a single line break",
            'hr': "        Defines a thematic change in the content",
            '!--...--': "                               Defines a comment",

            ############ formatting tags ######################
            'abbr': "              Defines an abbreviation or an acronym",
            'address': "  Defines contact information for the author/own...",
            'b': "                                  Defines bold text",
            'bdi': "  Isolates a part of text that might be formatte...",
            'bdo': "               Overrides the current text direction",

            'blockquote': "  Defines a section that is quoted from another ...",

            'cite': "                        Defines the title of a work",
            'code': "                   Defines a piece of computer code",
            'del': "  Defines text that has been deleted from a docu...",
            'dfn': "  Specifies a term that is going to be defined w...",
            'em': "                            Defines emphasized text",
            'i': "  Defines a part of text in an alternate voice o...",
            'ins': "  Defines a text that has been inserted into a d...",
            'kbd': "                             Defines keyboard input",
            'mark': "                    Defines marked/highlighted text",
            'meter': "  Defines a scalar measurement within a known ra...",
            'pre': "                          Defines preformatted text",
            'progress': "                  Represents the progress of a task",
            'q': "                          Defines a short quotation",
            'rp': "  Defines what to show in browsers that do not s...",
            'rt': "  Defines an explanation/pronunciation of charac...",
            'ruby': "  Defines a ruby annotation (for East Asian typo...",
            's': "             Defines text that is no longer correct",
            'samp': "      Defines sample output from a computer program",
            'small': "                               Defines smaller text",
            'strong': "                             Defines important text",
            'sub': "                           Defines subscripted text",
            'sup': "                         Defines superscripted text",
            'template': "  Defines a container for content that should be...",
            'time': "              Defines a specific time (or datetime)",

            'u': "  Defines some text that is unarticulated and st...",
            'var': "                                 Defines a variable",
            'wbr': "                      Defines a possible line-break",

        }
        self.help_fa = {
            ############ basic tags ##################
            '!DOCTYPE': "	از این تگ، برای مشخص کردن نسخه HTML استفاده می شود.",
            'html': "	از این تگ، برای تعریف ریشه یا root اصلی یک سند HTML استفاده می شود.",
            'title': "	از این تگ، برای تعریف عنوان یک صفحه استفاده می شود.",
            'body': "	از این تگ، برای تعریف بدنه سند HTML استفاده می شود.",
            'h': "	از این تگ، برای گروه بندی عناصر h1 تا h6 استفاده می شود.",
            'p': "	از این تگ، برای تعریف یک پاراگراف استفاده می شود.",
            'br': "	Inserts a single line break",
            'hr': "	از این تگ، برای کشیدن یک خط بین محتوی استفاده می شود.",
            '!--...--': "	از این تگ، برای قرار دادن توضیحات در کد استفاده می شود.",
            ############ formatting tags ######################
            'abbr': "  از این تگ، برای تعریف یک مخفف استفاده می شود.",
            'address': "   از این تگ، برای نمایش اطلاعات مربوط به تماس نویسنده استفاده می شود./article",
            'b': " از این تگ، برای ضخیم یا bold کردن متن استفاده می شود.",
            'bdi': "   از این تگ، برای جهت دادن به متن یا کاراکتراهایی که خارج از زبان اصلی صفحه است استفاده می شود.",
            'bdo': "   از این تگ، برای برعکس کردن متن استفاده می شود.",
            'blockquote': "    از این تگ، برای تعیین محتوایی که به نقل از منبع دیگر آورده شده است استفاده می شود.",
            'cite': "  از این تگ، برای مشخص کردن عنوان یک کار استفاده می شود.",
            'code': "  از این تگ، برای نمایش متن بنحوی که بصورت یک قطعه کد کامپیوتری بنظر آید، استفاده می شود.",
            'del': "   از این تگ، برای نمایش متن بصورت خط خورده استفاده می شود.",
            'dfn': "   از این تگ، برای نمایش متن، بنحوی که بصورت یک عبارت تعریفی بنظر آید استفاده می شود.",
            'em': "    از این تگ، برای مورب کردن متن بنحوی که بصورت تأکید شده (emphasized) بنظر آید استفاده می شود.",
            'i': " از این تگ، برای نمایش متن بصورت مورب یا Italik استفاده می شود.",
            'ins': "   از این تگ، در کنار عنصر del برای نشانه گذاری تکه متنی که اخیراً به متن اصلی اضافه شده استفاده می شود.",
            'kbd': "   از این تگ، برای فرمت دهی متن بنحوی که مانند ورودی صفحه کلید بنظر آید استفاده می شود.",
            'mark': "  از این تگ، برای برجسته و علامت دار کردن متن استفاده می شود.",
            'meter': " از این تگ، برای نمایش یک گیج یا اندازه سنج عددی، استفاده می شود. البته محدوده اعداد باید از قبل مشخص شود.",
            'pre': "   از این تگ، برای نمایش فاصله و خط ها اضافه ای که در کد وجود دارد استفاده می شود.",
            'progress': "  از این تگ، برای نمایش میزان پیشرفت یک پروسه استفاده می شود.",
            'q': " از این تگ، برای تعریف یک نقل قول کوتاه استفاده می شود.",
            'rp': "    این تگ، تعریف می کند که چه چیزی نشان داده شود، اگر مرورگر از حاشیه نویسی ruby پشتیبانی نکند.",
            'rt': "    از این تگ، برای مشخص کردن یک راهنما برای توضیح یا نحوه ی تلفظ کاراکترهای آسیای شرقی استفاده می شود. (برای زبان های آسیای شرقی کاربرد دارد)",
            'ruby': "  از این تگ، برای تعریف یک حاشیه روبی استفاده می شود. (برای زبان های آسیای شرقی کاربرد دارد)",
            's': " از این تگ، برای نمایش متن بصورت خط خورده استفاده می شود.",
            'samp': "  از این تگ، برای فرمت دهی متن بنحوی که شکل خروجی یک برنامه کامپوتری باشید، استفاده می شود.",
            'small': " از این تگ، برای کوچکتر نشان دادن متن استفاده می شود.",
            'strong': "    از این تگ، برای بولد کردن متن استفاده می شود.",
            'sub': "   از این تگ، برای نمایش متن، کمی پایین تر استفاده می شود.",
            'sup': "   از این تگ، برای نمایش متن، کمی بالاتر استفاده می شود.",
            'time': "  از این تگ، برای نمایش تاریخ یا زمان استفاده می شود.",
            'u': " از این تگ، برای خط زیردار کردن متن استفاده می شود.",
            'var': "   از این تگ، برای فرمت دهی متغییرها استفاده می شود.",
            'wbr': "   این تگ، برای رفتن به خط جدید استفاده می شود.",
            ############# forms in html ##################
            'form': "	از این تگ، برای تعریف فرم ورود اطلاعات استفاده می شود.",
            'input': "	از این تگ، برای تعریف کنترل های ورود اطلاعات استفاده می شود.",
            'textarea': "	از این تگ، برای تعریف یک فیلد ورودی چند خطی استفاده می شود.",
            'button': "	از این تگ، برای تعریف یک دکمه استفاده می شود.",
            'select': "	از این تگ، برای تعریف یک لیست کشوئی استفاده می شود.",
            'optgroup': "	از این تگ، برای گروه بندی آیتم های مربوط به هم در یک لیست کشویی استفاده می شود.",
            'option': "	از این تگ، برای تعریف آیتم های لیست های کشوئی استفاده می شود.",
            'label': "	از این تگ، برای تعریف یک لیبل برای یک فیلد ورودی استفاده می شود.",
            'fieldset': "	از این تگ، برای گروه بندی فیلدهای وابسته بهم در یک فرم استفاده می شود.",
            'legend': "	از این تگ، برای تعریف عنوان برای عنصر fieldset استفاده می شود.",
            'datalist': "	از این تگ، برای تعریف یک لیست پیشنهادی برای یک تکس باکس استفاده می شود.",
            'keygen': "	از این تگ، برای تولید کلید در فرم های ورود اطلاعات استفاده می شود.",
            'output': "	از این تگ، برای نمایش نتیجه یک محاسبه استفاده می شود.",
            #################### frame tags in html ##################
            'iframe': "	از این تگ، برای تعریف فریم در یک صفحه استفاده می شود.",
            #################### images tags ######################
            'img': "	از این تگ، برای نمایش عکس استفاده می شود.",
            'map': "	از این تگ، برای تعریف یک نقشه تصویری یا image-map استفاده می شود.",
            'area': "	از این تگ، برای تعیین مناطق در یک image-map استفاده می شود.",
            'canvas': "	از این تگ، برای رسم اشکال در یک صفحه وب بهمراهJavaScript استفاده می شود.",
            'figcaption': "	از این تگ، برای تعریف یک عنوان در عنصر figure استفاده می شود.",
            'figure': "	از این تگ، برای تعریف محتوایی مانند تصاویر، نمودار ها، عکس ها، لیست کد و ... استفاده می شود.",
            ############ audio and video tags ##################
            'audio': "	از این تگ، برای پخش صدا استفاده می شود.",
            'source': "	از این تگ، برای مشخص کردن منابع فایل های ویدئوی یا صوتی در تگ های audio و video استفاده می شود.",
            'track': "	از این تگ، برای نمایش زیرنویس در تگ های مدیا استفاده می شود.",
            'video': "	از این تگ، برای پخش صدا استفاده می شود.",
            ############################ link tags #############
            'a': "	از این تگ، برای تعریف یک لینک استفاده می شود.",
            'link': "	از این تگ، برای لینک به یک منبع خارجی مثل CSS استفاده می شود.",
            'nav': "	از این تگ، برای تعریف لیستی از لینک های ناوبری استفاده می شود.",
            ############ lists tags ##############
            'ul': "	از این تگ، برای تعریف یک لیست نامرتب استفاده می شود.",
            'ol': "	از این تگ، برای تعریف یک لیست مرتب استفاده می شود.",
            'li': "	از این تگ، برای تعیین آیتم های لیست های مرتب و نامرتب استفاده می شود.",
            'dl': "	از این تگ، برای تعریف یک لیست تعریفی استفاده می شود.",
            'dt': "	از این تگ، برای تعریف آیتم های لیست تعریفی استفاه می شود.",
            'dd': "	از این تگ، برای مشخص کردن آیتم های لیست تعریفی (dl) استفاده می شود.",
            'menu': "	از این تگ، برای تعریف یک منو استفاده می شود.",
            'menuitem': "	از این تگ، برای تعریف آیتم های منو استفاده می شود.",
            ################# table tags #############
            'table': "	از این تگ، برای تعریف یک جدول استفاده می شود.",
            'caption': "	از این تگ، برای تعریف یک جدول استفاده می شود. caption",
            'th': "	از این تگ، برای تعریف عنوان ستون های یک جدول استفاده می شود.",
            'tr': "	از این تگ، برای تعریف ردیف در جدول استفاده می شود.",
            'td': "	از این تگ، برای تعریف یک سلول از جدول استفاده می شود.",
            'thead': "	از این تگ، برای گروه بندی سرعنوان های یک جدول استفاده می شود.",
            'tbody': "	از این تگ، برای تعریف بدنه جدول استفاده می شود.",
            'tfoot': "	از این تگ، برای گروه بندی فوتر جدول استفاده می شود.",
            'col': "	از این تگ، داخل عنصر colgroup برای قالب بندی ستون های جدول استفاده می شود.",
            'colgroup': "	از این تگ، برای گروه بندی یک یا چند ستون (col) در یک جدول، جهت قالب بندی استفاده می شود.",

        }
        self.html_code = ""

    ################# basic tags #####################
    def doctype(self, version: str = None, add_to_body=True):

        # this is doctype tag every html docs have version and some other information for browser
        doctype_tag = ''
        if version is not None:
            doctype_tag = f'!DOCTYPE {version}'
        if version is None:
            doctype_tag = '!DOCTYPE'
            # i created element tag method
        return self.general_tag(tag_name=doctype_tag, single=True, add_to_body=add_to_body)

    def html(self, *args, **kwargs):
        name = 'html'
        # I created it by hungry tag it is useful for special
        self.hungry_tag(tag_name=name, args=args, attribute=kwargs)

    def head(self, inner, *args, **kwargs):
        name = 'head'
        self.inner_tag(tag_name=name, inner=str(inner), args=args, attribute=kwargs)

    def title(self, inner, *args, **kwargs):
        name = 'title'
        self.general_tag(tag_name=name, inner=str(inner), args=args, attribute=kwargs)

    ## body tag todo ######## 

    ############ h1 to h6 tags #########################
    def h1(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h1'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    def h2(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h2'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    def h3(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h3'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    def h4(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h4'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    def h5(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h5'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    def h6(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'h6'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    ################# p tag ##############################
    def p(self, add_to_body=True, inner=None, pyclass=None, pyid=None, *args, **kwargs):
        tag_name = 'p'
        self.general_tag(tag_name=tag_name, add_to_body=add_to_body, inner=inner, pyclass=pyclass, pyid=pyid, args=args,
                         attribute=kwargs)

    ################# br tag ###################
    def br(self):
        name = 'br'
        self.general_tag(tag_name=name, single=True)

    ################# hr tag ###################
    def hr(self):
        name = 'hr'
        self.general_tag(tag_name=name, single=True)

    def comment(self, inner):
        self.html_code += f'\n<!- {inner} ->'

    ################ formatimg tags ##################

    def abbr(self, *args, **kwargs):
        name = 'abbr'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def address(self, *args, **kwargs):
        name = 'address'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def b(self, *args, **kwargs):
        name = 'b'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def bdi(self, *args, **kwargs):
        name = 'bdi'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def bdo(self, *args, **kwargs):
        name = 'bdo'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def blockquote(self, *args, **kwargs):
        name = 'blockquote'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def cite(self, *args, **kwargs):
        name = 'cite'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def abbr(self, *args, **kwargs):
        name = 'abbr'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def code(self, *args, **kwargs):
        name = 'code'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    def dele(self, *args, **kwargs):
        name = 'del'
        self.general_tag(tag_name=name, args=args, attribute=kwargs)

    ################# hungry tags #####################

    ################# inner tags #####################
    def script(self, func=None, src=None, internal=True, **requires):
        name = 'script'
        if internal:
            inner = Faloodeh_Js2Py().js2py(func=func, kwargs=requires)
            self.inner_tag(tag_name=name, inner=inner)
        if internal == False:
            self.inner_tag(tag_name=name, src=src)

################# general tags #####################

#  POWERED BY AMIR MOHAMMAD DEHGHAN

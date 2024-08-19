from fasthtml.common import *


def class_list(*args):
    return ' '.join(f'{pre}{arg}' if arg is not True else pre for pre, arg in zip(args[::2], args[1::2]) if arg)


def Wrapper(title, description, content, style=1, align=None, color=None, invert=False):
    wrapper_classes = class_list('wrapper style', style, 'align-', align, 'invert', invert, 'color', color)
    inner_content = [H2(title), P(description), content]
    section = Section(Div(*inner_content, cls='inner'), cls=wrapper_classes)
    return section

def TechWrapper(title, description, style=1, align=None, color=None, invert=False, id=None):
    # wrapper_classes = class_list('wrapper style', style, 'align-', align, 'invert', invert, 'color', color)
    inner_content = [Div(Section(Header(H3(title)), P(description)), cls="index align-left")]
    section = Section(Div(*inner_content), id=id)
    return section

def my_wrapper(*content):
    mysec = Section(Div(Div(content, cls='index align-left'), cls='inner'), cls='wrapper style1 align-center')
    return mysec



def MyContent(title, description, style=1, align=None, color=None, invert=False):
    wrapper_classes = class_list('wrapper style', style, 'align-', align, 'invert', invert, 'color', color)
    inner_content = [Div(Section(Header(H3(title)), Div(P(description), cls='content')), cls="index align-left")]
    section = Section(Div(*inner_content, cls=''), cls=wrapper_classes)
    return section

def MyContent2(title, description):
    return Section(Header(H3(title)), Div(P(description), cls='content'))


def ItemContent(title, description, image_url=None, icon_type=None, icon=None, xtra=None, url=None):
    content = []
    icon_type = icon_type or "fa"
    if icon: content.append(Span(cls=f"{icon_type} fa-{icon}"))
    content.extend([H3(title), P(description)])
    if xtra: content.append(xtra if isinstance(xtra, (list, tuple)) else [xtra])
    if image_url:
        return Article(
            A(Img(src=image_url, alt=""), cls="image"),
            Div(*content, cls="caption"))
    if url:
        # return Div(A(Section(*content), href=url, cls="mylink", target="_blank"), cls="hover-container")
        return A(Section(*content), href=url, cls="mylink")
    return Div(Section(*content))

def ItemContent2(title, description, date=None):
    content = []
    if date: content.extend([H4(B(title)), P(date), P(description)])
    else: content.extend([H4(B(title)), P(description)])
    return Div(Section(*content))


def Item(items, style=1, size="medium", onscroll_fade=True):
    return Div(*items, cls=class_list('items style', style, '', size, 'onscroll-fade-in', onscroll_fade))

def TechItem(items, style=1, size="medium", onscroll_fade=True):
    return Div(*items, cls=class_list(style, '', size, 'onscroll-fade-in', onscroll_fade))


def Gallery(items, style=2, size="medium", lightbox=True, fade_in=True):
    return Div(*items, cls=class_list('gallery style', style, '', size, 'lightbox', lightbox, 'onscroll-fade-in', fade_in))

scr_fns = ['jquery.min', 'jquery.scrollex.min', 'jquery.scrolly.min', 'browser.min', 'breakpoints.min', 'util', 'main']
scripts = [Script(src=f"assets/js/{js}.js") for js in scr_fns]
def PageWrapper(title, *content): return Title(title), Div(*content, id="wrapper", cls="divided"), *scripts

def get_app(hdrs=None, *args, **kwargs):
    if hdrs is None: hdrs=[]
    hdrs.append(Link(rel="stylesheet", href="assets/css/main.css"))
    app = FastHTML(hdrs=hdrs, *args, **kwargs)
    @app.get("/{fname:path}.{ext:static}")
    def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')
    return app, app.route

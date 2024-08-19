from story import *

app,rt = get_app()


def footer():
    links = (A('items', href='/'), A('gallery', href='/gallery'))
    return Footer(Div(links, cls='inner'), cls='wrapper style1 align-center')


def about_me():
    description = "I am a Senior Software Engineer with a strong background in climate modeling, earth system science, and geospatial data analysis"
    about_me = MyContent("About me", description, style=1, align='left')
    return about_me


def technical_skills():
    items = [
        ItemContent2("Python", "Something about Python experience"),
        ItemContent2("Databases", "Something about Databases experience"),
        ItemContent2("Web Development", "Something about Web Development experience"),
        ItemContent2("Mobile Development", "Something about Mobile Development experience"),
        ItemContent2("Machine Learning", "Something about Machine Learning experience"),
        ItemContent2("Cloud Computing", "Something about Cloud Computing experience"),

    ]
    items = TechItem(items)
    # wrapper = TechWrapper("Nemanja Komar", sub, Item(items), style=1, align='center')
    tech_skills = TechWrapper("Technical skills", items, style=1, align='left')
    return tech_skills


def work_experience():
    items = [
        ItemContent2("Senior Software Engineer", "Something about Python experience"),
        ItemContent2("Software Engineer", "Something about Databases experience"),
        ItemContent2("Data Scientist", "Something about Web Development experience"),
        ItemContent2("Climate Modeler", "Something about Mobile Development experience"),
        ItemContent2("Geospatial Analyst", "Something about Machine Learning experience"),
        ItemContent2("Research Scientist", "Something about Cloud Computing experience"),

    ]
    items = TechItem(items)
    # wrapper = TechWrapper("Nemanja Komar", sub, Item(items), style=1, align='center')
    tech_skills = TechWrapper("Work Experience", items, style=1, align='left')
    return tech_skills


def certifications():
    items = [
        ItemContent2("AWS Certified Solutions Architect", "Something about Python experience"),
        ItemContent2("AWS Certified", "Something about Databases experience"),
        ]
    items = TechItem(items)
    return TechWrapper("Certifications", items, style=1, align='left')

setup_toasts(app)
@rt("/")
def get(session):
    add_toast(session, f"Thanks for visiting. This page is still work in progress", "info")
    items = [
        ItemContent("Location", "Colorado, USA", icon="map-marker-alt", url="#"),
        ItemContent("Github", "Some of my projects", icon_type="fa-brands", icon="github", url="https://github.com/nems808"),
        ItemContent("LinkedIn", "Preferred contact method", icon_type="fa-brands", icon="linkedin", url="https://www.linkedin.com/in/nemanjakomar/"),
        ItemContent("Publications", "Carbon cycle and climate modeling", icon_type="fa-brands", icon="researchgate", url="https://www.researchgate.net/profile/Nemanja_Komar"),
        ItemContent("Portfolio", "Various Projects, Web, and Mobile apps", icon="earth-americas", url="#"),
    ]
    sub = "Senior Software Engineer"
    wrapper = Wrapper("Nemanja Komar", sub, Item(items), style=1, align='center')
    return PageWrapper("Nemo's portfolio", wrapper, about_me(), technical_skills(), work_experience(), certifications(), footer())


@rt("/gallery")
def get():
    xtra = A("Details", cls="button small")
    items = [
        ItemContent("Title 1", "Short description 1", "images/pic01.jpg", xtra=xtra),
        ItemContent("Title 2", "Short description 2", "images/pic02.jpg", xtra=xtra),
        ItemContent("Title 3", "Short description 3", "images/pic03.jpg", xtra=xtra),
    ]
    sub = "This is a demonstration of the Gallery element."
    wrapper = Wrapper("Gallery", sub, Gallery(items), style=1)
    return PageWrapper("Gallery Demo", wrapper, footer())

@rt('/toasting')
def get(session):
    # Normally one toast is enough, this allows us to see
    # different toast types in action.
    add_toast(session, f"Toast is being cooked", "info")
    add_toast(session, f"Toast is ready", "success")
    add_toast(session, f"Toast is getting a bit crispy", "warning")
    add_toast(session, f"Toast is burning!", "error")
    return Titled("I like toast")

serve()


from models.work import WorkExperience
from story import *

app, rt = get_app()


def footer():
    links = (A('Built with FastHTML', href='https://docs.fastht.ml/'))
    return Footer(Div(links, cls='inner'), cls='wrapper style1 align-center')


def about_me():
    description = "I am a Senior Software Engineer with a strong background in climate modeling, earth system " \
                  "science, geospatial data analysis and data visualization. I have a passion for developing " \
                  "mobile games in my free time. "
    about_me = MyContent2("About me", description)
    return about_me


def technical_skills():
    items = [
        ItemContent2("Python", "Extensive experience with Python programming language: RESTful APIs, Django, FastAPI, "
                               "Flask, SQLAlchemy, Pandas, Numpy, Scipy, Matplotlib, Plotly, Geopandas, Shapely, "
                               "GDAL, Scikit-learn,  GUI development with PyQt"),
        ItemContent2("Databases", "Proficient in PostgreSQL, PostGIS, SQLite, TimescaleDB, AWS RDS, database design "
                                  "and writing efficient geospatial queries"),
        ItemContent2("Web Development", "React, Typescript, GraphQL, HTMX, HTML, CSS, JavaScript, Bootstrap"),
        ItemContent2("Mobile Development",
                     "Android, Java, ARCore, Unity, C#, AR and VR-based mobile applications, Swift"),
        ItemContent2("Data Visualization",
                     "Extensive experience with data visualization libraries: Matplotlib, Plotly, Leaflet"),
        ItemContent2("Cloud Computing",
                     "Terraform, AWS (Fargate, ECS, ECR, Lambda, SQS, SES, Cognito), Docker, Docker-compose, CircleCI (CI/CD)"),

    ]
    items = TechItem(items)
    tech_skills = TechWrapper("Technical skills", items, style=1, align='center')
    return tech_skills


def work_experience():
    insight = Ul(Li("Led development of a distributed, automated service using GraphQL, FastAPI, and React, "
                    "significantly enhancing delivery efficiency of aerially collected methane data."),
                 Li("Engineered scalable microservices with AWS (Fargate, ECS, ECR, Lambda, SQS, SES) and Terraform, "
                    "ensuring robust and secure operations (AWS Cognito)."),
                 Li("Improved product generation time by 200-300% through effective use of Python’s multiprocessing, "
                    "optimizing resource utilization and processing speed."),
                 Li("Optimized SQLAlchemy PostGIS queries, achieving up to 100x performance increase for faster "
                    "geodata retrieval."),
                 Li("Led technical interviews to assess and evaluate the competencies of prospective hires.")
                 ),

    sealevel_center = Ul(Li("Led collaboration with USGS to develop AR and VR-based mobile applications and 3D "
                            "visualization tools for studying sea level rise."),
                         Li("Developed open-source Python GUI applications to enhance the accuracy and efficiency of "
                            "sea level data analysis."),
                         Li("Engineered web-based geospatial data visualization products using protobuf for "
                            "high-performance data handling."),
                         Li("Engineered robust RESTful APIs with Flask to streamline data access and manipulation for "
                            "geospatial climatological tools."),
                         Li("Managed all phases of the software development lifecycle (planning, design, "
                            "implementation, deployment, and support), ensuring product quality and timely delivery.")
                         ),

    research = Ul(Li("Developed numerical models for simulation of past climate events and carbon cycling."),
                  Li("Built Bash and Shell scripts for analyzing large amounts of numerical data produced by a "
                     "High Performance Computing (HPC) in Solar System stability simulations."),
                  Li("Demonstrated expertise in Earth sciences through authorship and publication of multiple "
                     "papers in high-impact journals, showcasing strong writing and collaborative abilities."),
                  ),
    link = A("https://www.endangeredlanguages.com/", href="https://www.endangeredlanguages.com/", target="_blank")
    full_stack = Ul(Li("Developed and maintained a Full-stack Django website: ", link),
                    Li("Reduced loading time of certain pages by over 90%."),
                    ),
    items = [
        WorkExperience(position="Senior Software Engineer", company="InsightM", date_range="January 2022 - Present",
                       bullets=insight),
        WorkExperience(position="Scientific Programmer", company="University of Hawaii Sea Level Center",
                       date_range="May 2018 - January 2022",
                       bullets=sealevel_center),
        WorkExperience(position="Research Specialist", company="University of Hawaii",
                       date_range="January 2018 - May 2018",
                       bullets=research),
        WorkExperience(position="Full-stack Web Developer", company="University of Hawaii",
                       date_range="January 2017 - December 2022",
                       bullets=full_stack),

    ]
    items = TechItem(items)
    # wrapper = TechWrapper("Nemanja Komar", sub, Item(items), style=1, align='center')
    tech_skills = TechWrapper("Work Experience", items, style=1, align='left')
    return tech_skills


def certifications():
    items = [
        ItemContent2("Introduction to Data Science in Python", "University of Michigan"),
        ItemContent2("Applied Machine Learning in Python", "University of Michigan"),
        ItemContent2("An Introduction to Interactive Programming in Python", "Rice University"),
    ]
    items = TechItem(items)
    return TechWrapper("Certifications", items, style=1, align='left')


def additional_experience():
    items = [
        ItemContent2("Best Augmented Reality App at the AT&T Honolulu Hackathon, Apr 2018", "Developed an AR demo app "
                                                                                            "for helping Hawaii "
                                                                                            "tourist navigate the "
                                                                                            "island"),
        ItemContent2("Former Division I volleyball collegiate athlete", "University of Hawaii Student-Athlete Award "),
        ItemContent2("Current Semi-pro beach volleyball player", "Competing on the AVP tour and FIVB World Tour"),
        ItemContent2("Phi Beta Kappa member", ""),
    ]
    items = TechItem(items)
    return TechWrapper("Additional Experiences", items, style=1, align='left')


def portfolio():
    link = A("https://apps.apple.com/app/sea-level-rise-ar-visualizer/id1563315544",
             href="https://apps.apple.com/app/sea-level-rise-ar-visualizer/id1563315544", target="_blank")
    puho = Ul(Li("iOS: ", link),
              Li("Android:", "Coming soon"),
              ),

    link = A("https://uhslc.soest.hawaii.edu/stations/",
             href="https://uhslc.soest.hawaii.edu/stations/", target="_blank")
    data_explorer = Ul(Li("Web: ", link)),

    link = A("https://uhslc.soest.hawaii.edu/products/pacific-islands-flooding-outlook/",
             href="https://uhslc.soest.hawaii.edu/products/pacific-islands-flooding-outlook/", target="_blank")
    visualizer = Ul(Li("Web: ", link)),

    ios_link = A("https://apps.apple.com/app/sea-level-rise-ar-visualizer/id1563315544",
                 href="https://apps.apple.com/app/sea-level-rise-ar-visualizer/id1563315544", target="_blank")
    android_link = A("https://play.google.com/store/apps/details?id=com.freegames.gibberish",
                     href="https://play.google.com/store/apps/details?id=com.freegames.gibberish", target="_blank")
    web_link = A("https://gibberishgame.com",
                 href="https://gibberishgame.com", target="_blank")
    gibberish = Ul(Li("iOS: ", ios_link),
                   Li("Android:", android_link),
                   Li("Web:", web_link),
                   ),

    ios_link = A("https://apps.apple.com/us/app/the-setting-sun-zen-puzzle/id1588174839",
                 href="https://apps.apple.com/us/app/the-setting-sun-zen-puzzle/id1588174839", target="_blank")
    setting_sun = Ul(Li("iOS: ", ios_link)),

    ios_link = A("https://apps.apple.com/us/app/diamond-ring-reflex-tester/id1493050483",
                 href="https://apps.apple.com/us/app/diamond-ring-reflex-tester/id1493050483", target="_blank")
    diamond = Ul(Li("iOS: ", ios_link)),
    items = [
        ItemContent("Sea Level Rise AR Visualizer", "Utilized aerial LIDAR data to create an immersive sea level "
                                                    "projection visualization tool in AR using Unity3D", xtra=puho),
        ItemContent("Sea level warning tool", "A dashboard for early warning of extreme coastal water levels in the "
                                              "Pacific Ocean", xtra=visualizer),
        ItemContent("Real-time Sea level data explorer", "Real-time, high-frequency sea-level data web interface",
                    xtra=data_explorer),

        ItemContent("Gibberish Game Against Friends", "A cross-platform (iOS, Android, and Web), real-time "
                                                      "multiplayer game in Unity3D",
                    xtra=gibberish),
        ItemContent("The Setting Sun Puzzle", "A small brain teaser using Unity3D as inspired by a physical game I "
                                              "was introduced to at he Museum of Illusions",
                    xtra=setting_sun),
        ItemContent("Diamond Ring - reflex tester", "A small, hyper-casual game that tests your patience and "
                                                    "reflexes. It also features a cross-platform multiplayer race. "
                                                    "Built in Unity3D.",
                    xtra=diamond),
    ]
    items = TechItem(items)
    return TechWrapper("Projects", items, style=1, align='left', id='portfolio')


setup_toasts(app)


@rt("/")
def get(session):
    add_toast(session, f"Thanks for visiting. This page is still work in progress", "info")
    items = [
        ItemContent("Location", "Colorado, USA", icon="map-marker-alt", url="#"),
        ItemContent("Github", "Some of my projects", icon_type="fa-brands", icon="github",
                    url="https://github.com/nems808"),
        ItemContent("LinkedIn", "Preferred contact method", icon_type="fa-brands", icon="linkedin",
                    url="https://www.linkedin.com/in/nemanjakomar/"),
        ItemContent("Publications", "Carbon cycle and climate modeling", icon_type="fa-brands", icon="researchgate",
                    url="https://www.researchgate.net/profile/Nemanja_Komar"),
        ItemContent("Portfolio", "Various Projects, Web, and Mobile apps", icon="earth-americas", url="#portfolio"),
    ]
    sub = "Senior Software Engineer"
    all_text = my_wrapper(about_me(), technical_skills(), work_experience(), certifications(), additional_experience(),
                          portfolio(), footer())
    wrapper = Wrapper("Nemanja Komar", sub, Item(items), style=1, align='center')
    return PageWrapper("Nemo's portfolio", wrapper, all_text)


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

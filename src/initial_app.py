from fasthtml.common import *
from monsterui.all import *

# Choose a theme color
hdrs = Theme.blue.headers()

# Create your app with the theme
app, rt = fast_app(hdrs=hdrs)

# Global state (in a real app, use proper state management)
show_splash = True
show_sidebar = False


def create_navbar():
    return NavBar(
        A("Main", href="/"),
        A("Page 1", href="/page1"),
        A("Page 2", href="/page2"),
        Button("Toggle Sidebar", onclick="toggleSidebar()"),
    )


def create_sidebar():
    return NavContainer(  # Using NavContainer for sidebar
        NavHeaderLi("Navigation"),
        NavLi(A("Main", href="/")),
        NavLi(A("Page 1", href="/page1")),
        NavLi(A("Page 2", href="/page2")),
        cls="sidebar",  # Apply CSS class for styling
    )


def create_splash_screen():
    return Modal(
        Card(
            H3("Welcome to our App!"),
            P("This is the splash screen with information about the app."),
            footer=Button("Dismiss", onclick="dismissSplash()"),
        ),
        id="splash-modal",
    )


@rt
def index():
    global show_sidebar, show_splash  # Declare show_sidebar and show_splash as global
    content = Card(H1("Main Page"), P("This is the main page content."))

    # Conditionally include the sidebar
    sidebar = create_sidebar() if show_sidebar else ""

    layout = Container(create_navbar(), sidebar, content)  # Sidebar content

    return Titled(
        "MonsterUI Experiment",
        layout,
        create_splash_screen() if show_splash else "",
        style="""
        <style>
            .sidebar {
                width: 200px;
                background-color: #f0f0f0;
                padding: 10px;
                position: fixed;
                top: 50px;
                left: -200px; /* Initially hidden */
                transition: left 0.3s ease;
                height: 100%;
                overflow-y: auto;
            }

            .sidebar.open {
                left: 0; /* Slide in when open class is added */
            }

            #splash-modal {
                display: """
        + ("block" if show_splash else "none")
        + """; /* Control initial splash screen visibility */
            }
        </style>
        """,
        script="""
        function dismissSplash() {
            document.getElementById('splash-modal').style.display = 'none';
            fetch('/dismiss_splash');
        }
        function toggleSidebar() {
            var sidebar = document.getElementById('app-sidebar');
            sidebar.classList.toggle('open');
            fetch('/toggle_sidebar');
        }
        """,
    )


@rt
def page1():
    return Titled(
        "Page 1",
        Container(
            create_navbar(), Card(H1("Page 1"), P("This is the content of Page 1."))
        ),
    )


@rt
def page2():
    return Titled(
        "Page 2",
        Container(
            create_navbar(), Card(H1("Page 2"), P("This is the content of Page 2."))
        ),
    )


@rt
def dismiss_splash():
    global show_splash
    show_splash = False
    return "OK"


@rt
def toggle_sidebar():
    global show_sidebar
    show_sidebar = not show_sidebar
    return "OK"


serve()

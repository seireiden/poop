from splashgen import launch
from splashgen.components import SplashSite, CTAButton, Form, TextInput, EmailInput, SelectInput

site = SplashSite(title="poop", logo="logo.png", theme="dark")
site.headline = "poop effortlessly, and beautifully"
site.subtext = """
In less than 20 lines of python, create clean and beautiful poop. You can add farts as well, and yes, it is stress-free.
"""
site.call_to_action = CTAButton(
    "https://github.com/thenerdsuperuser", "Poop on GitHub")


inputs = [
        TextInput(id="name", label="Name", required=True,
            placeholder="First and Last"),
        EmailInput(id="email", label="Email address", required=True),
        SelectInput(id="role", label="Role", options=[
            ("Student", "exec"),
            "Engineer",
            "Other"
            ])
        ]
site.call_to_action = Form(endpoint="http://postman-echo.com/post",
        inputs=inputs,
        submit_text="Get Started")

launch(site)


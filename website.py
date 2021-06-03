from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="poop", logo="logo.png", theme="dark")
site.headline = "poop effortlessly, and beautifully"
site.subtext = """
In less than 20 lines of python, create clean and beautiful poop. You can add farts as well, and yes, it is stress-free.
"""
site.call_to_action = CTAButton(
    "https://github.com/thenerdsuperuser", "Poop on GitHub")

launch(site)

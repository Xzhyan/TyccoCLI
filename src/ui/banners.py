# constants
from core import settings

# ui
from .ui_cli import Colors


class Banners:
    TOOL_LOGO = f"""          {Colors.UI_ONE}████████╗██╗   ██╗ ██████╗ ██████╗ ██████╗ {Colors.UI_TWO} ██████╗██╗     ██╗
          {Colors.UI_ONE}╚══██╔══╝╚██╗ ██╔╝██╔════╝██╔════╝██╔═══██╗{Colors.UI_TWO}██╔════╝██║     ██║
          {Colors.UI_ONE}   ██║    ╚████╔╝ ██║     ██║     ██║   ██║{Colors.UI_TWO}██║     ██║     ██║
          {Colors.UI_ONE}   ██║     ╚██╔╝  ██║     ██║     ██║   ██║{Colors.UI_TWO}██║     ██║     ██║
          {Colors.UI_ONE}   ██║      ██║   ╚██████╗╚██████╗╚██████╔╝{Colors.UI_TWO}╚██████╗███████╗██║
          {Colors.UI_ONE}   ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ {Colors.UI_TWO} ╚═════╝╚══════╝╚═╝
                        {Colors.TEXT_ONE}Developed by {Colors.TEXT_TWO}{settings.AUTHOR} {Colors.TEXT_ONE}- version: {Colors.TEXT_TWO}{settings.VERSION}"""

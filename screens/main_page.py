'''This is a page for viewing all exercise records. '''
import flet as ft
from util.globals import root_page

class MainPage(ft.View):
    '''A Widget for viewing exercise records'''
    def __add_record__(self, event = None):
            self.root_page.route = "/bike_new"
            self.root_page.go("/bike_new")

    def __init__(self, root_page:ft.Page, *args, **kwargs):
        self.root_page = root_page
        super().__init__(
            "/",
            appbar = ft.AppBar(
                title = ft.Text("Exercise Records"),
                actions = [
                    ft.IconButton(
                        ft.icons.ADD,
                        on_click = self.__add_record__
                    )
                ]
            ),
            controls = [
                ft.Text(
                    "Hello Main Page.",
                    expand = True,
                    text_align = ft.TextAlign.CENTER,
                    style = ft.TextStyle(color = ft.colors.WHITE),
                ),
            ],
        )


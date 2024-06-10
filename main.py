import flet as ft
from screens.main_page import MainPage
from util.globals import root_page

def main(page: ft.Page):
   
    def route_change(route):
        page.views.clear() # this clears all the views, so any press of back will go to the root regardless of depth. Removing it causes duplicate views though.
        page.views.append(MainPage(root_page = page))

        if page.route == "/bike_new":
            page.views.append(
                ft.View(
                    "/bike_new", 
                    [
                        ft.AppBar(title = ft.Text("Add New Bike Record"),),
                        ft.TextButton(text = "Test", on_click = lambda _: page.go("/layer2"))
                    ]
                )
            )
        if page.route == "/layer2":
            page.views.append(
                ft.View(
                    "/layer2",
                    [
                        ft.AppBar(title = ft.Text("Layer2"))
                    ]
                )
            )

        page.update()

    def view_pop(event):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    def go_new(type: str):
        if type == "biking":
            page.route = "new_biking"
            page.go(page.route)
        else:
            pass

    page.pubsub.subscribe_topic("go_new", go_new)

ft.app(main)

import flet as ft

#Landing class


def main(page: ft.Page)->None:
    page.add(
        ft.SafeArea(
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Divider(height=10,
                                color="transparent"),
                                ft.Container(
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            #Landing
                                            ft.Container(
                                                #form
                                            ),

                                        ]
                                    )
                                ),
                            ]
                            )
                    )
                ],
                expand=True,

            )
        )
    )

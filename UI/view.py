import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.anno=None
        self.brand=None
        self.retailer=None
        self.btn_topvendite=None
        self.btn_analizzavendite=None
        self.txt_result = None
        self.txt_container = None
        self.tendinaretail=None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.anno=ft.Dropdown(width=200,label='anno',hint_text='inserire anno')
        self.brand = ft.Dropdown(width=200,label='brand',hint_text='inserire brand')
        self.retailer =ft.Dropdown(width=500,label='retailer',hint_text='inserire venditore')

        self.fillanno()
        self.fillbrand()
        self.fillretailer()



        r1= ft.Row([self.anno,self.brand,self.retailer],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(r1)

        self.btn_topvendite=ft.ElevatedButton(text='top vendite',on_click=self._controller.topvendite,width=200)
        self.btn_analizzavendite=ft.ElevatedButton(text='analizza vendite',on_click=self._controller.analizzavendite,width=200)

        r2=ft.Row([self.btn_topvendite,self.btn_analizzavendite],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(r2)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fillanno(self):
        self.anno.options.append(ft.dropdown.Option('Nessun filtro'))
        date = self._controller.getdate()
        for i in date:
            self.anno.options.append(ft.dropdown.Option(i))

    def fillbrand(self):
        self.brand.options.append(ft.dropdown.Option('Nessun filtro'))
        brand = self._controller.getbrand()
        for i in brand:
            self.brand.options.append(ft.dropdown.Option(i))

    def fillretailer(self):
        self.retailer.options.append(ft.dropdown.Option('Nessun filtro'))
        r = self._controller.getretails()
        for i in r:
            self.retailer.options.append(ft.dropdown.Option(key=i.cod, text=i.name,data=i, on_click=self.read_retailer))

    def read_retailer(self,e):
        retailer = e.control.data
        self.tendinaretail=retailer

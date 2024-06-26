import flet as ft
import database.DAO as d


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.dd=d.DAO()

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def topvendite(self,e):
        vendite = self._model.venditedecr
        fine=[]
        anno = self._view.anno.value
        brand = self._view.brand.value
        ret= self._view.retailer.value
        if anno is None:
            self._view.create_alert("Inserire l' anno")
            return
        if brand is None:
            self._view.create_alert("Inserire il brand")
            return
        if ret is None:
            self._view.create_alert("Inserire il retail")
            return
        if anno =='Nessun filtro' and brand =='Nessun filtro' and ret =='Nessun filtro':
            for i in range(0,5):
                self._view.txt_result.controls.append(ft.Text(vendite[i]))
            self._view.update_page()
        if anno == 'Nessun filtro' and brand == 'Nessun filtro' and ret !='Nessun filtro':
            fine=self._model.take(None,None,self._view.tendinaretail.cod)
            if len(fine)>=5:
                for i in range(0,5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()
        if anno != 'Nessun filtro' and brand == 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(anno, None, None)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()
        if anno == 'Nessun filtro' and brand != 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(None, brand, None)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()
        if anno != 'Nessun filtro' and brand != 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(anno, brand, None)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()
        if anno != 'Nessun filtro' and brand == 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(anno, None, ret)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()
        if anno == 'Nessun filtro' and brand != 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(None, brand, ret)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine) > 0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile', color='red', size=24))
                self._view.update_page()
        if anno != 'Nessun filtro' and brand != 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(anno, brand, ret)
            if len(fine) >= 5:
                for i in range(0, 5):
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            elif len(fine)>0:
                for i in fine:
                    self._view.txt_result.controls.append(ft.Text(fine[i]))
                self._view.update_page()
            else:
                self._view.txt_result.controls.append(ft.Text('Nessun dato disponibile',color='red',size=24))
                self._view.update_page()


    def analizzavendite(self,e):
        vendite = self._model.venditedecr
        fine = []
        anno = self._view.anno.value
        brand = self._view.brand.value
        ret = self._view.retailer.value
        if anno is None:
            self._view.create_alert("Inserire l' anno")
            return
        if brand is None:
            self._view.create_alert("Inserire il brand")
            return
        if ret is None:
            self._view.create_alert("Inserire il retail")
            return
        if anno =='Nessun filtro' and brand =='Nessun filtro' and ret =='Nessun filtro':
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(vendite)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(vendite)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero retails coinvolti: {self._model.contaretails(vendite)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(vendite)}'))
            self._view.update_page()
        if anno == 'Nessun filtro' and brand == 'Nessun filtro' and ret !='Nessun filtro':
            fine=self._model.take(None,None,self._view.tendinaretail.cod)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno != 'Nessun filtro' and brand == 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(anno, None, None)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno == 'Nessun filtro' and brand != 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(None, brand, None)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno != 'Nessun filtro' and brand != 'Nessun filtro' and ret == 'Nessun filtro':
            fine = self._model.take(anno, brand, None)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno != 'Nessun filtro' and brand == 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(anno, None, ret)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno == 'Nessun filtro' and brand != 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(None, brand, ret)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()
        if anno != 'Nessun filtro' and brand != 'Nessun filtro' and ret != 'Nessun filtro':
            fine = self._model.take(anno, brand, ret)
            self._view.txt_result.controls.append(ft.Text(f'Statistiche vendita:'))
            self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {self._model.solditot(fine)}'))
            self._view.txt_result.controls.append(ft.Text(f'numero vendite: {len(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero retails coinvolti: {self._model.contaretails(fine)}'))
            self._view.txt_result.controls.append(
                ft.Text(f'numero prodotti coinvolti: {self._model.contaprodotti(fine)}'))
            self._view.update_page()









    def getdate(self):
        return self.dd.anni()

    def getbrand(self):
        return self.dd.prodotti()

    def getretails(self):
        return self.dd.retails()
class Pojazd:

    def __init__(self,marka,model,rocznik,poj,przebieg,cena):
        self._marka = marka
        self._model = model
        self._rocznik = rocznik
        self._poj = poj
        self._przebieg = przebieg
        self._cena = cena

    @property
    def marka(self):
        return self._marka
    @property
    def model(self):
        return self._model
    @property
    def rocznik(self):
        return self._rocznik
    @property
    def poj(self):
        return self._poj
    @property
    def przebieg(self):
        return self._przebieg
    @property
    def cena(self):
        return self._cena

    @marka.setter
    def marka(self,marka):
        self._marka = marka
    @model.setter
    def model(self, model):
        self._model = model
    @rocznik.setter
    def rocznik(self, rocznik):
        self._rocznik = rocznik
    @poj.setter
    def poj(self, poj):
        self._poj = poj
    @przebieg.setter
    def przebieg(self, przebieg):
        self._przebieg = przebieg
    @cena.setter
    def cena(self, cena):
        self._cena = cena

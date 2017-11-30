#-*- coding:latin -*-

from wx import *
import json

texte=json.loads(open('biblex.json').read(), 'utf')
livres=texte.keys()

class Fenetre(Frame):

        def __init__(self, *args, **kwargs):
                Frame.__init__(self, *args, **kwargs)
                self.SetTitle('Biblex')
                self.SetSize(500,400)
                self.InitUI()
                self.feuille=""
                self.livre_liste.SetSelection(0)
                self.SetFeuille()
                self.Show(True)

        def SetFeuille(self):
                livre=self.livre_liste.GetString(self.livre_liste.GetSelection())
                self.chap.SetMax(len(texte[livre].keys()))
                chapitre=str(self.chap.GetValue())
                self.feuille=""

                for verset, txt in texte[livre][chapitre].items():
                        self.feuille += u'{0}-{1} '.format(verset, txt)
                self.lab.SetValue(self.feuille)

        def OnLivreSelect(self, e):
                livre=self.livre_liste.GetString(self.livre_liste.GetSelection())
                chapitre=str(self.chap.GetValue())
                self.feuille=""

                for verset, txt in texte[livre][chapitre].items():
                        self.feuille += '{0}-{1}\n'.format(verset, txt)
                self.lab.SetValue(self.feuille)

        def OnChapSet(self, e):
                self.SetFeuille()

        def InitUI(self):
                panel=Panel(self)
                box=BoxSizer(VERTICAL)

                rbox=BoxSizer(HORIZONTAL)
                self.livre_liste=Choice(panel, choices=livres)
                rbox.Add(self.livre_liste, 1, EXPAND, 10)
                self.chap=SpinCtrl(panel, ID_ANY, EmptyString, DefaultPosition, DefaultSize, SP_ARROW_KEYS, 1, 10, 1)
                self.chap.Bind(EVT_SPINCTRL, self.OnChapSet)
                rbox.Add(self.chap, 1, EXPAND, 20)
                box.Add(rbox, 0, EXPAND)

                self.livre_liste.Bind(EVT_COMBOBOX, self.OnLivreSelect)

                lbox=BoxSizer(VERTICAL)
                self.lab=TextCtrl(panel, style=TE_MULTILINE|TE_READONLY)
                lbox.Add(self.lab, 1, EXPAND|ALL)
                box.Add(lbox, 1, EXPAND)

                panel.SetSizer(box)


if __name__ == '__main__':
        app=App()
        Fenetre(None)
        app.MainLoop()

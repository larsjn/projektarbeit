# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import random
from IPython.display import display
from IPython.display import clear_output
from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Box
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import Button
from ipywidgets import Text
from ipywidgets import FloatText
from ipywidgets import Tab
from ipywidgets import ColorPicker
from ipywidgets import Checkbox
from ipywidgets import BoundedFloatText

# Hinweise:
#   - übergabe Parameter wurden mit einem A vor dem Namen gekennzeichnet
#   - def übergreifende Variablen wurden zunächst alle in der Init vor definiert
#            o  def übergreifende Variablen wurden mit einem F vor dem Namen gekennzeichnet
#   - Texte die angezeigt werden wurden in der Init definiert und mit RS_ gekennzeichnet
#            o  wenn Widget im Init definiert wurde ggf. der String direkt im Widget definiert

class Class_Plot_Menu (object):

    def __init__(self, ASignal, AToPlot=None, AtxtLegende=None):

    # =============================================== verwendete Texte ===============================================
        self.RS_Ploteinstellungen       = 'Diagrammeinstellungen'
        self.RS_X_Aches_Einstellungen   = 'X-Achsen-Einstellungen'
        self.RS_Y_Aches_Einstellungen   = 'Y-Achsen-Einstellungen'
        self.RS_Signal                  = 'Signal: '
        self.RS_Linie                   = 'Linie: '
        self.RS_Diagrammtitel           = 'Diagrammtitel'
        self.RS_x_Achse_Titel           = 'X Achsentitel'
        self.RS_y_Achse_Titel           = 'Y Achsentitel'
        self.RS_Abtastfrequenz          = 'Abtastfrequenz'
        self.RS_Linien_Staerke          = 'Linienstärke'
        self.RS_Marker_Groeße           = 'Markergröße'
        self.RS_Baseline_Staerke        = 'Baseline-Stärke'
        self.RS_Linien_Farbe            = 'Linienfarbe'
        self.RS_Marker_Farbe            = 'Markerfarbe'
        self.RS_Baseline_Farbe          = 'Baselinefarbe'
        self.RS_x_Min                   = 'x Minimum'
        self.RS_x_Max                   = 'x Maximum'
        self.RS_y_Min                   = 'y Minimum'
        self.RS_y_Max                   = 'y Maximum'
        self.RS_Plot                    = 'Diagramm anzeigen'
        self.RS_Clear                   = 'Diagramme löschen'
        self.RS_Show_Grid               = 'Grid anzeigen'
        self.RS_Linienname              = 'Linienname für Legende'
        self.RS_Legende_anzeigen        = 'Legende anzeigen'
        self.RS_Show_Line               = 'Linie anzeigen'
        self.RS_Polarplot               = 'In Polarform anzeigen'
        self.RS_FigSize_X               = 'Ausgabegröße X'
        self.RS_FigSize_Y               = 'Ausgabegröße Y'
        self.RS_Hinweis_Polar           = 'Signal B ist im Polarplot für "add" und "sub" nicht unterstützt --> Im Menu ausblenden '

    # =============================================== def übergreifende Variablen ===============================================
        self.FSignal            = ASignal
        self.FPolar             = False
        self.Ftxt_Linetitle     = []
        self.FCol_Line          = []
        self.FFloat_Linewidth   = []
        self.Fbol_Show_Line     = []

        # Prüft ob ein anderes Signal als das übergabe-Signal geplottet werden soll (z.B. bei komplexen Zaheln)
        # Wenn nicht dann ist das übergabe-Signal auch das zu plottende
        if AToPlot == None:
            self.FToPlot = ASignal
        else:
            self.FToPlot = AToPlot


        # Wenn Legende mit übergeben dann diese verwenden (bei komplexen Zahlen)
        if AtxtLegende != None:
            # Wenn es weniger oder mehr Legenden als Signale gibt keine Legende
            # übernehmen
            if len(AtxtLegende) == len(self.FToPlot):
                self.FDefaultLegend = AtxtLegende
            else:
                self.FDefaultLegend = None
        else:
            self.FDefaultLegend = None

    # =============================================== def übergreifende Widgets  ===============================================
        # Layouteinstellungen der Widgets
        self.F_wdg_Layout       = Layout(display='flex', flex_flow='row', justify_content='center')
        self.F_wdg_Box_Layout   = Layout(display='flex', flex_flow='column', align_items='stretch', width='100%')

        # Allgemeine Diagrammeinstellungen
        self.Ftxt_Diagrammtitle     = Text(layout=self.F_wdg_Layout, visible=True)
        self.FFloat_Baselinewidth   = FloatText(layout=self.F_wdg_Layout, value=2, disabled=False)
        self.FFloat_Markersize      = FloatText(layout=self.F_wdg_Layout, value=0.5, disabled=False)
        self.FCol_Marker            = ColorPicker(concise=False, value='blue')
        self.FCol_Baseline          = ColorPicker(concise=False, value='blue')
        self.Fbol_Show_Grid         = Checkbox(value=False,disabled=False)
        self.Fbol_Show_Legende      = Checkbox(value=False,disabled=False)
        self.Fbol_Polar             = Checkbox(value=False,disabled=False)
        self.FFloat_FigSize_X       = BoundedFloatText(layout=self.F_wdg_Layout, value=10, disabled=False, min=1, max=20.0)
        self.FFloat_FigSize_Y       = BoundedFloatText(layout=self.F_wdg_Layout, value=5, disabled=False, min=1, max=20.0)
        self.FFloat_Abtastfrequenz  = FloatText(layout=self.F_wdg_Layout, value=50, disabled=False)

        # X Achseneinstellungen
        self.Ftxt_x_Achse_Titel = Text(layout=self.F_wdg_Layout, visible=True)
        self.FFloat_x_Min       = FloatText(layout=self.F_wdg_Layout, value=-10, disabled=False)
        self.FFloat_x_Max       = FloatText(layout=self.F_wdg_Layout, value=10, disabled=False)
        self.FBoxXAchseItems    = []
        self.FBoxXAchse         = None

        # Y Achseneinstellungen
        self.Ftxt_y_Achse_Titel = Text(layout=self.F_wdg_Layout, visible=True)
        self.FFloat_y_Min       = FloatText(layout=self.F_wdg_Layout, value=-10, disabled=False)
        self.FFloat_y_Max       = FloatText(layout=self.F_wdg_Layout, value=10, disabled=False)
        self.FBoxYAchseItems    = []
        self.FBoxYAchse         = None

        # Diagramm anzeigen
        self.Fbtn_plot       = Button(layout=self.F_wdg_Layout,button_style='warning', description=self.RS_Plot)
        self.Fbtn_clear      = Button(layout=self.F_wdg_Layout, button_style='warning', description=self.RS_Clear)
        self.FBoxDoPlotItems = []
        self.FBoxDoPlot      = None
        # Accordion das alle Einstellungen anzeigt
        self.FAccItems = []
        self.FAcc      = None

    # =============================================== nach init auszuführende def  ===============================================
        # Zusammensetzen der Widgets
        self.show()
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Sperrt die Einstellungen die nicht im Polarplot möglich sind
    def bol_Event_Polar_Changed(self, ADummy):
        self.FPolar                     = self.Fbol_Polar.value
        self.FFloat_x_Min.disabled      = self.Fbol_Polar.value
        self.FFloat_x_Max.disabled      = self.Fbol_Polar.value
        self.FFloat_y_Min.disabled      = self.Fbol_Polar.value
        self.FFloat_y_Max.disabled      = self.Fbol_Polar.value
        self.Fbol_Show_Legende.disabled = self.Fbol_Polar.value
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Kopieren der Diagrammeinstellungen die bei jedem Plot gemacht werden müssen
    def Copy_Input(self):
        plt.title(self.Ftxt_Diagrammtitle.value)
        plt.xlabel(self.Ftxt_x_Achse_Titel.value)
        plt.ylabel(self.Ftxt_y_Achse_Titel.value)
        plt.grid(self.Fbol_Show_Grid.value)

        if not self.FPolar:
            plt.ylim([self.FFloat_y_Min.value, self.FFloat_y_Max.value])
            plt.xlim([self.FFloat_x_Min.value, self.FFloat_x_Max.value])
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Erzeugen des Diagrammes je nach Siganal-Typ
    def btn_Event_show_plot(self, ADummy):
        # Einstellen der Ausgabegröße
        plt.figure(figsize=(self.FFloat_FigSize_X.value,self.FFloat_FigSize_Y.value))

        # IF die unterscheidet welcher Signaltyp vorhanden ist
        if self.FSignal.FTyp == self.FSignal.RS_Typ_discrete:

            # Plotten des diskreten Signals
            xValues = np.arange(self.FFloat_x_Min.value,
                                self.FFloat_x_Max.value,
                                1 / self.FFloat_Abtastfrequenz.value)

            yValues = self.FSignal.getList(xValues)

            # Wenn aus Datei eingelesen diese Werte nehmen; Bis jetzt nur Ansatz daher erst mal auskommentiert
            #if yValues[0] == False:
            #    xValues = yValues[1][0]
            #    yValues = yValues[2][0]

            # Plotten mit der Matplotlib und diverse Einstellungen übernehmen
            markerline, stemlines, baseline = plt.stem(xValues, yValues, '-.')

            plt.setp(markerline, linewidth=self.FFloat_Markersize.value,
                     color=self.FCol_Marker.value)
            plt.setp(stemlines, linewidth=self.FFloat_Linewidth.value,
                     color=self.FCol_Line.value)
            plt.setp(baseline, linewidth=self.FFloat_Baselinewidth.value,
                     color=self.FCol_Baseline.value)

            self.Copy_Input()  # Kopieren der Diagrammeinstellungen die bei jeden Plot gemacht werden müssen

            plt.show()

        elif self.FSignal.FTyp == self.FSignal.RS_Typ_continuous:

            # Plotten des kontinuierlichen Signals
            xValues = np.arange(self.FFloat_x_Min.value,
                                self.FFloat_x_Max.value,
                                1 / self.FFloat_Abtastfrequenz.value)
            yValues = self.FSignal.getList(xValues)

            # Plotten mit der Matplotlib und diverse Einstellungen übernehmen
            plt.title(self.Ftxt_Diagrammtitle.value)
            plt.xlabel(self.Ftxt_x_Achse_Titel.value)
            plt.ylabel(self.Ftxt_y_Achse_Titel.value)
            plt.grid(self.Fbol_Show_Grid.value)
            plt.plot(xValues, yValues, linewidth=self.FFloat_Linewidth.value,
                     color=self.FCol_Line.value,)

            plt.show()

        elif self.FSignal.FTyp == self.FSignal.RS_Typ_complex:
            # Plotten des komplexen Signals
            # Wenn NICHT Polarplot gewählt dann Zeigerdiagramm erstellen, sonst Polarplot
            if not self.FPolar:
                # Wenn eine Liste von Zeigern übergeben wurde dann diese Plotten, sonst einfacher Zeiger
                if isinstance(self.FToPlot, (list)):
                    # Init der Listen zum Plotten
                    ReStart = []
                    ReEnd   = []
                    ImStart = []
                    ImEnd   = []
                    ar      = []
                    leg     = []

                    # Übergebende Liste auswerten und in neuen Listen zusammen setzen
                    for i in range(0, len(self.FToPlot)):
                        ReStart = ReStart + [self.FToPlot[i][0].real]
                        ReEnd   = ReEnd + [self.FToPlot[i][1].real]
                        ImStart = ImStart + [self.FToPlot[i][0].imag]
                        ImEnd   = ImEnd + [self.FToPlot[i][1].imag]

                    # Plott für jeden Pfeil in der Liste ausführen
                    for i in range(0, len(ReStart)):
                        if self.Fbol_Show_Line[i].value:
                            # Plotts merken für Legende
                            ar = ar + [plt.arrow(ReStart[i],  # x1
                                                 ImStart[i],  # y1
                                                 ReEnd[i] - ReStart[i],# x2 - x1
                                                 ImEnd[i] - ImStart[i], # y2 - y1
                                                 linewidth=self.FFloat_Linewidth[i].value,
                                                 color=self.FCol_Line[i].value,
                                                 head_width=self.FFloat_Markersize.value / 2,
                                                 head_length=self.FFloat_Markersize.value,
                                                 length_includes_head=True
                                                 )]
                            # Legenden Beschriftung erstellen
                            leg = leg + [self.Ftxt_Linetitle[i].value]
                    # Wenn Legende anzeigen, dann diese erstellen
                    if self.Fbol_Show_Legende.value:
                        plt.legend(ar, leg)

                # Wenn keine Liste übergeben nur einen Pfeil anzeigen
                else:

                    ReEnd = self.FToPlot.getZ(True).real
                    ImEnd = self.FToPlot.getZ(True).imag

                    plt.arrow(0, 0, ReEnd, ImEnd,
                              linewidth=self.FFloat_Linewidth.value,
                              color=self.FCol_Line.value,
                              head_width=self.FFloat_Markersize.value / 2,
                              head_length=self.FFloat_Markersize.value,
                              length_includes_head=True
                              )
            # Wenn Polarplot gewählt dann diesen anzeigen
            else:
                # Wenn eine Liste von Zeigern übergeben wurde dann diese Plotten, sonst einfacher Zeiger
                if isinstance(self.FToPlot, (list)):
                    # Init der Listen zum Plotten
                    thetaStart  = []
                    thetaEnd    = []
                    rStart      = []
                    rEnd        = []
                    ar          = []
                    leg         = []

                    # Übergebende Liste auswerten und in neuen Listen zusammen setzen
                    for i in range(0, len(self.FToPlot)):
                        thetaStart  = thetaStart + [np.angle(self.FToPlot[i][0], False)]
                        thetaEnd    = thetaEnd + [np.angle(self.FToPlot[i][1], False)]
                        rStart      = rStart + [np.absolute(self.FToPlot[i][0])]
                        rEnd        = rEnd + [np.absolute(self.FToPlot[i][1])]

                    # Plott für jeden Pfeil in der Liste ausführen
                    for i in range(0, len(thetaStart)):
                        if self.Fbol_Show_Line[i].value:
                            ar = ar + [plt.polar([thetaStart[i], thetaEnd[i]],
                                                 [rStart[i], rEnd[i]],
                                                 linewidth=self.FFloat_Linewidth[i].value,
                                                 color=self.FCol_Line[i].value,
                                                 marker='o',
                                                 markersize=self.FFloat_Markersize.value,
                                                 markerfacecoloralt=self.FCol_Marker.value
                                                 )]
                # Wenn keine Liste übergeben nur einen Pfeil anzeigen
                else:
                    thetaEnd = self.FToPlot.getAngle(False)
                    rEnd     = self.FToPlot.getAbs()
                    plt.polar([0, thetaEnd], [0, rEnd],
                              linewidth=self.FFloat_Linewidth.value,
                              color=self.FCol_Line.value,
                              marker='o',
                              markersize=self.FFloat_Markersize.value,
                              markerfacecoloralt=self.FCol_Marker.value
                              )
                # Hinweise zum Polarplot anzeigen
                print(self.RS_Hinweis_Polar)

            self.Copy_Input() # Kopieren der Diagrammeinstellungen die bei jedem Plot gemacht werden müssen
            plt.show()

        return None  # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF -----------------------------------------------

    # Alte Diagramme wieder löschen
    def btn_Event_clear(self, ADummy):
        clear_output()
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Anzeigen der Diagrammeinstellungen, werden je nach Signaltyp zusammengesetzt
    def show(self):

        # Zuweisen der Widgetevents
        self.Fbtn_plot.on_click(self.btn_Event_show_plot)
        self.Fbtn_clear.on_click(self.btn_Event_clear)
        self.Fbol_Polar.observe(self.bol_Event_Polar_Changed)

        # Wenn eine Liste übergeben wurde entsprechende Widgets einbinden  (Linieneinstellungen usw.)
        if isinstance(self.FToPlot, (list)):
            # Init der Listen
            self.FCol_Line          = []
            self.FFloat_Linewidth   = []
            self.Ftxt_Linetitle     = []
            self.FTabLineSetUpItems = []
            self.Fbol_Show_Line     = []
            self.FTabLineSetUp      = Tab(children=self.FTabLineSetUpItems)
            # Zufällige Farbe erzeugen, damit nicht alle Linien die gleiche Farbe haben
            r = lambda: random.randint(0, 255)
            # Für jede Linie eigene Einstellungen erstellen
            for i in range(0, len(self.FToPlot)):

                # Beschriftungen
                subHBox_1_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Farbe, disabled=True, visible=True),
                                   Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Staerke, disabled=True, visible=True)
                                   ]

                subHBox_1 = HBox(children=subHBox_1_items)

                # Widgets zur Linien-Einstellung in Liste speichern, um diese Später einfacher zu verwenden
                self.FCol_Line        = self.FCol_Line + [ ColorPicker(concise=False, value='#%02X%02X%02X' % (r(), r(), r()))]
                self.FFloat_Linewidth = self.FFloat_Linewidth + [FloatText(layout=self.F_wdg_Layout, value=1, disabled=False)]
                self.Fbol_Show_Line   = self.Fbol_Show_Line + [Checkbox(value=True,    disabled=False)]

                # Wenn Legende übergeben wurde diese Texte automatisch eintragen
                if self.FDefaultLegend  != None:
                    self.Ftxt_Linetitle = self.Ftxt_Linetitle + [Text(layout=self.F_wdg_Layout,value=self.FDefaultLegend[i], visible=True)]
                else:
                    self.Ftxt_Linetitle = self.Ftxt_Linetitle + [Text(layout=self.F_wdg_Layout,value=self.RS_Signal + str(i + 1), visible=True)]

                subHBox_2_items = [self.FCol_Line[i], self.FFloat_Linewidth[i]]
                subHBox_2       = HBox(children=subHBox_2_items)

                # Alle Sub Boxen sammeln und in ein Tabfenster speichern, pro Linie ein Tabfenster
                subTabItems = [Text(layout=self.F_wdg_Layout, value=self.RS_Show_Line, disabled=True),
                               self.Fbol_Show_Line[i],
                               Text(layout=self.F_wdg_Layout,
                                    value=self.RS_Linienname, disabled=True),
                               self.Ftxt_Linetitle[i],
                               subHBox_1,
                               subHBox_2, ]
                subTab = Box(children=subTabItems)

                # Aktuelles Tabfenster zur Anzeigeliste hinzufügen
                self.FTabLineSetUpItems = self.FTabLineSetUpItems + [subTab]
                self.FTabLineSetUp.set_title(i, self.RS_Linie + str(i + 1))

            # Wenn alle Tabs für jede Linie erzeugt wurden diese als Tab anzeigen
            self.FTabLineSetUp.children = self.FTabLineSetUpItems
        # Wenn nur eine Linie übergeben dann nur diese Anzeigen, ohne Legende usw.
        else:

            self.FCol_Line = ColorPicker(concise=False, value='blue')
            self.FFloat_Linewidth = FloatText(layout=self.F_wdg_Layout, value=1, disabled=False)

            subHBox_1_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Farbe, disabled=True, visible=True),
                               Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Staerke, disabled=True, visible=True)
                               ]

            subHBox_1 = HBox(children=subHBox_1_items)

            subHBox_2_items = [self.FCol_Line,
                               self.FFloat_Linewidth
                               ]
            subHBox_2 = HBox(children=subHBox_2_items)

        if self.FSignal.FTyp == self.FSignal.RS_Typ_discrete:
        # Wenn diskretes Signal zusätzlich Linien der Punkte, und Baseline und Marker Einstellungen anzeigen
            subHBox_3_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Marker_Farbe, disabled=True, visible=True),
                               Text(
                                   layout=self.F_wdg_Layout, value=self.RS_Marker_Groeße, disabled=True, visible=True)
                               ]
            subHBox_3 = HBox(children=subHBox_3_items)

            subHBox_4_items = [self.FCol_Marker, self.FFloat_Markersize]
            subHBox_4 = HBox(children=subHBox_4_items)

            subHBox_5_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Baseline_Farbe, disabled=True, visible=True),
                               Text(
                                   layout=self.F_wdg_Layout, value=self.RS_Baseline_Staerke, disabled=True, visible=True),

                               ]
            subHBox_5 = HBox(children=subHBox_5_items)

            subHBox_6_items = [self.FCol_Baseline,
                               self.FFloat_Baselinewidth
                               ]
            subHBox_6 = HBox(children=subHBox_6_items)

            self.FBoxAllgemeinItems = [Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel, disabled=True, visible=True),
                                       self.Ftxt_Diagrammtitle,
                                       subHBox_1,
                                       subHBox_2,
                                       subHBox_3,
                                       subHBox_4,
                                       subHBox_5,
                                       subHBox_6,
                                       Text(
                                           layout=self.F_wdg_Layout, value=self.RS_Show_Grid, disabled=True, visible=True),
                                       self.Fbol_Show_Grid,
                                       Text(
                                       layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True),
                                       self.FFloat_Abtastfrequenz,
                                      ]
# Für Plotten mehrere Linien, immoment nicht verwendet
#            if isinstance(self.FToPlot, (list)):
#
#                self.FBoxAllgemeinItems = [ Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel,disabled=True, visible = True),
#                                            self.Ftxt_Diagrammtitle,
#                                            self.FTabLineSetUp,
#                                            subHBox_3,
#                                            subHBox_4,
#                                            subHBox_5,
#                                            subHBox_6,
#                                            Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid,disabled=True, visible = True),
#                                            self.Fbol_Show_Grid,
#                                            Text(layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True),
#                                            self.FFloat_Abtastfrequenz,
#                                            Text(layout=self.F_wdg_Layout, value=self.RS_Legende_anzeigen,disabled=True, visible = True),
#                                            self.Fbol_Show_Legende,
#                                          ]
#
#            else:
#
#                self.FBoxAllgemeinItems = [ Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel,disabled=True, visible = True),
#                                            self.Ftxt_Diagrammtitle,
#                                            subHBox_1,
#                                            subHBox_2,
#                                            subHBox_3,
#                                            subHBox_4,
#                                            subHBox_5,
#                                            subHBox_6,
#                                            Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid,disabled=True, visible = True),
#                                            self.Fbol_Show_Grid,
#                                            Text(layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True),
#                                            self.FFloat_Abtastfrequenz,
#
#                                          ]
        elif self.FSignal.FTyp == self.FSignal.RS_Typ_continuous:
        # Wenn kontinuierliches Siganl dieses entsprechend Einstellungen anzeigen

            self.FBoxAllgemeinItems = [Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel, disabled=True, visible=True),
                                       self.Ftxt_Diagrammtitle,
                                       subHBox_1,
                                       subHBox_2,
                                       Text(
                                           layout=self.F_wdg_Layout, value=self.RS_Show_Grid, disabled=True, visible=True),
                                       self.Fbol_Show_Grid,
                                       Text(
                                       layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True),
                                       self.FFloat_Abtastfrequenz,
                                       ]

        elif self.FSignal.FTyp == self.FSignal.RS_Typ_complex:
        # Wenn komplexes Signal zunächst für alle Pfeile geltende Einstellungen erzeugen
            subHBox_3_items = [
                Text(layout=self.F_wdg_Layout, value=self.RS_Marker_Groeße,
                     disabled=True, visible=True)
            ]
            subHBox_3 = HBox(children=subHBox_3_items)

            subHBox_4_items = [
                self.FFloat_Markersize
            ]
            subHBox_4 = HBox(children=subHBox_4_items)
            # Wenn mehrere Pfeile dann entsprechend für jeden Pfeil Einstellungen erzeugen
            if isinstance(self.FToPlot, (list)):
                self.FBoxAllgemeinItems = [Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel, disabled=True, visible=True),
                                           self.Ftxt_Diagrammtitle,
                                           self.FTabLineSetUp,
                                           subHBox_3,
                                           subHBox_4,
                                           Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid, disabled=True, visible=True),
                                           self.Fbol_Show_Grid,
                                           Text(layout=self.F_wdg_Layout, value=self.RS_Legende_anzeigen, disabled=True, visible=True),
                                           self.Fbol_Show_Legende,
                                           Text(layout=self.F_wdg_Layout, value=self.RS_Polarplot, disabled=True, visible=True),
                                           self.Fbol_Polar,
                                           ]

            else: # Wenn nur ein Pfeil, Legende usw. entfallen lassen
                self.FBoxAllgemeinItems = [Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel, disabled=True, visible=True),
                                           self.Ftxt_Diagrammtitle,
                                           subHBox_1,
                                           subHBox_2,
                                           subHBox_3,
                                           subHBox_4,
                                           Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid, disabled=True, visible=True),
                                           self.Fbol_Show_Grid,
                                           Text(layout=self.F_wdg_Layout, value=self.RS_Polarplot, disabled=True, visible=True),
                                           self.Fbol_Polar,
                                           ]

        # Für alle Signaltypen notwendige Einstellungen erzeugen

        # Ausgabegröße
        subHBox_8_items = [
            Text(layout=self.F_wdg_Layout, value=self.RS_FigSize_X, disabled=True, visible=True),
            Text(layout=self.F_wdg_Layout, value=self.RS_FigSize_Y, disabled=True, visible=True)
        ]
        subHBox_8 = HBox(children=subHBox_8_items)


        subHBox_9_items = [self.FFloat_FigSize_X, self.FFloat_FigSize_Y ]
        subHBox_9 = HBox(children=subHBox_9_items)

        self.FBoxAllgemeinItems = self.FBoxAllgemeinItems +  [subHBox_8] + [subHBox_9]

        self.FBoxAllgemein = VBox(children=self.FBoxAllgemeinItems)

        # X-Achsen Einstellungen
        self.FBoxXAchseItems = [Text(layout=self.F_wdg_Layout, value=self.RS_x_Achse_Titel, disabled=True, visible=True),
                                self.Ftxt_x_Achse_Titel,
                                Text(
            layout=self.F_wdg_Layout, value=self.RS_x_Min, disabled=True, visible=True),
            self.FFloat_x_Min,
            Text(
            layout=self.F_wdg_Layout, value=self.RS_x_Max, disabled=True, visible=True),
            self.FFloat_x_Max
        ]

        self.FBoxXAchse = VBox(children=self.FBoxXAchseItems)

        # Y-Achsen Einstellungen
        self.FBoxYAchseItems = [Text(layout=self.F_wdg_Layout, value=self.RS_y_Achse_Titel, disabled=True, visible=True),
                                self.Ftxt_y_Achse_Titel,
                                Text(
            layout=self.F_wdg_Layout, value=self.RS_y_Min, disabled=True, visible=True),
            self.FFloat_y_Min,
            Text(
            layout=self.F_wdg_Layout, value=self.RS_y_Max, disabled=True, visible=True),
            self.FFloat_y_Max
        ]
        self.FBoxYAchse = VBox(children=self.FBoxYAchseItems)

        # Diagramm Anzeigen
        subHBox_7_items = [self.Fbtn_plot, self.Fbtn_clear]
        subHBox_7 = HBox(children=subHBox_7_items)
        self.FBoxDoPlotItems = [subHBox_7]
        self.FBoxDoPlot = VBox(children=self.FBoxDoPlotItems)

        # Alles Einstellungen in Accordion anzeigen
        self.FAccItems = [self.FBoxAllgemein,
                          self.FBoxXAchse, self.FBoxYAchse, self.FBoxDoPlot]

        self.FAcc = Accordion(children=self.FAccItems)

        self.FAcc.set_title(0, self.RS_Ploteinstellungen)
        self.FAcc.set_title(1, self.RS_X_Aches_Einstellungen)
        self.FAcc.set_title(2, self.RS_Y_Aches_Einstellungen)
        self.FAcc.set_title(3, self.RS_Plot)

        # Anzeigen der Widgets für den Nutzer
        display(self.FAcc)
# ----------------------------------------------- ENDE DEF -----------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++

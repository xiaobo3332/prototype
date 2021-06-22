from technologies import silicon_photonics
import ipkiss3.all as i3


class Interface_mmi12(i3.PCell):
    _name_prefix = "INTERFACE_"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.HFW)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=2500)  # shrink
    width = i3.PositiveNumberProperty(default=3000.0 * 0.6)

    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500 + 4000, y0 + 4500 - 1800),
                                  box_size=(6000, 1000 * 0.6))  # change

            # elems += i3.Rectangle(layer=i3.TECH.PPLAYER.NONE.DOC, center=(x0 + 7500, y0 + 4500),
            #                       box_size=(15000, 1000))

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500 + 4000, y0 + 500 - 200),
                                  box_size=(6000, 1000 * 0.6))
            elems += i3.Rectangle(layer=self.layer, center=(x0 + 12500 + 1000 - 250, y0 + 2500 - 1000),  # change
                                  box_size=(self.length, self.width))

            if self.pocket:
                PO = i3.Rectangle(layer=self.layer_bool, center=(10001 + 2000, 2500 - 1000),
                                  box_size=(2, 160))  # change
                elems += PO
                generated1 = self.layer - self.layer_bool
                mapping = {generated1: self.layer}
                elems = i3.get_elements_for_generated_layers(elems, mapping)

            if self.tilt:
                # TI = i3.Rectangle(layer=self.layer_bool, center=(10001, 2500), box_size=(2, 160))
                # elems += TI
                TI_shape = i3.Shape(points=[(10000.0 + 2000, 2470.0 - 1000), (10010.58 + 2000, 2530.0 - 1000),
                                            (10000.0 + 2000, 2530.0 - 1000)], closed=True)  # change
                TI = i3.Boundary(layer=self.layer_bool, shape=TI_shape)
                elems += TI

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)

            return elems


# GDS-file generation for debugging
# Interface_mmi12(pocket= False, tilt=False).Layout.view.write_gdsii("interface1.gds")
# print("Done writing Release.gds!")
# Interface(pocket= True, tilt=False).Layout.view.write_gdsii("interface2.gds")
# print("Done writing Release.gds!")
# Interface(pocket= False, tilt=True).Layout.view.write_gdsii("interface3.gds")
# print("Done writing Release.gds!")
# Interface(pocket= True, tilt=True).Layout.view.write_gdsii("interface4.gds")
# print("Done writing Release.gds!")

class NP_mmi12(i3.PCell):
    _name_prefix = "NP_"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.HFW)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=180)
    width = i3.PositiveNumberProperty(default=79.0)

    pillar = i3.BoolProperty(default=False)
    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)
    double = i3.BoolProperty(default=True)

    # Recess label
    label = i3.StringProperty(default="NP")

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position
            width2 = 338 + 15 + 15
            elems += i3.Rectangle(layer=self.layer, center=(x0 + 6500 + 2000 + 2000, y0 + 600 + (1800 - width2) / 4),
                                  box_size=(3000, (1800 - width2) / 2))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(x0 + 6500 + 2000 + 2000, y0 + 600 + width2 + (1800 - width2) * 3 / 4),
                                  box_size=(3000, (1800 - width2) / 2))

            elems += i3.SRef(reference=Interface_mmi12(pocket=self.pocket, tilt=self.tilt))

            if self.pillar:
                self.label = "NO"
                for i in range(4):
                    elems += i3.Rectangle(layer=self.layer,
                                          center=(
                                              10000 - 725 - i * 750 + 2000 + 550, 1316 + self.width / 2),
                                          box_size=(self.length, self.width))
                    elems += i3.Rectangle(layer=self.layer, center=(
                        10000 - 725 - i * 750 + 2000 + 550, 1684 - self.width / 2),  # change
                                          box_size=(self.length, self.width))
                    if self.double:
                        elems += i3.Rectangle(layer=self.layer,
                                              center=(
                                                  10000 - 725 - i * 750 + 2000 + 550 - 400,
                                                  1316 + self.width / 2),
                                              box_size=(self.length, self.width))
                        elems += i3.Rectangle(layer=self.layer, center=(
                            10000 - 725 - i * 750 + 2000 + 550 - 400, 1684 - self.width / 2),
                                              # change
                                              box_size=(self.length, self.width))
            if self.width > 79:
                self.label += "W"
            if self.pocket:
                self.label += "_WP"
            if self.tilt:
                self.label += "WT"
            elems += i3.PolygonText(layer=self.layer_bool,
                                    text=self.label,

                                    coordinate=(10800, 2600),
                                    # alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
                                    font=2,
                                    height=400.0)

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)
            return elems


# NP(width=330, pocket=True).Layout.view.write_gdsii("NP.gds")


# NP(width=338, pocket=True, tilt=True).Layout.view.write_gdsii("NP.gds")
# NP_mmi12(pillar=True, pocket=True, tilt=True, width=94, length=220,).Layout.view.write_gdsii("NO.gds")


"""

Al mask

"""


class AL_NP(i3.PCell):
    _name_prefix = "AL_NP"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.CONTACT.PILLAR)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    offset = i3.PositiveNumberProperty(default=20)
    # width = i3.PositiveNumberProperty(default=79)

    # pillar = i3.BoolProperty(default=False)
    reservoir = i3.BoolProperty(default=False)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position
            # width2 = 338 + 15 + 15

            elems += i3.Rectangle(layer=self.layer, center=(8750 - 15-10+5, 1500),
                                  box_size=(500 - 40, 1800 - 100))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(10500 - 15-10, 1500),
                                  box_size=(3000 + 50, 145))



            for i in range(4):
                elems += i3.Rectangle(layer=self.layer,
                                      center=(
                                          10000 - 725 - i * 750 + 2000 + 350+self.offset, 1316+72.75),
                                      box_size=(145, 77.5))
                elems += i3.Rectangle(layer=self.layer, center=(
                    10000 - 725 - i * 750 + 2000 + 350+self.offset, 1684-72.75),  # change
                                      box_size=(145, 77.5))

            # Avoid solder spill on facet
            elems += i3.Rectangle(layer=self.layer_bool, center=(12000 - 20, 1500), box_size=(40, 50))
            elems += i3.Rectangle(layer=self.layer_bool, center=(12000 - 750*2, 1500), box_size=(80, 50))
            elems += i3.Rectangle(layer=self.layer_bool, center=(12000 - 750*3, 1500), box_size=(80, 50))
            elems += i3.Rectangle(layer=self.layer_bool, center=(12000 - 750*4, 1500), box_size=(80, 50))

            # reservoir
            if self.reservoir:
                for i in range(3):
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1572.5+20), box_size=(149, 40))
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1427.5 - 20), box_size=(149, 40))
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1572.5 + 20), box_size=(149, 40))
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1427.5 - 20), box_size=(149, 40))
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1572.5 + 20), box_size=(149, 40))
                    elems += i3.Rectangle(layer=self.layer, center=(-750*i+12000 - 750, 1427.5 - 20), box_size=(149, 40))
                elems += i3.PolygonText(layer=self.layer,
                                        text="RE",
                                        coordinate=(12000, 2600),
                                        # alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
                                        font=2,
                                        height=400.0)

            # Markers
            for i in range(-3, 1, 1):
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78, 1568.75), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5, 1572-32), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5-57, 1572-32), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78, 1568.75-57.5), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75, 1572.5-13.25), box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-38.5, 1572.5 - 13.25), box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75, 1572.5 - 13.25-38.5), box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-38.5, 1572.5 - 13.25-38.5), box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78, 1568.75-80), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5, 1572 - 32-80), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5 - 57, 1572 - 32-80), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78, 1568.75 - 57.5-80), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-2.5, 1572.5 - 13.25-80-2.5), box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 - 38.5+2.5, 1572.5 - 13.25-80-2.5),
                                      box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-2.5, 1572.5 - 13.25 - 38.5-80+2.5),
                                      box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 - 38.5+2.5, 1572.5 - 13.25 - 38.5-80+2.5),
                                      box_size=(16.5, 16.5))

                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78-594, 1568.75), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5-594, 1572 - 32), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5 - 57-594, 1572 - 32), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78-594, 1568.75 - 57.5), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-594-2.5, 1572.5 - 13.25-2.5), box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 - 38.5-594+2.5, 1572.5 - 13.25-2.5),
                                      box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75-594-2.5, 1572.5 - 13.25 - 38.5+2.5),
                                      box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 - 38.5-594+2.5, 1572.5 - 13.25 - 38.5+2.5),
                                      box_size=(16.5, 16.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78-594, 1568.75 - 80), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5-594, 1572 - 32 - 80), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 49.5 - 57-594, 1572 - 32 - 80), box_size=(7, 7))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 78-594, 1568.75 - 57.5 - 80), box_size=(7, 7.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 -594, 1572.5 - 13.25 - 80 ),
                                      box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 - 38.5 -594, 1572.5 - 13.25 - 80 ),
                                      box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool, center=(750*i+12000 - 58.75 -594, 1572.5 - 13.25 - 38.5 - 80 ),
                                      box_size=(11.5, 11.5))
                elems += i3.Rectangle(layer=self.layer_bool,
                                      center=(750*i+12000 - 58.75 - 38.5 -594, 1572.5 - 13.25 - 38.5 - 80 ),
                                      box_size=(11.5, 11.5))



            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)
            return elems


# AL_NP(reservoir=True).Layout.view.write_gdsii("AL_NP2.gds")

"""

SiN mask

"""


class SiN_NP(i3.PCell):
    _name_prefix = "SiN_NP"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.SIL.LINE)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=180.0)
    width = i3.PositiveNumberProperty(default=79.0)
    tilt = i3.PositiveNumberProperty(default=10.0)

    pillar = i3.BoolProperty(default=True)
    double = i3.BoolProperty(default=True)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(8750 - 15 - 10 + 5, 1500),
                                  box_size=(500 - 40, 1800 - 100))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(10500 - 15 - 10+self.tilt/2, 1500),
                                  box_size=(3000 + 50+self.tilt, 368-15*2))

            # for i in range(4):
            #     elems += i3.Rectangle(layer=self.layer,
            #                           center=(
            #                               10000 - 725 - i * 750 + 2000 + 350, 1316+72.75),
            #                           box_size=(145, 77.5))
            #     elems += i3.Rectangle(layer=self.layer, center=(
            #         10000 - 725 - i * 750 + 2000 + 350, 1684-72.75),  # change
            #                           box_size=(145, 77.5))

            if self.pillar:
                for i in range(4):
                    elems += i3.Rectangle(layer=self.layer_bool,
                                          center=(
                                              10000 - 725 - i * 750 + 2000 + 550, 1316 + self.width / 2),
                                          box_size=(self.length+30, self.width+30))
                    elems += i3.Rectangle(layer=self.layer_bool, center=(
                        10000 - 725 - i * 750 + 2000 + 550, 1684 - self.width / 2),  # change
                                          box_size=(self.length+30, self.width+30))
                    if self.double:
                        elems += i3.Rectangle(layer=self.layer_bool,
                                              center=(
                                                  10000 - 725 - i * 750 + 2000 + 550 - 400,
                                                  1316 + self.width / 2),
                                              box_size=(self.length+30, self.width+30))
                        elems += i3.Rectangle(layer=self.layer_bool, center=(
                            10000 - 725 - i * 750 + 2000 + 550 - 400, 1684 - self.width / 2),
                                              # change
                                              box_size=(self.length+30, self.width+30))

            # if self.tilt_0:
            #     elems += i3.Rectangle(layer=self.layer,
            #                           center=(x0 + 6500 - 40 + 20 + 7.5, 2500),
            #                           box_size=(self.length + 40 + 15, self.width - 40 * 2))
            # else:
            #     elems += i3.Rectangle(layer=self.layer,
            #                           center=(x0 + 6500 - 40 + 20 + 5, 2500),
            #                           box_size=(self.length + 40 + 10, self.width - 40 * 2))
            #
            # if self.pillar:
            #     for i in range(7):
            #         elems += i3.Rectangle(layer=self.layer_bool,
            #                               center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + 30),
            #                               box_size=(130, 140))
            #         elems += i3.Rectangle(layer=self.layer_bool, center=(
            #             10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + self.width - 30),
            #                               box_size=(130, 140))

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)
            return elems

# SiN_NP().Layout.view.write_gdsii("SiN_NP.gds")

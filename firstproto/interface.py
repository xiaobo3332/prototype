from technologies import silicon_photonics
import ipkiss3.all as i3


class Interface(i3.PCell):
    _name_prefix = "INTERFACE"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.HFW)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=5000.0)
    width = i3.PositiveNumberProperty(default=3000.0)

    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500, y0 + 4500),
                                  box_size=(15000, 1000))

            # elems += i3.Rectangle(layer=i3.TECH.PPLAYER.NONE.DOC, center=(x0 + 7500, y0 + 4500),
            #                       box_size=(15000, 1000))

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500, y0 + 500),
                                  box_size=(15000, 1000))
            elems += i3.Rectangle(layer=self.layer, center=(x0 + 12500, y0 + 2500),
                                  box_size=(self.length, self.width))

            if self.pocket:
                PO = i3.Rectangle(layer=self.layer_bool, center=(10001, 2500), box_size=(2, 160))
                elems += PO
                generated1 = self.layer - self.layer_bool
                mapping = {generated1: self.layer}
                elems = i3.get_elements_for_generated_layers(elems, mapping)

            if self.tilt:
                # TI = i3.Rectangle(layer=self.layer_bool, center=(10001, 2500), box_size=(2, 160))
                # elems += TI
                TI_shape = i3.Shape(points=[(10000.0, 2470.0), (10010.58, 2530.0), (10000.0, 2530.0)], closed=True)
                TI = i3.Boundary(layer=self.layer_bool, shape=TI_shape)
                elems += TI

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)

            return elems


# # GDS-file generation for debugging
# Interface(pocket= False, tilt=False).Layout.view.write_gdsii("interface1.gds")
# print("Done writing Release.gds!")
# Interface(pocket= True, tilt=False).Layout.view.write_gdsii("interface2.gds")
# print("Done writing Release.gds!")
# Interface(pocket= False, tilt=True).Layout.view.write_gdsii("interface3.gds")
# print("Done writing Release.gds!")
# Interface(pocket= True, tilt=True).Layout.view.write_gdsii("interface4.gds")
# print("Done writing Release.gds!")

class NP(i3.PCell):
    _name_prefix = "NP"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.HFW)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=7000.0)
    width = i3.PositiveNumberProperty(default=330.0)

    pillar = i3.BoolProperty(default=False)
    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)

    # Recess label
    label = i3.StringProperty(default="NP")

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 6500, y0 + 1000 + (3000 - self.width) / 4),
                                  box_size=(self.length, (3000 - self.width) / 2))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(x0 + 6500, y0 + 1000 + self.width + (3000 - self.width) * 3 / 4),
                                  box_size=(self.length, (3000 - self.width) / 2))

            elems += i3.SRef(reference=Interface(pocket=self.pocket, tilt=self.tilt))

            if self.pillar:
                self.label = "NO"
                for i in range(7):
                    elems += i3.Rectangle(layer=self.layer,
                                          center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + 30),
                                          box_size=(50, 60))
                    elems += i3.Rectangle(layer=self.layer, center=(
                        10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + self.width - 30),
                                          box_size=(50, 60))
            if self.width > 330:
                self.label += "W"
            if self.pocket:
                self.label += "_WP"
            if self.tilt:
                self.label += "WT"
            elems += i3.PolygonText(layer=self.layer_bool,
                                    text=self.label,

                                    coordinate=(6000, 4000),
                                    # alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
                                    font=2,
                                    height=700.0)

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)
            return elems


# NP(width=330, pocket=True).Layout.view.write_gdsii("NP.gds")
# NP(width=338, pocket=True, tilt=True).Layout.view.write_gdsii("NP.gds")
# NP(width=330, pillar=True, pocket=True, tilt=True).Layout.view.write_gdsii("NO.gds")

class PI(i3.PCell):
    _name_prefix = "PI"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.HFW)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=7000.0)
    width = i3.PositiveNumberProperty(default=630.0)

    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)

    # Recess label
    label = i3.StringProperty(default="PI_")

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 6500, y0 + 1000 + (3000 - self.width) / 4),
                                  box_size=(self.length, (3000 - self.width) / 2))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(x0 + 6500, y0 + 1000 + self.width + (3000 - self.width) * 3 / 4),
                                  box_size=(self.length, (3000 - self.width) / 2))

            elems += i3.SRef(reference=Interface(pocket=self.pocket, tilt=self.tilt))

            for i in range(7):
                elems += i3.Rectangle(layer=self.layer,
                                      center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + 185),
                                      box_size=(50, 50))
                elems += i3.Rectangle(layer=self.layer,
                                      center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + self.width - 185),
                                      box_size=(50, 50))
            if self.pocket:
                self.label += "WP"
            if self.tilt:
                self.label += "WT"
            elems += i3.PolygonText(layer=self.layer_bool,
                                    text=self.label,

                                    coordinate=(6000, 4000),
                                    # alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
                                    font=2,
                                    height=700.0)

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)

            return elems


# PI(pocket=False, tilt=False).Layout.view.write_gdsii("PI.gds")
# PI(pocket=True, tilt=False).Layout.view.write_gdsii("PI.gds")


# Al mask

class AL_PI(i3.PCell):
    _name_prefix = "AL_PI"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.CONTACT.PILLAR)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NONE.DOC)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=7000.0)
    width = i3.PositiveNumberProperty(default=630.0)


    # Recess label
    label = i3.StringProperty(default="PI_")

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(1500-20, 2500),
                                  box_size=(3000 - 40, 3000 - 40 * 2))

            elems += i3.Rectangle(layer=self.layer,
                                  center=(x0 + 6500-40, 2500),
                                  box_size=(7000, self.width-40*2))

            for i in range(7):
                elems += i3.Rectangle(layer=self.layer_bool,
                                      center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + 185),
                                      box_size=(130, 130))
                elems += i3.Rectangle(layer=self.layer_bool,
                                      center=(10000 - 725 - i * 750, 1000 + (3000 - self.width) / 2 + self.width - 185),
                                      box_size=(130, 130))
            # if self.pocket:
            #     self.label += "WP"
            # if self.tilt:
            #     self.label += "WT"
            # elems += i3.PolygonText(layer=self.layer_bool,
            #                         text=self.label,
            #
            #                         coordinate=(6000, 4000),
            #                         # alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
            #                         font=2,
            #                         height=700.0)
            #
            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)

            return elems

AL_PI().Layout.view.write_gdsii("AL_PI.gds")
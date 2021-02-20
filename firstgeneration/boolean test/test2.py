import ipkiss3.all as i3


class Release(i3.PCell):
    _name_prefix = "RELEASE"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    lay_release = i3.Layer(number=4, name="release")
    layer = i3.LayerProperty(default=lay_release)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=800.0)
    width = i3.PositiveNumberProperty(default=40.0)

    release_margin = i3.PositiveNumberProperty(default=12.5)
    release_tether_period = i3.PositiveNumberProperty(default=45.0)
    release_tether_length = i3.PositiveNumberProperty(default=17.5)
    release_tether_width = i3.PositiveNumberProperty(default=8.0)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            # Center of the structure
            (x0, y0) = self.position

            # elems += i3.Rectangle(layer=self.layer, center=(x0, y0),
            #                       box_size=(self.length + self.release_margin, self.width + self.release_margin))

            elems += i3.Rectangle(layer=self.layer, center=(300, 300),
                                  box_size=(200,200))

            rec = i3.Rectangle(layer=self.layer, center=(0,0), box_size=(200,200))

            remove = i3.Wedge(layer=self.layer, begin_coord=(-100, 0), end_coord=(-50, 0), begin_width=8,
                              end_width=0.001)
            elems += rec,
            # # elems = elems | wedge,
            # haha = rec | remove,
            elems += remove,
            # # elems +=rec,
            # elems = elems.extend(haha),
            return elems


# GDS-file generation for debugging
Release().Layout.view.write_gdsii("test.gds")
print("Done writing Release.gds!")

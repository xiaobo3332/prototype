from firstgeneration.LayerDefinitions import *


class Release(i3.PCell):
    _name_prefix = "RELEASE"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
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

            elems += i3.Rectangle(layer=self.layer, center=(x0, y0),
                                  box_size=(self.length + self.release_margin, self.width + self.release_margin))

            # coordinates_tilted_rectangle = i3.Shape(points=[(5.0, -5.0), (0.0, 0.0), (5.0, 5.0), (10.0, 0.0), (15,0)], closed=True)
            # # rectangle = i3.Shape (points=[(-10,10),(10,10),(10,-10),(-10,-10)], closed = True)
            # # abc=coordinates_tilted_rectangle + rectangle,
            # elems += i3.Boundary(layer=self.layer, shape=coordinates_tilted_rectangle)

            wedge = i3.Wedge(layer=self.layer, begin_coord=(-100, 0), end_coord=(-50, 0), begin_width=8,
                              end_width=0.001)

            # rec = i3.Circle(layer=self.layer, center=(0,0), radius= 100.0)
            # # elems = elems | wedge,
            # haha = wedge & rec,
            elems += wedge,
            # # elems +=rec,
            # elems = elems.extend(haha),
            return elems

# GDS-file generation for debugging
Release().Layout.view.write_gdsii("test.gds")
print("Done writing Release.gds!")

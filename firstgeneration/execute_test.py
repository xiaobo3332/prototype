# from technologies import silicon_photonics
import ipkiss3.all as i3
from interface import Interface
# from MMI22 import my_dc


class AlignmentMarkerSet(i3.PCell):
    _name_prefix = "ALIGNMENT MARKER SET"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Spacing
    v_spacing = i3.PositiveNumberProperty(default=5000.0)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            # Center of the structure
            (x0, y0) = self.position

            # ADD RELEASE
            elems += i3.SRef(reference=Interface(pocket= False, tilt=False),
                             transformation=i3.Translation((x0, 0.0 * self.v_spacing + y0)))
            elems += i3.SRef(reference=Interface(pocket= True, tilt=False),
                             transformation=i3.Translation((x0, 1.0 * self.v_spacing + y0)))

            elems += i3.SRef(reference=Interface(pocket=False, tilt=True),
                             transformation=i3.Translation((x0, 2.0 * self.v_spacing + y0)))
            elems += i3.SRef(reference=Interface(pocket=True, tilt=True),
                             transformation=i3.Translation((x0, 3.0 * self.v_spacing + y0)))



            return elems


# GDS-file generation for debugging 
AlignmentMarkerSet().Layout.view.write_gdsii("execute_test.gds")
print("Done writing AlignmentMarkerSet.gds!")

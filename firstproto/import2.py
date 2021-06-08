from technologies import silicon_photonics
import ipkiss3.all as i3
from ipkiss3.pcell.gdscell import GDSCell


# from interface import AL_PI, AL_NP


class markers_from_Rik(GDSCell):

    # center of the structure (51.969, 49.19)

    def _default_filename(self):
        return 'import.gds'

    def _default_cell_name(self):
        return '20210208_Suggestion_aligning_mar'


class ImportRik(i3.PCell):
    _name_prefix = "ImportRik"

    # Center of the structure
    position = i3.Coord2Property(default=(-51.969, -49.19))

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            # Center of the structure
            (x0, y0) = self.position

            # elems += i3.SRef(reference=markers_from_Rik(),
            #                  transformation=i3.Translation((x0, y0)))

            for j in range(0, 6, 1):
                elems += i3.SRef(reference=markers_from_Rik(name=("nima{}".format(j))),
                                 transformation=i3.Translation((x0 + 5000 + 700 / 2, y0 - 2500 + 5000 * j)))
                elems += i3.SRef(reference=markers_from_Rik(),
                                 transformation=i3.Translation((x0 + 5000 + 750 * 3 + 700 / 2, y0 - 2500 + 5000 * j)))
                elems += i3.SRef(reference=markers_from_Rik(),
                                 transformation=i3.Translation((x0 + 5000 + 750 * 6 + 700 / 2, y0 - 2500 + 5000 * j)))
                elems += i3.SRef(reference=markers_from_Rik(name=("nimafan{}".format(j))),
                                 transformation=i3.Translation((x0 - 5000 - 700 / 2, y0 - 2500 + 5000 * j)))
                elems += i3.SRef(reference=markers_from_Rik(),
                                 transformation=i3.Translation((x0 - 5000 - 750 * 3 + 700 / 2, y0 - 2500 + 5000 * j)))
                elems += i3.SRef(reference=markers_from_Rik(),
                                 transformation=i3.Translation((x0 - 5000 - 750 * 6 + 700 / 2, y0 - 2500 + 5000 * j)))
            return elems

#
# m = ImportRik()
# layout = m.Layout()
# # layout.visualize()
# layout.write_gdsii("import2_test.gds")

from technologies import silicon_photonics
import ipkiss3.all as i3
from ipkiss3.pcell.gdscell import GDSCell


class mmi_slots_cell(GDSCell):

    def _default_filename(self):
        return 'MMI22.gds'

    def _default_cell_name(self):
        return 'PCELL_1'




mmi_slots = mmi_slots_cell()


from picazzo3.routing.place_route import PlaceAndAutoRoute


pr = PlaceAndAutoRoute(child_cells={"mmi1": mmi_slots,
                                    # "mmi2": mmi_slots,

                                    },
                       links=[])

layout = pr.Layout(child_transformations={"mmi1": i3.Rotation(rotation=90),
                                          # "score": (4745., 400.),
                                          # "sbundle1": (-200., 499 + 10.),
                                          # "sbundle2": (-200., 598 + 20),
                                          # "sbundle3": (-200., 697. + 30),
                                          # "spirals150": (304.97, 698 + 99. + 43),
                                          # "spirals200": (304.97, 824 + 99. + 56),
                                          # "rbundle1": (-200., 950 + 99. + 66),
                                          # "rbundle2": (-200., 1036 + 99. + 76),
                                          # "rbundle3": (-200., 1036 + 99 + 86. + 86),
                                          # "spiral06":(304.97,1120+99+86),
                                          # "spiral07":(304.97,1290+99+86)
                                          }
                   )

# layout.visualize()
layout.write_gdsii("importtest.GDS")

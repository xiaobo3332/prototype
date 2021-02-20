from technologies import silicon_photonics
import ipkiss3.all as i3
from ipkiss3.pcell.gdscell import GDSCell
from MMI22 import my_dc


class mmi_slots_cell(GDSCell):

    def _default_filename(self):
        return 'recess_v5.GDS'

    def _default_cell_name(self):
        return 'normal'


# class mmi_ribs_cell(GDSCell):
#
#     def _default_filename(self):
#         return 'MMI_ribs.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_22'
#
#
# class small_core_cell(GDSCell):
#
#     def _default_filename(self):
#         return 'smallcore.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_122'
#
#
# class rib_bundle_cell(GDSCell):
#
#     def _default_filename(self):
#         return 'ribbundles.gds'
#
#     def _default_cell_name(self):
#         return 'PCELL_6'
#
#
# class slot_bundle_cell(GDSCell):
#
#     def _default_filename(self):
#         return 'slotbundle.gds'
#
#     def _default_cell_name(self):
#         return 'PCELL_7'
#
#
# class spiral_06_cell(GDSCell):
#     def _default_filename(self):
#         return 'spiral_0.6.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_3'
#
#
# class spiral_07_cell(GDSCell):
#     def _default_filename(self):
#         return 'spiral_0.7.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_3'
#
#
# class spiral_slot_150_cell(GDSCell):
#     def _default_filename(self):
#         return 'spirals_150.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_4'
#
#
# class spiral_slot_200_cell(GDSCell):
#     def _default_filename(self):
#         return 'spirals_200.gds'
#
#     def _default_cell_name(self):
#         return 'AUTOTP_4'


mmi_slots = mmi_slots_cell()
# a = mmi_slots.Layout()
# a.write_gdsii("importtest.gds")
# mmi_ribs = mmi_ribs_cell()
# small_core = small_core_cell()
# rib_bundle = rib_bundle_cell()
# slot_bundle = slot_bundle_cell()
# spiral_06 = spiral_06_cell()
# spiral_07 = spiral_07_cell()
# spiral_slot_150 = spiral_slot_150_cell()
# spiral_slot_200 = spiral_slot_200_cell()

from picazzo3.routing.place_route import PlaceAndAutoRoute

dc_10 = my_dc(gap_inc_vec=[390, 398, 406], name="ring1")
dc_10_layout = dc_10.Layout()

dc_15 = my_dc(gap_inc_vec=[390, 398, 406], name="ring2")
dc_15_layout = dc_15.Layout()

pr = PlaceAndAutoRoute(child_cells={"mmi1": mmi_slots,
                                    "dc1": dc_10,
                                    "dc2": dc_15,

                                    },
                       links=[])

layout = pr.Layout(child_transformations={"mmi1": i3.Rotation(rotation=90) - i3.Translation((15000, 0)),
                                          "dc1": (0, 0),
                                          "dc2": i3.HMirror(2500) - i3.Translation((5000, 0)),
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
layout.write_gdsii("import.gds")

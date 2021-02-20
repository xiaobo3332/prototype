from technologies import silicon_photonics
# from picazzo3.traces.wire_wg.trace import WireWaveguideTemplate
# # from picazzo3.routing.place_route import ConnectComponents
# from picazzo3.traces.wire_wg import WireWaveguideTransitionLinear
# # from picazzo3.routing.place_route import PlaceAndConnect
# from picazzo3.routing.place_route import PlaceAndAutoRoute
import ipkiss3.all as i3
# from picazzo3.container.transition_ports import AutoTransitionPorts
# from picazzo3.filters.mmi.cell import MMI2x2Tapered
from MMI22 import my_dc
from interface import Interface

dc_10 = my_dc(gap_inc_vec=[390, 398, 406], name="ring1")
dc_10_layout = dc_10.Layout()
# dc_10_layout.visualize(annotate=True)
# dc_10_layout.write_gdsii("DC_V4.gds")
#

# Interface(pocket= False, tilt=False).Layout.view.write_gdsii("interface1.gds")
dc20 = Interface(pocket=True, tilt=True)
dc30 = Interface(pocket=True, tilt=False)
dc40 = Interface(pocket=False, tilt=True)
dc50 = Interface(pocket=False, tilt=False)
# dc20_layout = Interface(pocket= False, tilt=False).Layout()
# dc20.visualize()

print("Done writing Release.gds!")

dc_15 = my_dc(gap_inc_vec=[390, 398, 406], name="ring2")
dc_15_layout = dc_15.Layout()

pr = i3.PlaceComponents(
    child_cells={
        "dc1": dc_10,
        "dc2": dc_15,
        "dc3": dc20,
        "dc4": dc30,
        "dc5": dc40,
        "dc6": dc50
        # "dc3": dc_20,
        # "dc4": dc_25
    }
)
pr_layout = pr.Layout(child_transformations={"dc1": (0, 0),
                                             "dc2": i3.HMirror(2500) - i3.Translation((5000, 0)),
                                             "dc3": (-15000, 0),
                                             "dc4": (-15000, 0 + 5000 * 1),
                                             "dc5": (-15000, 0 + 5000 * 2),
                                             "dc6": (-15000, 0 + 5000 * 3),


                                             })
pr_layout.visualize()
pr_layout.write_gdsii("execute_test3.gds")

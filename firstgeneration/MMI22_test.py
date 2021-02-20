from technologies import silicon_photonics
# from picazzo3.traces.wire_wg.trace import WireWaveguideTemplate
# # from picazzo3.routing.place_route import ConnectComponents
# from picazzo3.traces.wire_wg import WireWaveguideTransitionLinear
# from picazzo3.routing.place_route import PlaceAndConnect
# from picazzo3.routing.place_route import PlaceAndAutoRoute
import ipkiss3.all as i3
# from picazzo3.container.transition_ports import AutoTransitionPorts
# from picazzo3.filters.mmi.cell import MMI2x2Tapered
from MMI22 import my_dc
from ipkiss.boolean_ops.boolean_ops_elements import get_elements_for_generated_layers




dc_10 = my_dc(gap_inc_vec=[390, 398, 406], name="ring1")
dc_10_layout = dc_10.Layout()
# dc_10_layout.visualize(annotate=True)
# dc_10_layout.write_gdsii("DC_V4.gds")


dc_15 = my_dc(gap_inc_vec=[390, 398, 406],  name="ring2")
dc_15_layout = dc_15.Layout()


pr = i3.PlaceComponents(
    child_cells={
        "dc1": dc_10,
        "dc2": dc_15,
    }
)
pr_layout = pr.Layout(child_transformations={"dc1": (0, 0),
                                             "dc2": i3.HMirror(2500) - i3.Translation((5000, 0)),

                                             })
# pr_layout.visualize()
# pr_layout.write_gdsii("MMI22_test.gds")

wg_mask = i3.TECH.PPLAYER.WG.CLADDING-i3.TECH.PPLAYER.WG.CORE

generated_elements = get_elements_for_generated_layers(pr_layout.layout, {wg_mask: i3.TECH.PPLAYER.NONE.DOC})
generated_layout = i3.LayoutCell("generated_mask").Layout(elements=generated_elements)
generated_layout.visualize()
generated_layout.write_gdsii("MMI22_test.gds")

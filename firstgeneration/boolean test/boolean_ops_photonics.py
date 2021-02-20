from technologies.silicon_photonics import TECH
import ipkiss3.all as i3
from picazzo3.traces.wire_wg.transitions import WireWaveguideTemplate
from picazzo3.filters.ring import RingRectSymm180DropFilter
from ipkiss.boolean_ops.boolean_ops_elements import get_elements_for_generated_layers
from ipkiss.plugins.vfabrication.process_flow import VFabricationProcessFlow

# process layers and purposes
wg_process = i3.ProcessLayer("waveguide", "WG")
core_purpose = i3.PatternPurpose("waveguide core", "CORE")
clad_purpose = i3.PatternPurpose("waveguide cladding", "CLAD")
# drawing layers
wg_core = i3.PPLayer(wg_process, core_purpose, "WG_COREx")
wg_clad = i3.PPLayer(wg_process, clad_purpose, "WG_CLADx")
# generated layers: boolean formula for mask making
wg_mask = wg_clad - wg_core

# waveguide template
wg_tmpl = WireWaveguideTemplate()
wg_tmpl.Layout(core_width=0.5,
               cladding_width=4.5,
               core_process=wg_process,
               core_purpose=core_purpose,
               cladding_process=wg_process,
               cladding_purpose=clad_purpose)

# ring resonator
ring = RingRectSymm180DropFilter(ring_trace_template=wg_tmpl, coupler_trace_templates=[wg_tmpl, wg_tmpl])
ring_lo = ring.Layout(bend_radius=5.0, coupler_lengths=[1.0, 1.0], coupler_angles=[60.0, 60.0],
                      straights=(0.0, 0.0))
ring_lo.visualize()

# # use as a generated mask layer
# generated_elements = get_elements_for_generated_layers(ring_lo.layout, {wg_mask: i3.Layer(1)})
# generated_layout = i3.LayoutCell("generated_mask").Layout(elements=generated_elements)
# generated_layout.visualize()
# generated_layout.write_gdsii("boolean_ops_photonics.gds")

# use as a generated mask layer
generated_elements = get_elements_for_generated_layers(ring_lo.layout, {wg_mask: TECH.PPLAYER.NONE.DOC})
generated_layout = i3.LayoutCell("generated_mask").Layout(elements=generated_elements)
generated_layout.visualize()
generated_layout.write_gdsii("boolean_ops_photonics.gds")


# define a virtual fabrication flow, using the material stacks in the silicon_photonics technology
vfab_process = VFabricationProcessFlow(active_processes=[wg_process],
                                       process_layer_map={wg_process: wg_mask},
                                       is_lf_fabrication={wg_process: False},
                                       process_to_material_stack_map=[
                                           ((0, ), TECH.MATERIAL_STACKS.MSTACK_SOI_SI_220nm),
                                           ((1, ), TECH.MATERIAL_STACKS.MSTACK_SOI_SI_100nm),
                                       ])
# visualize the result of the virtual fabrication
# top-down
ring_lo.visualize_2d(vfabrication_process_flow=vfab_process)
ring_xs = ring_lo.cross_section(process_flow=vfab_process,
                                cross_section_path=i3.Shape([(0.0, 4.0), (0.0, 7.0)])
                                )
ring_xs.visualize()

# generated_layout.visualize(vfabrication_process_flow=vfab_process)
# generated_layout.write_gdsii("boolean_ops_photonics.gds")
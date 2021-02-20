# This example shows how to generate elements on generated layers.

import ipkiss3.all as i3

# drawn layers
layer1 = i3.Layer(1)
layer2 = i3.Layer(2)
layer3 = i3.Layer(3)

# original layout
rect = i3.RoundedRectangle(layer=layer3, center=(0.0, 0.0), box_size=(30.0, 30.0), radius=2.0)
circle = i3.Circle(layer=layer1, center=(0.0, 0.0), radius=10.0)
circle_path = i3.CirclePath(layer=layer2, center=(9.0, 9.0), radius=6.0, line_width=1.0)

layout = i3.LayoutCell(name="original").Layout(elements=[rect, circle, circle_path])
layout.visualize()

# specify generated layers and the layer to use in the output
generated1 = (layer1 ^ layer2) & layer1
generated2 = ~layer3
mapping = {generated1: i3.Layer(10),
           generated2: i3.Layer(20)
           }

# generated layout
output_elems = i3.get_elements_for_generated_layers(layout.layout, mapping)
final_layout = i3.LayoutCell(name="generated").Layout(elements=output_elems)
final_layout.visualize()

# create and visualize a hierarchical layout
simple_layout = i3.LayoutCell(name="circle_and_path").Layout(elements=[circle, circle_path])
top_layout = i3.LayoutCell(name="top_original").Layout(elements=[
    i3.SRef(simple_layout, (0.0, 0.0)),
    i3.SRef(simple_layout, (0.0, 15.0)),
    # cover the full layout with layer3
    i3.Boundary(layer=layer3,
                shape=[(-10.0, -10.0), (-10.0, 35.0), (20.0, 35.0), (20.0, -10.0)])
])

top_layout.visualize()

# and create and visualize the generated result
top_output_elems = i3.get_elements_for_generated_layers(top_layout.layout, mapping)
final_top_layout = i3.LayoutCell(name="top_generated").Layout(elements=top_output_elems)
final_top_layout.visualize()


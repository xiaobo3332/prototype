# This example shows how to use Boolean operations on Boundary elements

import ipkiss3.all as i3
import matplotlib.pyplot as plt

#1. Define two elements
circle = i3.Circle(layer=i3.Layer(1), center=(0.0, 0.0), radius=10.0)
rectangle = i3.RoundedRectangle(layer=i3.Layer(1), center=(8.0, 7.0), box_size=(12.0, 8.0), radius=1.0)

#2. Boolean operations between two shapes
# AND, OR, XOR and NOT are supported
# Each operation returns a *list* of Boundary elements, so make sure to process them further as a list
elems_and = circle & rectangle
elems_or = circle | rectangle
elems_xor = circle ^ rectangle
elems_not = circle - rectangle

#3. make a layout with the elements so we can visualize them and save to GDSII
layout_original = i3.LayoutCell(name="original").Layout(elements=([circle, rectangle]+elems_and))
layout_and = i3.LayoutCell(name="AND").Layout(elements=elems_and)
layout_or = i3.LayoutCell(name="OR").Layout(elements=elems_or)
layout_xor = i3.LayoutCell(name="XOR").Layout(elements=elems_xor)
layout_not = i3.LayoutCell(name="NOT").Layout(elements=elems_not)

layout=i3.LayoutCell(name="boolean_ops_shape").Layout(elements=[
    i3.SRef(layout_original, (0.0, 0.0)),
    i3.SRef(layout_and, (50.0, 0.0)),
    i3.SRef(layout_or, (100.0, 0.0)),
    i3.SRef(layout_xor, (150.0, 0.0)),
    i3.SRef(layout_not, (200.0, 0.0))
])

#4. Write to GDSII and visualize
layout.write_gdsii("boolean_ops_boundaries.gds")
layout.visualize()

#5. Try boolean between elements on different layers:
rectangle2 = i3.RoundedRectangle(layer=i3.Layer(2), center=(8.0, 7.0), box_size=(12.0, 8.0), radius=1.0)
elems_and_2 = circle & rectangle2
print("Result of boolean between elements on different layers is: {}".format(elems_and_2))
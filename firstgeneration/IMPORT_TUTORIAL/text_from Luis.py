#from technologies import silicon_photonics
import ipkiss3.all as i3
class My_Coupon(i3.PCell):

	_name_prefix = "My_coupon"

	class Layout(i3.LayoutView):

		def _generate_elements(self, elems):
			# The shape of the coupon you want to print
			for i in range(16):
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(500,-3+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(4950,-3+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
			for i in range(16):
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(500,507+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(4950,507+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
			for i in range(16):
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(500,1017+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
				elems += i3.PolygonText(layer=i3.Layer(5),
					coordinate=(4950,1017+i*30),
					text=str(300+i*50),
					alignment=(i3.TEXT.ALIGN.CENTER,
						   i3.TEXT.ALIGN.TOP),
					font=i3.TEXT.FONT.DEFAULT,
					height=22,
					transformation=i3.Rotation((0.0, 0.0), 0.0))
			return elems

obj1 = My_Coupon()
layout = obj1.Layout()
total = i3.PlaceComponents(name = 'all_coupons', child_cells = {'c1':obj1,
								})
total_layout = total.Layout(child_transformations = {'c1': i3.Translation((0,0)),})
#total_layout.visualize()
total_layout.write_gdsii('text.gds')
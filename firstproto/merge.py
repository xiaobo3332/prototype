from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from execute import my_exe
from AlignmentMarkerSet import PlaceMarkers


mask = my_exe(name="final")
mask_layout = mask.Layout()


dc_15 = my_dc(gap_inc_vec=[390, 398, 406], name="ring2")

recess0 = NP(width=338)
recess1 = NP(width=338, pocket=True, tilt=False)
recess2 = NP(width=338, pocket=True, tilt=True)
recess3 = NP(pillar=True)
recess4 = NP(pillar=True, pocket=True, tilt=False)
recess5 = NP(pillar=True, pocket=True, tilt=True)
recess6 = NP(pocket=False, tilt=False)
recess7 = NP(pocket=False, tilt=False)
recess8 = NP(pocket=False, tilt=False)
recess9 = NP(pocket=False, tilt=False)
recess10 = PI(pocket=False, tilt=False)
recess11 = PI(pocket=False, tilt=False)


pr = PlaceComponents(
    child_cells={
        "dc1": dc_10,
        "dc2": dc_15,
        "R0": recess0,
        "R1": recess1,
        "R2": recess2,
        "R3": recess3,
        "R4": recess4,
        "R5": recess5
    }
)
pr_layout = pr.Layout(child_transformations={"dc1": (0, 0),
                                             "dc2": i3.HMirror(2500) - i3.Translation((5000, 0)),
                                             "R0": (-15000, 0 + 5000 * -1),
                                             "R1": (-15000, 0 + 5000 * 0),
                                             "R2": (-15000, 0 + 5000 * 1),
                                             "R3": (-15000, 0 + 5000 * 2),
                                             "R4": (-15000, 0 + 5000 * 3),
                                             "R5": (-15000, 0 + 5000 * 4),

                                             })
# pr_layout.visualize()
pr_layout.write_gdsii("execute.gds")

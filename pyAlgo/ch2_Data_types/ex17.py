mugs_ordered = 47
mugs_per_box = 6

# TODO: use mugs_ordered // mugs_per_box
full_boxes = mugs_ordered // mugs_per_box

# TODO: use mugs_ordered % mugs_per_box
leftover_mugs = mugs_ordered % mugs_per_box

# TODO: use leftover_mugs > 0
extra_box_needed = leftover_mugs > 0

# TODO: use full_boxes + int(extra_box_needed)
boxes_to_ship = full_boxes + int(extra_box_needed)

print(f"Full boxes: {full_boxes}")
print(f"Leftover mugs: {leftover_mugs}")
print(f"Extra box needed: {extra_box_needed}")
print(f"Boxes to ship: {boxes_to_ship}")
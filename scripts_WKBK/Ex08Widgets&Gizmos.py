#program Ex08Widgets&Gizmos :

#initialize widget in grams
#initialize gizmo in grams
widget = 75
gizmo = 112

#READ number of widget
num_widget = int(raw_input("Enter # of widget:\n"))
#READ number or gizmos
num_gizmo = int(raw_input("Enter # of widget:\n"))

#compute total weight widgets
#compute total wight gizmos
#compute total weight of gizmos and widgets
widget_total_weight = num_widget * widget
gizmo_total_weight = num_gizmo * gizmo
order_weight = widget_total_weight + gizmo_total_weight

#write total weight of order
print "The total weight of the order is: %s grams" % order_weight
#end Ex08Widgets&Gizmos

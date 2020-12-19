def eval_tree(floor_number, height, floor_area, total_floor_area, beams, columns, flooring, exterior_walls, corridor_walls, room_partitions, main_stair, window, ceiling, main_door, trusses, roof, boiler_provided, lpg_installation_with_permit, fuel_with_storage_permit, generator_set, generator_fuel_storage_permit, refuse_handling, refuse_handling_fire_protection, electrical_hazard, mechanical_hazard, hazardous_material, hazardous_material_stored, defects, avg_fire_rating, building_age):
     if building_age <= 1052.00:
         if total_floor_area <= 13984.00:
             if building_age <= 726.50:
                 if avg_fire_rating <= 2.79:
                     if roof <= 5.50:
                         result = True
                     if roof >  5.50:
                         result = False
                 if avg_fire_rating >  2.79:
                     if total_floor_area <= 8074.00:
                         if avg_fire_rating <= 3.38:
                             if building_age <= 658.00:
                                 if roof <= 1.00:
                                     if lpg_installation_with_permit <= 0.50:
                                         result = False
                                     if lpg_installation_with_permit >  0.50:
                                         result = True
                                 if roof >  1.00:
                                     result = False
                             if building_age >  658.00:
                                 result = True
                         if avg_fire_rating >  3.38:
                             if building_age <= 577.00:
                                 if main_stair <= 3.50:
                                     result = True
                                 if main_stair >  3.50:
                                     if refuse_handling_fire_protection <= 0.50:
                                         result = True
                                     if refuse_handling_fire_protection >  0.50:
                                         if exterior_walls <= 2.00:
                                             result = True
                                         if exterior_walls >  2.00:
                                             result = False
                             if building_age >  577.00:
                                 result = False
                     if total_floor_area >  8074.00:
                         if floor_number <= 62.00:
                             result = True
                         if floor_number >  62.00:
                             result = False
             if building_age >  726.50:
                 if total_floor_area <= 2479.50:
                     result = True
                 if total_floor_area >  2479.50:
                     if mechanical_hazard <= 0.50:
                         if height <= 134.00:
                             if trusses <= 2.50:
                                 if lpg_installation_with_permit <= 0.50:
                                     result = True
                                 if lpg_installation_with_permit >  0.50:
                                     if roof <= 5.50:
                                         result = False
                                     if roof >  5.50:
                                         result = True
                             if trusses >  2.50:
                                 result = False
                         if height >  134.00:
                             result = True
                     if mechanical_hazard >  0.50:
                         if floor_number <= 13.00:
                             if window <= 0.50:
                                 result = False
                             if window >  0.50:
                                 result = True
                         if floor_number >  13.00:
                             if building_age <= 765.00:
                                 if main_stair <= 2.50:
                                     result = True
                                 if main_stair >  2.50:
                                     result = False
                             if building_age >  765.00:
                                 result = False
         if total_floor_area >  13984.00:
             if generator_fuel_storage_permit <= 0.50:
                 if roof <= 3.50:
                     if floor_number <= 48.00:
                         if refuse_handling <= 0.50:
                             result = False
                         if refuse_handling >  0.50:
                             if hazardous_material <= 0.50:
                                 result = True
                             if hazardous_material >  0.50:
                                 result = False
                     if floor_number >  48.00:
                         if building_age <= 990.00:
                             result = True
                         if building_age >  990.00:
                             result = False
                 if roof >  3.50:
                     if window <= 2.50:
                         if room_partitions <= 1.50:
                             if fuel_with_storage_permit <= 0.50:
                                 result = True
                             if fuel_with_storage_permit >  0.50:
                                 result = False
                         if room_partitions >  1.50:
                             result = False
                     if window >  2.50:
                         if building_age <= 926.00:
                             if hazardous_material_stored <= 0.50:
                                 result = False
                             if hazardous_material_stored >  0.50:
                                 result = True
                         if building_age >  926.00:
                             result = True
             if generator_fuel_storage_permit >  0.50:
                 if main_door <= 3.50:
                     if floor_area <= 333.50:
                         result = False
                     if floor_area >  333.50:
                         if corridor_walls <= 5.50:
                             if trusses <= 0.50:
                                 if hazardous_material <= 0.50:
                                     result = True
                                 if hazardous_material >  0.50:
                                     result = False
                             if trusses >  0.50:
                                 if main_stair <= 0.50:
                                     if building_age <= 549.50:
                                         result = False
                                     if building_age >  549.50:
                                         result = True
                                 if main_stair >  0.50:
                                     result = True
                         if corridor_walls >  5.50:
                             result = False
                 if main_door >  3.50:
                     result = True
     if building_age >  1052.00:
         if building_age <= 1385.00:
             if building_age <= 1378.50:
                 if total_floor_area <= 12977.50:
                     if main_stair <= 3.50:
                         result = False
                     if main_stair >  3.50:
                         if corridor_walls <= 3.50:
                             if building_age <= 1262.50:
                                 result = True
                             if building_age >  1262.50:
                                 result = False
                         if corridor_walls >  3.50:
                             if boiler_provided <= 0.50:
                                 result = True
                             if boiler_provided >  0.50:
                                 result = False
                 if total_floor_area >  12977.50:
                     if avg_fire_rating <= 1.96:
                         if flooring <= 1.50:
                             result = True
                         if flooring >  1.50:
                             result = False
                     if avg_fire_rating >  1.96:
                         result = False
             if building_age >  1378.50:
                 result = True
         if building_age >  1385.00:
             result = False

     return result
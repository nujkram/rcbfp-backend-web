def eval_tree(floor_number, height, floor_area, total_floor_area, beams, columns, flooring, exterior_walls, corridor_walls, room_partitions, main_stair, window, ceiling, main_door, trusses, roof, boiler_provided, lpg_installation_with_permit, fuel_with_storage_permit, generator_set, generator_fuel_storage_permit, refuse_handling, refuse_handling_fire_protection, electrical_hazard, mechanical_hazard, hazardous_material, hazardous_material_stored, defects, avg_fire_rating, building_age):
     if building_age <= 1113.50:
         if building_age <= 827.50:
             if roof <= 4.50:
                 if avg_fire_rating <= 2.96:
                     if height <= 207.50:
                         if floor_number <= 24.50:
                             if height <= 37.50:
                                 if generator_set <= 0.50:
                                     result = True
                                 if generator_set >  0.50:
                                     result = False
                             if height >  37.50:
                                 result = True
                         if floor_number >  24.50:
                             if hazardous_material <= 0.50:
                                 if electrical_hazard <= 0.50:
                                     if hazardous_material_stored <= 0.50:
                                         result = False
                                     if hazardous_material_stored >  0.50:
                                         result = True
                                 if electrical_hazard >  0.50:
                                     if ceiling <= 4.50:
                                         result = False
                                     if ceiling >  4.50:
                                         result = True
                             if hazardous_material >  0.50:
                                 if total_floor_area <= 11583.50:
                                     result = True
                                 if total_floor_area >  11583.50:
                                     if ceiling <= 3.50:
                                         if hazardous_material_stored <= 0.50:
                                             result = True
                                         if hazardous_material_stored >  0.50:
                                             if electrical_hazard <= 0.50:
                                                 result = True
                                             if electrical_hazard >  0.50:
                                                 result = False
                                     if ceiling >  3.50:
                                         result = False
                     if height >  207.50:
                         result = True
                 if avg_fire_rating >  2.96:
                     if avg_fire_rating <= 3.29:
                         if generator_set <= 0.50:
                             if height <= 249.00:
                                 if trusses <= 1.50:
                                     if hazardous_material <= 0.50:
                                         result = True
                                     if hazardous_material >  0.50:
                                         result = False
                                 if trusses >  1.50:
                                     result = False
                             if height >  249.00:
                                 result = True
                         if generator_set >  0.50:
                             if window <= 3.50:
                                 if mechanical_hazard <= 0.50:
                                     if boiler_provided <= 0.50:
                                         result = True
                                     if boiler_provided >  0.50:
                                         if corridor_walls <= 3.00:
                                             result = False
                                         if corridor_walls >  3.00:
                                             result = True
                                 if mechanical_hazard >  0.50:
                                     result = False
                             if window >  3.50:
                                 result = True
                     if avg_fire_rating >  3.29:
                         if room_partitions <= 3.50:
                             if building_age <= 570.50:
                                 result = True
                             if building_age >  570.50:
                                 if boiler_provided <= 0.50:
                                     if building_age <= 657.50:
                                         result = False
                                     if building_age >  657.50:
                                         result = True
                                 if boiler_provided >  0.50:
                                     result = False
                         if room_partitions >  3.50:
                             result = True
             if roof >  4.50:
                 if boiler_provided <= 0.50:
                     if building_age <= 349.00:
                         if main_stair <= 4.50:
                             if building_age <= 332.50:
                                 result = True
                             if building_age >  332.50:
                                 if corridor_walls <= 2.50:
                                     result = False
                                 if corridor_walls >  2.50:
                                     result = True
                         if main_stair >  4.50:
                             result = False
                     if building_age >  349.00:
                         if building_age <= 652.00:
                             result = False
                         if building_age >  652.00:
                             if generator_fuel_storage_permit <= 0.50:
                                 result = True
                             if generator_fuel_storage_permit >  0.50:
                                 result = False
                 if boiler_provided >  0.50:
                     if corridor_walls <= 0.50:
                         if building_age <= 490.50:
                             result = False
                         if building_age >  490.50:
                             result = True
                     if corridor_walls >  0.50:
                         if ceiling <= 0.50:
                             result = False
                         if ceiling >  0.50:
                             if ceiling <= 5.50:
                                 result = True
                             if ceiling >  5.50:
                                 if beams <= 1.50:
                                     result = False
                                 if beams >  1.50:
                                     result = True
         if building_age >  827.50:
             if floor_area <= 341.00:
                 if total_floor_area <= 2280.00:
                     result = True
                 if total_floor_area >  2280.00:
                     if columns <= 0.50:
                         if trusses <= 3.50:
                             result = False
                         if trusses >  3.50:
                             result = True
                     if columns >  0.50:
                         if room_partitions <= 5.50:
                             result = False
                         if room_partitions >  5.50:
                             if refuse_handling <= 0.50:
                                 result = True
                             if refuse_handling >  0.50:
                                 result = False
             if floor_area >  341.00:
                 if floor_area <= 493.50:
                     if columns <= 5.00:
                         result = True
                     if columns >  5.00:
                         result = False
                 if floor_area >  493.50:
                     if corridor_walls <= 4.50:
                         if building_age <= 960.50:
                             if window <= 5.50:
                                 result = True
                             if window >  5.50:
                                 result = False
                         if building_age >  960.50:
                             result = False
                     if corridor_walls >  4.50:
                         result = False
     if building_age >  1113.50:
         if building_age <= 1396.50:
             if total_floor_area <= 26108.00:
                 if floor_area <= 292.00:
                     if main_stair <= 3.50:
                         result = False
                     if main_stair >  3.50:
                         if flooring <= 4.00:
                             result = True
                         if flooring >  4.00:
                             if mechanical_hazard <= 0.50:
                                 if building_age <= 1336.00:
                                     result = True
                                 if building_age >  1336.00:
                                     result = False
                             if mechanical_hazard >  0.50:
                                 result = False
                 if floor_area >  292.00:
                     result = False
             if total_floor_area >  26108.00:
                 if floor_number <= 53.50:
                     result = True
                 if floor_number >  53.50:
                     if electrical_hazard <= 0.50:
                         result = True
                     if electrical_hazard >  0.50:
                         result = False
         if building_age >  1396.50:
             result = False

     return result
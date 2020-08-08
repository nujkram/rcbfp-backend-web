def eval_tree(floor_number, height, floor_area, total_floor_area, beams, columns, flooring, exterior_walls,
              corridor_walls, room_partitions, main_stair, window, ceiling, main_door, trusses, roof, boiler_provided,
              lpg_installation_with_permit, fuel_with_storage_permit, generator_set, generator_fuel_storage_permit,
              refuse_handling, refuse_handling_fire_protection, electrical_hazard, mechanical_hazard,
              hazardous_material, hazardous_material_stored, defects, avg_fire_rating, building_age):
    if building_age <= 70.50:
        result = False
    if building_age > 70.50:
        if fuel_with_storage_permit <= 0.50:
            if building_age <= 9767.50:
                if avg_fire_rating <= 4.38:
                    if flooring <= 0.50:
                        if beams <= 2.00:
                            result = True
                        if beams > 2.00:
                            if hazardous_material <= 0.50:
                                if building_age <= 7308.50:
                                    if mechanical_hazard <= 0.50:
                                        if generator_fuel_storage_permit <= 0.50:
                                            if refuse_handling <= 0.50:
                                                pass
                                            if refuse_handling > 0.50:
                                                result = False
                                        if generator_fuel_storage_permit > 0.50:
                                            if avg_fire_rating <= 2.46:
                                                pass
                                            if avg_fire_rating > 2.46:
                                                result = True
                                    if mechanical_hazard > 0.50:
                                        result = True
                                if building_age > 7308.50:
                                    result = False
                            if hazardous_material > 0.50:
                                result = True
                    if flooring > 0.50:
                        if ceiling <= 5.50:
                            if trusses <= 0.50:
                                if main_stair <= 0.50:
                                    if hazardous_material <= 0.50:
                                        result = False
                                    if hazardous_material > 0.50:
                                        result = True
                                if main_stair > 0.50:
                                    if columns <= 5.50:
                                        result = True
                                    if columns > 5.50:
                                        if building_age <= 5668.00:
                                            result = True
                                        if building_age > 5668.00:
                                            if building_age <= 6061.00:
                                                result = False
                                            if building_age > 6061.00:
                                                result = True
                            if trusses > 0.50:
                                result = True
                        if ceiling > 5.50:
                            if main_stair <= 5.50:
                                if building_age <= 644.50:
                                    if beams <= 5.00:
                                        result = True
                                    if beams > 5.00:
                                        result = False
                                if building_age > 644.50:
                                    if main_door <= 1.00:
                                        if mechanical_hazard <= 0.50:
                                            if boiler_provided <= 0.50:
                                                result = False
                                            if boiler_provided > 0.50:
                                                result = True
                                        if mechanical_hazard > 0.50:
                                            result = True
                                    if main_door > 1.00:
                                        result = True
                            if main_stair > 5.50:
                                if building_age <= 2339.00:
                                    result = True
                                if building_age > 2339.00:
                                    result = False
                if avg_fire_rating > 4.38:
                    if building_age <= 7975.00:
                        result = True
                    if building_age > 7975.00:
                        result = False
            if building_age > 9767.50:
                if building_age <= 10002.50:
                    result = False
                if building_age > 10002.50:
                    result = True
        if fuel_with_storage_permit > 0.50:
            if roof <= 1.50:
                if refuse_handling <= 0.50:
                    if building_age <= 3689.00:
                        if floor_area <= 220.00:
                            if hazardous_material <= 0.50:
                                result = False
                            if hazardous_material > 0.50:
                                result = True
                        if floor_area > 220.00:
                            if columns <= 0.50:
                                result = False
                            if columns > 0.50:
                                if building_age <= 608.50:
                                    if flooring <= 1.50:
                                        result = False
                                    if flooring > 1.50:
                                        result = True
                                if building_age > 608.50:
                                    if building_age <= 2590.00:
                                        result = True
                                    if building_age > 2590.00:
                                        if building_age <= 2872.50:
                                            result = False
                                        if building_age > 2872.50:
                                            result = True
                    if building_age > 3689.00:
                        if hazardous_material_stored <= 0.50:
                            if height <= 77.00:
                                result = True
                            if height > 77.00:
                                result = False
                        if hazardous_material_stored > 0.50:
                            if generator_set <= 0.50:
                                result = True
                            if generator_set > 0.50:
                                if floor_number <= 49.50:
                                    result = True
                                if floor_number > 49.50:
                                    result = False
                if refuse_handling > 0.50:
                    if refuse_handling_fire_protection <= 0.50:
                        if flooring <= 0.50:
                            if lpg_installation_with_permit <= 0.50:
                                result = True
                            if lpg_installation_with_permit > 0.50:
                                result = False
                        if flooring > 0.50:
                            if avg_fire_rating <= 1.58:
                                result = False
                            if avg_fire_rating > 1.58:
                                if corridor_walls <= 5.50:
                                    result = True
                                if corridor_walls > 5.50:
                                    if building_age <= 3301.50:
                                        result = True
                                    if building_age > 3301.50:
                                        result = False
                    if refuse_handling_fire_protection > 0.50:
                        result = True
            if roof > 1.50:
                if mechanical_hazard <= 0.50:
                    if hazardous_material <= 0.50:
                        if height <= 247.50:
                            if building_age <= 347.50:
                                result = False
                            if building_age > 347.50:
                                if electrical_hazard <= 0.50:
                                    if beams <= 5.50:
                                        if main_stair <= 4.50:
                                            result = True
                                        if main_stair > 4.50:
                                            if corridor_walls <= 0.50:
                                                result = False
                                            if corridor_walls > 0.50:
                                                pass
                                    if beams > 5.50:
                                        if height <= 190.50:
                                            if building_age <= 4107.50:
                                                pass
                                            if building_age > 4107.50:
                                                result = False
                                        if height > 190.50:
                                            if building_age <= 3329.50:
                                                result = False
                                            if building_age > 3329.50:
                                                result = True
                                if electrical_hazard > 0.50:
                                    if main_door <= 0.50:
                                        if generator_fuel_storage_permit <= 0.50:
                                            if beams <= 1.50:
                                                result = True
                                            if beams > 1.50:
                                                pass
                                        if generator_fuel_storage_permit > 0.50:
                                            result = True
                                    if main_door > 0.50:
                                        result = True
                        if height > 247.50:
                            if refuse_handling_fire_protection <= 0.50:
                                if floor_area <= 119.50:
                                    if generator_set <= 0.50:
                                        result = False
                                    if generator_set > 0.50:
                                        result = True
                                if floor_area > 119.50:
                                    result = True
                            if refuse_handling_fire_protection > 0.50:
                                if hazardous_material_stored <= 0.50:
                                    if lpg_installation_with_permit <= 0.50:
                                        result = False
                                    if lpg_installation_with_permit > 0.50:
                                        result = True
                                if hazardous_material_stored > 0.50:
                                    result = False
                    if hazardous_material > 0.50:
                        if floor_area <= 584.50:
                            if total_floor_area <= 2135.50:
                                if boiler_provided <= 0.50:
                                    result = False
                                if boiler_provided > 0.50:
                                    result = True
                            if total_floor_area > 2135.50:
                                if corridor_walls <= 5.50:
                                    result = True
                                if corridor_walls > 5.50:
                                    if height <= 65.50:
                                        result = False
                                    if height > 65.50:
                                        if window <= 2.50:
                                            if main_door <= 3.50:
                                                pass
                                            if main_door > 3.50:
                                                result = False
                                        if window > 2.50:
                                            result = True
                        if floor_area > 584.50:
                            if flooring <= 4.00:
                                result = True
                            if flooring > 4.00:
                                result = False
                if mechanical_hazard > 0.50:
                    if height <= 71.00:
                        if building_age <= 7174.00:
                            if columns <= 0.50:
                                if electrical_hazard <= 0.50:
                                    result = False
                                if electrical_hazard > 0.50:
                                    result = True
                            if columns > 0.50:
                                if height <= 69.00:
                                    if building_age <= 5659.00:
                                        result = True
                                    if building_age > 5659.00:
                                        if hazardous_material <= 0.50:
                                            result = True
                                        if hazardous_material > 0.50:
                                            result = False
                                if height > 69.00:
                                    if hazardous_material <= 0.50:
                                        result = True
                                    if hazardous_material > 0.50:
                                        result = False
                        if building_age > 7174.00:
                            result = False
                    if height > 71.00:
                        if building_age <= 2194.00:
                            if building_age <= 2178.50:
                                if corridor_walls <= 0.50:
                                    if boiler_provided <= 0.50:
                                        result = True
                                    if boiler_provided > 0.50:
                                        if exterior_walls <= 2.00:
                                            result = False
                                        if exterior_walls > 2.00:
                                            result = True
                                if corridor_walls > 0.50:
                                    result = True
                            if building_age > 2178.50:
                                result = False
                        if building_age > 2194.00:
                            result = True


    return result

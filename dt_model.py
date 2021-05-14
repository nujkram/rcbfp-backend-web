def eval_tree(beams, columns, flooring, exterior_walls, corridor_walls, room_partitions, main_stair, window, ceiling, main_door, trusses, roof, defects, checklist_rating, avg_fire_rating, building_age):
     if building_age <= 1374.00:
         if avg_fire_rating <= 4.54:
             if checklist_rating <= 90.00:
                 if exterior_walls <= 4.50:
                     if building_age <= 1232.00:
                         if building_age <= 552.50:
                             if building_age <= 548.50:
                                 if corridor_walls <= 2.50:
                                     result = True
                                 if corridor_walls >  2.50:
                                     if roof <= 3.50:
                                         if exterior_walls <= 3.50:
                                             if avg_fire_rating <= 2.54:
                                                 result = False
                                             if avg_fire_rating >  2.54:
                                                 pass
                                         if exterior_walls >  3.50:
                                             if building_age <= 179.50:
                                                 result = True
                                             if building_age >  179.50:
                                                 result = False
                                     if roof >  3.50:
                                         result = True
                             if building_age >  548.50:
                                 result = False
                         if building_age >  552.50:
                             result = True
                     if building_age >  1232.00:
                         if flooring <= 3.50:
                             result = True
                         if flooring >  3.50:
                             result = False
                 if exterior_walls >  4.50:
                     if columns <= 4.50:
                         if window <= 2.50:
                             if avg_fire_rating <= 2.58:
                                 if building_age <= 765.50:
                                     result = True
                                 if building_age >  765.50:
                                     result = False
                             if avg_fire_rating >  2.58:
                                 result = True
                         if window >  2.50:
                             if checklist_rating <= 62.50:
                                 if building_age <= 648.00:
                                     if checklist_rating <= 52.50:
                                         result = True
                                     if checklist_rating >  52.50:
                                         result = False
                                 if building_age >  648.00:
                                     if roof <= 3.50:
                                         if building_age <= 697.50:
                                             result = True
                                         if building_age >  697.50:
                                             if building_age <= 1147.50:
                                                 result = False
                                             if building_age >  1147.50:
                                                 result = True
                                     if roof >  3.50:
                                         result = True
                             if checklist_rating >  62.50:
                                 result = True
                     if columns >  4.50:
                         if main_door <= 2.50:
                             if checklist_rating <= 55.00:
                                 result = True
                             if checklist_rating >  55.00:
                                 if checklist_rating <= 62.50:
                                     result = False
                                 if checklist_rating >  62.50:
                                     result = True
                         if main_door >  2.50:
                             result = True
             if checklist_rating >  90.00:
                 result = False
         if avg_fire_rating >  4.54:
             if checklist_rating <= 47.50:
                 result = True
             if checklist_rating >  47.50:
                 result = False
     if building_age >  1374.00:
         if flooring <= 2.00:
             if avg_fire_rating <= 1.50:
                 result = False
             if avg_fire_rating >  1.50:
                 if checklist_rating <= 90.00:
                     if building_age <= 1695.00:
                         result = False
                     if building_age >  1695.00:
                         result = True
                 if checklist_rating >  90.00:
                     if building_age <= 14382.00:
                         result = False
                     if building_age >  14382.00:
                         result = False
         if flooring >  2.00:
             result = False

     return result
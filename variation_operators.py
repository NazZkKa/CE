import random
import math

def one_action_flip(ind, len_map):
    mutation_point = random.randint(0,len_map-1)
    action_extra = random.randint(1,3)
    new_action = ind["genotype"][mutation_point]+action_extra
    ind["genotype"][mutation_point]=new_action%4


def line_flip(ind, len_map):
    lines = int(math.sqrt(len_map))
    line_to_mutate = random.randint(0,lines-1)
    prob = random.random()
    if prob <= 0.5:
        for i in range(lines):
            action_extra = random.randint(1,3)
            new_action = ind["genotype"][i + (line_to_mutate*lines)]+action_extra
            ind["genotype"][i + line_to_mutate*lines]=new_action%4
    else:
        for i in range(lines):
            action_extra = random.randint(1,3)
            new_action = ind["genotype"][line_to_mutate + (i * lines)]+action_extra
            ind["genotype"][i + line_to_mutate*lines]=new_action%4

            
def square_flip(ind, len_map):
    
    line_length = int(math.sqrt(len_map))
    
    temp = math.floor((len_map-1)/2)
    
    starting_points = []
    
    if ((len_map-1)/2)%2 == 0:
        starting_points.append(int((len_map-1)/2))
    
    temp2 = 0
    
    while temp2 < temp:
        starting_points.append(temp2)
        temp2+=line_length+1
        
    mutation_point = random.choice(starting_points)
    
    inverse_point = len_map - mutation_point - 1
    
    cycle =line_length - mutation_point%line_length
    
    point1 = mutation_point
    point2 = mutation_point
    point3 = inverse_point
    point4 = inverse_point
    
    points_to_mutate = [mutation_point, inverse_point]
    
    for i in range(cycle-1):
        point1+=line_length
        point2+=1
        point3-=line_length
        point4-=1
        if point1 < inverse_point and point2 < inverse_point and point3 > mutation_point and point4 > mutation_point:
            points_to_mutate.append(point1)
            points_to_mutate.append(point1)
            points_to_mutate.append(point2)
            points_to_mutate.append(point3)
            points_to_mutate.append(point4)
        
        
    points_to_mutate = list(dict.fromkeys(points_to_mutate))
    
    for point in points_to_mutate:
        action_extra = random.randint(1,3)
        new_action = ind["genotype"][point]+action_extra
        ind["genotype"][point]=new_action%4


def one_point(ind1, ind2, genotype,len_map):
    crossing_point = random.randint(0,len_map-1)
    parte1=ind1["genotype"][:crossing_point]
    parte2=ind2["genotype"][crossing_point:]
    genotype[:] = parte1 + parte2


def uniform_crossover(ind1, ind2, genotype,len_map):
    for i in range(len_map):
        prob_swap = random.random()
        if prob_swap < 0.5:
            genotype[i]=ind1["genotype"][i]
        else:
            genotype[i]=ind2["genotype"][i]

############### STRING #####################

def mutations_string(ind):
    prob_type_of_mut = random.random()
    if prob_type_of_mut < 0.5:#delete
        if len(ind["genotype"])>0: 
            local_delete = random.randint(0, len(ind["genotype"])-1)
            ind["genotype"].pop(local_delete)
    else:#flip
        if len(ind["genotype"])>0: 
            local_flip = random.randint(0, len(ind["genotype"])-1)
            action_extra = random.randint(1,3)
            new_action = ind["genotype"][local_flip]+action_extra
            ind["genotype"][local_flip]=new_action%4

def one_point_string(ind1, ind2, genotype, len_map):
    if len(ind1['genotype']) > 1:
        cut_point1 = random.randint(0, len(ind1["genotype"])-1)
        if cut_point1 > len_map/2:
            cut_point1 = random.randint(0, len_map)
        part1 = ind1["genotype"][0:cut_point1]
    else:
        part1 = [ind1["genotype"][0]]
    
    if len(ind2['genotype']) > 1:
        cut_point2 = random.randint(0, len(ind2["genotype"])-1)
        if cut_point2 > len_map/2:
            cut_point2 = random.randint(0, len_map)
        part2 = ind2["genotype"][len(ind2['genotype'])-cut_point2:len(ind2['genotype'])]
    else:
        part2 = [ind2["genotype"][0]]

    genotype[:]= part1 + part2
        
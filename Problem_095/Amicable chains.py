from time import time
from urllib import request
from copy import deepcopy
from itertools import combinations


def eliminator(array, n):
    if n < 3:
        for nn in range(3):
            array[nn] = -1
    elif n < 6:
        for nn in range(3):
            array[nn + 3] = -1
    else:
        for nn in range(3):
            array[nn + 6] = -1
    return array


def check_rows(matrix):
    global update_flag
    for j in range(3):
        rows = matrix[3*j:3*j+3]
        for i in range(1, 10):
            columns_to_check = list(range(9))
            for row in rows:
                if i in row:
                    columns_to_check = eliminator(columns_to_check, row.index(i))
                else:
                    row_to_check = row
            columns_to_check = list(filter(lambda a: a != -1, columns_to_check))
            if len(columns_to_check) == 3:
                for index in reversed(columns_to_check):
                    if type(row_to_check[index]) != list:
                        columns_to_check.remove(index)
                        continue
                    else:
                        if i in [item[index] for item in matrix]:
                            columns_to_check.remove(index)
                            continue
            if len(columns_to_check) == 1:
                matrix[matrix.index(row_to_check)][columns_to_check.pop()] = i
                update_flag = 1
    return matrix


def check_columns(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = check_rows(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def slicer(m, n):
    limits = []
    for i in (m, n):
        if i < 3:
            limits.append((0, 3))
        elif i < 6:
            limits.append((3, 6))
        else:
            limits.append((6, 9))
    return limits


def check_row_singular(matrix):
    global update_flag
    for row in matrix:
        candidates = []
        indexes = []
        index_count = 0
        for item in row:
            if type(item) == list:
                candidates += item
                indexes.append(index_count)
            index_count += 1
        candidates = list(set(candidates))
        for candidate in candidates:
            subset = []
            for index in indexes:
                if candidate in row[index]:
                    subset.append(index)
                if len(subset) > 1:
                    break
            if len(subset) == 1:
                matrix[matrix.index(row)][subset[0]] = candidate
                # Update candidates in column
                for a in matrix:
                    if type(a[subset[0]]) == list and candidate in a[subset[0]]:
                        matrix[matrix.index(a)][subset[0]].remove(candidate)
                # Update candidates in box
                box_limits = slicer(matrix.index(row), subset[0])
                for k in range(box_limits[0][0], box_limits[0][1]):
                    for z in range(box_limits[1][0], box_limits[1][1]):
                        element = matrix[k][z]
                        if type(element) == list and candidate in element:
                            matrix[k][matrix[k].index(element)].remove(candidate)
                indexes.remove(subset.pop())
                update_flag = 1
    return matrix


def check_column_singular(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = check_row_singular(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def check_box_singular(matrix):
    global update_flag
    for i in range(3):
        for j in range(3):
            box = matrix[3 * i: 3 * i + 3]
            for k in range(len(box)):
                box[k] = box[k][3*j: 3*j+3]
            candidates = []
            indexes = []
            for m in range(3):
                for n in range(3):
                    if type(box[m][n]) == list:
                        candidates += box[m][n]
                        indexes.append((m, n))
            candidates = set(candidates)
            for candidate in candidates:
                subset = []
                for index in indexes:
                    if candidate in box[index[0]][index[1]]:
                        subset.append(index)
                    if len(subset) > 1:
                        break
                if len(subset) == 1:
                    matrix[3*i + subset[0][0]][3*j + subset[0][1]] = candidate
                    # Update candidates in column
                    for a in matrix:
                        if type(a[3 * j + subset[0][1]]) == list and candidate in a[3 * j + subset[0][1]]:
                            matrix[matrix.index(a)][3 * j + subset[0][1]].remove(candidate)
                    # Update candidates in row
                    for element in matrix[3*i + subset[0][0]]:
                        if type(element) == list and candidate in element:
                            matrix[3*i + subset[0][0]][matrix[3*i + subset[0][0]].index(element)].remove(candidate)
                    indexes.remove(subset.pop())
                    update_flag = 1
    return matrix


def assign_single_candidates(matrix):
    while True:
        global update_flag
        update_flag = 0
        for i in range(9):
            for j in range(9):
                if type(matrix[i][j]) == list and len(matrix[i][j]) == 1:
                    candidate = matrix[i][j].pop()
                    update_flag = 1
                    matrix[i][j] = candidate
                    # Update candidates in row
                    for element in matrix[i]:
                        if type(element) == list and candidate in element:
                            matrix[i][matrix[i].index(element)].remove(candidate)
                    # Update candidates in column
                    for a in matrix:
                        if type(a[j]) == list and candidate in a[j]:
                            matrix[matrix.index(a)][j].remove(candidate)
                    # Update candidates in box
                    box_limits = slicer(i, j)
                    for k in range(box_limits[0][0], box_limits[0][1]):
                        for z in range(box_limits[1][0], box_limits[1][1]):
                            element = matrix[k][z]
                            if type(element) == list and candidate in element:
                                matrix[k][z].remove(candidate)

                    # for m in range(9):
                    #     for n in range(9):
                    #         if type(matrix[m][n]) == list and len(matrix[m][n]) == 0:
                    #             print("me")
        if update_flag == 0:
            matrix = update_candidate_matrix(matrix)
            if update_flag == 0:
                return matrix


def singularity_check(matrix):
    while True:
        global update_flag
        update_flag = 0
        matrix = check_row_singular(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        matrix = assign_single_candidates(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        matrix = check_column_singular(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        matrix = assign_single_candidates(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        matrix = check_box_singular(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        matrix = assign_single_candidates(matrix)
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)
        if update_flag == 0:
            return matrix


def deterministic_check(matrix):
    while True:
        global update_flag
        update_flag = 0
        matrix = check_rows(matrix)
        matrix = check_columns(matrix)
        if update_flag == 0:
            return matrix
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)


def update_candidate_matrix(matrix):
    global update_flag
    while True:
        update_flag = 0
        removal_set = []
        for i in range(9):
            for j in range(9):
                if type(matrix[i][j]) == list:
                    # Column
                    for row in matrix:
                        if type(row[j]) == int and row[j] in matrix[i][j]:
                            removal_set.append(row[j])
                    # Row
                    for element in matrix[i]:
                        if type(element) == int and element not in removal_set and element in matrix[i][j]:
                            removal_set.append(element)
                    # Box
                    box_limits = slicer(i, j)
                    for k in range(box_limits[0][0], box_limits[0][1]):
                        for z in range(box_limits[1][0], box_limits[1][1]):
                            element = matrix[k][z]
                            if type(element) == int and element not in removal_set and element in matrix[i][j]:
                                removal_set.append(element)
                    while removal_set:
                        matrix[i][j].remove(removal_set.pop())
                    if len(matrix[i][j]) == 1:
                        matrix[i][j] = matrix[i][j].pop()
                        update_flag = 1
        if update_flag == 0:
            return matrix
        flag = 1
        for item in matrix[0][:3]:
            if type(item) == list:
                flag = 0
                break
        if flag:
            number = ""
            for digit in matrix[0][:3]:
                number += str(digit)
            return int(number)


def intersection_removal_column_to_box(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = intersection_removal_row_to_box(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def intersection_removal_row_to_box(matrix):
    global update_flag
    for row in matrix:
        candidates = {}
        for index in range(9):
            element = row[index]
            if type(element) == list:
                for num in element:
                    if num not in candidates.keys():
                        candidates[num] = [index]
                    else:
                        candidates[num].append(index)
        for num, indexes in candidates.items():
            if set(indexes) <= {0, 1, 2}:
                box_limits = slicer(matrix.index(row), 0)
            elif set(indexes) <= {3, 4, 5}:
                box_limits = slicer(matrix.index(row), 3)
            elif set(indexes) <= {6, 7, 8}:
                box_limits = slicer(matrix.index(row), 6)
            else:
                continue
            for k in range(box_limits[0][0], box_limits[0][1]):
                if row == matrix[k]:
                    continue
                for z in range(box_limits[1][0], box_limits[1][1]):
                    if type(matrix[k][z]) == list and num in matrix[k][z]:
                        matrix[k][z].remove(num)
                        update_flag = 1
    return matrix


def intersection_removal_box_to_row(matrix):
    global update_flag
    for m in range(3):
        for n in range(3):
            box_limits = slicer(3*m, 3*n)
            candidates = {}
            for x in range(box_limits[0][0], box_limits[0][1]):
                for y in range(box_limits[1][0], box_limits[1][1]):
                    element = matrix[x][y]
                    if type(element) == list:
                        for num in element:
                            if num not in candidates.keys():
                                candidates[num] = [x]
                            else:
                                candidates[num].append(x)
            for num, indexes in candidates.items():
                if len(set(indexes)) == 1:
                    for element in matrix[indexes[0]]:
                        if matrix[indexes[0]].index(element) < box_limits[1][0] or \
                                matrix[indexes[0]].index(element) >= box_limits[1][1]:
                            if type(element) == list and num in element:
                                matrix[indexes[0]][matrix[indexes[0]].index(element)].remove(num)
                                update_flag = 1
    return matrix


def intersection_removal_box_to_column(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = intersection_removal_box_to_row(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def naked_pairs_column(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = naked_pairs_row(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def naked_pairs_row(matrix):
    global update_flag
    for row in matrix:
        for m in range(9):
            for n in range(m+1, 9):
                if row[m] == row[n] and len(row[m]) == 2:
                    for num in row[m]:
                        for p in range(9):
                            if p != m and p != n:
                                if type(row[p]) == list and num in row[p]:
                                    matrix[matrix.index(row)][p].remove(num)
                                    update_flag = 1
                    break
    return matrix


def x_wing_row(matrix):
    global update_flag
    for m in range(9):
        candidates = {}
        for element in matrix[m]:
            if type(element) == list:
                for num in element:
                    if num not in candidates.keys():
                        candidates[num] = [matrix[m].index(element)]
                    else:
                        candidates[num].append(matrix[m].index(element))
        for num, indexes in candidates.items():
            if len(indexes) == 2:
                for row_index in range(m+1, 9):
                    element = matrix[row_index][indexes[0]]
                    if type(element) == list and num in element:
                        if type(matrix[row_index][indexes[1]]) == list and \
                                num in matrix[row_index][indexes[1]]:
                            count = 0
                            for item in matrix[row_index]:
                                if type(item) == list and num in item:
                                    count += 1
                            if count == 2:
                                row_indexes = list(range(m+1, 9))
                                row_indexes.remove(row_index)
                                for index in row_indexes:
                                    for ind in indexes:
                                        if type(matrix[index][ind]) == list and num in matrix[index][ind]:
                                            matrix[index][ind].remove(num)
                                            update_flag = 1
    return matrix


def naked_triplet_row(matrix):
    global update_flag
    for row in matrix:
        candidates = []
        ambiguous = []
        index_count = 0
        for element in row:
            if type(element) == list:
                ambiguous.append(index_count)
                for num in element:
                    if num not in candidates:
                        candidates.append(num)
            index_count += 1
        if len(candidates) > 3:
            candidate_combinations = list(combinations(candidates, 3))
            for combination in candidate_combinations:
                count = 0
                to_be_updated = []
                for index in ambiguous:
                    if set(row[index]) <= set(combination):
                        count += 1
                    else:
                        to_be_updated.append(index)
                if count == 3:
                    for index in to_be_updated:
                        for num in combination:
                            if num in row[index]:
                                matrix[matrix.index(row)][index].remove(num)
                                update_flag = 1
    return matrix


def naked_triplet_column(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = naked_triplet_row(transposed_matrix)
    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def solve_sudoku(matrix):
    all_numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if not matrix[i][j]:
                matrix[i][j] = deepcopy(all_numbers)
    count = 0
    while True:
        update_flag = 0
        matrix = deterministic_check(matrix)
        if type(matrix) == int:
            return matrix
        matrix = update_candidate_matrix(matrix)
        if type(matrix) == int:
            return matrix
        matrix = singularity_check(matrix)
        if type(matrix) == int:
            return matrix
        if update_flag == 0:
            count += 1
        else:
            count = 0
        if count:
            matrix = intersection_removal_row_to_box(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
            matrix = intersection_removal_column_to_box(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
            matrix = naked_pairs_row(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
            matrix = naked_pairs_column(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
        if count > 1:
            matrix = intersection_removal_box_to_row(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
            matrix = intersection_removal_box_to_column(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
        if count > 2:
            matrix = x_wing_row(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
        if count > 3:
            matrix = naked_triplet_row(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
            matrix = naked_triplet_column(matrix)
            matrix = singularity_check(matrix)
            if type(matrix) == int:
                return matrix
        if count == 20:
            return 0


start = time()
data = request.urlopen("https://projecteuler.net/project/resources/p096_sudoku.txt")
puzzle = []
total = 0
password = ''
for line in data:
    line = line.decode("utf-8")
    if "\n" not in line:
        break
    line = line.replace("\n", "")
    if "Grid 01" in line:
        continue
    elif "Grid" in line:
        total += solve_sudoku(puzzle)
        puzzle.clear()
        continue
    puzzle.append(list(map(int, line)))
puzzle.append(list(map(int, line)))
total += solve_sudoku(puzzle)
print(total)
end = time()
print("Time elapsed", end - start, "seconds")

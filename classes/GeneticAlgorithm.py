from typing import Callable, TypeVar, List, Tuple

import more_itertools

_T = TypeVar("_T")

PARENT_COUNT_NEEDED_FOR_REPRODUCTION = 2


def genetic_algorithm(scoring_function: Callable[[_T], int],
                      mutation_function: Callable[[_T, int], _T],
                      crossover_function: Callable[[_T, _T, int], List[_T]],
                      selection_function: Callable[[List[_T], List[int]], List[_T]],
                      generations_count: int,
                      population: List[_T],
                      crossover_probability: int,
                      mutation_probability: int):

    evolved = []
    for generation in range(generations_count):
        scores = [scoring_function(person) for person in population]
        selected_parents = selection_function(population, scores)
        new_generation = list()
        for parent_1, parent_2 in more_itertools.chunked(selected_parents, PARENT_COUNT_NEEDED_FOR_REPRODUCTION):
            new_generation += [mutation_function(child, mutation_probability) for child in
                               crossover_function(parent_1, parent_2, crossover_probability)]
        evolved = new_generation
    return evolved[max(range(len(evolved)), key=lambda idx: scoring_function(evolved[idx]))]

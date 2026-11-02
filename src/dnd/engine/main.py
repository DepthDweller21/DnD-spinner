import random

from .utils.debug import *
from .utils.loadFile import *


def applyGraph(algorithm,weights,step):
    if algorithm == "uniform":
        return weights
    elif algorithm == "linear":
        return [weight + (index * step) for index, weight in enumerate(weights)]
    elif algorithm == "negative-linear":
        return [max(0, weight - (index * step)) for index, weight in enumerate(weights)]


def calculateWeightage(count,algorithm,step):
    # step 1: pre algorithm weight modification
    # step 2: algorithm weight modification
    # step 3: post algorithm weight modification
    # step 4: modifier based weight modification (categories)
    # step 5: post modifier weight modification
    # step 6: set percentage item/category weightage
    weights = [100]*count
    weights = applyGraph(algorithm,weights,step)
    return weights
    


def selectRandom(value,algorithm,step=0):
    data = load(value)
    roll = random.choices(
        data,
        weights=calculateWeightage(len(data),algorithm,step)
    )[0]
    print(f"{value}: {roll["tag"]}")
    roll["category"]=value
    return roll


def start() -> list:
    rolls=[]
    rolls.append(selectRandom("race","uniform"))
    rolls.append(selectRandom("speed","uniform"))
    rolls.append(selectRandom("strength","uniform"))
    rolls.append(selectRandom("defence","uniform"))
    rolls.append(selectRandom("smart","uniform"))
    rolls.append(selectRandom("fight","uniform"))
    rolls.append(selectRandom("weapon","uniform"))
    rolls.append(selectRandom("weaponMastery","uniform"))
    rolls.append(selectRandom("archetype","uniform"))
    return rolls

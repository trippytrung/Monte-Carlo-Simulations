import random

def dice_sum():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    d5 = random.randint(1,6)
    sum = d1+d2+d3+d4+d5
    return sum

def monte_carlo_simulation(num_simulations):
    num_of_16 = 0
    num_of_20 = 0
    for i in range(num_simulations):
        sum_of_faces = dice_sum()
        if sum_of_faces == 16:
            num_of_16 += 1
        elif sum_of_faces == 20:
            num_of_20 += 1
    odds_of_16 = num_of_16 / num_simulations
    odds_of_20 = num_of_20 / num_simulations

    return odds_of_16, odds_of_20

num_simulations = 100000
odds_of_16, odds_of_20 = monte_carlo_simulation(num_simulations)

if odds_of_16 > odds_of_20:
    print("The probability of getting a sum of 16 ("+str(odds_of_16)+") is bigger than the probability of getting a sum of 20 ("+str(odds_of_20)+").")
else:
    print("The probability of getting a sum of 16 ("+str(odds_of_16)+") is not bigger than the probability of getting a sum of 20 ("+str(odds_of_20)+").")
  
##
## This prints "The probability of getting a sum of 16 (0.09363) is bigger than the probability of getting a sum of 20 (0.08323)."
##

num_simulations = 1000000
count = 0
for i in range(num_simulations):
    if (random.random() < 1/5) and (random.random() < 1/5) and (random.random() > 1/3) and (random.random() > 1/3):
      count += 1
prob = count / num_simulations
print("Odds of rain:", 1 - prob)

##
## This prints "Odds of rain: 0.982157"
##

def atlanta(num_simulations):
  total_distance = 0
  for i in range(num_simulations):
    alanta_stlouis_blocked = random.choice([True,False])

    if alanta_stlouis_blocked:
      distance = 866 + 470 + 505
    else:
      distance = 866 + 555 + 662
    total_distance += distance

    average_distance = total_distance/num_simulations

  return average_distance

def nashville(num_simulations):
  total_distance = 0
  for i in range(num_simulations):
    nashville_stlouis_blocked = random.choice([True,False])

    if nashville_stlouis_blocked:
      distance = 900 + 532 + 505
    else:
      distance = 900 + 309 + 662
    total_distance += distance

    average_distance = total_distance/num_simulations

  return average_distance

print(atlanta(1000000))
print(nashville(1000000))

if atlanta(1000000) < nashville(1000000):
    print("Mad Max should start toward Atlanta")
else:
    print("Mad Max should start toward Nashville")

##
## 1961.937806
## 1903.988846
## Mad Max should start toward Nashville
##

from scipy.stats import norm
X = norm.rvs(size = 1000000, loc = 4, scale = 3)
probability = sum((X > -1)&(X < 2)) / 1000000
print(probability)

##
## 0.204506
##


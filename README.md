# Ecological Ocean Simulation Model: Predators, Prey, and Obstacles

## Description
This repository contains a simple ecological simulation model of an ocean ecosystem. The model includes three main types of objects: predators, prey, and obstacles. The simulation aims to model the interaction between these objects based on predefined rules.

### Objects in the Simulation
1. Predators (e.g., Sharks): Predators are entities that hunt and consume prey. They have a predation rate that determines how many prey they can capture in a simulation step. Predators can also reproduce and increase their population.

2. Prey (e.g., Fish): Prey represents the animals that serve as food for predators. They have a growth rate that determines how fast their population can increase. Prey can also die due to various factors.

3. Obstacles: Obstacles are natural or artificial elements that can affect the dynamics of the ecosystem. Unlike barriers, obstacles do not completely block predators; instead, they alter their behavior or movement patterns.

## How the Simulation Works
The simulation is implemented in Python and follows these basic steps for each simulation iteration:

1. Predators hunt prey based on their predation rate, reducing the prey population accordingly.
2. Prey species reproduce, increasing their population based on the growth rate.
3. 3Predators reproduce, increasing their population by a fixed percentage.
4. Some individuals of both predator and prey populations may die based on predefined factors.
5. Predators interact with obstacles, which may influence their hunting patterns or population dynamics.

## License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute this simulation model following the terms of the MIT License.

## Acknowledgments
This simulation model was created for educational purposes to demonstrate a basic ecological interaction between predators, prey, and obstacles in an ocean ecosystem. It may not accurately represent real-world ecological systems and is intended as a simple learning tool.
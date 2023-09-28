# FlappyBirdAI

*Project is based on the FlappyBird AI created by TechWithTim*
* [Flappy Bird AI Tutorial Playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2)
* [TechWithTim NEAT-Flappy-Bird Github Repo](https://github.com/techwithtim/NEAT-Flappy-Bird)

### Repository Contents
* Flappy Bird implementation in Python using pygame
* Flappy Bird AI implemented using the neat-python library

![NEAT Flappy Bird AI](/readme_imgs/img1.jpg?raw=true "NEAT Flappy Bird AI")

* Inputs: bird location, top pipe location, bottom pipe location
* Outputs: jump or don't jump

Since Flappy Bird is a relatively simple game, given a large population size, the NEAT AI often creates an optimal bird in the first or second generation that is able to play Flappy Bird to infinity. A simple fitness function which optimizes for horizontal distance travelled is all that is required to produce this result.   

### Next Steps
* NEAT implementation without using neat-python library
* Visualization of input, output, and hidden nodes + connections between nodes used in the AI

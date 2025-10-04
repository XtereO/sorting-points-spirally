## About this project

This project contains module which allows to sort some points in flat XY spirally. This module is tested (there are at least 10 cases).

![alt text](doc_imgs/algorithm_purpose.png)

## Idea of the algorithm

At the start we pick pivot point that should be connected to a next point (at the start we take the most left point, in case there are two such points we take the most down one). After that algorithm consists of three major steps:

- Step 1: shifting points at the center of cartesian system

![alt text](doc_imgs/algorithm_step1.png)

- Step 2: rotating points with the angle that is required to rotate our pivot point to the axis x

![alt text](doc_imgs/algorithm_step2.png)

- Step 3: pick a next point with the biggest angle (atan2 is used to define angles)

![alt text](doc_imgs/algorithm_step3.png)

After that we use the picked point as a new pivot point and repeat steps 1, 2, 3 without using connected points until unconnected points left.

## Mini-usage documentation
documentation in process...

## Covered tests
| № | Test title | Input | Output |
|---|----|-----|-----------|
| 1 | Simple square | ![alt text](doc_imgs/test_input_simple_square.png) | ![alt text](doc_imgs/test_output_simple_square.png) |
| 2 | Simple curve | ![alt text](doc_imgs/test_input_simple_curve.png) | ![alt text](doc_imgs/test_output_simple_curve.png) |
| 3 | Curve | ![alt text](doc_imgs/test_input_curve.png) | ![alt text](doc_imgs/test_output_curve.png) |
| 4 | Square | ![alt text](doc_imgs/test_input_square.png) | ![alt text](doc_imgs/test_output_square.png) |
| 5 | Horizontal line | ![alt text](doc_imgs/test_input_horizontal_line.png) | ![alt text](doc_imgs/test_output_horizontal_line.png) |
| 6 | Vertical line | ![alt text](doc_imgs/test_input_vertical_line.png) | ![alt text](doc_imgs/test_output_vertical_line.png) |
| 7 | Shifted points | ![alt text](doc_imgs/test_input_shifted_points.png) | ![alt text](doc_imgs/test_output_shifted_points.png) |
| 8 | Similar points on flat xy | ![alt text](doc_imgs/test_input_similar_points_xy.png) | ![alt text](doc_imgs/test_output_similar_points_xy.png) |
| 9 | Four-grouped points | ![alt text](doc_imgs/test_input_four_grouped_points.png) | ![alt text](doc_imgs/test_output_four_grouped_points.png) |
| 10 | Spiral in one area | ![alt text](doc_imgs/test_input_spiral_in_one_area.png) | ![alt text](doc_imgs/test_output_spiral_in_one_area.png) |

## Setup launching

First you should define virtual environment (base module venv of python is used), in the root directory of project run these commands in your terminal to create and activate virtual environment:

`python -m venv venv`

`.\venv\Scripts\activate`

After that run command to install required packages for this projects:

`pip install -r req.txt`

Then run `pip install -e .` in the root of project so you can setup "importing" paths between folders src and tests.

To run tests you should run this command in the root of project:

`pytest tests`

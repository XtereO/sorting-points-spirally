## About this project

This project contains the module which allows to sort some points in flat XY spirally. This module is tested (there are at least 10 cases).

![alt text](doc_imgs/algorithm_purpose.png)

## Idea of the algorithm

At the start we pick a pivot point that should be connected to a next point (we take the most left point along the axis x, in case there are two such points we take the lowest point along the axis y). After that the algorithm consists of three major steps:

- Step 1: shifting points at the center of cartesian system

![alt text](doc_imgs/algorithm_step1.png)

- Step 2: rotating points with the angle that is required to rotate our pivot point to the axis x

![alt text](doc_imgs/algorithm_step2.png)

- Step 3: picking a next point with the biggest angle (atan2 is used to define angles)

![alt text](doc_imgs/algorithm_step3.png)

After that we use the picked point as a new pivot point and repeat the steps 1, 2, 3 without using connected points until unconnected points left.

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

## Mini-usage documentation

This project contains the function `sort_points_spirally` in the src/main.py. There is the description of inputs, outputs and example for this function in this section.

### Inputs

`points: List[List[float]]` is the first argument of the function, it should be a list of points e.g. `[[-2, -2, 1], [-1.9, -1, 1]]`.

`showing_result: boolean` is the second argument of the function if it is `True` then the function will also show a result as a plot (a scattered plot of input `points` and then a plot of output as connections of ordered points). By default it is `False`.

### Outputs

`points_order: List[int]` is a list of indexes which show index of input `points`. For example, `[1, 0]` means that a first point is a point with index 1 of input `points` so to get this point you can access it by this index e.g. `points[1]`.

### Example
```
points = [[-2, -2, 1], [-1.9, -1, 1], [-1.5, 0, 1], [-1, 1, 0], [ 0, 1.2, 0], [1, 0.8, 0], [1.5, 0, 0], [1, -1, 0], [0, -0.7, 0], [0, 0, 0], [0.1, 0, 0]]

points_order = sort_points_spirally(points, True)
# result is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# it has True as a second arg so it also will show the result as a plot
```

## Setup launching

First you should define a virtual environment (basic module venv of python is used), in the root directory of the project run these commands in your terminal to create and activate the virtual environment:

`python -m venv venv`

`.\venv\Scripts\activate`

After that run the following command to install required packages for this projects:

`pip install -r req.txt`

Then run `pip install -e .` in the root of the project so you can setup the "importing" paths between the folders src and tests.

To run all tests you should run this command in the root of the project:

`pytest tests`

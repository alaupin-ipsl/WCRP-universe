Grid properties are specific to the native grid of each model component on which the component is integrated.

The horizontal and vertical parts of the grid are described with a standardised specification that is based on selections from controlled vocabularies or the provision of numerical values. 

There are many properties in the grid descriptions, but only a subset will apply to any given grid. For instance, a regular latitude-longitude grid does not need to provide any of the spectral grid truncation properties.

**Note:** _A model component may output variables on non-native grids (such as data on constant pressure levels from a model component with a terrain-following native vertical grid), or its output variables may be post-processed to non-native grids for storage in archived datasets (such as data interpolated to a regular 1 degree grid from a model component with a variable resolution native horizontal grid). However, it is always the native grid on which the model component is integrated that is requested here._

# EMD Controlled Vocabularies - Status Report

This document lists all controlled vocabularies defined in the Essential Model Documentation (EMD) v0.992 and identifies which ones have corresponding folders in the WCRP universe structure.

## Controlled Vocabularies in EMD Document

### Section 7.1 - **component** CV
Component types describing sets of interactive processes simulated by model components.

**Status: ✅ IMPLEMENTED as `model-component-type`**

**Options:**
- aerosol - *The behaviour and evolution of aerosols suspended in the atmosphere*
- atmosphere - *Dynamical, thermodynamical, and physical processes in the atmosphere*
- atmospheric_chemistry - *The behaviour and evolution of the chemical composition of the atmosphere*
- land_surface - *Water, energy, and mass fluxes between the surface and the atmosphere*
- land_ice - *Frozen freshwater in glaciers, ice-caps, ice-sheets, and ice-shelves*
- ocean - *Dynamical, thermodynamical, and physical processes in the ocean*
- ocean_biogeochemistry - *Biological, geological, and chemical processes in the ocean*
- sea_ice - *Frozen seawater that floats on the ocean surface*

### Section 7.2 - **calendar** CV
Calendar types defining valid dates and times.

**Status: ✅ IMPLEMENTED as `model-calendar`**

**Options:**
- standard - *Mixed Gregorian/Julian calendar*
- proleptic_gregorian - *Gregorian rules extended to dates before 1582-10-15*
- julian - *Julian calendar with leap years divisible by 4*
- 360_day - *All years are 360 days, divided into 30 day months*
- 365_day - *All years are 365 days with no leap years*
- 366_day - *All years are 366 days (every year is a leap year)*
- none - *No calendar*

### Section 7.3 - **grid** CV
Horizontal grid types describing methods for distributing grid points over the sphere.

**Status: ❌ MISSING - Should be `native-horizontal-grid-type` or `grid-type`**

**Options:**
- regular_latitude_longitude - *Rectilinear lat-lon grid with evenly spaced points*
- regular_gaussian - *Gaussian grid with constant longitudinal points*
- reduced_gaussian - *Gaussian grid with reduced longitudinal points near poles*
- spectral_gaussian - *Grid based on transformation from spectral space*
- spectral_reduced_gaussian - *Spectral transformation to reduced Gaussian*
- linear_spectral_gaussian - *Smallest wavelength represented by 2 grid points*
- quadratic_spectral_gaussian - *Smallest wavelength represented by 3 grid points*
- cubic_octahedral_spectral_reduced_gaussian - *4 grid points, octahedron-based reduction*
- rotated_pole - *Regular lat-lon grid with different north pole location*
- stretched - *Higher resolution over area of interest*
- displaced_pole - *Ocean grid with poles over land*
- tripolar - *Global curvilinear ocean grid with three poles over land*
- cubed_sphere - *Six coupled logically square regions*
- icosahedral_geodesic - *Triangular tiles from subdivided icosahedron*
- icosahedral_geodesic_dual - *Hexagonal/pentagonal tiles, dual of icosahedral*
- yin_yang - *Two overlapping grid patches*
- unstructured_triangular - *Unstructured mesh of triangles*
- unstructured_polygonal - *Unstructured mesh of arbitrary polygons*
- plane_projection - *Transformation of spherical surface to plane*
- none - *No horizontal grid*

### Section 7.4 - **grid_mapping** CV
Horizontal grid mappings (coordinate reference systems).

**Status: ❌ MISSING - Should be `native-horizontal-grid-grid-mapping`**

**Options:**
- albers_conical_equal_area
- azimuthal_equidistant
- geostationary
- lambert_azimuthal_equal_area
- lambert_conformal_conic
- lambert_cylindrical_equal_area
- latitude_longitude
- orthographic
- polar_stereographic
- rotated_latitude_longitude
- sinusoidal
- stereographic
- transverse_mercator
- vertical_perspective

### Section 7.5 - **region** CV
Horizontal grid regions (contiguous parts of Earth's surface).

**Status: ✅ IMPLEMENTED as `native-horizontal-grid-region`**

**Options:**
- antarctica - *Geographical region of Antarctica*
- global - *Whole Earth's surface*
- greenland - *Geographical region of Greenland*
- limited_area - *Any contiguous subregion of Earth's surface*

### Section 7.6 - **temporal_refinement** CV
How grid cell distribution varies with time.

**Status: ✅ IMPLEMENTED as `native-horizontal-grid-temporal-refinement`**

**Options:**
- static - *Grid points stay constant, no refinement*
- dynamically_stretched - *Constant number of points, dynamically relocated*
- adaptive - *Variable number of points, refined/coarsened as needed*

### Section 7.7 - **arrangement** CV
Relative locations of mass- and velocity-related quantities on computed grid.

**Status: ❌ MISSING - Should be `native-horizontal-grid-arrangement`**

**Options:**
- arakawa_a - *Mass and velocity at same location*
- arakawa_b - *Velocity at corners of mass cells*
- arakawa_c - *Velocity at centers of mass cell edges, perpendicular*
- arakawa_d - *Velocity at centers of mass cell edges, tangential*
- arakawa_e - *Mass at centers of velocity cell edges*

### Section 7.8 - **horizontal_units** CV
Physical units of horizontal grid resolution values.

**Status: ❌ MISSING - Should be `native-horizontal-grid-units` or `horizontal-units`**

**Options:**
- km - *kilometre (unit for length)*
- degree - *degrees (unit for angular measure)*

### Section 7.9 - **truncation_method** CV
Truncation methods for spherical harmonic representation.

**Status: ❌ MISSING - Should be `native-horizontal-grid-truncation-method`**

**Options:**
- triangular - *Triangular truncation*
- rhomboidal - *Rhomboidal truncation*

### Section 7.10 - **nominal_resolution** CV
Nominal resolution categories based on mean resolution.

**Status: ❌ MISSING - Should be `native-horizontal-grid-nominal-resolution`**

**Options:**
Range-based mapping from mean_resolution_km to nominal categories (0.05 km to 10000 km)

### Section 7.11 - **coordinate** CV
Vertical grid coordinate types (vertical coordinate reference systems).

**Status: ✅ IMPLEMENTED as `native-vertical-grid-coordinate`**

**Options:**
- none - *No vertical dimension*
- height - *Vertical distance above earth's surface*
- geopotential_height - *Geopotential divided by standard gravity*
- air_pressure - *Pressure in air medium*
- air_potential_temperature - *Temperature if moved dry adiabatically*
- atmosphere_ln_pressure_coordinate - *Parametric atmosphere ln pressure*
- atmosphere_sigma_coordinate - *Parametric atmosphere sigma*
- atmosphere_hybrid_sigma_pressure_coordinate - *Parametric hybrid sigma pressure*
- atmosphere_hybrid_height_coordinate - *Parametric hybrid height*
- atmosphere_sleve_coordinate - *Parametric smooth vertical level*
- depth - *Vertical distance below earth's surface*
- sea_water_pressure - *Pressure in sea water medium*
- sea_water_potential_temperature - *Temperature if moved adiabatically*
- ocean_sigma_coordinate - *Parametric ocean sigma*
- ocean_s_coordinate - *Parametric ocean s-coordinate*
- ocean_s_coordinate_g1 - *Parametric ocean s-coordinate, generic form 1*
- ocean_s_coordinate_g2 - *Parametric ocean s-coordinate, generic form 2*
- ocean_sigma_z_coordinate - *Parametric ocean sigma over z*
- ocean_double_sigma_coordinate - *Parametric ocean double sigma*
- land_ice_sigma_coordinate - *Land ice sigma coordinate*
- z_star - *z* coordinate of Adcroft and Campin (2004)*

### Section 7.12 - **vertical_units** CV
Physical units of vertical grid measurements.

**Status: ✅ IMPLEMENTED as `native-vertical-grid-units`**

**Options:**
- m - *metre (unit for length)*
- Pa - *pascal (unit for pressure)*
- K - *kelvin (unit for temperature)*

## Summary

### ✅ IMPLEMENTED (8 out of 12):
1. `model-component-type` (component CV)
2. `model-calendar` (calendar CV)
3. `native-horizontal-grid-region` (region CV)
4. `native-horizontal-grid-temporal-refinement` (temporal_refinement CV)
5. `native-vertical-grid-coordinate` (coordinate CV)
6. `native-vertical-grid-units` (vertical_units CV)
7. `resolution` (related to nominal_resolution CV)
8. `realm` (related but distinct from component CV)

### ❌ MISSING (4 out of 12):
1. **grid** CV - Should be implemented as `native-horizontal-grid-type`
2. **grid_mapping** CV - Should be implemented as `native-horizontal-grid-grid-mapping`
3. **arrangement** CV - Should be implemented as `native-horizontal-grid-arrangement`
4. **horizontal_units** CV - Should be implemented as `native-horizontal-grid-units`
5. **truncation_method** CV - Should be implemented as `native-horizontal-grid-truncation-method`
6. **nominal_resolution** CV - Should be implemented as `native-horizontal-grid-nominal-resolution`

Note: Some of these have placeholder folders in the `/empty/` directory but are not yet fully implemented.

## Additional Existing Folders Not in EMD CVs:
- `activity` - Climate modeling activities/experiments
- `frequency` - Temporal sampling frequency
- `grid-label` - Grid configuration labels
- `license` - Licensing terms
- `mip` - Model Intercomparison Projects
- `organisation` - Institutions/organizations
- `product` - Output product types
- `source-type` - Model type/configuration classification
- `model-family` - Model family groupings



<section id="description">

# Native Vertical Grid Coordinate  (universal)



## Description
Defines the vertical coordinate systems used by model components, based on the EMD coordinate controlled vocabulary (e.g., height, air_pressure, ocean_s_coordinate, land_ice_sigma_coordinate).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate/native-vertical-grid-coordinate)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:native-vertical-grid-coordinate` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-vertical-grid-coordinate` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate](https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-coordinate) |


</section>
    No external links found. 
<section id="schema">

## Content Schema

- **`id`**  
   [**unknown**]
  No Pydantic model found.
- **`validation-key`**  
   [**unknown**]
  No Pydantic model found.
- **`ui-label`**  
   [**unknown**]
  No Pydantic model found.
- **`description`**  
   [**unknown**]
  No Pydantic model found.
- **`@context`**  
   [**unknown**]
  No Pydantic model found.
- **`type`**  
   [**unknown**]
  No Pydantic model found.





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-vertical-grid-coordinate/air-potential-temperature.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:native-vertical-grid-coordinate/air-potential-temperature")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-vertical-grid-coordinate/_context_",
            "@type": "wcrp:native-vertical-grid-coordinate",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:native-vertical-grid-coordinate/air-potential-temperature" , frame)

```
</section>

    
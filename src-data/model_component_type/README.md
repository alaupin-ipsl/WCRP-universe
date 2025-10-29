

<section id="description">

# Model Component Type  (universal)



## Description
Classifies the types of model components that make up earth system models, corresponding to the EMD component controlled vocabulary (e.g., atmosphere, ocean, land_surface, sea_ice, etc.).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/model-component-type/model-component-type)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:model-component-type` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:model-component-type` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/model-component-type](https://wcrp-cmip.github.io/WCRP-universe/model-component-type) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-component-type) |


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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-component-type/aerosol.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:model-component-type/aerosol")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/model-component-type/_context_",
            "@type": "wcrp:model-component-type",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:model-component-type/aerosol" , frame)

```
</section>

    
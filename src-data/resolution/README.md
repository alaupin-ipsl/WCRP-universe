

<section id="description">

# Resolution  (universal)



## Description
Specifies the spatial resolution characteristics of climate model grids, corresponding to the EMD nominal resolution controlled vocabulary with standardized resolution categories (e.g., 100 km, 25 km, 5 km).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/resolution/resolution)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:resolution` |
| Pydantic class | [`resolution`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/resolution.py): Resolution |
| | |
| JSON-LD | `universal:resolution` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/resolution](https://wcrp-cmip.github.io/WCRP-universe/resolution) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/resolution) |


</section>
    No external links found. 
<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`description`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`drs_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`unit`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`value`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/resolution/0.5km.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:resolution/0.5km")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/resolution/_context_",
            "@type": "wcrp:resolution",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:resolution/0.5km" , frame)

```
</section>

    
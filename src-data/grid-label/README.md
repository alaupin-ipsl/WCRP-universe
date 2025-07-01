

<section id="description">

# Grid Label  (universal)



## Description
Provides labels for different grid configurations used in climate models, helping to identify and categorize the spatial grid arrangements for data output.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/grid-label/grid-label)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:grid-label` |
| Pydantic class | [`grid_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/grid_label.py): GridLabel |
| | |
| JSON-LD | `universal:grid-label` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/grid-label](https://wcrp-cmip.github.io/WCRP-universe/grid-label) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/grid-label) |


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
- **`region`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`short_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/grid-label/gm.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:grid-label/gm")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/grid-label/_context_",
            "@type": "wcrp:grid-label",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:grid-label/gm" , frame)

```
</section>

    
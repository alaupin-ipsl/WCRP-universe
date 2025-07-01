

<section id="description">

# License  (universal)



## Description
Defines the licensing terms and conditions under which climate model data and documentation are made available for use and distribution.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/license/license)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:license` |
| Pydantic class | [`license`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/license.py): License |
| | |
| JSON-LD | `universal:license` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/license](https://wcrp-cmip.github.io/WCRP-universe/license) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/license) |


</section>
    No external links found. 
<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`drs_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`kind`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`license`** (**str | None**) 
  << No description in pydantic model (see esgvoc) >>
- **`url`** (**str | None**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/license/cc-by-4.0.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:license/cc-by-4.0")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/license/_context_",
            "@type": "wcrp:license",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:license/cc-by-4.0" , frame)

```
</section>

    
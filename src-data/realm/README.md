

<section id="description">

# Realm  (universal)



## Description
Defines the physical domains or realms of the Earth system that model variables are associated with (e.g., atmosphere, ocean, land, sea ice). Note: This differs from EMD component types as realms classify output variables rather than model components.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/realm/realm)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:realm` |
| Pydantic class | [`realm`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/realm.py): Realm |
| | |
| JSON-LD | `universal:realm` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/realm](https://wcrp-cmip.github.io/WCRP-universe/realm) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/realm) |


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
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/realm/aerosol.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:realm/aerosol")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/realm/_context_",
            "@type": "wcrp:realm",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:realm/aerosol" , frame)

```
</section>

    
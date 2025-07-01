

<section id="description">

# Source Type  (universal)



## Description
Classifies the type and configuration of climate models, indicating the components and complexity of the modeling system (e.g., coupled models, atmosphere-only models).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/source-type/source-type)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:source-type` |
| Pydantic class | [`source_type`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/source_type.py): SourceType |
| | |
| JSON-LD | `universal:source-type` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/source-type](https://wcrp-cmip.github.io/WCRP-universe/source-type) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/source-type) |


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
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/source-type/aer.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:source-type/aer")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/source-type/_context_",
            "@type": "wcrp:source-type",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:source-type/aer" , frame)

```
</section>

    
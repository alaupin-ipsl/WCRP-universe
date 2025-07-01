

<section id="description">

# Organisation  (universal)



## Description
Identifies the institutions or organizations responsible for developing and maintaining climate models, providing attribution and contact information.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/organisation/organisation)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:organisation` |
| Pydantic class | [`organisation`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/organisation.py): Organisation |
| | |
| JSON-LD | `universal:organisation` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/organisation](https://wcrp-cmip.github.io/WCRP-universe/organisation) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/organisation) |


</section>
    No external links found. 
<section id="schema">

## Content Schema

- **`id`** (**str**) 
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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/organisation/aer.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:organisation/aer")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/organisation/_context_",
            "@type": "wcrp:organisation",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:organisation/aer" , frame)

```
</section>

    
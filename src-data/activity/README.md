

<section id="description">

# Activity  (universal)



## Description
Defines the type of climate modeling activity or experiment being performed. Activities represent different categories of climate experiments such as historical simulations, future projections, or paleoclimate studies.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/activity/activity)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:activity` |
| Pydantic class | [`activity`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/activity.py): Activity |
| | |
| JSON-LD | `universal:activity` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/activity](https://wcrp-cmip.github.io/WCRP-universe/activity) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/activity) |


</section>
    No external links found. 
<section id="schema">

## Content Schema

- **`id`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`drs_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`long_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`name`** (**str**) 
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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/activity/aera-mip.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:activity/aera-mip")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/activity/_context_",
            "@type": "wcrp:activity",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:activity/aera-mip" , frame)

```
</section>

    
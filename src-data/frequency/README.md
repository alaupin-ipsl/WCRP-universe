

<section id="description">

# Frequency  (universal)



## Description
Specifies the temporal sampling frequency for climate model output data, defining how often data values are recorded (e.g., daily, monthly, yearly).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/frequency/frequency)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:frequency` |
| Pydantic class | [`frequency`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/frequency.py): Frequency |
| | |
| JSON-LD | `universal:frequency` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/frequency](https://wcrp-cmip.github.io/WCRP-universe/frequency) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/frequency) |


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
- **`long_name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`name`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`unit`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/frequency/1hr.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:frequency/1hr")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/frequency/_context_",
            "@type": "wcrp:frequency",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:frequency/1hr" , frame)

```
</section>

    
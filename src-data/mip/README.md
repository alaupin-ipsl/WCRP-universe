

<section id="description">

# Mip  (universal)



## Description
Identifies Model Intercomparison Projects (MIPs) that coordinate and define specific climate modeling experiments and data requirements within the CMIP framework.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/mip/mip)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:mip` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:mip` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/mip](https://wcrp-cmip.github.io/WCRP-universe/mip) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/mip) |


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
- **`end`**  
   [**unknown**]
  No Pydantic model found.
- **`start`**  
   [**unknown**]
  No Pydantic model found.
- **`url`**  
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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/mip/cmip5.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:mip/cmip5")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/mip/_context_",
            "@type": "wcrp:mip",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:mip/cmip5" , frame)

```
</section>

    
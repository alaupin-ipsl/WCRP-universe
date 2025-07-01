

<section id="description">

# Native Horizontal Grid Temporal Refinement  (universal)



## Description
Defines how horizontal grid cell distribution varies over time, based on the EMD temporal_refinement controlled vocabulary (e.g., static, dynamically_stretched, adaptive).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement/native-horizontal-grid-temporal-refinement)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:native-horizontal-grid-temporal-refinement` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-horizontal-grid-temporal-refinement` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-horizontal-grid-temporal-refinement) |


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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-horizontal-grid-temporal-refinement/adaptive.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:native-horizontal-grid-temporal-refinement/adaptive")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-temporal-refinement/_context_",
            "@type": "wcrp:native-horizontal-grid-temporal-refinement",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:native-horizontal-grid-temporal-refinement/adaptive" , frame)

```
</section>

    
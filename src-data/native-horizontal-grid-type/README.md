

<section id="description">

# Native Horizontal Grid Type  (universal)



## Description
Specifies the horizontal grid types used by model components, following the EMD grid controlled vocabulary (e.g., regular_latitude_longitude, cubed_sphere, unstructured_triangular).

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type/native-horizontal-grid-type)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:native-horizontal-grid-type` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:native-horizontal-grid-type` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type](https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-horizontal-grid-type) |


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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/native-horizontal-grid-type/cubed-sphere.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:native-horizontal-grid-type/cubed-sphere")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/native-horizontal-grid-type/_context_",
            "@type": "wcrp:native-horizontal-grid-type",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:native-horizontal-grid-type/cubed-sphere" , frame)

```
</section>

    
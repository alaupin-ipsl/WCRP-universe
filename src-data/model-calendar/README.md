

<section id="description">

# Model Calendar  (universal)



## Description
Specifies the calendar system used by climate models to define valid dates and time periods. Based on the EMD calendar controlled vocabulary, including options like standard, 360_day, 365_day, and others.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/model-calendar/model-calendar)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:model-calendar` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `universal:model-calendar` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/model-calendar](https://wcrp-cmip.github.io/WCRP-universe/model-calendar) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-calendar) |


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
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/model-calendar/360-day.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:model-calendar/360-day")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/model-calendar/_context_",
            "@type": "wcrp:model-calendar",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:model-calendar/360-day" , frame)

```
</section>

    
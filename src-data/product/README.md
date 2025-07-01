

<section id="description">

# Product  (universal)



## Description
Categorizes different types of climate model output products, distinguishing between various data processing levels and output formats.

[View in HTML](https://wcrp-cmip.github.io/WCRP-universe/product/product)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:product` |
| Pydantic class | [`product`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/product.py): Product |
| | |
| JSON-LD | `universal:product` |
| Expanded reference link | [https://wcrp-cmip.github.io/WCRP-universe/product](https://wcrp-cmip.github.io/WCRP-universe/product) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/product) |


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
- **`kind`** (**str**) 
  << No description in pydantic model (see esgvoc) >>
- **`type`** (**str**) 
  << No description in pydantic model (see esgvoc) >>





</section>   

<section id="usage">

## Usage

### Online Viewer 
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/WCRP-universe/tree/main/src-data/product/derived.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "universal:product/derived")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```js
frame = {
            "@context": "https://wcrp-cmip.github.io/WCRP-universe/product/_context_",
            "@type": "wcrp:product",
            "keys we want": "",
            "@explicit": True

        }
        
```

```python

import cmipld
cmipld.frame( "universal:product/derived" , frame)

```
</section>

    
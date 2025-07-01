# Universal terms for World Climate Modelling

WCRP-universe repository used by CMIP and other WCRP activities. 


[![⇑ Update Issue Templates](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/issue-templates.yml/badge.svg)](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/issue-templates.yml)
[![∆ src-data](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/src-data-change.yml/badge.svg?branch=src-data)](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/src-data-change.yml)
[![→ workflows](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/sync-workflows.yml/badge.svg)](https://github.com/WCRP-CMIP/WCRP-universe/actions/workflows/sync-workflows.yml)
-------

> [!CAUTION]
> ### THIS REPOSITORY IS CURRENTLY UNDER ACTIVE DEVELOPMENT

--------




## JSON branch structure (ignore these and use esgvoc for now)

| Required |  |
|--------|-------------|
| [`main`](https://github.com/WCRP-CMIP/WCRP-universe/tree/main) | The landing page directing users to the relevant content. |
| [`docs`](https://github.com/WCRP-CMIP/WCRP-universe/tree/docs) | Contains the documentation and is version-controlled. This is the branch where documentation edits are made. Actions and automations (e.g., workflows that update docs or summaries) are also configured from this branch. |
| [`src-data`](https://github.com/WCRP-CMIP/WCRP-universe/tree/src-data) | Stores the JSONLD content used to link all files. Updates here trigger automated workflows that identify changed JSON files and update documentation or summaries accordingly. |
| [`production`](https://github.com/WCRP-CMIP/WCRP-universe/tree/production) | Not for user digestion. Hosts the compiled documentation and JSONLD files, as well as the static pages site. Updated automatically via workflows when changes in `src-data` or `docs` are processed. |



| Optional |  |
|--------|-------------|
| `dev_*` | Other branches used for updating things. |
| `*` | All other branches are usually ones containing submissions to update the content. |






## Contributors

[![Contributors](https://contrib.rocks/image?repo=WCRP-CMIP/WCRP-universe)](https://github.com/WCRP-CMIP/WCRP-universe/graphs/contributors)

Thanks to our contributors!

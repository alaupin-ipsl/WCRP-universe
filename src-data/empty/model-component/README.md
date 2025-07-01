The dynamic model component(s), which are those that dynamically simulate their processes and interact with each other either directly or indirectly. Direct interactions between components can be characterised as either "embedded" or "coupled."

What are the characteristics of an "embedded" component? 
<details>
<summary>Click the arrow to learn more.</summary>

  - shares the same horizontal grid as the host component;
  - is constructed such that the code representing the component would be exceedingly difficult to extract and transfer to another coupled model;
  - is coded such that within a single time-step, interactions between it and its host might involve exchanges of information affecting both;
  - cannot be easily "driven" independently of its host (e.g. it cannot be run by itself in standalone "offline" mode with prescribed external conditions imposed);
  - may not have a recognisable name or version number (other than those of the host component).

</details>

What are the characteristics of a "coupled" component? 
<details>
<summary>Click the arrow to learn more.</summary>

  - is identified using a recognisable name, and often a version number (e.g. "MOM5," the fifth version of the Modular Ocean Model);
  - interacts at regular intervals with other components by exchanging the collection of quantities needed by each to advance a simulation (such as mass, momentum, energy, etc.), either via a coupler (i.e. code specially adapted to represent the exchanges between the various components) or by other means;
  - is coded such that it is relatively isolated from other parts of a coupled model code and (by design) might be extracted to be adopted in another model.

</details>

**Note:** _A component must be either embedded in another component or else coupled with other components, but can not be both._

**Note:** _The distinction between these two types may not always be obvious, and in some cases a somewhat arbitrary choice may have to be made. For instance, this could be the case when a component satisfies characteristics from both interaction types (e.g. it is possible for a component with a recognisable name and version number to be embedded in a host, rather than coupled)._

An embedded component has a single host component, and cannot be coupled with any other components. Multiple components can be embedded in the same host. When there is more than one candidate for the host component, it should be chosen as the one that most directly influences the other components' processes. For instance, the ocean biogeochemistry, sea ice, and ocean components of a coupled model might be treated together in the model code, but both sea ice and ocean biogeochemistry are considered to be embedded in the host ocean because, although there may be direct interactions and exchanges between the ocean biogeochemistry and sea ice, both of these components are more strongly influenced by properties primarily determined by the ocean component (e.g. the sea water temperature and salinity).

A non-embedded component must be coupled with one or more other components. Coupling (unlike embedding) is symmetrical, in that if component X is coupled with component Y, then component Y must also be coupled with component X, and this would be recorded in the Coupled with properties of both components. For instance, an ocean component might commonly be coupled with the atmosphere, sea ice, and ocean biogeochemistry, but it could also be coupled with the land surface component (if river water discharge into the ocean were explicitly calculated by the land model and "seen" by the ocean) and the land ice component (if the melting of an ice shelf contributed mass to the ocean or if heat or momentum fluxes were exchanged at the base of the ice shelf).
